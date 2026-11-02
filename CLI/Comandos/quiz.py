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
        print(f"Erro: {error}")

def adicionar_pergunta():
    ...