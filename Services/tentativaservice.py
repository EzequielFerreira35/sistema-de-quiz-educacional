from Repository.TentativaRepository import TentativaRepository
from Repository.QuizRepository import QuizRepository
from Repository.UsuarioRepository import UsuarioRepository
from Entidades.tentativa import Tentativa
from configmanager import ConfigManager

class TentativaService:
    """
    Gerencia as regras de negócio e o ciclo de vida das Tentativas.
    Herda atributos e métodos da Classe BaseService.
    """
    _CONFIG = ConfigManager()

    def __init__(self, usuario_repo: UsuarioRepository, quiz_repo: QuizRepository, tentativa_repo: TentativaRepository):
        self.usuario_repo = usuario_repo
        self.quiz_repo = quiz_repo
        self.tentativa_repo = tentativa_repo

    def iniciar_quiz(self, usuario_id: str, quiz_id: str):
        if not isinstance(usuario_id, str) or not usuario_id.strip():
            raise ValueError("Usuario_id deve ser uma string não vazia!")  

        if not isinstance(quiz_id, str) or not quiz_id.strip():
            raise ValueError("Quiz_id deve ser uma string não vazia!")

        quiz_id = quiz_id.strip()
        usuario_id = usuario_id.strip()

        quiz = self.quiz_repo.buscar_por_id(quiz_id)
        usuario = self.usuario_repo.buscar_por_id(usuario_id)

        if quiz is None:
            raise ValueError("Esse Quiz não existe!")

        if usuario is None:
            raise ValueError("Esse Usuário não existe!")

        if self.tentativa_repo.contar_por_usuario_e_quiz(usuario_id, quiz_id) >= self._CONFIG.max_tentativas_por_quiz:
            raise ValueError("Limite de tentativas atingido!")
        
        tentativa = Tentativa(
            quiz=quiz,
            usuario=usuario,
            respostas=[]
        )

        self.tentativa_repo.salvar(tentativa)

        return tentativa

    def responder_quiz(self, tentativa_id: str, pergunta_id: str, respostas: list[int], tempo: int):
        if not isinstance(pergunta_id, str) or not pergunta_id.strip():
            raise ValueError("O id da pergunta deve ser uma string não vazia!")

        if not isinstance(tentativa_id, str) or not tentativa_id.strip():
            raise ValueError("O id da tentativa deve ser uma string não vazia!")

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

        if tempo > quiz.tempo_limite:
            self.terminar_quiz(tentativa_id, quiz.tempo_limite)

        tentativa.respostas = respostas
        self.tentativa_repo.salvar(tentativa)
        return tentativa
        
    def terminar_quiz(self, tentativa_id: str, tempo_total = 0):
        if not isinstance(tentativa_id, str) or not tentativa_id.strip():
            raise ValueError("O id da tentativa deve ser uma string não vazia!")

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