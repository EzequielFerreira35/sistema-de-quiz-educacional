import re

from Entidades.usuario import Usuario
from Repository.UsuarioRepository import UsuarioRepository
from .hash import HashServices


class UsuarioService:
    """
    Gerencia as regras de negócio e o ciclo de vida dos Usuários.
    Herda atributos e métodos da Classe BaseService.
    """
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario | None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome deve ser uma string não vazia!")
       
        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email deve ser uma string não vazia!")
       
        if not isinstance(senha, str) or not senha.strip():
            raise ValueError("Senha deve ser uma string não vazia!")
        
        if len(senha) < 8:
            raise ValueError("A senha deve conter pelomenos 8 caracteres!")

        if not re.search(r"[A-Z]", senha):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        
        if not re.search(r"[a-z]", senha):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula.")
        
        if not re.search(r"[0-9]", senha):
            raise ValueError("A senha deve conter pelo menos uma números.")
        
        if not re.search(r"[!@#$%¨&*]", senha):
            raise ValueError("A senha deve conter pelo menos um caractere especial.")

        if self.repository.buscar_por_email(email):
            raise ValueError("Email já cadastrado")


        senha = HashServices.criptografar(senha)
        usuario = Usuario(nome, email, senha)

        self.repository.salvar(usuario)

        return usuario

    def atualizar_email(self, email: str, usuario_id: str) -> Usuario:
        if not isinstance(email, str) or not email.strip():
            raise ValueError("Email deve ser uma string não vazia!")

        email = email.strip()

        usuario = self.repository.buscar_por_email(email)
        usuario_por_id = self.repository.buscar_por_id(usuario_id)

        if usuario is None:
            raise ValueError(f"Não existe usuário com email: {email}")

        if usuario_por_id.email != email:
            raise ValueError("Não é possível alterar o email!")


        usuario.email = email

        self.repository.salvar(usuario)

        return usuario