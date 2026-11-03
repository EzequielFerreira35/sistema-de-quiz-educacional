from src.CLI.apresentacao import desenhar_tabela

def criar_pergunta(args, pergunta_service, tema_repo):
    try:
        tema_instancia = tema_repo.buscar_por_id(tema_id=args.tema)

        pergunta = pergunta_service.criar_pergunta(
            tema=tema_instancia,
            enunciado=args.enunciado,
            alternativas=args.alternativas,
            indice_resposta=args.indice_resposta,
            dificuldade=args.dificuldade
        )

        print("\n=== PERGUNTA CRIADA ===")
        print("Pergunta criada com sucesso!")
        print(f"ID: {pergunta.id}")
        print(f"Enunciado: {pergunta.enunciado}")
        print(f"Tema: {pergunta.tema.nome}")
        print(f"Dificuldade: {pergunta.dificuldade}")
        print(f"Alternativas: {pergunta.alternativas}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def listar_perguntas(args, pergunta_repo):
    try:
        perguntas = pergunta_repo.listar_todos()

        if perguntas is None:
            print("\n\033[31mNenhuma pergunta cadastrada.\033[0m")
            return

        cabecalhos = ["ID DA PERGUNTA","ENUNCIADO", "TEMA", "DIFICULDADE", "ALTERNATIVAS"]
        
        larguras = [38, 40, 14, 14, 30]

        dados = []
        for pergunta in perguntas:
            dados.append([pergunta.id, pergunta.enunciado, pergunta.tema.nome, pergunta.dificuldade, pergunta.alternativas])

        print("\n=== PERGUNTAS CADASTRADAS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def listar_por_tema(args, pergunta_service):
    try:
        perguntas = pergunta_service.listar_por_tema()

        if perguntas is None:
            print("\n\033[31mNenhuma pergunta cadastrada.\033[0m")
            return

        cabecalhos = ["ID DA PERGUNTA","ENUNCIADO", "TEMA", "DIFICULDADE", "ALTERNATIVAS"]
        
        larguras = [38, 55, 20, 18, 45]

        dados = []
        for pergunta in perguntas:
            dados.append([pergunta.id, pergunta.enunciado, pergunta.tema.nome, pergunta.dificuldade, pergunta.alternativas])

        print("\n=== PERGUNTAS CADASTRADAS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def editar_pergunta(args, pergunta_service):
    try:
        pergunta = pergunta_service.editar_pergunta(
            pergunta_id=args.pergunta,
            enunciado=args.enunciado,
            alternativas=args.alternativas,
            indice_resposta=args.indice_resposta,
            dificuldade=args.dificuldade
        )

        print("\n=== PERGUNTA CRIADA ===")
        print("Pergunta criada com sucesso!")
        print(f"ID: {pergunta.id}")
        print(f"Enunciado: {pergunta.enunciado}")
        print(f"Tema: {pergunta.tema.nome}")
        print(f"Dificuldade: {pergunta.dificuldade}")
        print(f"Alternativas: {pergunta.alternativas}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")