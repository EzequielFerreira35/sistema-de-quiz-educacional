from abc import ABC, abstractmethod
from Entidades.usuario import Usuario
from pathlib import Path
import sqlite3

class UsuarioRepository(ABC):

    @abstractmethod
    def criar_tabela(self):
        pass

    @abstractmethod
    def deletar(self, usuario_id: str):
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: str):
        pass

    @abstractmethod
    def salvar(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Usuario]:
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario:
        pass

