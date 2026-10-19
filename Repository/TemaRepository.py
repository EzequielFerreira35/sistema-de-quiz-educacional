from abc import ABC, abstractmethod
from Entidades.tema import Tema
import sqlite3

class TemaRepository(ABC):

    @abstractmethod
    def deletar(self, tema_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, tema_id: str) -> Tema:
        pass

    @abstractmethod
    def salvar(self, tema: Tema):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Tema]:
        pass
