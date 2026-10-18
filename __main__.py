from Entidades.tema import Tema
from Entidades.pergunta import Pergunta
from Entidades.quiz import Quiz
from Entidades.usuario import Usuario, Tentativa
import pprint

def main():
    quimica = Tema("Química")
    # Pergunta 1
    pgt = "Qual das seguintes alternativas apresenta exclusivamente uma substância pura?"
    alt = ["0.Água mineral", "1.Ar atmosférico", "2.Vinagre", "3.Fio de cobre", "4.Aço inoxidável"]
    p1 = Pergunta(quimica, pgt, alt, 3, "facil")

    # Pergunta 2
    pgt = "O número atômico (Z) de um elemento representa a quantidade de prótons. Se um átomo neutro possui Z = 11 e número de massa A = 23, qual é a sua quantidade de nêutrons?"
    alt = ["0.11", "1.12", "2.23", "3.34", "4.15"]
    p2 = Pergunta(quimica, pgt, alt, 1, "facil")

    # Pergunta 3
    pgt = "O modelo atômico que comparava o átomo a uma 'bola de bilhar' — maciça, esférica e indivisível — foi proposto por qual cientista?"
    alt = ["0.J. J. Thomson", "1.Ernest Rutherford", "2.John Dalton", "3.Niels Bohr", "4.Linus Pauling"]
    p3 = Pergunta(quimica, pgt, alt, 2, "facil")

    # Pergunta 4
    pgt = "Qual é o tipo de ligação química que ocorre por meio do compartilhamento de pares de elétrons entre os átomos?"
    alt = ["0.Ligação iônica", "1.Ligação metálica", "2.Ligação de hidrogênio", "3.Ligação covalente", "4.Força dipolo-induzido"]
    p4 = Pergunta(quimica, pgt, alt, 3, "facil")

    # Pergunta 5
    pgt = "O sal de cozinha é composto majoritariamente por cloreto de sódio. Qual é a fórmula química correta dessa substância?"
    alt = ["0.HCl", "1.CaCl₂", "2.NaCl", "3.NaOH", "4.NaHCO₃"]
    p5 = Pergunta(quimica, pgt, alt, 2, "facil")

    # Pergunta 6
    pgt = "Na tabela periódica, qual letra representa o símbolo químico do elemento Potássio?"
    alt = ["0.P", "1.Po", "2.Pt", "3.K", "4.Ka"]
    p6 = Pergunta(quimica, pgt, alt, 3, "facil")

    # Pergunta 7
    pgt = "Qual das seguintes alternativas descreve uma transformação puramente física da matéria?"
    alt = ["0.Queima de um pedaço de madeira", "1.Cozimento de um ovo", "2.Derretimento de um cubo de gelo", "3.Enferrujamento de um prego de ferro", "4.Azedamento do leite"]
    p7 = Pergunta(quimica, pgt, alt, 2, "facil")

    # Pergunta 8
    pgt = "Uma solução com pH igual a 3 é classificada como:"
    alt = ["0.Neutra", "1.Ácida", "2.Básica ou alcalina", "3.Anfótera", "4.Salina"]
    p8 = Pergunta(quimica, pgt, alt, 1, "facil")

    # Pergunta 9
    pgt = "Qual é o método de separação de misturas mais adequado para isolar os componentes de uma mistura heterogênea de água e óleo?"
    alt = ["0.Filtração simples", "1.Destilação fracionada", "2.Decantação", "3.Evaporação", "4.Centrifugação"]
    p9 = Pergunta(quimica, pgt, alt, 2, "facil")

    # Pergunta 10
    pgt = "Substâncias que aceleram a velocidade de uma reação química sem serem consumidas durante o processo são chamadas de:"
    alt = ["0.Reagentes", "1.Produtos", "2.Inibidores", "3.Solutos", "4.Catalisadores"]
    p10 = Pergunta(quimica, pgt, alt, 4, "facil")

    lista_de_perguntas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    q1 = Quiz("Quiz de Química")
    for p in lista_de_perguntas:
        q1.adicionar_perguntas(p)

    dados = q1.lista_perguntas
    lista_De_respsotas = []

    for x in dados:
        print(x.enunciado)

        for y in x.alternativas:
            print(y)

        escolha = int(input("Escolha a alternativa: "))

        x.verificar_resposta(escolha)
        acerto = lista_De_respsotas.append(escolha)
        print()
        if acerto:
            print("Resposta correta!!!")
        else:
            print("Resposta errada!!!")
            print(f"Alternativa correta: {x.alternativas[x.indice_resposta]}")
        print()

    novo_usuario = Usuario(
        nome="DevQuimica",
        email="usuario@email.com",
        senha="SenhaSegura@123"
    )

    t1 = Tentativa(q1, lista_De_respsotas, 1000)
    t1.calcular_pontuacao()
    print(f"Pontuação: {t1.pontuacao}")
    print(f"Taxa de acerto: {t1.taxa_acertos()}")
    print(f"Conclusão: {t1.status_conclusao}")

if __name__ == "__main__":
    main()