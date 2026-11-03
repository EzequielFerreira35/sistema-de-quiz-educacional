import pytest

from src.Entidades.tema import Tema
from src.Entidades.pergunta import Pergunta
from src.Entidades.quiz import Quiz

tema_python = Tema(nome="Python")

pergunta1 = Pergunta(
    tema=tema_python,
    enunciado="Qual palavra-chave define uma função em Python?",
    alternativas=["func", "def", "function", "fun"],
    indice_resposta=1,
    dificuldade="facil"
)

pergunta2 = Pergunta(
    tema=tema_python,
    enunciado="Qual é o tipo de dado de [1, 2, 3] em Python?",
    alternativas=["tuple", "dict", "list", "set"],
    indice_resposta=2,
    dificuldade="facil"
)

pergunta3 = Pergunta(
    tema=tema_python,
    enunciado="Qual conceito permite que uma classe herde características de outra?",
    alternativas=["Encapsulamento", "Herança", "Polimorfismo", "Abstração"],
    indice_resposta=1,
    dificuldade="medio"
)



quiz1 = Quiz(
    titulo="Avaliação de Banco de Dados",
    tempo_limite=12,
    limite_tentativas=1
)
lista_temas = ["Programação Orientada a Objetos", "Banco de Dados SQL", "Algoritmos"]

def test_criar_tema_corretamente():
    lista_temas = ["Programação Orientada a Objetos", "Banco de Dados SQL", "Algoritmos"]

    for nome in lista_temas:
        tema = Tema(nome=nome)

        assert tema.nome == nome
        assert tema.id is not None

def test_resposta_correta_da_pergunta():
    pergunta = pergunta1

    assert pergunta.verificar_resposta(1) is True
    assert pergunta.verificar_resposta(0) is False

def test_adicionar_pergunta():
    quiz = quiz1

    resultado = quiz.adicionar_pergunta(pergunta1)

    assert resultado is True
    assert len(quiz) == 1


def test_duplicata():
    quiz = quiz1

    quiz.adicionar_pergunta(pergunta2)
    resultado = quiz.adicionar_pergunta(pergunta2)

    assert resultado is False
    assert len(quiz) == 2