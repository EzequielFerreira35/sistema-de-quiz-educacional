from Repository.TemaRepository import TemaRepository
from Entidades.tema import Tema


class TemaService():
    """
    Gerencia as regras de negócio e o ciclo de vida dos Temas.
    Herda atributos e métodos da Classe BaseService.
    """
    def __init__(self, repository: TemaRepository):
        self.repository = repository

    def criar_tema(self, nome: str) -> Tema | None:
        if not isinstance(nome, str) or not nome.strip():
            return

        nome = nome.strip()
        temas = self.repository.listar_todos()

        if nome.casefold() in [tema.nome.casefold() for tema in temas]:
            raise ValueError("Já existe um Tema com esse nome!")
        
    
        tema = Tema(nome=nome)
        self.repository.salvar(tema)
        return tema

            

    def deletar_tema(self, tema_id):
        if not isinstance(tema_id, str) or not tema_id.strip():
            return
        
        if self.repository.buscar_por_id(tema_id) is None:
            raise ValueError("Não é possível deletar temas que não existem!")
        
        self.repository.deletar(tema_id)