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
        self.conteudo = conteudo

    @property
    def data_gerada(self) -> datetime:
        return self.__data
