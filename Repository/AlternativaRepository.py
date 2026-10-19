from abc import ABC, abstractmethod
from Entidades.pergunta import Pergunta
import sqlite3

class AlternativaRepository(ABC):

    @abstractmethod
    def deletar(self, alternativa_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, alternativa_id: str) -> Pergunta:
        pass

    @abstractmethod
    def salvar(self, pergunta: Pergunta):
        pass

    @abstractmethod
    def listar_por_pergunta(self) -> list[Pergunta]:
        pass



class RespostaTentativaRepository(ABC):

    @abstractmethod
    def deletar(self, alternativa_id: str):   
        pass

    @abstractmethod
    def buscar_por_id(self, alternativa_id: str) -> Pergunta:
        pass

    @abstractmethod
    def salvar(self, pergunta: Pergunta):
        pass

    @abstractmethod
    def listar_por_tentativa(self) -> list[Pergunta]:
        pass
