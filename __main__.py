from CLI.parser import criar_parser

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

    args.func(args, quiz_service)




if __name__ == "__main__":
    main()

