class RelatorioService:
    """
    Gerencia as regras de negócio e o ciclo de vida dos Relatórios.
    
    Métodos:
        + calcular_taxa_aprovacao() -> float: Retorna a porcentagem de Usuários aprovados
        + gerar_distribuicao_notas() -> dict: Agrupa os Usuários por notas
        + gerar_ranking_usuarios() -> list: gera um Relátorio com o Ranking dos Usuários
        + gerar_desempenho_usuario() -> dict: Fetorna um Relatório do desempenho do usuário (taxa de acerto geral e por tema)
        + gerar_questoes_mais_erradas() -> list: Retorna as questões mais erradas
        + evoluo_usuario() -> list: Gera um Relatório de evolução de desempenho com base nas Tentativas e Relatórios passados
    """
    pass