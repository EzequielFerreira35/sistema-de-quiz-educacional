from datetime import time

def responder_quiz(usuario_id, quiz_id, usuario_repo, quiz_repo, tentativa_service):
    usuario = usuario_repo.buscar_por_id(usuario_id)
    quiz = quiz_repo.buscar_por_id(quiz_id)

    if usuario is None:
        print("\nUsuário não encontrado.")
        return

    if quiz is None:
        print("\nQuiz não encontrado.")
        return

    perguntas = quiz.lista_perguntas

    if not perguntas:
        print("\nEste quiz ainda não possui perguntas.")
        return

    try:
        tentativa = tentativa_service.iniciar_quiz(usuario_id, quiz_id)
    except (ValueError, TypeError) as erro:
        print(f"\nNão foi possível iniciar: {erro}")
        return

    respostas = [None] * len(perguntas)

    print("\n" + "=" * 45)
    print(f"QUIZ: {quiz.titulo}")
    print(f"Participante: {usuario.username}")
    print(f"Quantidade de perguntas: {len(perguntas)}")
    print("=" * 45)

    inicio = time.monotonic()

    for numero, pergunta in enumerate(perguntas, start=1):
        print(f"\nPergunta {numero}/{len(perguntas)}")
        print("-" * 45)
        print(pergunta.enunciado)

        for indice, alternativa in enumerate(pergunta.alternativas, start=1):
            print(f"  {indice}. {alternativa}")

        while True:
            escolha = input("\nSua resposta (número): ").strip()

            try:
                escolha = int(escolha)
                if 1 <= escolha <= len(pergunta.alternativas):
                    break
            except ValueError:
                pass

            print("Opção inválida. Digite o número de uma alternativa.")

        respostas[numero - 1] = escolha - 1

        try:
            tentativa_service.responder_quiz(
                tentativa.id,
                pergunta.id,
                respostas.copy(),
                0
            )
        except (ValueError, TypeError) as erro:
            print(f"\nErro ao registrar resposta: {erro}")
            return

    tempo_total = int(time.monotonic() - inicio)

    try:
        tentativa = tentativa_service.terminar_quiz(
            tentativa.id,
            tempo_total
        )
    except (ValueError, TypeError) as erro:
        print(f"\nErro ao finalizar tentativa: {erro}")
        return

    pontuacao_maxima = quiz.calcular_pontuacao_maxima()

    print("\n" + "=" * 45)
    print("QUIZ FINALIZADO!")
    print("=" * 45)
    print(f"Participante: {usuario.username}")
    print(f"Quiz: {quiz.titulo}")
    print(f"Pontuação: {tentativa.pontuacao:g} / {pontuacao_maxima:g}")
    print(f"Tempo: {tempo_total} segundos")
    print(f"ID da tentativa: {tentativa.id}")
    print("=" * 45)