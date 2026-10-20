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
    def buscar_por_id(self, usuario_id: str) -> Usuario:
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

class UsuarioRepositorySQLite(UsuarioRepository):
    def __init__(self, caminho_db: Path) -> None:
        self.caminho = Path(caminho_db)

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.row_factory = sqlite3.Row
        return conn

    def deletar(self, usuario_id: str):
        with self.conectar() as conn:
            conn.execute("DELETE FROM usuario WHERE id = ?", (usuario_id))

        conn.commit()
        conn.close()

    def buscar_por_id(self, usuario_id: str) -> Usuario:
        with self.conectar() as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE id = ?", (usuario_id,))
            usuario = cursor.fetchone()

        conn.close() 
        return Usuario(id=usuario[0], nome=usuario[1], email=usuario[2], senha=usuario[3])
        
    def salvar(self, usuario: Usuario) -> None:
        with self.conectar() as conn:
            conn.execute("""INSERT INTO usuario (id, username, email, senha)
                            VALUES (?, ?, ?, ?)""", 
                            (usuario.id, usuario.username, usuario.email, usuario. senha))

        conn.commit()
        conn.close

    def listar_todos(self) -> list[Usuario]:
        with closing(self.conectar()) as conn:
            cursor = conn.execute("SELECT * FROM usuario ORDER BY username")

            dados = cursor.fetchall()
            usuario = [Usuario.from_row(linha) for linha in dados]

        return usuario

    def buscar_por_email(self, email: str) -> Usuario:
        with self.conectar() as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE email = ?", (email,))
            usuario = cursor.fetchone()

        conn.close()
        return Usuario(usuario[0], usuario[1], usuario[2], usuario[3])