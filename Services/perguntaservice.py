from Entidades.pergunta import Pergunta
from Entidades.tema import Tema
from Repository.PerguntaRepository import PerguntaRepository
from Repository.TemaRepository import TemaRepository
from Repository.QuizRepository import QuizRepository

class PerguntaService:
    """
    Gerencia as regras de negócio e o ciclo de vida das Perguntas.
    Herda atributos e métodos da Classe BaseService.
    """
    def __init__(self, pergunta_repo: PerguntaRepository, tema_repo: TemaRepository, quiz_repo: QuizRepository):
        self.pergunta_repo = pergunta_repo
        self.tema_repo = tema_repo
        self.quiz_repo = quiz_repo

    def criar_pergunta(self, enunciado: str, tema: Tema, alternativas: list[str], indice_resposta: int, dificuldade: str):
        pergunta = Pergunta(
            tema=tema,
            enunciado=enunciado,
            alternativas=alternativas,
            indice_resposta=indice_resposta,
            dificuldade=dificuldade
        )

        if self.tema_repo.buscar_por_id(tema.id) is None:
            ValueError("Tema inválido")

        perguntas_tema =  self.pergunta_repo.listar_por_tema(tema.id)

        if pergunta in perguntas_tema:
            ValueError("Pergunta duplicata: Essa pergunta já existe no Tema!")

        self.pergunta_repo.salvar(pergunta)

        return pergunta

    def editar_pergunta(self, pergunta_id: str, enunciado = None, alternativas = None, indice_resposta = None, dificuldade = None):
        if not isinstance(pergunta_id, str) or not pergunta_id.strip():
            raise ValueError("O id da pergunta deve ser uma string não vazia!")

        pergunta_id = pergunta_id.strip()

        pergunta = self.pergunta_repo.buscar_por_id(pergunta_id)

        if enunciado is not None:
            pergunta.enunciado = enunciado

        if alternativas is not None:
            pergunta.alternativas = alternativas
        if indice_resposta is not None:
            pergunta.indice_resposta = indice_resposta

        if dificuldade is not None:   
            pergunta.dificuldade = dificuldade


        for p in self.pergunta_repo.listar_por_tema(pergunta.tema.id):
            if pergunta == p and pergunta.id != p.id:
                raise ValueError("Pergunta duplicata: Essa pergunta já existe no Tema!")
            
        self.pergunta_repo.salvar(pergunta)

        return pergunta

    def listar_por_tema(self, tema_id):
        if not isinstance(tema_id, str) or not tema_id.strip():
            raise ValueError("O id do tema deve ser uma string não vazia!")

        if self.tema_repo.buscar_por_id(tema_id) is None:
            raise ValueError("Esse tema não existe!")
        
        perguntas = self.pergunta_repo.listar_por_tema(tema_id)

        return perguntas
