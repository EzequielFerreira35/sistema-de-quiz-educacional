from CLI.apresentacao import desenhar_tabela

def criar_quiz(args, quiz_service):
    try:
        quiz = quiz_service.criar_quiz(
            titulo=args.titulo,
            tempo_limite=args.tempo,
            limite_tentativas=args.tentativas
        )

        print("\n=== QUIZ CRIADO ===")
        print("Quiz criado com sucesso!")
        print(f"Título: {quiz.titulo}")
        print(f"ID: {quiz.id}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def listar_quizzes(args, quiz_repo):
    try:
        quizzes = quiz_repo.listar_todos()

        if quizzes is None:
            print("\n\033[31mNenhum quiz cadastrado.\033[0m")
            return

        cabecalhos = ["ID DO QUIZ", "TÍTULO DO QUIZ"]
        
        larguras = [40, 52] 

        dados = []
        for quiz in quizzes:
            dados.append([quiz.id, quiz.titulo])

        print("\n=== QUIZZES CADASTRADOS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def adicionar_pergunta(args, quiz_service):
    try:
        adicionada = quiz_service.adicionar_pegunta(
            quiz_id=args.quiz, 
            pergunta_id=args.pergunta
            )

        if adicionada:
            print("Pergunta adicionada com sucesso!")
        else:
            print("A pergunta não foi adicionada!")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def consultar_quiz(args, quiz_repo):
    try:
        quiz = quiz_repo.buscaar_por_id(quiz_id = args.quiz)

        if quiz is None:
            print("\n\033[Esse não quiz existe.\033[0m")

        cabecalhos = ["ID DO QUIZ", "TÍTULO DO QUIZ"]
        
        larguras = [40, 52] 

        dados = []
        dados.append([quiz.id, quiz.titulo])

        print("\n=== RESULTADO DA BUSCA ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def responder_quiz():
    ...