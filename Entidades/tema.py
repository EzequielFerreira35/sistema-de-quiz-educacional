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
