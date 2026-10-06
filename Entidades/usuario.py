import uuid

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
                tentativas: list
    ) -> None:
        self.__id = str(uuid.uuid4())
        self.username = nome
        self.email = email
        self.__senha = senha
        self.__tentativas = tentativas

    @property
    def id(self) -> str:
        return self.__id

    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, nova_senha: str) -> None:
        self.__senha = nova_senha

    @property
    def tentativas(self):
        return self.__tentativas

    @tentativas.setter
    def tentativas(self, tentativa):
        self.__tentativas.append(tentativa)