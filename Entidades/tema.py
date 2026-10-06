import uuid

class Tema:
    """
    Essa classe representa o assunto ao qual uma pergunta pertence.
    
    Atributos:
        - id (str): Número de identificação do Tema
        - nome (str): Número de identificação do Nome
    """
    def __init__(self, nome) -> None:
        self.__id = str(uuid.uuid4())
        self.__nome = nome

    @property
    def id(self) -> str:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None: 
        if not valor.strip():
            raise ValueError("O nome do tema não pode ser vazio!")
        if not isinstance(valor, str):
            raise ValueError("O nome do tema deve ser do tipo string!")

        self.__nome = valor