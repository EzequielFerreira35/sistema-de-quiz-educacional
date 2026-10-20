from abc import ABC, abstractmethod
from Entidades.pergunta import Pergunta
from Entidades.tema import Tema
from contextlib import closing
import sqlite3
import uuid

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
    def listar_por_tema(self) -> list[Pergunta]:
        pass

    @abstractmethod
    def listar_por_quiz(self) -> list[Pergunta]:
        pass

class PerguntaRepositorySQLite(PerguntaRepository):
    def __init__(self, caminho_db) -> None:
        self.caminho = caminho_db
 
    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, pergunta_id: str):
        with closing(self.conectar()) as conn:
            conn.execute("DELETE FROM pergunta WHERE id = ?", (pergunta_id,))
            conn.commit()

    def salvar(self, pergunta: Pergunta) -> None:
        with closing(self.conectar()) as conn:
            conn.execute("""INSERT INTO pergunta (id, id_tema, enunciado, indice_resposta, dificuldade)
                            VALUES (?, ?, ?, ?, ?)""",
                            (pergunta.id, pergunta.tema.id, pergunta.enunciado, pergunta.indice_resposta, pergunta.dificuldade))
 
            for posicao, texto in enumerate(pergunta.alternativas):
                conn.execute("""INSERT INTO alternativa (id, id_pergunta, enunciado, posicao)
                                VALUES (?, ?, ?, ?)""", (str(uuid.uuid4()), pergunta.id, texto, posicao))
 
            conn.commit()

    def buscar_por_id(self, pergunta_id: str) -> Pergunta | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     WHERE pergunta.id = ?""", (pergunta_id,))
            pergunta = cursor.fetchone()
 
            if pergunta is None:
                return
 
            return pergunta

    def listar_todos(self) -> list[Pergunta]:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     ORDER BY pergunta.enunciado""")
            dados = cursor.fetchall()
 
            return dados


    def listar_por_tema(self, tema_id: str) -> list[Pergunta]:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta JOIN tema ON pergunta.id_tema = tema.id
                                     WHERE pergunta.id_tema = ?
                                     ORDER BY pergunta.enunciado""", (tema_id,))
            dados = cursor.fetchall()
 
            return dados
 
    def listar_por_quiz(self, quiz_id: str) -> list[Pergunta]:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("""SELECT pergunta.*, tema.nome AS nome_tema
                                     FROM pergunta
                                     JOIN tema ON pergunta.id_tema = tema.id
                                     JOIN quiz_pergunta ON quiz_pergunta.id_pergunta = pergunta.id
                                     WHERE quiz_pergunta.id_quiz = ?
                                     ORDER BY quiz_pergunta.rowid""", (quiz_id,))
            dados = cursor.fetchall()
 
            return dados