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
                tempo_total: int,  
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.__usuario = usuario
        self.__quiz = quiz
        self.respostas = respostas
        self.__pontuacao = 0.0
        self.tempo_total = tempo_total
        self.__status_conclusao = False

    @property
    def id(self) -> str:
        return self.__id

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def quiz(self) -> Quiz:
        return self.__quiz

    @property
    def respostas(self) -> list:
        return self.__respostas

    @respostas.setter
    def respostas(self, valor: list[int]):
        if not isinstance(valor, list):
            raise ValueError("Respostas deve ser uma lista de índices!")

        self.__respostas = list(valor)

    @property
    def pontuacao(self) -> float:
        return self.__pontuacao

    @property
    def tempo_total(self) -> int:
        return self.__tempo_total

    @tempo_total.setter
    def tempo_total(self, valor: int):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("Tempo total não pode ser negativo!")

        self.__tempo_total = valor

    @property
    def status_conclusao(self) -> bool:
        return self.__status_conclusao
    
    def calcular_pontuacao(self) -> float:
        p = self.__quiz.lista_perguntas
        total = 0

        for resposta, pergunta in zip(self.respostas, p):
            if resposta is not None and pergunta.verificar_resposta(resposta):
                total += pergunta.peso()

        self.__pontuacao = total
        self.__status_conclusao = len(self.respostas) == len(p)
        return total

    def taxa_acertos(self) -> float:
        p = self.__quiz.lista_perguntas
        acertos = 0

        for resposta, pergunta in zip(self.respostas, p):
            if resposta is not None and pergunta.verificar_resposta(resposta):
                acertos += 1

        return acertos / len(p)
