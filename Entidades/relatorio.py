from datetime import datetime

class Relatorio:
    """
    Representa um relatório gerado pelo sistema.
    
    Atributos:
        data (datetime): Data que o Relatório foi gerado
        nome (str): Nome do Relatório
        tipo (str): Tipo do Relatório
        conteudo (dict): Conteúdo do Relatório
    """
    def __init__(self, 
                nome: str,
                tipo: str,
                conteudo: dict
    ) -> None:
        self.__data = datetime.today()
        self.tipo = tipo
        self.nome = nome
        self.__conteudo = conteudo

    @property
    def data_gerada(self) -> datetime:
        return self.__data
    
    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Nome deve ser do tipo string!")
        self.__nome = valor.strip()

    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, valor: str):
        if not valor.strip() or not isinstance(valor, str):
            raise ValueError("Ripo deve ser do tipo string!")
        self.__tipo = valor.strip()

    @property
    def conteudo(self) -> dict:
        return self.__conteudo
