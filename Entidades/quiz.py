import uuid
from .pergunta import Pergunta

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
    TEMPO_LIMITE_PROVISORIO = 1200 # provisorio
    LIMITE_TENTATIVAS = 3 # provisorio

    def __init__(self, 
                titulo: str,
                id = None, 
                tempo_limite: int | None = None, 
                limite_tentativas: int | None = None
    ) -> None:

        self.__id = id if id is not None else str(uuid.uuid4())
        self.titulo = titulo
        self.tempo_limite = tempo_limite if tempo_limite is not None else self.TEMPO_LIMITE_PROVISORIO
        self.limite_tentativas = limite_tentativas if  limite_tentativas is not None else self.LIMITE_TENTATIVAS
        self.__lista_perguntas = []

    def __len__(self):
        return len(self.__lista_perguntas)

    def __iter__(self):
        return iter(self.__lista_perguntas)
    
    @staticmethod
    def _inteiro_positovo(valor, nome):
        if isinstance(valor, bool) or not isinstance(valor, int) or valor <=0:
            raise ValueError(f"{nome} deve ser um inteiro positivo")
        return valor
    
    @property
    def id(self) -> str:
        return self.__id

    @property
    def titulo(self) -> str:
        return self.__titulo

    @titulo.setter
    def titulo(self, valor: str):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O Título deve ser uma string não vazia!")
        
        self.__titulo = valor.strip()

    @property
    def tempo_limite(self) -> int:
        return self.__tempo_limite

    @tempo_limite.setter
    def tempo_limite(self, valor: int):
        self.__tempo_limite = self._inteiro_positovo(valor, "tempo_limite")

    @property
    def limite_tentativas(self) -> int:
        return self.__limite_tentativas

    @limite_tentativas.setter
    def limite_tentativas(self, valor):
        self.__limite_tentativas = self._inteiro_positovo(valor, "limite_tentativas")

    @property
    def lista_perguntas(self) -> list[Pergunta]:
        return self.__lista_perguntas

    def adicionar_pergunta(self, pergunta: Pergunta) -> bool:
        if not isinstance(pergunta, Pergunta):
            raise TypeError("Só é possivel adicionar obejtos do tipo Pergunta!")
        
        if pergunta in self.__lista_perguntas:
            return False

        self.__lista_perguntas.append(pergunta)
        return True
    
    def calcular_pontuacao_maxima(self) -> float:
        return float(sum(p.peso() for p in self.__lista_perguntas))

    @classmethod
    def from_row(cls, linha):
        quiz = cls(
            id = linha["id"],
            titulo = linha["titulo"],
            tempo_limite = linha["tempo_limite"],
            limite_tentativas = linha["limite_tentativas"]
        )

        return quiz