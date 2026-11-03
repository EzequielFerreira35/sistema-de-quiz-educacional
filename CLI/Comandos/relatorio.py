from CLI.apresentacao import desenhar_tabela, desenhar_card

def relatorio_perguntas_dificeis(args, relatorio_service):
    try:
        relatorio = relatorio_service.gerar_questoes_mais_erradas(args.limite)

        if relatorio is None or relatorio is []:
            print("\n\033[31mNenhuma pergunta cadastrado.\033[0m")
            return

        cabecalhos = ["ID DA PERGUNTA", "ENUNCIADO", "TEMA", "TOTAL RESPOSTAS", "ACERTOS", "TAXA  DE ERROS"]
        
        larguras = [38, 55, 20, 22, 18, 20]

        dados = []
        for pergunta in relatorio:
            dados.append([
                pergunta["pergunta_id"], 
                pergunta["pergunta_enunciado"], 
                pergunta["nome_tema"], 
                pergunta["total_respostas"], 
                pergunta["acertos"], 
                f'{pergunta["taxa_erros"] * 100:.1f}%'
            ])

        print("\n=== PERGUNTAS MAIS DIFíCEIS ===")

        desenhar_tabela(cabecalhos, larguras, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")

def relatorio_desempenho(args, relatorio_service, usuario_repo):
    try:
        relatorio = relatorio_service.gerar_desempenho_usuario(args.usuario)
        usuario = usuario_repo.buscar_por_id(args.usuario)

        if relatorio is None or relatorio is []:
            print("\n\033[31mNenhuma pergunta cadastrado.\033[0m")
            return

        cabecalhos = ["TEMA", "TOTAL RESPOSTAS", "ACERTOS", "TAXA DE ACERTOS"]
        
        larguras =  [30, 22, 18, 22]
        dados = {}

        for chave, valor in relatorio.items():
            if chave == "temas":
                break
            dados[chave] = valor
            

        dados_tema = []
        for tema in relatorio["temas"]:
            dados_tema.append([
                tema["nome_tema"], 
                tema["total_respostas"],
                tema["acertos"], 
                f'{tema["taxa_acertos"] * 100:.1f}%'
            ])

        print("\n=== DESEMPENHO GERAL DO USUÁRIO  ===")

        desenhar_card(usuario.username, usuario.id, dados)

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
        
        larguras = [22, 35, 25, 18, 18]

        dados = []
        for tentativa in tentativas:
            dados.append([
                tentativa["data"], 
                tentativa["quiz"], 
                f'{tentativa["percentual_pontuacao"] * 100:.1f}%', 
                tentativa["pontuacao"], 
                f'{tentativa["tempo_total"]} min'
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

        desenhar_card(tentativa.usuario.username, tentativa.usuario.id, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m")  

def relatorio_ranking(args, relatorio_service):
    try:
        usuarios = relatorio_service.gerar_ranking_usuarios()

        if usuarios is None:
            print("\n\033[31mNenhuma usuario cadastrado.\033[0m")
            return

        cabecalhos = ["POSIÇÃO", "ID DO USUÁRIO", "NOME", " PONTUACÃO TOTAL", "QUANTIDADE TENTATIVAS", "PONTUAÇÃO MÉDIA"]
        
        larguras = [12, 38, 25, 20, 28, 20]

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

        for chave, valor in taxa_aprovacao.items():
            dados[chave] = valor

        for chave, valor in distribuicao.items():
            dados[chave] = valor

        desenhar_card(quiz.titulo, args.quiz, dados)

    except ValueError as error:
        print(f"\033[31mErro: {error}\033[0m") 