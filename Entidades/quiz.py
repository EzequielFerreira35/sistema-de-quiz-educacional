import uuid
from pergunta import Pergunta
class Quiz:
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
    def __init__(self, 
                titulo: str, 
                tempo_limite: int, 
                limite_tentativas: int, 
                lista_perguntas: list[Pergunta]
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.titulo = titulo
        self.tempo_limite = tempo_limite
        self.limite_tentativas = limite_tentativas
        self.__lista_pergutnas = lista_perguntas

    @property
    def id(self) -> str:
        return self.__id

    @property
    def lista_perguntas(self) -> list[Pergunta]:
        return self.__lista_pergutnas

    @lista_perguntas.setter
    def lista_perguntas(self, pergunta: Pergunta) -> None:
        self.__lista_pergutnas.append(pergunta)

    def calcular_pontuacao_maxima(self):
        ...