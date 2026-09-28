class Pergunta:
    """
    Essa classe representa uma pergunta de múltipla escolha.

    Atributos:
        - id (int): Número de identificação da Pergunta
        - tema (Tema): Tema da pergunta
        - enunciado (str): Enunciado da pergunta
        - alternativas l(ist[str]): Alternativas da Pergunta
        - indice_respota (int): Indice que representa qual alternativa é a correta
        - dificuldade (str): Dificuldade da Pergunta

    Métodos
        + verificar_resposta() -> bool: Verifica se a resposta está certa
        + verificar_duplicata() -> bool: Verifica se existe duplicata da respsota
        + verificar_qtd_alternativas() -> bool: Verifica a quantidade de alternativas
        + peso() -> int: Calcula o peso da pergunta
    """
    pass