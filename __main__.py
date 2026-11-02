from CLI.parser import criar_parser
from CLI.Comandos.quiz import criar_quiz, listar_quizzes, adicionar_pergunta

from Repository.Inicializador import InicializarDataBase
from Repository.QuizRepository import QuizRepositorySQLite
from Repository.PerguntaRepository import PerguntaRepositorySQLite

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
        args.func

if __name__ == "__main__":
    main()

