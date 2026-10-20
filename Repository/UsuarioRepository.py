from abc import ABC, abstractmethod
from Entidades.usuario import Usuario
from pathlib import Path
from contextlib import closing
import sqlite3

class UsuarioRepository(ABC):

    @abstractmethod
    def deletar(self, usuario_id: str):
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: str) -> Usuario | None:
        pass

    @abstractmethod
    def salvar(self, usuario: Usuario) -> None:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Usuario] | None:
        pass

    @abstractmethod
    def buscar_por_email(self, email: str) -> Usuario | None:
        pass

class UsuarioRepositorySQLite(UsuarioRepository):
    def __init__(self, caminho_db: Path) -> None:
        self.caminho = Path(caminho_db)

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, usuario_id: str):
        with closing(self.conectar()) as conn:
            conn.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))

            conn.commit()

    def buscar_por_id(self, usuario_id: str) -> Usuario | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE id = ?", (usuario_id,))
            usuario = cursor.fetchone()

        if usuario is None:
            return

        return Usuario.from_row(usuario)
        
    def salvar(self, usuario: Usuario) -> None:
        with closing(self.conectar()) as conn:
            conn.execute("""INSERT INTO usuario (id, username, email, senha)
                            VALUES (?, ?, ?, ?)""", 
                            (usuario.id, usuario.username, usuario.email, usuario. senha))

            conn.commit()

    def listar_todos(self) -> list[Usuario] | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM usuario ORDER BY username")

            dados = cursor.fetchall()

            if dados is None:
                return 
            
            usuario = [Usuario.from_row(linha) for linha in dados]

        return usuario

    def buscar_por_email(self, email: str) -> Usuario | None:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE email = ?", (email,))
            usuario = cursor.fetchone()

        if usuario is None:
            return
        
        return Usuario.from_row(usuario)