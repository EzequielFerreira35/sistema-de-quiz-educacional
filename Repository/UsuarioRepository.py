from abc import ABC, abstractmethod
from Entidades.usuario import Usuario
from .sqlite_base import SQLiteBase


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

class UsuarioRepositorySQLite(UsuarioRepository, SQLiteBase):
    def __init__(self) -> None:
        super().__init__()

    def deletar(self, usuario_id: str):
        with self.conexao() as conn:
            conn.execute("DELETE FROM usuario WHERE id = ?", (usuario_id,))

    def buscar_por_id(self, usuario_id: str) -> Usuario | None:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE id = ?", (usuario_id,))
            usuario = cursor.fetchone()

        if usuario is None:
            return

        return Usuario.from_row(usuario)
        
    def salvar(self, usuario: Usuario) -> None:
        with self.conexao() as conn:
            conn.execute("""INSERT INTO usuario (id, username, email, senha)
                            VALUES (?, ?, ?, ?) ON CONFLICT (id) DO UPDATE SET
                            username = excluded.username,
                            email = excluded.email,
                            senha = excluded.senha""", 
                            (usuario.id, usuario.username, usuario.email, usuario. senha))


    def listar_todos(self) -> list[Usuario]:
        with self.conexao() as conn:
            cursor = conn.execute("SELECT * FROM usuario ORDER BY username")

            dados = cursor.fetchall()
            usuario = [Usuario.from_row(linha) for linha in dados]

        return usuario

    def buscar_por_email(self, email: str) -> Usuario | None:
        with self.conexao()as conn:
            cursor = conn.execute("SELECT * FROM usuario WHERE email = ?", (email,))
            usuario = cursor.fetchone()

        if usuario is None:
            return
        
        return Usuario.from_row(usuario)