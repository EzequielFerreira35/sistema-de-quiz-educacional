import time
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

def responder_quiz(args, tentativa_service):
    tentativa = tentativa_service.iniciar_quiz(
        usuario_id=args.usuario, 
        quiz_id=args.quiz
        )
    
    inicio = time.monotonic()
    
    perguntas = tentativa.quiz.lista_perguntas
    respostas = [None for p in perguntas]

    for i, pergunta in enumerate(perguntas, start=1):
        print(f"{i}. {pergunta.enunciado}")
        for j, alt in enumerate(pergunta.alternativas, start=1):
            print(f"{j}) {alt}")

        while True:
            resposta = int(input("Escolha uma alternativa: "))

            if resposta < 1 or resposta > len(pergunta.alternativas):
                print("Alternativa inválida! Tente novamente.")
                continue
            break

        respostas[i-1] = resposta

        tempo_atual = (time.monotonic() - inicio) / 60

        if tempo_atual >= tentativa.quiz.tempo_limite:
            print("Tempo esgotado!")
            break

        tentativa_service.responder_quiz(
                tentativa_id=tentativa.id,
                pergunta_id=pergunta.id,
                respostas=respostas,
                tempo=(tempo_atual)
        )

    fim = time.monotonic()
    tempo_segundos = fim - inicio
    tempo_minutos = int(tempo_segundos // 60)
    tentativa = tentativa_service.terminar_quiz(
        tentativa_id=tentativa.id,
        tempo_total=tempo_minutos
    )
    