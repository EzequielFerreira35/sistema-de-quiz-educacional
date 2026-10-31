import uuid
from .tema import Tema
from configmanager import ConfigManager

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
    _CONFIG = ConfigManager()
    PESO_PROVISORIO = _CONFIG.pergunta_peso 
    MIN = _CONFIG.qtd_alternativas[0]
    MAX = _CONFIG.qtd_alternativas[1]

    def __init__(self,
                tema: Tema,
                enunciado: str, 
                alternativas: list[str], 
                indice_resposta: int, 
                dificuldade: str,
                id: str | None = None
    ) -> None:
        
        self.__id = id if id is not None else str(uuid.uuid4())
        self.tema = tema
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.indice_resposta = indice_resposta
        self.dificuldade = dificuldade

    def __str__(self) -> str:
        return f"{self.enunciado} (Dificuldade: {self.dificuldade})"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Pergunta):
            return NotImplemented

        return (
            self.enunciado.strip().casefold() == value.enunciado.strip().casefold()
            and self.tema == value.tema
        )

    def __hash__(self) -> int:
        return hash((self.enunciado.strip().casefold(), self.tema))

    @property
    def id(self) -> str:
        return self.__id

    @property
    def tema(self) -> Tema:
        return self.__tema

    @tema.setter
    def tema(self, valor: Tema):
        if not isinstance(valor, Tema):
            raise ValueError("O valor tema deve ser do tipo Tema!")
        self.__tema = valor

    @property
    def enunciado(self) -> str:
        return self.__enunciado
    
    @enunciado.setter
    def enunciado(self, valor: str):      
        if not isinstance(valor, str):
            raise ValueError("O enunciado deve ser do tipo string!")
        
        if not valor.strip():
            raise ValueError("O enunciado não pode ser vazio!")

        self.__enunciado = valor.strip()

    @property
    def alternativas(self) -> list[str]:
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, valor: list) -> None:
        if not isinstance(valor, list):
            raise ValueError("As alternativas devem ser uma lista!")

        if not all(isinstance(alt, str) for alt in valor):
            raise ValueError("Todas as alternativas devem ser string")

        lista_copia = [str(alt).strip() for alt in valor]

        if "" in lista_copia:
            raise ValueError("A lista não pode conter alternativas vazias!")

        if not self.verificar_qtd_resposta(lista_copia):
            raise ValueError(f"A pergunta deve ter entre {self.MIN} a {self.MAX} alternativas!")
        
        if self.verificar_duplicata(lista_copia):
            raise ValueError("Não pode ter alternativas duplicadas!")

        self.__alternativas = lista_copia

    
    @property
    def indice_resposta(self) -> int:
        return self.__indice_resposta

    @indice_resposta.setter
    def indice_resposta(self, valor: int) -> None:
        if not isinstance(valor, int) or isinstance(valor, bool):
            raise ValueError("Indice da resposta deve ser do tipo int!")
        
        if not 0 <= valor < len(self.alternativas):
            raise ValueError("Indice da resposta fora do intervalo!")

        self.__indice_resposta = valor

    @property
    def dificuldade(self) -> str:
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor: str):
        if not isinstance(valor, str):
            raise ValueError("A dificuldade deve ser do tipo string!")

        valor = valor.lower()

        if valor not in self.PESO_PROVISORIO:
            print(valor, self.PESO_PROVISORIO)
            raise ValueError("A dificuldade deve ser uma das três opções: fácil, médio ou difícil")
        
        self.__dificuldade = valor
    
    def verificar_resposta(self, indice: int) -> bool:
        return indice == self.__indice_resposta

    @staticmethod
    def verificar_duplicata(alternativas: list[str]) -> bool:
        padrao = [str(x).strip().lower() for x in alternativas]
        return len(padrao) != len(set(padrao))

    @classmethod
    def verificar_qtd_resposta(cls, alternativas: list[str]) -> bool:
        tamanho = len(alternativas)
        return cls.MIN <= tamanho <= cls.MAX
    
    def peso(self) -> int:
        return self.PESO_PROVISORIO[self.__dificuldade]

    @classmethod
    def from_row(cls, linha):
        pergunta = cls(
            id = linha["id"],
            tema = Tema(
                nome=linha["nome_tema"],
                id=linha["id_tema"]),
            enunciado = linha["enunciado"],
            indice_resposta= linha["indice_resposta"],
            dificuldade = linha["dificuldade"],
            alternativas = linha["alternativas"]
                       )
        return pergunta

