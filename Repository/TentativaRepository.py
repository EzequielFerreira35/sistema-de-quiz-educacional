from abc import ABC, abstractmethod
from Entidades.tentativa import Tentativa
from Entidades.usuario import Usuario
from Entidades.quiz import Quiz
from contextlib import closing
from pathlib import Path

import sqlite3

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

class TentativaRepositorySQLite(TentativaRepository):
    def __init__(self, caminho_db: Path) -> None:
        self.caminho = Path(caminho_db)

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def salvar(self, tentativa: Tentativa):
        with closing(self.conectar()) as conn:
            conn.execute("""INSERT INTO tentativa (id, id_quiz, id_usuario, data, pontuacao, tempo_total, status_conclusao)
                            VALUES (?, ?, ?, ?, ?, ?, ?)""", 
                            (tentativa.id, tentativa.quiz.id, tentativa.usuario.id, tentativa.data, tentativa.pontuacao, tentativa.tempo_total, tentativa.status_conclusao))

            perguntas = tentativa.quiz.lista_perguntas

            for pergunta, resposta in zip(perguntas, tentativa.respostas):
                id_alternativa = None
                if resposta is not None:
                    with conn:
                        alternativa = conn.execute("""SELECT id from alternativa WHERE id_pergunta = ?""", (pergunta.id, resposta)).fetchone

                    if alternativa is None:
                        raise ValueError("Alternativa não encontrada")

                    id_alternativa = alternativa["id"]

            conn.commit()

    def deletar(self, tentativa_id: str):
        with closing(self.conectar()) as conn:
            conn.execute("""DELETE FROM respostas_tentativa WHERE id_tentativa = ?""", (tentativa_id,))
            conn.commit()

    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list | None:
        with self.conectar() as conn:
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

