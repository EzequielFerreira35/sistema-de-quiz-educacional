import argparse

from src.Seed.insirir_dados_iniciais import dados_iniciais

from .Comandos.quiz import criar_quiz, listar_quizzes, adicionar_pergunta, consultar_quiz, responder_quiz
from .Comandos.relatorio import relatorio_desempenho, relatorio_ranking, relatorio_evolucao, relatorio_perguntas_dificeis, relatorio_tentativa, relatorio_quiz
from .Comandos.pergunta import criar_pergunta, editar_pergunta, listar_perguntas, listar_por_tema
from .Comandos.usuario import cadastrar_usuario, consultar_usuario, atualizar_email, listar_usuarios
from .Comandos.tema import criar_tema, consultar_tema, listar_temas, deletar_tema

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

    cadastrar_usuario_parser.set_defaults(func=cadastrar_usuario)

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

    atualizar_email_parser.set_defaults(func=atualizar_email)

    listar_usuarios_parser = usuario_subcomandos.add_parser(
        "listar",
        help="Listar usuários cadastrados"
    )

    listar_usuarios_parser.set_defaults(func=listar_usuarios)

    consultar_usuario_parser = usuario_subcomandos.add_parser(
        "consultar",
        help="Consultar um usuário cadastrado"
    )

    consultar_usuario_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    consultar_usuario_parser.set_defaults(func=consultar_usuario)

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

    criar_tema_parser.set_defaults(func=criar_tema)

    deletar_tema_parser = tema_subcomandos.add_parser(
        "deletar",
        help="Deletar um tema cadastrado"
    )

    deletar_tema_parser.add_argument(
        "--tema",
        required=True,
        help="ID do tema"
    )

    deletar_tema_parser.set_defaults(func=deletar_tema)

    listar_tema_parser = tema_subcomandos.add_parser(
        "listar",
        help="Listar temas cadastrados"
    )

    listar_tema_parser.set_defaults(func=listar_temas)

    consultar_tema_parser = tema_subcomandos.add_parser(
        "consultar",
        help="Consultar um tema cadastrado"
    )

    consultar_tema_parser.add_argument(
        "--tema",
        required=True,
        help="ID do tema"
    )

    consultar_tema_parser.set_defaults(func=consultar_tema)

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

    responder_quiz_parser.set_defaults(func=responder_quiz)

    consultar_quiz_parser = quiz_subcomandos.add_parser(
        "consultar",
        help="Consultar um quiz cadastrado"
    )

    consultar_quiz_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    consultar_quiz_parser.set_defaults(func=consultar_quiz)

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
        choices=["facil", "medio", "dificil"],
        required=True,
        help="Dificuldade da pergunta"
    )

    criar_pergunta_parser.set_defaults(func=criar_pergunta)

    pergunta_editar_parser = pergunta_subcomandos.add_parser(
        "editar",
        help="Editar uma pergunta cadastrada"
    )

    pergunta_editar_parser.add_argument(
        "--pergunta",
        required=True,
        help="ID da pergunta"
    )

    pergunta_editar_parser.add_argument(
        "--enunciado",
        required=True,
        help="Novo enunciado da pergunta"
    )

    pergunta_editar_parser.add_argument(
        "--alternativas",
        nargs="+",
        required=True,
        help="Novas alternativas da pergunta"
    )

    pergunta_editar_parser.add_argument(
        "--indice-resposta",
        type=int,
        required=True,
        help="Índice da alternativa correta"
    )

    pergunta_editar_parser.add_argument(
        "--dificuldade",
        required=True,
        help="Nova dificuldade da pergunta"
    )

    pergunta_editar_parser.set_defaults(func=editar_pergunta)
    
    perguntas_listar_parser = pergunta_subcomandos.add_parser(
        "listar",
        help="Listar perguntas cadastradas"
    )

    perguntas_listar_parser.set_defaults(func=listar_perguntas)

    perguntas_listar_tema_parser = pergunta_subcomandos.add_parser(
        "tema",
        help="Listar perguntas de um tema"
    )

    perguntas_listar_tema_parser.add_argument(
        "--tema",
        required=True,
        help="ID do tema"
    )

    perguntas_listar_tema_parser.set_defaults(func=listar_por_tema)

    relatorio = comandos.add_parser(
        "relatorio",
        help="Gerenciamento de relatórios"
    )

    relatorio_subcomandos = relatorio.add_subparsers(
        dest="operacao",
        required=True
    )

    relatorio_perguntas_dificeis_parser = relatorio_subcomandos.add_parser(
        "perguntas-dificeis",
        help="Exibir as perguntas mais erradas"
    )

    relatorio_perguntas_dificeis_parser.add_argument(
        "--limite",
        type=int,
        required=True,
        help="Limite de perguntas que devem sesr listadas"
    )

    relatorio_perguntas_dificeis_parser.set_defaults(func=relatorio_perguntas_dificeis)

    relatorio_tentativa_parser = relatorio_subcomandos.add_parser(
        "tentativa",
        help="Exibir relatorio de um quiz"
    )

    relatorio_tentativa_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    relatorio_tentativa_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_tentativa_parser.set_defaults(func=relatorio_tentativa)

    relatorio_desempenho_parser = relatorio_subcomandos.add_parser(
        "desempenho",
        help="Exibir desempenho geral de um usuário"
    )

    relatorio_desempenho_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_desempenho_parser.set_defaults(func=relatorio_desempenho)

    relatorio_evolucao_parser = relatorio_subcomandos.add_parser(
        "evolucao",
        help="Exibir evolução de um usuário"
    )

    relatorio_evolucao_parser.add_argument(
        "--usuario",
        required=True,
        help="ID do usuário"
    )

    relatorio_evolucao_parser.set_defaults(func=relatorio_evolucao)

    ranking_parser = relatorio_subcomandos.add_parser(
        "ranking",
        help="Exibir ranking geral dos usuários"
    )

    ranking_parser.set_defaults(func=relatorio_ranking)

    relatorio_quiz_parser = relatorio_subcomandos.add_parser(
        "quiz",
        help="Relatório de um quiz"
    )

    relatorio_quiz_parser.add_argument(
        "--quiz",
        required=True,
        help="ID do quiz"
    )

    relatorio_quiz_parser.set_defaults(func=relatorio_quiz)

    seed_parser = comandos.add_parser(
        "seed",
        help="Popular Banco de Dados"
    )

    seed_parser.set_defaults(func=dados_iniciais)

    return parser