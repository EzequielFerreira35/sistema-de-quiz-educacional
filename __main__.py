import argparse
from CLI import criar_parser
from CLI.Comandos import *

from Repository import *
from Services import *


def main():
    inicializador = InicializarDataBase()
    inicializador.inicializar()

    quiz_repo = QuizRepositorySQLite()
    pergunta_repo = PerguntaRepositorySQLite()
    tema_repo = TemaRepositorySQLite()
    usuario_repo = UsuarioRepositorySQLite()
    tentativa_repo = TentativaRepositorySQLite()

    quiz_service = QuizService(quiz_repo, pergunta_repo)
    pergunta_service = PerguntaService(pergunta_repo, tema_repo)
    tentativa_service = TentativaService(usuario_repo, quiz_repo, tentativa_repo)
    relatorio_service = RelatorioService(tentativa_repo, quiz_repo, usuario_repo)
    usuario_service = UsuarioService(usuario_repo)
    tema_service = TemaService(tema_repo, pergunta_repo)


    parser = criar_parser()
    args = parser.parse_args()

    if args.func == criar_pergunta:
        args.func(args, pergunta_service, tema_repo)

    elif args.func == listar_perguntas:
        args.func(args, pergunta_repo)

    elif args.func == listar_por_tema:
        args.func(args, pergunta_service)

    elif args.func == editar_pergunta:
        args.func(args, pergunta_service)

    elif args.func == criar_quiz:
        args.func(args, quiz_service)

    elif args.func == listar_quizzes:
        args.func(args, quiz_repo)

    elif args.func == adicionar_pergunta:
        args.func(args, quiz_service)

    elif args.func == consultar_quiz:
        args.func(args, quiz_repo)

    elif args.func == responder_quiz:
        args.func(args, tentativa_service)

    elif args.func == relatorio_perguntas_dificeis:
        args.func(args, relatorio_service)

    elif args.func == relatorio_desempenho:
        args.func(args, relatorio_service, usuario_repo)

    elif args.func == relatorio_evolucao:
        args.func(args, relatorio_service)

    elif args.func == relatorio_tentativa:
        args.func(args, relatorio_service, tentativa_repo)

    elif args.func == relatorio_ranking:
        args.func(args, relatorio_service)

    elif args.func == relatorio_quiz:
        args.func(args, relatorio_service, quiz_repo)

    elif args.func == criar_tema:
        args.func(args, tema_service)

    elif args.func == listar_temas:
        args.func(args, tema_repo)

    elif args.func == consultar_tema:
        args.func(args, tema_repo)

    elif args.func == deletar_tema:
        args.func(args, tema_service)

    elif args.func == cadastrar_usuario:
        args.func(args, usuario_service)

    elif args.func == listar_usuarios:
        args.func(args, usuario_repo)

    elif args.func == consultar_usuario:
        args.func(args, usuario_repo)

    elif args.func == atualizar_email:
        args.func(args, usuario_service)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

