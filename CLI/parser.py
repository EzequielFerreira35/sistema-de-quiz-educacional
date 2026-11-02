import argparse

from .Comandos.quiz import criar_quiz, listar_quizzes, adicionar_pergunta

def criar_parser():
    parser = argparse.ArgumentParser(
        description="Sistema de Quiz Educacional"
    )

    comandos = parser.add_subparsers(
        dest="comando",
        required=True
    )

    usuario = comandos.add_parser(
        "usuario",
        help="Gerenciamento de usuários"
    )

    usuario_subcomandos = usuario.add_subparsers(
        dest="operacao",
        required=True
    )

    cadastrar_usuario_parser = usuario_subcomandos.add_parser(
        "cadastrar",
        help="Cadastrar um usuário"
    )

    cadastrar_usuario_parser.add_argument(
        "--nome",
        required=True,
        help="Nome do usuário"
    )

    cadastrar_usuario_parser.add_argument(
        "--email",
        required=True,
        help="E-mail do usuário"
    )

    cadastrar_usuario_parser.add_argument(
        "--senha",
        required=True,
        help="Senha do usuário"
    )

    atualizar_email_parser = usuario_subcomandos.add_parser(
        "atualizar-email",
        help="Atualizar e-mail de um usuário"
    )

    atualizar_email_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    atualizar_email_parser.add_argument(
        "--novo-email",
        required=True,
        help="Novo e-mail do usuário"
    )

    usuario_subcomandos.add_parser(
        "listar",
        help="Listar usuários cadastrados"
    )

    consultar_usuario_parser = usuario_subcomandos.add_parser(
        "consultar",
        help="Consultar um usuário cadastrado"
    )

    consultar_usuario_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    tema = comandos.add_parser(
        "tema",
        help="Gerenciamento de conteúdos"
    )

    tema_subcomandos = tema.add_subparsers(
        dest="operacao",
        required=True
    )

    criar_tema_parser = tema_subcomandos.add_parser(
        "criar",
        help="Criar um novo tema"
    )

    criar_tema_parser.add_argument(
        "--titulo",
        required=True,
        help="Título do tema"
    )

    deletar_tema_parser = tema_subcomandos.add_parser(
        "deletar",
        help="Deletar um tema cadastrado"
    )

    deletar_tema_parser.add_argument(
        "--tema",
        required=True,
        help="ID do tema"
    )

    tema_subcomandos.add_parser(
        "listar",
        help="Listar temas cadastrados"
    )

    quiz = comandos.add_parser(
        "quiz",
        help="Gerenciamento de conteúdos"
    )

    quiz_subcomandos = quiz.add_subparsers(
        dest="operacao",
        required=True
    )

    criar_quiz_parser = quiz_subcomandos.add_parser(
        "criar",
        help="Criar um novo quiz"
    )

    criar_quiz_parser.add_argument(
        "--titulo",
        required=True,
        help="Título do quiz"
    )

    criar_quiz_parser.add_argument(
        "--tempo",
        type=int,
        default=None,
        help="Tempo limite em minutos"
    )

    criar_quiz_parser.add_argument(
        "--tentativas",
        type=int,
        default=None,
        help="Limite de tentativas"
    )

    criar_quiz_parser.set_defaults(func=criar_quiz)

    listar_quiz_parser = quiz_subcomandos.add_parser(
        "listar",
        help="Listar quizzes cadastrados"
    )

    listar_quiz_parser.set_defaults(func=listar_quizzes)

    responder_quiz_parser = quiz_subcomandos.add_parser(
        "responder",
        help="Reponder um quiz"
    )

    responder_quiz_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    responder_quiz_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuario"
    )

    adicionar_pergunta_parser = quiz_subcomandos.add_parser(
        "adicionar-pergunta",
        help="Adicionar pergunta a um quiz"
    )

    adicionar_pergunta_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    adicionar_pergunta_parser.add_argument(
        "--pergunta",
        required=True,
        help="ID da pergunta"
    )

    adicionar_pergunta_parser.set_defaults(func=adicionar_pergunta)
    
    pergunta = comandos.add_parser(
        "pergunta",
        help="Gerenciamento de conteúdos"
    )

    pergunta_subcomandos = pergunta.add_subparsers(
        dest="operacao",
        required=True
    )

    criar_pergunta_parser = pergunta_subcomandos.add_parser(
        "criar",
        help="Criar uma nova pergunta"
    )

    criar_pergunta_parser.add_argument(
        "--enunciado",
        required=True,
        help="Enunciado da pergunta"
    )

    criar_pergunta_parser.add_argument(
        "--tema",
        required=True,
        help="ID do tema"
    )

    criar_pergunta_parser.add_argument(
        "--alternativas",
        required=True,
        nargs="+",
        help="Alternativas da pergunta"
    )

    criar_pergunta_parser.add_argument(
        "--indice-resposta",
        type=int,
        required=True,
        help="Índice da resposta da pergunta"
    )

    criar_pergunta_parser.add_argument(
        "--dificuldade",
        required=True,
        help="Dificuldade da pergunta"
    )

    pergunta_subcomandos.add_parser(
        "listar",
        help="Listar perguntas cadastradas"
    )

    relatorio = comandos.add_parser(
        "relatorio",
        help="Gerenciamento de relatórios"
    )

    relatorio_subcomandos = relatorio.add_subparsers(
        dest="operacao",
        required=True
    )

    relatorio_subcomandos.add_parser(
        "perguntas-dificeis",
        help="Exibir as perguntas mais erradas"
    )

    relatorio_quiz_parser = relatorio_subcomandos.add_parser(
        "quiz",
        help="Exibir relatorio de um quiz"
    )

    relatorio_quiz_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    relatorio_quiz_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_desempenho_parser = relatorio_subcomandos.add_parser(
        "desempenho",
        help="Exibir desempenho geral de um usuário"
    )

    relatorio_desempenho_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_evolucao_parser = relatorio_subcomandos.add_parser(
        "evolucao",
        help="Exibir evolução de um usuário"
    )

    relatorio_evolucao_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_subcomandos.add_parser(
        "ranking",
        help="Exibir ranking geral dos usuários"
    )

    return parser