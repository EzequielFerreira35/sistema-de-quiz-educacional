from abc import ABC, abstractmethod
from Entidades.relatorio import Relatorio
from pathlib import Path
import sqlite3

class TentativaRepository(ABC):

    @abstractmethod
    def criar_tabela(self):
        pass

    @abstractmethod
    def deletar(self, relatorio_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, realtorio_id: str) -> Relatorio:
        pass

    @abstractmethod
    def salvar(self, relatorio: Relatorio):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Relatorio]:
        pass

    