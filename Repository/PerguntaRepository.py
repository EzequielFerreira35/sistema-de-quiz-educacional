from abc import ABC, abstractmethod
from Entidades.pergunta import Pergunta
import sqlite3

class PerguntaRepository(ABC):

    @abstractmethod
    def deletar(self, pergunta_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, pergunta_id: str) -> Pergunta:
        pass

    @abstractmethod
    def salvar(self, pergunta: Pergunta):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Pergunta]:
        pass

    @abstractmethod
    def listar_por_tema(self) -> list[Pergunta]:
        pass

    @abstractmethod
    def listar_por_quiz(self) -> list[Pergunta]:
        pass