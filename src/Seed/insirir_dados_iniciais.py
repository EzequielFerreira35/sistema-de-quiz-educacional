import json
from pathlib import Path

from src.Repository.TemaRepository import TemaRepository
from src.Services.quizservice import QuizService
from src.Services.perguntaservice import PerguntaService
from src.Services.temaservice import TemaService


def dados_iniciais(args, tema_service: TemaService, pergunta_service: PerguntaService, quiz_service: QuizService, tema_repo: TemaRepository):
    CAMINHO_DADOS_INICIAIS = Path(__file__).parent / "dados_iniciais.json"

    with open(CAMINHO_DADOS_INICIAIS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    try:
        temas = {}
        perguntas = {}

        for item in dados["temas"]:
            nome = item["nome"]

            existentes = tema_repo.listar_todos()

            tema = [tema for tema in existentes if tema.nome.casefold() == nome.casefold()]

            if not tema:
                tema = [tema_service.criar_tema(nome)]

            temas[nome] = tema[0]

        for item in dados["perguntas"]:
            
            tema = temas[item["tema"]]

            existentes = pergunta_service.pergunta_repo.listar_por_tema(tema.id)

            pergunta_instancia = next(
                (pergunta for pergunta in existentes if pergunta.enunciado.casefold() == item["enunciado"].casefold()),
                None
            )

            if pergunta_instancia is None:
                pergunta_instancia = pergunta_service.criar_pergunta(
                    item["enunciado"],
                    tema,
                    item["alternativas"],
                    item["indice_resposta"],
                    item["dificuldade"]
                )

            perguntas[item["enunciado"]] = pergunta_instancia

        for item in dados["quizzes"]:

            existentes = quiz_service.quiz_repo.listar_todos()

            quiz_instancia = next(
                (quiz for quiz in existentes if quiz.titulo.casefold() == item["titulo"].casefold()),
                None
            )

            if quiz_instancia is None:
                quiz = quiz_service.criar_quiz(
                    item["titulo"],
                )
            else:
                quiz = quiz_service.quiz_repo.buscar_por_id(quiz_instancia.id)

            for enunciado in item["perguntas"]:
                pergunta_instancia = perguntas[enunciado]
                quiz_service.adicionar_pergunta(quiz.id, pergunta_instancia.id)

        print("Dados insiridos no banco com sucesso!")

    except ValueError as error:
        print(f"Erro: {error}")