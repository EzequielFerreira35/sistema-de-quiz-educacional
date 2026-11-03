from CLI.apresentacao import desenhar_tabela, desenhar_card

def relatorio_perguntas_dificeis(args, relatorio_service):
    try:
        relatorio = relatorio_service.gerar_questoes_mais_erradas()

        if relatorio is None or relatorio is []:
            print("\n\033[31mNenhuma pergunta cadastrado.\033[0m")
            return

        cabecalhos = ["ID DA PERGUNTA", "ENUNCIADO", "TEMA", "TOTAL RESPOSTAS", "ACERTOS", "TAXA  DE ERROS"]
        
        larguras = [40, 52] 

        dados = []
        for pergunta in relatorio:
            dados.append([
                pergunta["pergunta_id"], 
                pergunta["pergunta_enunciado"], 
                pergunta["nome_tema"], 
                pergunta["total_respostas"], 
                pergunta["acertos"], 
                pergunta["taxa_erros"]
            ])

        print("\n=== PERGUNTAS MAIS DIFíCEIS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def relatorio_desempenho(args, relatorio_service, usuario_service):
    try:
        relatorio = relatorio_service.gerar_desempenho_usuario()
        usuario = usuario_service.buscar_por_id(args.usuario)

        if relatorio is None or relatorio is []:
            print("\n\033[31mNenhuma pergunta cadastrado.\033[0m")
            return

        cabecalhos = ["TEMA", "TOTAL RESPOSTAS", "ACERTOS", "TAXA DE ACERTOS"]
        
        larguras = [40, 52]
        dados = {}

        for chave, valor in relatorio.items():
            if chave == "tema":
                break
            dados[chave] = valor
            

        dados_tema = []
        for tema in relatorio["tema"]:
            dados_tema.append([
                tema["nome_tema"], 
                tema["total_respostas"], 
                tema["acertos"], 
                tema["taxa_acertos"], 
            ])

        desenhar_card(usuario.nome, usuario.id, dados)

        print("\n=== DESEMPENHO DO USUÁRIO NOS TEMAS ===")
        
        desenhar_tabela(cabecalhos, larguras, dados_tema)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")


def relatorio_evolucao(args, relatorio_service):
    try:
        tentativas = relatorio_service.evolucao_usuario(args.usuario)

        if tentativas is None:
            print("\n\033[31mNenhuma tentativa cadastrado.\033[0m")
            return

        cabecalhos = ["DATA", "QUIZ", " PERCENTUAL PONTUACÃO", "PONTUAÇÃO", "TEMPO TOTAL"]
        
        larguras = [40, 52] 

        dados = []
        for tentativa in tentativas:
            dados.append([
                tentativa["data"], 
                tentativa["quiz"], 
                tentativa["percentual_pontuacao"], 
                tentativa["pontuacao"], 
                tentativas["tempo_total"]
            ])

        print("\n=== EVOLUÇÃO DO USUÁRIO ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")    

def relatorio_tentativa(args, relatorio_service, tentativa_repo):
    try:
        relatorio = relatorio_service.gerar_relatorio_basico(args.tentativa)
        tentativa = tentativa_repo.buscar_por_id(args.tentativa)

        if relatorio is None:
            print("\n\033[31mentativa não cadastrado.\033[0m")
            return
        
        dados = {}
        for chave, valor in relatorio:
            dados[chave] = valor

        print("\n=== RELÁTORIO ===")

        desenhar_card(tentativa.usuario.nome, tentativa.usuario.id, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")  

def relatorio_ranking(args, relatorio_service):
    try:
        usuarios = relatorio_service.gerar_ranking_usuarios()

        if usuarios is None:
            print("\n\033[31mNenhuma usuario cadastrado.\033[0m")
            return

        cabecalhos = ["POSIÇÃO", "ID DO USUÁRIO", "NOME", " PONTUACÃO TOTAL", "QUANTIDADE TENTATIVAS", "PONTUAÇÃO MÉDIA"]
        
        larguras = [40, 52] 

        dados = []
        for usuario in usuarios:
            dados.append([
                usuario["posicao"], 
                usuario["id"], 
                usuario["nome"],
                usuario["pontuacao_total"], 
                usuario["quantidade_tentativas"], 
                usuario["pontuacao_media"]
            ])

        print("\n=== RANKING ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m") 


def relatorio_quiz(args, relatorio_service, quiz_repo):
    try:
        taxa_aprovacao = relatorio_service.calcular_taxa_aprovacao(args.quiz)
        distribuicao = relatorio_service.gerar_distribuicao_notas(args.quiz)
        quiz = quiz_repo.buscar_por_id(args.quiz)

        if taxa_aprovacao is None or distribuicao is None:
            print("\n\033[31mDados insuficientes.\033[0m")
            return

        dados = {}

        for chave, valor in taxa_aprovacao:
            dados[chave] = valor

        for chave, valor in distribuicao:
            dados[chave] - valor

        desenhar_card(args.quiz, quiz.nome, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m") 