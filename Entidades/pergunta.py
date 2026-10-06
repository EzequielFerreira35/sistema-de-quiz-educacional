import uuid
from tema import Tema
class Pergunta:
    """
    Essa classe representa uma pergunta de múltipla escolha.

    Atributos:
        - id (str): Número de identificação da Pergunta
        - tema (Tema): Tema da pergunta
        - enunciado (str): Enunciado da pergunta
        - alternativas l(ist[str]): Alternativas da Pergunta
        - indice_respota (int): Indice que representa qual alternativa é a correta
        - dificuldade (str): Dificuldade da Pergunta
    """

    def __init__(self,
                tema: Tema,
                enunciado: str, 
                alternativas: list[str], 
                indice_resposta: int, 
                dificuldade: str
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.tema = tema
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.__indice_resposta = indice_resposta
        self.dificuldade = dificuldade

    @property
    def id(self) -> str:
        return self.__id

    @property
    def indice_resposta(self) -> int:
        return self.__indice_resposta

    @indice_resposta.setter
    def indice_resposta(self, valor: int) -> None:
        self.__indice_resposta = valor

    def verificar_resposta(self) -> bool:
        ...
    def verificar_duplicata(self) -> bool:
        ...
    def verificar_qtd_resposta(self) -> bool:
        ...
    def peso(self) -> int:
        ...