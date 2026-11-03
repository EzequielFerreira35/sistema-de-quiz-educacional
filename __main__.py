import argparse
from CLI.parser import criar_parser
from CLI.Comandos.quiz import criar_quiz, listar_quizzes, adicionar_pergunta, consultar_quiz, responder_quiz
from CLI.Comandos.relatorio import relatorio_desempenho, relatorio_ranking, relatorio_evolucao, relatorio_perguntas_dificeis, relatorio_tentativa, relatorio_quiz
from CLI.Comandos.pergunta import criar_pergunta, editar_pergunta, listar_perguntas, listar_por_tema
from CLI.Comandos.usuario import cadastrar_usuario, consultar_usuario, atualizar_email, listar_usuarios
from CLI.Comandos.tema import criar_tema, consultar_tema, listar_temas, deletar_tema

from Repository.Inicializador import InicializarDataBase
from Repository.QuizRepository import QuizRepositorySQLite
from Repository.PerguntaRepository import PerguntaRepositorySQLite
from Repository.TemaRepository import TemaRepositorySQLite
from Repository.UsuarioRepository import UsuarioRepositorySQLite
from Repository.TentativaRepository import TentativaRepository

from Services.perguntaservice import PerguntaService
from Services.quizservice import QuizService
from Services.relatorioservice import RelatorioService
from Services.temaservice import TemaService
from Services.tentativaservice import TentativaService
from Services.usuarioservice import UsuarioService

from Entidades.tema import Tema
from Entidades.usuario import Usuario
from Entidades.pergunta import Pergunta
from Entidades.relatorio import Relatorio
from Entidades.quiz import Quiz

from Services.quizservice import QuizService

def main():
    inicializador = InicializarDataBase()
    inicializador.inicializar()

    quiz_repo = QuizRepositorySQLite()
    pergunta_repo = PerguntaRepositorySQLite()

    quiz_service = QuizService(quiz_repo, pergunta_repo)

    parser = criar_parser()
    args = parser.parse_args()

    if args.func == criar_quiz:
        args.func(args, quiz_service)

    elif args.func == listar_quizzes:
        args.func(args, quiz_repo)

    elif args.func == adicionar_pergunta:
        args.func(args, quiz_service)

if __name__ == "__main__":
    main()

