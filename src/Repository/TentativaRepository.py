from abc import ABC, abstractmethod
from src.Entidades.tentativa import Tentativa
from .sqlite_base import SQLiteBase
from .QuizRepository import QuizRepositorySQLite
from .UsuarioRepository import UsuarioRepositorySQLite


class TentativaRepository(ABC):

    @abstractmethod
    def deletar(self, tentativa_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, tentativa_id: str) -> Tentativa:
        pass

    @abstractmethod
    def salvar(self, tentativa: Tentativa):
        pass

    @abstractmethod
    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list[dict] | None:
        pass

    @abstractmethod
    def contar_por_usuario_e_quiz(self, usuario_id: str, quiz_id: str) -> int:
        pass

    @abstractmethod
    def listar_concluidas_por_quiz(self, quiz_id: str) -> list[dict]:
        pass

    @abstractmethod
    def listar_concluidas_por_usuario(self, usuario_id: str | None = None) -> list[dict]:
        pass

    @abstractmethod
    def listar_respostas_por_pergunta(self, usuario_id: str | None = None) -> list[dict]:
        pass

class TentativaRepositorySQLite(TentativaRepository, SQLiteBase):
    def __init__(self) -> None:
        super().__init__()

    def buscar_por_id(self, tentativa_id: str) -> Tentativa | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT * FROM tentativa WHERE id = ?""", (tentativa_id,))
            
            tentativa = cursor.fetchone()
            if tentativa is None:
                return

            repo_quiz = QuizRepositorySQLite()
            quiz = repo_quiz.buscar_por_id(tentativa["id_quiz"])

            repo_usuario = UsuarioRepositorySQLite()
            usuario = repo_usuario.buscar_por_id(tentativa["id_usuario"])

            linhas_respostas = cursor.execute("""SELECT respostas_tentativa.id_pergunta, alternativa.posicao
                                FROM respostas_tentativa  
                                LEFT JOIN alternativa ON respostas_tentativa.id_alternativa = alternativa.id
                                WHERE id_tentativa = ?""", (tentativa_id,)).fetchall()
        

            por_pergunta = {}

            for resposta in linhas_respostas:
                por_pergunta[resposta["id_pergunta"]] = resposta["posicao"]

            respostas = []

            for pergunta in quiz.lista_perguntas:
                respostas.append(por_pergunta.get(pergunta.id))


        return Tentativa(
                quiz=quiz,
                respostas=respostas,
                usuario=usuario,
                data=tentativa["data"],
                tempo_total=tentativa["tempo_total"],
                id=tentativa["id"],
                pontuacao=tentativa["pontuacao"],
                status_conclusao=tentativa["status_conclusao"]
            )


        
    def salvar(self, tentativa: Tentativa):
        with self.conexao() as conn:
            conn.execute("""INSERT INTO tentativa (id, id_quiz, id_usuario, data, pontuacao, tempo_total, status_conclusao)
                            VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT (id) DO UPDATE SET
                            data = excluded.data,
                            pontuacao = excluded.pontuacao,
                            tempo_total = excluded.pontuacao,
                            status_conclusao = excluded.status_conclusao""",
                            (tentativa.id, tentativa.quiz.id, 
                             tentativa.usuario.id, 
                             tentativa.data, 
                             tentativa.pontuacao, 
                             tentativa.tempo_total, 
                             tentativa.status_conclusao))

            conn.execute("""DELETE FROM respostas_tentativa WHERE id_tentativa = ?""", (tentativa.id,))

            perguntas = tentativa.quiz.lista_perguntas
 
            for pergunta, resposta in zip(perguntas, tentativa.respostas):
                id_alternativa = None
                if resposta is not None:
                    alternativa = conn.execute("""SELECT id FROM alternativa WHERE id_pergunta = ? AND posicao = ?""", 
                                               (pergunta.id, resposta)).fetchone()
 
                    if alternativa is None:
                        raise ValueError("Alternativa não encontrada")
 
                    id_alternativa = alternativa["id"]
 
                conn.execute("""INSERT INTO respostas_tentativa (id_tentativa, id_pergunta, id_alternativa)
                                VALUES (?, ?, ?)""", (tentativa.id, pergunta.id, id_alternativa))
 

    def deletar(self, tentativa_id: str):
        with self.conexao() as conn:
            conn.execute("""DELETE FROM tentativa WHERE id = ?""", (tentativa_id,))

    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list[dict] | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT tentativa.data, tentativa.pontuacao, tentativa.tempo_total, tentativa.status_conclusao,
                                    quiz.titulo, tentativa.id   
                                    FROM tentativa 
                                    JOIN quiz ON tentativa.id_quiz = quiz.id

                                    WHERE tentativa.id_usuario = ?
                                    AND tentativa.id_quiz = ? 

                                    ORDER BY tentativa.data
                                    """, (usuario_id, quiz_id))

            dados = cursor.fetchall()
        
        return [dict(linha) for linha in dados]




    def contar_por_usuario_e_quiz(self, usuario_id: str, quiz_id: str) -> int | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT COUNT(*) FROM tentativa 
                                WHERE id_quiz = ? AND id_usuario = ?""", (quiz_id, usuario_id))
            contagem = cursor.fetchone()
            return contagem[0]


    def listar_concluidas_por_quiz(self, quiz_id: str) -> list[dict]:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT pontuacao, tempo_total FROM tentativa
                                    WHERE id_quiz = ?  AND status_conclusao = 1""", (quiz_id,))

            dados = cursor.fetchall()
        
        return [dict(linha) for linha in dados]



    def listar_concluidas_por_usuario(self, usuario_id: str | None = None) -> list[dict]:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT 
                                    usuario.id AS usuario_id, usuario.username AS usuario_nome,
                                    quiz.id AS quiz_id, quiz.titulo AS quiz_titulo, 
                                    tentativa.pontuacao, tentativa.tempo_total, tentativa.data

                                    FROM tentativa
                                    JOIN usuario ON tentativa.id_usuario = usuario.id
                                    JOIN quiz ON tentativa.id_quiz = quiz.id
                                    
                                    WHERE tentativa.status_conclusao = 1
                                    AND (? IS NULL OR tentativa.id_usuario = ?)
                                    ORDER BY tentativa.data""", (usuario_id, usuario_id))

            dados = cursor.fetchall()

        return [dict(linha) for linha in dados]



    def listar_respostas_por_pergunta(self, usuario_id: str | None = None) -> list:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT 
                                    pergunta.id AS pergunta_id, pergunta.enunciado AS pergunta_enunciado,
                                    tema.id AS tema_id, tema.nome AS nome_tema,
                                    
                                    COUNT(*) as total_respostas,
                                    SUM(CASE WHEN alternativa.posicao = pergunta.indice_resposta THEN 1 ELSE 0 END) AS acertos

                                    FROM respostas_tentativa
                                    LEFT JOIN alternativa ON respostas_tentativa.id_alternativa = alternativa.id
                                    JOIN pergunta ON respostas_tentativa.id_pergunta = pergunta.id
                                    JOIN tema ON pergunta.id_tema = tema.id
                                    JOIN tentativa ON respostas_tentativa.id_tentativa = tentativa.id 
                                    
                                    WHERE tentativa.status_conclusao = 1 AND (? IS NULL OR tentativa.id_usuario = ?)
                                    
                                    GROUP BY  pergunta_id, pergunta_enunciado, nome_tema
                                    
                                    """, (usuario_id, usuario_id))
            dados = cursor.fetchall()

        return [dict(linha) for linha in dados]
