import uuid

from abc import ABC, abstractmethod
from Entidades.pergunta import Pergunta
from .sqlite_base import SQLiteBase



class PerguntaRepository(ABC):

    @abstractmethod
    def deletar(self, pergunta_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, pergunta_id: str) -> Pergunta:
        pass

    @abstractmethod
    def salvar(self, pergunta: Pergunta):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Pergunta]:
        pass

    @abstractmethod
    def listar_por_tema(self, tema_id) -> list[Pergunta]:
        pass

    @abstractmethod
    def listar_por_quiz(self, quiz_id) -> list[Pergunta]:
        pass

class PerguntaRepositorySQLite(PerguntaRepository, SQLiteBase):
    def __init__(self) -> None:
        super().__init__()

    def deletar(self, pergunta_id: str):
        with self.conexao() as conn:
            conn.execute("DELETE FROM pergunta WHERE id = ?", (pergunta_id,))

    def salvar(self, pergunta: Pergunta) -> None:
        with self.conexao() as conn:
            conn.execute("""INSERT INTO pergunta (id, id_tema, enunciado, indice_resposta, dificuldade)
                            VALUES (?, ?, ?, ?, ?) ON CONFLICT (id) DO UPDATE SET
                                id_tema = excluded.id_tema,
                                enunciado = excluded.enunciado,
                                indice_resposta = excluded.indice_resposta,
                                dificuldade = excluded.dificuldade""",
                            (pergunta.id, pergunta.tema.id, pergunta.enunciado, pergunta.indice_resposta, pergunta.dificuldade))
 
            for posicao, texto in enumerate(pergunta.alternativas):
                conn.execute("""INSERT INTO alternativa (id, id_pergunta, enunciado, posicao)
                                VALUES (?, ?, ?, ?) ON CONFLICT (id) DO UPDATE SET
                                id_pergunta = excluded.id_pergunta,
                                enunciado = excluded_enunciado,
                                posicao = excluded.posicao""", (str(uuid.uuid4()), pergunta.id, texto, posicao))
 
    def buscar_por_id(self, pergunta_id: str) -> Pergunta | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     WHERE pergunta.id = ?""", (pergunta_id,))
    
            pergunta = cursor.fetchone()

            if pergunta is None:
                return
            
            cursor.execute("""SELECT * FROM alternativas WHERE pergunta_id = ? ORDER BY posicao""", (pergunta_id,))

            alternativas = cursor.fetchall()

            dados = dict(pergunta)
            dados["alternativas"] = [alternativa["enunciado"] for alternativa in alternativas]

            return Pergunta.from_row(dados)

    def listar_todos(self) -> list[Pergunta]:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     ORDER BY pergunta.enunciado""")
            perguntas = cursor.fetchall()

            resultado = []

            for pergunta in perguntas:
                cursor.execute("""SELECT * FROM alternativas WHERE pergunta_id = ? ORDER BY posicao""", (pergunta["id"],))

                dados = dict(pergunta)
                alternativas = cursor.fetchall()
                dados["alternativas"] = [alternativa["enunciado"] for alternativa in alternativas]

                resultado.append(Pergunta.from_row(dados))


            return resultado


    def listar_por_tema(self, tema_id: str) -> list[Pergunta]:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     WHERE pergunta.id_tema = ?
                                     ORDER BY pergunta.enunciado""", (tema_id,))
            perguntas = cursor.fetchall()
            resultado = []

            for pergunta in perguntas:
                cursor.execute("""SELECT * FROM alternativas WHERE pergunta_id = ? ORDER BY posicao""", (pergunta["id"],))

                dados = dict(pergunta)
                alternativas = cursor.fetchall()
                dados["alternativas"] = [alternativa["enunciado"] for alternativa in alternativas]

                resultado.append(Pergunta.from_row(dados))


            return resultado
 
    def listar_por_quiz(self, quiz_id: str) -> list[Pergunta]:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta
                                     JOIN tema ON pergunta.id_tema = tema.id
                                     JOIN quiz_pergunta ON quiz_pergunta.id_pergunta = pergunta.id
                                     WHERE quiz_pergunta.id_quiz = ?
                                     ORDER BY quiz_pergunta.rowid""", (quiz_id,))
            perguntas = cursor.fetchall()
 
            resultado = []

            for pergunta in perguntas:
                cursor.execute("""SELECT * FROM alternativas WHERE pergunta_id = ? ORDER BY posicao""", (pergunta["id"],))

                dados = dict(pergunta)
                alternativas = cursor.fetchall()
                dados["alternativas"] = [alternativa["enunciado"] for alternativa in alternativas]

                resultado.append(Pergunta.from_row(dados))


            return resultado