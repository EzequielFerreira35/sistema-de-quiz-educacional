import argparse

from Repository.Inicializador import InicializarDataBase
from Repository.QuizRepository import QuizRepositorySQLite
from Repository.PerguntaRepository import PerguntaRepositorySQLite
from Services.quizservice import QuizService

def criar_parser():
    parser = argparse.ArgumentParser(
        description="Sistema de Quiz Educacional"
    )

    comandos = parser.add_subparsers(
        dest="comando",
        required=True
    )

    quiz = comandos.add_parser("quiz")
    operacoes_quiz = quiz.add_subparsers(
        dest="operacao",
        required=True
    )

    criar = operacoes_quiz.add_parser("criar")
    criar.add_argument(
        "--titulo",
        required=True,
        help="Título do Quiz"
    )

    responder = operacoes_quiz.add_parser("responder")
    responder.add_argument(
        "--tentativa",
        required=True,
        help="ID da Tentativa"
    )

    relatorio = comandos.add_parser("relatorio")
    tipos_relatorios = relatorio.add_subparsers(
        dest="tipo",
        required=True
    )

    usuario = tipos_relatorios.add_parser("usuario")
    usuario.add_argument(
        "--id",
        required=True,
        help="ID do Usuário"
    )

    return parser

def main():
    parser = criar_parser()
    args = parser.parse_args()

    InicializarDataBase()

    if args.comando == "quiz":
        if args.operacao == "criar":
            quiz_repo = QuizRepositorySQLite()
            pergunta_repo = PerguntaRepositorySQLite()

            service = QuizService(quiz_repo, pergunta_repo)
            quiz = service.criar_quiz(args.titulo)

            print("Quiz criado com sucesso!")
            print(f"Título: {quiz.titulo}")
            print(f"ID: {quiz.titulo}")

        elif args.operacao == "responder":
            print(f"Responder tentativa: Funcionalidade ainda não implementada.")


    elif args.comando == "relatorio":
        if args.tipo == "usuario":
            print(f"Relatório do usuário: Funcionalidade ainda não implementada.")

if __name__ == "__main__":
    main()