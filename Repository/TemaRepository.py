from abc import ABC, abstractmethod
from Entidades.tema import Tema
from contextlib import closing
import sqlite3

class TemaRepository(ABC):

    @abstractmethod
    def deletar(self, tema_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, tema_id: str) -> Tema | None:
        pass

    @abstractmethod
    def salvar(self, tema: Tema):
        pass

    @abstractmethod
    def listar_todos(self) -> list[Tema]:
        pass


class TemaRepositorySQLite(TemaRepository):
    def __init__(self, caminho_db) -> None:
        self.caminho = caminho_db

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, tema_id: str):
        with closing(self.conectar()) as conn:
            conn.execute("DELETE FROM tema WHERE id = ?", (tema_id,))

            conn.commit()

    def buscar_por_id(self, tema_id: str) -> Tema | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM tema WHERE id = ?", (tema_id,))
            tema = cursor.fetchone()

        if tema is None:
            return
        
        return Tema.from_row(tema)

    def salvar(self, tema: Tema):
        with closing(self.conectar()) as conn:
            conn.execute("""INSERT INTO tema (id, nome)
                            VALUES (?, ?)""", (tema.id, tema.nome))

            conn.commit()

    def listar_todos(self) -> list[Tema]:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM tema ORDER BY nome")
            dados = cursor.fetchall()
            
        return [Tema.from_row(linha) for linha in dados]
