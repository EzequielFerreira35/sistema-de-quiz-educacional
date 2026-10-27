from abc import ABC, abstractmethod
from Entidades.tentativa import Tentativa
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
    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list | None:
        pass

    @abstractmethod
    def contar_por_usuario_e_quiz(self, usuario_id: str, quiz_id: str) -> int:
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
                                LEFT JOIN alternativa ON respostas_tentativa.id_pergunta = alternativa.id_pergunta
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
                            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                            (tentativa.id, tentativa.quiz.id, 
                             tentativa.usuario.id, 
                             tentativa.data, 
                             tentativa.pontuacao, 
                             tentativa.tempo_total, 
                             tentativa.status_conclusao))

            conn.execute("""DELETE FROM respostas_tentativa WHERE id_tentativa = ?""", (tentativa, id))

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
            conn.execute("""DELETE FROM tentativa WHERE id_tentativa = ?""", (tentativa_id,))

    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT * FROM tentativa 
                                    JOIN usuario ON tentativa.id_usuario = usuario.id
                                    JOIN quiz ON tentativa.id_quiz = quiz.id

                                    WHERE tentativa.id_usuario = ?
                                    AND tentativa.id_quiz = ?
                                    """, (usuario_id, quiz_id))

            dados = cursor.fetchall()

        if dados is None:
            return
        
        return dados

    def contar_por_usuario_e_quiz(self, usuario_id: str, quiz_id: str) -> int | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT COUNT(*) FROM tentativa 
                                WHERE id_quiz = ? AND id_usuario = ?""", (usuario_id, quiz_id))
            contagem = cursor.fetchone()
            return contagem[0]