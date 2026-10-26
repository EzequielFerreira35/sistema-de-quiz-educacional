from abc import ABC, abstractmethod
from Entidades.quiz import Quiz
from .sqlite_base import SQLiteBase


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


class QuizRepositorySQLite(QuizRepository, SQLiteBase):
    def __init__(self, caminho_db) -> None:
        super().__init__(caminho_db)

    def deletar(self, quiz_id: str):
        with self.conexao() as conn:
            conn.execute("DELETE FROM quiz WHERE id = ?", (quiz_id,))

    def buscar_por_id(self, quiz_id: str) -> Quiz | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM quiz WHERE id = ?", (quiz_id,))
            quiz = cursor.fetchone()

        if quiz is None:
            return

        return Quiz.from_row(quiz)

    def salvar(self, quiz: Quiz) -> None:
        with self.conexao() as conn:
            conn.execute("""INSERT INTO quiz (id, titulo, tempo_limite, limite_tentativas)
                            VALUES (?, ?, ?, ?)""", 
                            (quiz.id, quiz.titulo, quiz.tempo_limite, quiz. limite_tentativas))
            perguntas = quiz.lista_perguntas

            for pergunta in perguntas:
                conn.execute("""INSERT INTO quiz_pergunta (id_quiz, id_pergunta)
                                VALUES (?, ?)""", (quiz.id, pergunta.id))

    def listar_todos(self) -> list[Quiz] | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM quiz ORDER BY titulo")
            quizzes = cursor.fetchall()

        return [Quiz.from_row(linha) for linha in quizzes]