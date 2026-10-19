from abc import ABC, abstractmethod
from Entidades.tentativa import Tentativa
import sqlite3

class TentativaRepository(ABC):

    @abstractmethod
    def deletar(self, tentativa_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, tentativa_id: str) -> Tentativa:
        pass

    @abstractmethod
    def salvar(self, tentativa: Tentativa):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Tentativa]:
        pass

    @abstractmethod
    def buscar_por_usuario(self, usuario_id: str) -> list[Tentativa]:
        pass
    
    @abstractmethod
    def buscar_por_usuario_e_quiz(self, usuario_id: str , quiz_id: str) -> list[Tentativa]:
        pass