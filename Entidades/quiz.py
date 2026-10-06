import uuid
from pergunta import Pergunta
class Quiz:
    TEMPO_LIMITE_PROVISORIO = 1200 # provisorio
    LIMITE_TENTATIVAS = 3
    """
    Essa classe representa um quiz  com um conjunto de perguntas com título, limite de tentativas, tempo limite(opcional) 
    e pontuação máxima calculada automaticamente.

    Atributos:
        - id (str): Número de identificação do Quiz
        - titulo (str): Título do Quiz
        - tempo_limite (int): Tempo limite do Quiz
        - limite_tentativas (int): Limite de Tentativas do Quiz
        - lista_perguntas (list): Lista de perguntas do Quiz
    """
    def __init__(self, titulo: str ) -> None:
        self.__id = str(uuid.uuid4())
        self.titulo = titulo
        self.__tempo_limite = self.TEMPO_LIMITE_PROVISORIO
        self.__limite_tentativas = self.LIMITE_TENTATIVAS
        self.__lista_perguntas = []

    @property
    def id(self) -> str:
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not valor.strip():
            raise ValueError("O Título não pode ser vazio!")
        
        if not isinstance(valor, str):
            raise ValueError("O Título deve ser do tipo string!")
        
        self.__titulo = valor

    @property
    def tempo_limite(self) -> int:
        return self.__tempo_limite

    @property
    def limite_tentaticas(self) -> int:
        return self.__limite_tentativas

    @property
    def lista_perguntas(self) -> list[Pergunta]:
        return self.__lista_perguntas

    def adicionar_perguntas(self, pergunta: Pergunta) -> bool:
        if not isinstance(pergunta, Pergunta):
            raise TypeError("Só é possivel adicionar obejtos do tipo Pergunta!")
        
        if any(p.id == pergunta.id for p in self.__lista_perguntas): # Verifica se a pergunta já existe na lista
            return False

        self.__lista_perguntas.append(pergunta)
        return True
    
    def calcular_pontuacao_maxima(self) -> float:
        return float(sum(p.peso() for p in self.__lista_perguntas))