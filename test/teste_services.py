import tempfile
from pathlib import Path
from src.Repository.sqlite_base import SQLiteBase
SQLiteBase._CAMINHO_DB = Path(tempfile.mkdtemp()) / "t.db"

from src.Repository.Inicializador import InicializarDataBase
InicializarDataBase()

from src.Repository.QuizRepository import QuizRepositorySQLite
from src.Repository.UsuarioRepository import UsuarioRepositorySQLite
from src.Repository.TentativaRepository import TentativaRepositorySQLite
from src.Repository.PerguntaRepository import PerguntaRepositorySQLite
from src.Repository.TemaRepository import TemaRepositorySQLite

from src.Services.quizservice import QuizService
from src.Services.usuarioservice import UsuarioService
from src.Services.tentativaservice import TentativaService
from src.Services.perguntaservice import PerguntaService
from src.Services.temaservice import TemaService

quiz_repo = QuizRepositorySQLite()
usuario_repo = UsuarioRepositorySQLite()
tentativa_repo = TentativaRepositorySQLite()
pergunta_repo = PerguntaRepositorySQLite()
tema_repo = TemaRepositorySQLite()

tema = TemaService(tema_repo, pergunta_repo).criar_tema("Python")
quiz = QuizService(quiz_repo, None).criar_quiz("Q", 600, 2)
user = UsuarioService(usuario_repo).cadastrar("Ana", "ana@x.com", "Senha@123")

tent_service = TentativaService(usuario_repo, quiz_repo, tentativa_repo)
perg_service = PerguntaService(pergunta_repo, tema_repo)

pergunta = perg_service.criar_pergunta("Oque é o que é?", tema, ["a", "b", "c", "d"], 2, "facil")
rec = pergunta_repo.buscar_por_id(pergunta.id)

print("Tema certo?", rec.tema.id == tema.id)
print("alternativas: ", rec.alternativas)

perg_service.editar_pergunta(pergunta.id, enunciado="Qual agora?")
perg_service.editar_pergunta(pergunta.id, alternativas=["a", "b", "c", "d", "e"])
print("Depois de editar: ", pergunta_repo.buscar_por_id(pergunta.id).alternativas)

# tent = tent_service.iniciar_quiz(user.id, quiz.id)
# print("Iniciou: ", tent.id)
# tent_service.terminar_quiz(tent.id, 30)
# print("Terminou")
# tent_service.iniciar_quiz(user.id, quiz.id)
# tent_service.iniciar_quiz(user.id, quiz.id)
# tent_service.iniciar_quiz(user.id, quiz.id)
# tent_service.iniciar_quiz(user.id, quiz.id)

# try:
#     tent_service.iniciar_quiz(user.id, quiz.id)

# except ValueError as error:
#     print("Limite: ", error)