from abc import ABC, abstractmethod
from Entidades.tema import Tema
from contextlib import closing
from .sqlite_base import SQLiteBase

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


class TemaRepositorySQLite(TemaRepository, SQLiteBase):
    def __init__(self, caminho_db) -> None:
        super().__init__(caminho_db)


    def deletar(self, tema_id: str):
        with self.conexao() as conn:
            conn.execute("DELETE FROM tema WHERE id = ?", (tema_id,))

    def buscar_por_id(self, tema_id: str) -> Tema | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM tema WHERE id = ?", (tema_id,))
            tema = cursor.fetchone()

        if tema is None:
            return
        
        return Tema.from_row(tema)

    def salvar(self, tema: Tema):
        with self.conexao() as conn:
            conn.execute("""INSERT INTO tema (id, nome)
                            VALUES (?, ?)""", (tema.id, tema.nome))

    def listar_todos(self) -> list[Tema]:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM tema ORDER BY nome")
            dados = cursor.fetchall()
            
        return [Tema.from_row(linha) for linha in dados]
