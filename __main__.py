import argparse

from Repository.Inicializador import InicializarDataBase
from Repository.QuizRepository import QuizRepositorySQLite
from Repository.PerguntaRepository import PerguntaRepositorySQLite
from Services.quizservice import QuizService
from CLI.criar import criar_parser
from CLI.responder import responder_quiz
from CLI.relatorio import relatorio_usuario

def main():
    inicializador = InicializarDataBase
    inicializador.inicializar()

    quiz_repo = QuizRepositorySQLite
    pergunta_repo = PerguntaRepositorySQLite

    quiz_service = QuizService(quiz_repo, pergunta_repo)

    parser = criar_parser()
    args = parser.parse_args()

    if args.comando == "quiz" and args.operacao == "criar":
        quiz = quiz_service.criar_quiz(
            titulo=args.titulo,
            tempo_limite=args.tempo,
            limite_tentativas=args.tentativas
        )

        print(f"Quiz criado com sucesso! ID: {quiz.id}")

    elif args.comando == "quiz" and args.operacao == "responder":
        responder_quiz(args.quiz, args.usuario)

    elif args.comando == "relatorio" and args.tipo == "usuario":
        relatorio_usuario(args.id)


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    main()