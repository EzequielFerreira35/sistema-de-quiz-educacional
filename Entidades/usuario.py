from __future__ import annotations
from typing import TYPE_CHECKING

import uuid
import re


if TYPE_CHECKING:
    from .tentativa import Tentativa

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
                id: str | None = None
    ) -> None:
        
        self.__id = id if id is not None else str(uuid.uuid4())
        self.username = nome
        self.email = email
        self.senha = senha
        self.__tentativas = []

    def __str__(self) -> str:
        return f"id={self.id}, username={self.username}, email={self.email}, senha={self.senha}, tentativas={self.tentativas}"

    @property
    def id(self) -> str:
        return self.__id

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Nome deve ser do tipo string não vazio!")
        self.__username = valor.strip()
    
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Email deve ser do tipo string não vazio!")

        valor =  valor.strip()
        
        padrao = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,}$"

        if re.match(padrao, valor):
            self.__email = valor
        else:
            raise ValueError("Email fora dos padrões!")

    @property
    def senha(self) -> str:
        return self.__senha_hash

    @senha.setter
    def senha(self, valor: str):
        self.__senha_hash = valor

    @property
    def tentativas(self):
        return self.__tentativas

    def registrar_tentativa(self, tentativa: Tentativa):
        self.__tentativas.append(tentativa)

    @classmethod
    def from_row(cls, linha):
        usuario = cls(
            id=linha["id"], 
            nome=linha["username"], 
            email=linha["email"], 
            senha=linha["senha"]
        )
        
        return usuario