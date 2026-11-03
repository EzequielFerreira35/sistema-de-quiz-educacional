from src.Repository.QuizRepository import QuizRepository
from src.Repository.PerguntaRepository import PerguntaRepository
from src.Entidades.pergunta import Pergunta
from src.Entidades.quiz import Quiz
from .baseservice import BaseService
from .mixins import ValidadorIdMixin

class QuizService(BaseService, ValidadorIdMixin):
    """
    Gerencia as regras de negócio e o ciclo de vida dos Quizzes.
    Herda atributos e métodos da Classe BaseService.
    """

    def __init__(self, quiz_repo: QuizRepository, pergunta_repo: PerguntaRepository):
        self.pergunta_repo = pergunta_repo
        self.quiz_repo = quiz_repo

    def criar_quiz(self, titulo: str, tempo_limite=None, limite_tentativas=None):
        quiz = Quiz(titulo=titulo, tempo_limite=tempo_limite, limite_tentativas=limite_tentativas)
        self.quiz_repo.salvar(quiz)
        return quiz

    def adicionar_pergunta(self, quiz_id: str, pergunta_id: str):
        quiz_id = self._validar_id(quiz_id, "quiz_id")

        pergunta_id = self._validar_id(pergunta_id, "pergunta_id")

        quiz = self.quiz_repo.buscar_por_id(quiz_id)
        pergunta = self.pergunta_repo.buscar_por_id(pergunta_id)

        if quiz is None:
            raise ValueError("Essa Quiz não existe!")

        if pergunta is None:
            raise ValueError("Esse Pergunta não existe!")

        adicionada = quiz.adicionar_pergunta(pergunta)

        if adicionada:
            self.quiz_repo.salvar(quiz)

        return adicionada
