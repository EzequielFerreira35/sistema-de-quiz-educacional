from abc import ABC, abstractmethod
from Entidades.quiz import Quiz
from .sqlite_base import SQLiteBase
from .PerguntaRepository import PerguntaRepositorySQLite



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
    def __init__(self) -> None:
        super().__init__()

    def deletar(self, quiz_id: str):
        with self.conexao() as conn:
            conn.execute("DELETE FROM quiz WHERE id = ?", (quiz_id,))

    def buscar_por_id(self, quiz_id: str) -> Quiz | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM quiz WHERE id = ?", (quiz_id,))
            quiz = cursor.fetchone()

        if quiz is None:
            return

        q = Quiz.from_row(quiz) 

        repo = PerguntaRepositorySQLite()
        perguntas = repo.listar_por_quiz(q.id)

        for pergunta in perguntas:
            q.adicionar_pergunta(pergunta)

        return q

    def salvar(self, quiz: Quiz) -> None:
        with self.conexao() as conn:
            conn.execute("""INSERT INTO quiz (id, titulo, tempo_limite, limite_tentativas)
                            VALUES (?, ?, ?, ?) ON CONFLICT (id) DO UPDATE SET
                            titulo = excluded.titulo,
                            tempo_limite = excluded.tempo_limite,
                            limite_tentativas = excluded.limite_tentativas""", 
                            (quiz.id, quiz.titulo, quiz.tempo_limite, quiz. limite_tentativas))
        
            perguntas = quiz.lista_perguntas

            for pergunta in perguntas:
                conn.execute("""INSERT INTO quiz_pergunta (id_quiz, id_pergunta)
                                VALUES (?, ?) ON CONFLICT (id_quiz, id_pergunta) DO NOTHING""",
                                (quiz.id, pergunta.id))

    def listar_todos(self) -> list[Quiz] | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM quiz ORDER BY titulo")
            quizzes = cursor.fetchall()

        return [Quiz.from_row(linha) for linha in quizzes]