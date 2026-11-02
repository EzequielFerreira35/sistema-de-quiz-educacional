from CLI.apresentacao import desenhar_tabela

def criar_tema(args, tema_service):
    try:
        tema = tema_service.criar_tema(
            nome=args.nome,
        )

        print("\n=== TEMA CRIADO ===")
        print("Tema criado com sucesso!")
        print(f"Nome: {tema.nome}")
        print(f"ID: {tema.id}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def listar_temas(args, tema_repo):
    try:
        temas = tema_repo.listar_todos()

        if temas is None:
            print("\n\033[31mNenhum tema cadastrado.\033[0m")
            return

        cabecalhos = ["ID DO TEMA", "NOME DO TEMA"]
        
        larguras = [40, 52] 

        dados = []
        for tema in temas:
            dados.append([tema.id, tema.nome])

        print("\n=== TEMAS CADASTRADOS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def consultar_tema(args, tema_repo):
    try:
        tema = tema_repo.buscaar_por_id(tema_id = args.tema)

        if tema is None:
            print("\n\033[Esse tema não existe.\033[0m")

        cabecalhos = ["ID DO TEMA", "NOME DO TEMA"]
        
        larguras = [40, 52] 

        dados = []
        dados.append([tema.id, tema.nome])

        print("\n=== RESULTADO DA BUSCA ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def deletar_tema(args, tema_service):
    try:
        tema_service.deletar_tema(tema_id=args.tema)

        print("\n=== TEMA DELETADO ===")
        print("Tema deletado com sucesso!")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")