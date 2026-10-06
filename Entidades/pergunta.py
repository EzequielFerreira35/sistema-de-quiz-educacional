import uuid
from tema import Tema
class Pergunta:
    PESO_PROVISORIO = {"facil": 1, "medio": 2, "dificil": 3} # Variavel provisória que será removida depois de criar as settings
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
        if not valor.strip():
            raise ValueError("O enunciado não pode ser vazio!")
        
        if not isinstance(valor, str):
            raise ValueError("O enunciado deve ser do tipo string!")

        self.__enunciado = valor

    @property
    def alternativas(self) -> list[str]:
        return self.__alternativas

    @alternativas.setter
    def alternativas(self, valor: list) -> None:
        lista_copia = list(valor)

        if not self.verificar_qtd_resposta(lista_copia):
            raise ValueError("A pergunta deve ter entre 2 a 5 alternativas!")
        
        if self.verificar_duplicata(lista_copia):
            raise ValueError("Não pode ter alternativas duplicadas!")
        self.__alternativas = lista_copia

    
    @property
    def indice_resposta(self) -> int:
        return self.__indice_resposta

    @indice_resposta.setter
    def indice_resposta(self, valor: int) -> None:
        if not isinstance(valor, int):
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
            raise ValueError("A dificuldade deve ser uma das três opções: fácil, médio ou difícil")
        
        self.__dificuldade = valor
    
    def verificar_resposta(self, indice: int) -> bool:
        return indice == self.__indice_resposta

    @staticmethod
    def verificar_duplicata(alternativas: list[str]) -> bool:
        padrao = [str(x).strip().lower() for x in alternativas]
        return len(padrao) != len(set(padrao))

    @staticmethod
    def verificar_qtd_resposta(alternativas: list[str]) -> bool:
        tamanho = len(alternativas)
        return 2 <= tamanho <= 5 # Provisorio(enquanto ainda não tem as settings)
    
    def peso(self) -> int:
        return self.PESO_PROVISORIO[self.__dificuldade]