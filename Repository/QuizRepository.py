from abc import ABC, abstractmethod
from Entidades.quiz import Quiz
import sqlite3

class QuizRepository(ABC):

    @abstractmethod
    def deletar(self, quiz_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, quiz_id: str) -> Quiz:
        pass

    @abstractmethod
    def salvar(self, quiz: Quiz):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Quiz]:
        pass


class QuizRepositorySQLite(QuizRepository):
    def __init__(self, caminho_db) -> None:
        self.caminho = caminho_db

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, quiz_id: str):
        with self.conectar() as conn:
            cursor = conn.execute("DELETE FROM quiz WHERE id = ?", (quiz_id))

        conn.commit()
        conn.close()

    def buscar_por_id(self, quiz_id: str) -> Quiz:
        with self.conectar() as conn:
            cursor = conn.execute("SELECT * FROM quiz WHERE id = ?", quiz_id)
            quiz = cursor.fetchone()

        conn.close()    
        return Quiz(id=quiz[0], titulo=quiz[1], tempo_limite=quiz[2], limite_tentativas=quiz[3])

    def salvar(self, quiz: Quiz) -> None:
        with self.conectar() as conn:
            conn.execute("""INSERT INTO quiz (id, titulo, tempo_limite, limite_tentativas)
                            VALUES (?, ?, ?, ?)""", 
                            (quiz.id, quiz.titulo, quiz.tempo_limite, quiz. limite_tentativas))

        conn.commit()
        conn.close

    def listar_todos(self) -> list[Quiz]:
        with self.conectar() as conn:
            cursor = conn.execute("SELECT * FROM quiz ORDER BY titulo")

        conn.close()
        return [Quiz.from_row(linha) for linha in cursor.fetchall()]