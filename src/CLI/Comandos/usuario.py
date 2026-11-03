from src.CLI.apresentacao import desenhar_tabela

def cadastrar_usuario(args, usuario_service):
    try:
        usuario = usuario_service.cadastrar(
            nome=args.nome,
            senha=args.senha,
            email=args.email
        )

        print("\n=== USUÁRIO CADASTRADO ===")
        print("Usuário cadastrado com sucesso!")
        print(f"Nome: {usuario.username}")
        print(f"ID: {usuario.id}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def listar_usuarios(args, usuario_repo):
    try:
        usuarios = usuario_repo.listar_todos()

        if usuarios is None:
            print("\n\033[31mNenhum quiz cadastrado.\033[0m")
            return

        cabecalhos = ["ID DO USUÁRIO", "NOME DO USUÁRIO", "EMAIL DO USUÁRIO"]
        
        larguras = [38, 40, 52]

        dados = []
        for usuario in usuarios:
            dados.append([usuario.id, usuario.username, usuario.email])

        print("\n=== USUÁRIOS CADASTRADOS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def consultar_usuario(args, usuario_repo):
    try:
        usuario = usuario_repo.buscar_por_id(usuario_id = args.usuario)

        if usuario is None:
            print("\n\033[Esse usuário não existe.\033[0m")

        cabecalhos = ["ID DO USUÁRIO", "NOME DO USUÁRIO", "EMAIL DO USUÁRIO"]
        
        larguras = [38, 40, 52]

        dados = []
        dados.append([usuario.id, usuario.username, usuario.email])

        print("\n=== RESULTADO DA BUSCA ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def atualizar_email(args, usuario_service):
    try:
        usuario = usuario_service.atualizar_email(
            email=args.novo_email,
            usuario_id=args.usuario
        )

        print("\n=== EMAIL ATUALIZADO CO SUCESSO ===")
        print("O novo email foi atualizado com sucesso!")
        print(f"Nome: {usuario.username}")
        print(f"Novo email: {usuario.email}")
        print(f"ID: {usuario.id}")

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")