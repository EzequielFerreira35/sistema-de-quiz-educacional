from src.Repository.TentativaRepository import TentativaRepository
from src.Repository.QuizRepository import QuizRepository
from src.Repository.UsuarioRepository import UsuarioRepository
from src.Entidades.tentativa import Tentativa
from .baseservice import BaseService
from .mixins import ValidadorIdMixin


class TentativaService(BaseService, ValidadorIdMixin):
    """
    Gerencia as regras de negócio e o ciclo de vida das Tentativas.
    Herda atributos e métodos da Classe BaseService.
    """

    def __init__(self, usuario_repo: UsuarioRepository, quiz_repo: QuizRepository, tentativa_repo: TentativaRepository):
        super().__init__()
        self.usuario_repo = usuario_repo
        self.quiz_repo = quiz_repo
        self.tentativa_repo = tentativa_repo

    def iniciar_quiz(self, usuario_id: str, quiz_id: str):
        usuario_id = self._validar_id(usuario_id, "usuario_id")
        quiz_id = self._validar_id(quiz_id, "quiz_id")

        quiz_id = quiz_id.strip()
        usuario_id = usuario_id.strip()

        quiz = self.quiz_repo.buscar_por_id(quiz_id)
        usuario = self.usuario_repo.buscar_por_id(usuario_id)

        if quiz is None:
            raise ValueError("Esse quiz não existe!")

        if not quiz.lista_perguntas:
            raise ValueError("Esse quiz não possui perguntas")

        if usuario is None:
            raise ValueError("Esse Usuário não existe!")

        if self.tentativa_repo.contar_por_usuario_e_quiz(usuario_id, quiz_id) >= quiz.limite_tentativas:
            raise ValueError("Limite de tentativas atingido!")
        
        tentativa = Tentativa(
            quiz=quiz,
            usuario=usuario,
            respostas=[]
        )

        self.tentativa_repo.salvar(tentativa)

        return tentativa

    def responder_quiz(self, tentativa_id: str, pergunta_id: str, respostas: list[int], tempo: int):
        pergunta_id = self._validar_id(pergunta_id, "pergunta_id")

        tentativa_id = self._validar_id(tentativa_id, "tentativa_id")

        if not isinstance(tempo, int) or isinstance(tempo, bool) or tempo < 0:
            raise ValueError("Tempo inválido")

        pergunta_id = pergunta_id.strip()
        tentativa_id = tentativa_id.strip()

        tentativa = self.tentativa_repo.buscar_por_id(tentativa_id)

        if tentativa is None:
            raise ValueError("Essa tentativa não existe!")

        if tentativa.status_conclusao:
            raise ValueError("Tentativa já concluída!")

        quiz = tentativa.quiz

        if quiz is None:
            raise ValueError("Esse quiz não existe!")

        if pergunta_id not in [p.id for p in quiz.lista_perguntas]:
            raise ValueError("Essa pergunta não pertence ao quiz!")

        if tempo >= quiz.tempo_limite:
             return self.terminar_quiz(tentativa_id, quiz.tempo_limite)

        tentativa.respostas = respostas
        self.tentativa_repo.salvar(tentativa)
        return tentativa
        
    def terminar_quiz(self, tentativa_id: str, tempo_total = 0):
        tentativa_id = self._validar_id(tentativa_id, "tentativa_id")

        tentativa_id = tentativa_id.strip()

        tentativa = self.tentativa_repo.buscar_por_id(tentativa_id)

        if tentativa is None:
            raise ValueError("Essa tentativa não existe!")

        if tentativa.status_conclusao:
            raise ValueError("Tentativa já concluida!")
        
        tentativa.tempo_total = tempo_total
        tentativa.concluir()

        self.tentativa_repo.salvar(tentativa)

        return tentativa