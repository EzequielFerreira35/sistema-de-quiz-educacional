def relatorio_usuario(usuario_id, usuario_repo, quiz_repo, tentativa_repo):
    usuario = usuario_repo.buscar_por_id(usuario_id)

    if usuario is None:
        print("\nUsuário não encontrado.")
        return

    print("\n" + "=" * 65)
    print("RELATÓRIO DE DESEMPENHO DO USUÁRIO")
    print("=" * 65)
    print(f"Nome: {usuario.username}")
    print(f"ID: {usuario.id}")

    total_tentativas = 0

    for quiz in quiz_repo.listar_todos():
        tentativas = tentativa_repo.listar_por_usuario(
            usuario_id,
            quiz.id
        )

        if not tentativas:
            continue

        for tentativa in tentativas:
            total_tentativas += 1

            status = (
                "Concluída"
                if tentativa["status_conclusao"]
                else "Em andamento"
            )

            print("\n" + "-" * 65)
            print(f"Quiz: {tentativa['titulo']}")
            print(f"Data: {tentativa['data']}")
            print(f"Pontuação: {tentativa['pontuacao']:g}")
            print(f"Tempo: {tentativa['tempo_total']} segundos")
            print(f"Status: {status}")

    print("\n" + "=" * 65)
    print(f"Total de tentativas: {total_tentativas}")
    print("=" * 65)
