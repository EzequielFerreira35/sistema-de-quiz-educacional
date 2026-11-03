from src.Repository.TemaRepository import TemaRepository
from src.Repository.PerguntaRepository import PerguntaRepository
from src.Entidades.tema import Tema
from .baseservice import BaseService
from .mixins import ValidadorIdMixin


class TemaService(BaseService, ValidadorIdMixin):
    """
    Gerencia as regras de negócio e o ciclo de vida dos Temas.
    Herda atributos e métodos da Classe BaseService.
    """
    def __init__(self, repository_tema: TemaRepository, repository_pergunta: PerguntaRepository):
        super().__init__()
        self.repository_tema = repository_tema
        self.repository_pergunta = repository_pergunta

    def criar_tema(self, nome: str) -> Tema | None:
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("Nome do Tema deve ser uma string não vazia!")

        nome = nome.strip()
        temas = self.repository_tema.listar_todos()

        if nome.casefold() in [tema.nome.casefold() for tema in temas]:
            raise ValueError("Já existe um Tema com esse nome!")
        
    
        tema = Tema(nome=nome)
        self.repository_tema.salvar(tema)
        return tema            

    def deletar_tema(self, tema_id):
        tema_id = self._validar_id(tema_id, "validar_id")

        tema_id = tema_id.strip()
        
        if self.repository_tema.buscar_por_id(tema_id) is None:
            raise ValueError("Não é possível deletar temas que não existem!")

        if self.repository_pergunta.listar_por_tema(tema_id):
            raise ValueError("Não é possivível deletar temas quesjá tem perguntas cadastradas!")
        
        self.repository_tema.deletar(tema_id)


