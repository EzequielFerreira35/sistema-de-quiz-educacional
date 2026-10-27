
import argparse

def criar_parser():
    parser = argparse.ArgumentParser(
        description="Sistema de Quiz Educacional"
    )

    comandos = parser.add_subparsers(
        dest="comando",
        required=True
    )

    quiz = comandos.add_parser("quiz")
    operacoes_quiz = quiz.add_subparsers(
        dest="operacao",
        required=True
    )

    criar = operacoes_quiz.add_parser("criar")
    criar.add_argument(
        "--titulo",
        required=True,
        help="Título do Quiz"
    )

    criar.add_argument(
        "--tempo",
        type=int,
        default=None,
        help="Tempo limite do quiz em minuto"
    )

    criar.add_argument(
        "--tentativas",
        type=int,
        default=None,
        help="Quantidade máxima de tentativas"
    )

    responder = operacoes_quiz.add_parser("responder")
    responder.add_argument(
        "--quiz",
        required=True,
        type=int  
    )

    responder.add_argument(
        "--usuario",
        required=True,
        type=int  
    )

    relatorio = comandos.add_parser("relatorio")
    tipos_relatorios = relatorio.add_subparsers(
        dest="tipo",
        required=True
    )

    usuario = tipos_relatorios.add_parser("usuario")
    usuario.add_argument(
        "--id",
        required=True,
        type=int,  
        help="ID do Usuário"
    )

    return parser
