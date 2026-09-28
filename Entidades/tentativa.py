class Tentativa:
    """
    Representa o registro de uma execução do Quiz por um Usuário.

    Atributos:
        - id (int): Número de Identificação da Tentativa
        - usuario (Usuario): Usuário ao qual a tentativa pertence
        - quiz (Quiz): Quiz ao qual a tentativa pertence
        - repostas (list): Respostas do Usuário
        - pontuacao (int): Pontuação obtida pelo Usuário
        - tempo_total (int): Tempo total gasto para responder o Quiz
        - status_conclusao (bool): Representa se o quiz foi concluído ou não

    Métodos:
        + calcular_pontuacao() -> float: Calcula a pontuação total com base nas respostas
        + taxa_acerto() -> float: Calcula a taxa de acertos
    """
    pass