from abc import ABC, abstractmethod
from Entidades.quiz import Quiz
import sqlite3

class QuizRepository(ABC):

    @abstractmethod
    def deletar(self, quiz_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, quiz_id: str) -> Quiz:
        pass

    @abstractmethod
    def salvar(self, quiz: Quiz):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Quiz]:
        pass
