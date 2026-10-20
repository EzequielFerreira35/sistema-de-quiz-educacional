from abc import ABC, abstractmethod
from Entidades.quiz import Quiz
from contextlib import closing
import sqlite3

class QuizRepository(ABC):

    @abstractmethod
    def deletar(self, quiz_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, quiz_id: str) -> Quiz | None:
        pass

    @abstractmethod
    def salvar(self, quiz: Quiz):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Quiz] | None:
        pass


class QuizRepositorySQLite(QuizRepository):
    def __init__(self, caminho_db) -> None:
        self.caminho = caminho_db

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, quiz_id: str):
        with closing(self.conectar()) as conn:
            conn.execute("DELETE FROM quiz WHERE id = ?", (quiz_id,))
            conn.commit()

    def buscar_por_id(self, quiz_id: str) -> Quiz | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM quiz WHERE id = ?", (quiz_id,))
            quiz = cursor.fetchone()

        if quiz is None:
            return

        return Quiz.from_row(quiz)

    def salvar(self, quiz: Quiz) -> None:
        with closing(self.conectar()) as conn:
            conn.execute("""INSERT INTO quiz (id, titulo, tempo_limite, limite_tentativas)
                            VALUES (?, ?, ?, ?)""", 
                            (quiz.id, quiz.titulo, quiz.tempo_limite, quiz. limite_tentativas))
            perguntas = quiz.lista_perguntas

            for pergunta in perguntas:
                conn.execute("""INSERT INTO quiz_pergunta (id_quiz, id_pergunta)
                                VALUES (?, ?)""", (quiz.id, pergunta.id))

        conn.commit()

    def listar_todos(self) -> list[Quiz] | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM quiz ORDER BY titulo")
            quizzes = cursor.fetchall()

        return [Quiz.from_row(linha) for linha in quizzes]