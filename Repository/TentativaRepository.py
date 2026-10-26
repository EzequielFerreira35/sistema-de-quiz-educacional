import sqlite3

from abc import ABC, abstractmethod
from Entidades.tentativa import Tentativa
from .sqlite_base import SQLiteBase


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


class TentativaRepositorySQLite(TentativaRepository, SQLiteBase):
    def __init__(self, caminho_db) -> None:
        super().__init__(caminho_db)

    def buscar_por_id(self, tentativa_id: str) -> sqlite3.Row | None:
        with self.conexao() as conn:
            cursor = conn.execute("""SELECT * FROM tentativa WHERE id = ?""", (tentativa_id,))
            return cursor.fetchone()
        
    def salvar(self, tentativa: Tentativa):
        with self.conexao() as conn:
            conn.execute("""INSERT INTO tentativa (id, id_quiz, id_usuario, data, pontuacao, tempo_total, status_conclusao)
                            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                            (tentativa.id, tentativa.quiz.id, 
                             tentativa.usuario.id, 
                             str(tentativa.data), 
                             tentativa.pontuacao, 
                             tentativa.tempo_total, 
                             tentativa.status_conclusao))
 
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
            conn.execute("""DELETE FROM respostas_tentativa WHERE id_tentativa = ?""", (tentativa_id,))
            conn.commit()

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

