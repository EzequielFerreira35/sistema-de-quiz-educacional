import uuid



class Tema:
    """
    Essa classe representa o assunto ao qual uma pergunta pertence.
    
    Atributos:
        - id (str): Número de identificação do Tema
        - nome (str): Nome do Tema
    """
    def __init__(self, nome: str, 
                id: str | None = None
    ) -> None:
    
        self.__id = id if id is not None else str(uuid.uuid4())
        self.nome = nome

    @property
    def id(self) -> str:
        return self.__id

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, valor: str) -> None: 
        if not isinstance(valor, str):
            raise ValueError("O nome do tema deve ser do tipo string!")
        
        if not valor.strip():
            raise ValueError("O nome do tema não pode ser vazio!")
        
        self.__nome = valor

    def __str__(self) -> str:
        return f"Tema: {self.nome}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value ,Tema):
            return NotImplemented

        return self.id == value.id

    @classmethod
    def from_row(cls, linha):
        tema = cls(
            nome = linha["nome"],
            id = linha["id"] 
        )
        return tema