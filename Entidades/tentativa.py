import uuid
from usuario import Usuario
from quiz import Quiz

class Tentativa:
    """
    Representa o registro de uma execução do Quiz por um Usuário.

    Atributos:
        - id (str): Número de Identificação da Tentativa
        - usuario (Usuario): Usuário ao qual a tentativa pertence
        - quiz (Quiz): Quiz ao qual a tentativa pertence
        - repostas (list): Respostas do Usuário
        - pontuacao (int): Pontuação obtida pelo Usuário
        - tempo_total (int): Tempo total gasto para responder o Quiz
        - status_conclusao (bool): Representa se o quiz foi concluído ou não
    """
    def __init__(self,
                id: str,
                usuario: Usuario,
                quiz: Quiz,
                respostas: list,
                pontuacao: int,
                tempo_total: int,  
                status_conclusao: bool,
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.usuario = usuario
        self.quiz = quiz
        self.respostas = respostas
        self.pontuacao = pontuacao
        self.tempo_total = tempo_total
        self.status_conclusao = status_conclusao

    @property
    def id(self) -> str:
        return self.__id

    def calcular_pontuacao(self) -> int:
        ...

    def taxa_acertos(self) -> float:
        ...
