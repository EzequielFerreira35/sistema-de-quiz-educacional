from Entidades.tema import Tema
from Entidades.pergunta import Pergunta
from Entidades.quiz import Quiz

tema_python = Tema(nome="Python")
tema_poo = Tema(nome="Programação Orientada a Objetos")
tema_sql = Tema(nome="Banco de Dados SQL")
tema_algoritmos = Tema(nome="Algoritmos")

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
    tema=tema_poo,
    enunciado="Qual conceito permite que uma classe herde características de outra?",
    alternativas=["Encapsulamento", "Herança", "Polimorfismo", "Abstração"],
    indice_resposta=1,
    dificuldade="medio"
)

pergunta4 = Pergunta(
    tema=tema_poo,
    enunciado="Qual método especial é chamado para criar uma instância de uma classe?",
    alternativas=["__str__", "__repr__", "__init__", "__eq__"],
    indice_resposta=2,
    dificuldade="medio"
)

pergunta5 = Pergunta(
    tema=tema_sql,
    enunciado="Qual comando SQL consulta dados de uma tabela?",
    alternativas=["INSERT", "UPDATE", "SELECT", "DELETE"],
    indice_resposta=2,
    dificuldade="facil"
)

pergunta6 = Pergunta(
    tema=tema_sql,
    enunciado="Qual restrição identifica unicamente cada registro de uma tabela?",
    alternativas=["FOREIGN KEY", "PRIMARY KEY", "DEFAULT", "CHECK"],
    indice_resposta=1,
    dificuldade="medio"
)

pergunta7 = Pergunta(
    tema=tema_algoritmos,
    enunciado="Qual estrutura de dados segue o princípio LIFO?",
    alternativas=["Fila", "Pilha", "Lista ligada", "Árvore"],
    indice_resposta=1,
    dificuldade="medio"
)

pergunta8 = Pergunta(
    tema=tema_algoritmos,
    enunciado="Qual é a complexidade temporal da busca binária em uma lista ordenada?",
    alternativas=["O(1)", "O(n)", "O(log n)", "O(n²)"],
    indice_resposta=2,
    dificuldade="dificil"
)


quiz1 = Quiz(
    titulo="Fundamentos de Python",
    tempo_limite=600,
    limite_tentativas=3
)

quiz2 = Quiz(
    titulo="POO em Python",
    tempo_limite=900,
    limite_tentativas=2
)

quiz3 = Quiz(
    titulo="Avaliação de Banco de Dados",
    tempo_limite=1200,
    limite_tentativas=1
)

quiz1 = Quiz(
    titulo="Fundamentos de Python",
    tempo_limite=600,
    limite_tentativas=3
)

quiz2 = Quiz(
    titulo="POO em Python",
    tempo_limite=900,
    limite_tentativas=2
)

quiz3 = Quiz(
    titulo="Avaliação de Banco de Dados",
    tempo_limite=1200,
    limite_tentativas=1
)