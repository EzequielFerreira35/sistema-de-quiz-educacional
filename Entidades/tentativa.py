from __future__ import annotations
from typing import TYPE_CHECKING
from datetime import datetime

import uuid


if TYPE_CHECKING:
    from .usuario import Usuario
    from .quiz import Quiz

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
                quiz: Quiz,
                respostas: list,
                usuario: Usuario,
                data: str | None = None,
                tempo_total: int = 0,
                id: str | None = None,
                pontuacao: float = 0.0,
                status_conclusao: bool = False
    ) -> None:
        
        self.__id = id if id is not None else str(uuid.uuid4())
        self.__usuario = usuario
        self.__quiz = quiz
        self.data = data if data is not None else str(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        self.respostas = respostas if respostas is not None else []
        self.__pontuacao = pontuacao
        self.tempo_total = tempo_total
        self.__status_conclusao = status_conclusao

    @property
    def id(self) -> str:
        return self.__id

    @property
    def quiz(self) -> Quiz:
        return self.__quiz

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, valor: str):
        formato_padrao = "%d/%m/%Y %H:%M:%S"
        try:
            datetime.strptime(valor, formato_padrao)
        except:
            raise ValueError("Data inválida")

        self.__data = valor

    @property
    def respostas(self) -> list:
        return self.__respostas

    @respostas.setter
    def respostas(self, valor: list[int]):
        if not isinstance(valor, list):
            raise ValueError("Respostas deve ser uma lista de índices!")
        perguntas = self.__quiz.lista_perguntas

        if len(valor) > len(perguntas):
            raise ValueError("Há mais respostas do que perguntas")

        for resposta, pergunta in zip(valor, perguntas):
            if resposta is None:
                continue

            if isinstance(resposta, bool) or not isinstance(resposta, int) or not 0 <= resposta <= len(pergunta.alternativas):
                raise ValueError("Resposta inválida")
            
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
    def status_conclusao(self) -> bool | None:
        return self.__status_conclusao
    
    def calcular_pontuacao(self) -> float:
        p = self.__quiz.lista_perguntas
        total = 0

        for resposta, pergunta in zip(self.respostas, p):
            if resposta is not None and pergunta.verificar_resposta(resposta):
                total += pergunta.peso()

        self.__pontuacao = float(total)
        return self.__pontuacao

    def concluir(self) -> float:
        self.calcular_pontuacao() 
        self.__status_conclusao = True
        return self.__pontuacao
    
    def taxa_acertos(self) -> float:
        p = self.__quiz.lista_perguntas
        acertos = 0
        if not p:
            return 0.0
        
        for resposta, pergunta in zip(self.respostas, p):
            if resposta is not None and pergunta.verificar_resposta(resposta):
                acertos += 1

        return acertos / len(p)

