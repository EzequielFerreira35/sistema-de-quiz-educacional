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

            pergunta_instancia = pergunta_service.criar_pergunta(
                item["enunciado"],
                tema,
                item["alternativas"],
                item["indice_resposta"],
                item["dificuldade"]
            )

            perguntas[item["enunciado"]] = pergunta_instancia

        for item in dados["quizzes"]:

            quiz = quiz_service.criar_quiz(
                item["titulo"],
            )

            for enunciado in item["perguntas"]:
                pergunta_instancia = perguntas[enunciado]
                if enunciado.casefold() == pergunta_instancia.enunciado.casefold():
                    quiz_service.adicionar_pergunta(quiz.id, pergunta_instancia.id)

        print("Dados insiridos no banco com sucesso!")

    except ValueError as error:
        print(f"Erro: {error}")