import uuid
import re
from tentativa import Tentativa

class Usuario:
    """
    Representa um Usuário.

    Atributos:
        - id (str): Número de identificação do Usuário
        - username (str): Nome do Usuário
        - email (str): Email do Usuário
        - senha (str): Senha do Usupario
        - tentativas (list): Lista de Tentativas
    """
    def __init__(self, 
                nome: str,
                email: str, 
                senha: str,
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.username = nome
        self.email = email
        self.senha = senha
        self.__tentativas = []

    @property
    def id(self) -> str:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Nome deve ser do tipo string!")
        self.__username = valor.strip()
    
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Email deve ser do tipo string!")
        
        padrao = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(padrao, valor):
            self.__email = valor
        else:
            raise ValueError("Email fora dos padrões!")

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Senha deve ser do tipo string!")
        if len(valor) < 8:
            raise ValueError("A senha deve conter pelomenos 8 caracteres!")

        if not re.search(r"[A-Z]", valor):
            raise ValueError("A senha deve conter pelo menos uma letra maiúscula.")
        
        if not re.search(r"[a-z]", valor):
            raise ValueError("A senha deve conter pelo menos uma letra minúscula.")
        
        if not re.search(r"[0-9]", valor):
            raise ValueError("A senha deve conter pelo menos uma números.")
        
        if not re.search(r"[!@#$%¨&*]", valor):
            raise ValueError("A senha deve conter pelo menos um caractere especial.")
        
        self.__senha = valor
    

    @property
    def tentativas(self):
        return self.__tentativas

    def registrar_tentativa(self, tentativa: Tentativa):
        self.__tentativas.append(tentativa)