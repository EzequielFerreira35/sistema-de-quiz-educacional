from Repository.QuizRepository import QuizRepository
from Repository.PerguntaRepository import PerguntaRepository
from Entidades.pergunta import Pergunta
from Entidades.quiz import Quiz

class QuizService:
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
        if not isinstance(pergunta_id, str) or not pergunta_id.strip():
            raise ValueError("Pergunta_id deve ser uma string não vazia!")

        if not isinstance(quiz_id, str) or not quiz_id.strip():
            raise ValueError("Quiz_id deve ser uma string não vazia!")

        quiz_id = quiz_id.strip()
        pergunta_id = pergunta_id.strip()

        quiz = self.quiz_repo.buscar_por_id(quiz_id)
        pergunta = self.pergunta_repo.buscar_por_id(pergunta_id)

        if quiz is None:
            raise ValueError("Essa Pergunta não existe!")

        if pergunta is None:
            raise ValueError("Esse Quiz não existe!")

        adicionada = quiz.adicionar_pergunta(pergunta)

        if adicionada:
            self.quiz_repo.salvar(quiz)

        return adicionada
