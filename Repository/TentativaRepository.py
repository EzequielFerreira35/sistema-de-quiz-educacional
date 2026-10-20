from abc import ABC, abstractmethod
from Entidades.tentativa import Tentativa, Usuario
from pathlib import Path
import uuid
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
    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list:
        pass

class TentativaRepositorySQLite(TentativaRepository):
    def __init__(self, caminho_db: Path) -> None:
        self.caminho = Path(caminho_db)

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.row_factory = sqlite3.Row
        return conn

    def salvar(self, tentativa: Tentativa):
        with self.conectar() as conn:
            conn.execute("""INSERT INTO tentativa (id, id_quiz, id_usuario, pontuacao, tempo_total, status_conclusao)
                            VALUES (?, ?, ?, ?, ?, ?)""", 
                            (tentativa.id, tentativa.quiz.id, tentativa.usuario.id, tentativa.pontuacao, tentativa.tempo_total, tentativa.status_conclusao))
        
        perguntas = tentativa.quiz.lista_perguntas

        for pergunta, resposta in zip(perguntas, tentativa.respostas):
            conn.execute("""INSERT INTO respostas_tentativa (id, id_tentativa, id_pergunta, id_alternativa)
                            VALUES (?, ?, ?, ?)""",
                            (str(uuid.uuid4()), tentativa.id, pergunta.id, resposta))

        conn.commit()
        conn.close()

    def deletar(self, tentativa_id: str):
        with self.conectar() as conn:
            conn.execute("""DELETE FROM respostas_tentativa WHERE id_tentativa = ?""", (tentativa_id))
            conn.execute("""DELETE FROM tentativa WHERE id = ?""", (tentativa_id))

        conn.commit()
        conn.close()

    def listar_por_usuario(self, usuario_id: str, quiz_id: str) -> list:
        with self.conectar() as conn:
            cursor = conn.execute("""SELECT * FROM tentativa 
                                    JOIN usuario ON tentativa.id_usuario = usuario.id
                                    JOIN quiz ON tentativa.id_quiz = quiz.id

                                    WHERE tentativa.id_usuario = ?
                                    AND tentativa.id_quiz = ?
                                    """, (usuario_id, quiz_id))

            dados = cursor.fetchall()

        conn.close()
        return dados

        
