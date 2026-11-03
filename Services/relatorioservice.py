from Repository.TentativaRepository import TentativaRepository
from Repository.QuizRepository import QuizRepository
from Repository.UsuarioRepository import UsuarioRepository
from configmanager import ConfigManager
from .mixins import ValidadorIdMixin

class RelatorioService(ValidadorIdMixin):
    """
    Gerencia as regras de negócio e o ciclo de vida dos Relatórios.
    Herda atributos e métodos da Classe BaseService.
    """

    def __init__(self, tentativa_repo: TentativaRepository, quiz_repo: QuizRepository, usuario_repo: UsuarioRepository):
        self.tentativa_repo = tentativa_repo
        self.quiz_repo = quiz_repo
        self.usuario_repo = usuario_repo
        self.nota_corte = ConfigManager().taxa_aprovacao
        self.respostas_minima = ConfigManager().respostas_minimas

    def _percentuais(self, quiz_id) -> list[float]:
        quiz_id = self._validar_id(quiz_id, "quiz_id")
        quiz = self.quiz_repo.buscar_por_id(quiz_id)

        if quiz is None:
            raise ValueError("Esse quiz não existe!")

        maximo = quiz.calcular_pontuacao_maxima()
        if maximo == 0:
            return []

        concluidas = self.tentativa_repo.listar_concluidas_por_quiz(quiz_id)

        return [tentativa["pontuacao"] / maximo for tentativa in concluidas]

    def _maximo(self, quiz_id: str):
        quiz_id = self._validar_id(quiz_id)

        quiz = self.quiz_repo.buscar_por_id(quiz_id)

        return quiz.calcular_pontuacao_maxima()

    def calcular_taxa_aprovacao(self, quiz_id: str) -> dict:
        percentuais = self._percentuais(quiz_id)
        aprovados = sum(percentual >= self.nota_corte for percentual in percentuais)
        return {
            "tentativas_condluidas": len(percentuais),
            "aprovados": aprovados,
            "taxa_parovados": aprovados / len(percentuais) if percentuais else None
        }

    def gerar_distribuicao_notas(self, quiz_id: str) -> dict:
        taxas = ["0-19%", "20-39%", "40-59%", "60-79%", "80-100%"]
        distribuitcao = dict.fromkeys(taxas, 0)

        for percentual in self._percentuais(quiz_id):
            n = percentual * 100

            if 0 <= n <= 19:
                distribuitcao["0-19%"] += 1

            elif 20 <= n <= 39:
                distribuitcao["20-39%"] += 1

            elif 40 <= n <= 59:
                distribuitcao["40-59%"] += 1

            elif 60 <= n <= 79:
                distribuitcao["60-79%"] += 1

            else:
                distribuitcao["80-100%"] += 1

        return distribuitcao

    def gerar_relatorio_basico(self, tentativa_id: str):
        tentativa_id = self._validar_id(tentativa_id, "tentativa_id")

        tentativa = self.tentativa_repo.buscar_por_id(tentativa_id)

        if tentativa is None:
            raise ValueError("Essa tentativa não existe!")

        perguntas = tentativa.quiz.lista_perguntas
        maximo = tentativa.quiz.calcular_pontuacao_maxima()

        dados = {
            "pontuacao_atingida": tentativa.pontuacao,
            "pontuacao_maxima": maximo,
            "taxa_de_acertos": tentativa.taxa_acertos(),
            "aproveitamento_pontuacao": tentativa.pontuacao/ maximo if maximo > 0 else 0,
            "tempo_gasto": tentativa.tempo_total,
            "respostas_usuario": tentativa.respostas,
            "gabarito": [p.indice_resposta for p in perguntas]
        }

        return dados

    def gerar_ranking_usuarios(self):
        tentativas = self.tentativa_repo.listar_concluidas_por_usuario()

        usuarios_agrupados = {}
        ranking = [] 

        for tentativa in tentativas:
            usuario = tentativa["usuario_id"]
            if usuario not in usuarios_agrupados:
                usuarios_agrupados[usuario] = {
                    "nome": tentativa["usuario_nome"],
                    "pontuacao_total": 0,
                    "quantidade_tentativas": 0,
                }

            usuarios_agrupados[usuario]["pontuacao_total"] += tentativa["pontuacao"]
            usuarios_agrupados[usuario]["quantidade_tentativas"] += 1

        for usuario, dados in usuarios_agrupados.items():
            ranking.append(
                {
                    "id": usuario,
                    "nome": dados["nome"],
                    "pontuacao_total": dados["pontuacao_total"],
                    "quantidade_tentativas": dados["quantidade_tentativa"],
                    "pontuacao_media": dados["pontuacao_total"] / dados["quantidade_tentativas"]
                }
            )

        ranking = sorted(ranking, key= lambda x: (x["pontuacao_media"], x["pontuacao_total"]), reverse=True)

        for posicao, usuario in enumerate(ranking, start=1):
            usuario["posicao"] = posicao

        return ranking

    def gerar_desempenho_usuario(self, usuario_id: str):
        usuario_id = self._validar_id(usuario_id, "usuario_id")

        if self.usuario_repo.buscar_por_id(usuario_id) is None:
            raise ValueError("Esse usuário não existe!")

        questoes = self.tentativa_repo.listar_respostas_por_pergunta(usuario_id)

        acertos_geral, respostas_geral = 0, 0

        desempenho = {"taxa_acertos_geral": 0,
                       "total_respostas": 0, 
                       "temas": []}

        temas_agrupados = {}

        for q in questoes:
            tema = q["tema_id"]
            if tema not in temas_agrupados:
                temas_agrupados[tema] = {
                    "nome_tema": q["nome_tema"],
                    "acertos": 0,
                    "total_respostas": 0,
                    "taxa_acertos": 0
                }

            acertos_geral += q["acertos"]
            respostas_geral += q["total_respostas"]
            
            temas_agrupados[tema]["acertos"] += q["acertos"]
            temas_agrupados[tema]["total_respostas"] += q["total_respostas"]

            temas_agrupados[tema]["taxa_acertos"] = temas_agrupados[tema]["acertos"] / temas_agrupados[tema]["total_respostas"]


        desempenho["temas"] = list(temas_agrupados.values())
        desempenho["total_respostas"] = respostas_geral
        desempenho["taxa_acertos_geral"] = acertos_geral / respostas_geral if respostas_geral != 0 else None

        return desempenho
    
    def gerar_questoes_mais_erradas(self, limite: int) -> list[dict]:
        if isinstance(limite, bool) or not isinstance(limite, int) or limite <=0: 
            raise ValueError("Limite inválido!")
        
        questoes = self.tentativa_repo.listar_respostas_por_pergunta()

        # cada item: {"pergunta_id": ..., "pergunta_enunciado": ...,
        #             "tema_id": ..., "nome_tema": ...,
        #             "total_respostas": 3, "acertos": 2}

        questoes = [q for q in questoes if q["total_respostas"] >= self.respostas_minima]

        for q in questoes:
            erros = q["total_respostas"] - q["acertos"]
            taxa = erros / q["total_respostas"]

            q["taxa_erros"] = taxa

        questoes_mais_erradas = sorted(questoes, key=lambda x: (x["taxa_erros"], x["total_respostas"]), reverse=True)

        return questoes_mais_erradas[:limite]

    def evolucao_usuario(self, usuario_id: str) -> list[dict]:
        usuario_id = self._validar_id(usuario_id)

        if self.usuario_repo.buscar_por_id(usuario_id) is None:
            raise ValueError("Esse usuário não existe!")

        tentativas = self.tentativa_repo.listar_concluidas_por_usuario(usuario_id)
        maximos = {}

        evolucao = [] 

        for tentativa in tentativas:
            quiz_id = tentativa["quiz_id"]

            if quiz_id not in maximos:
                maximos[quiz_id] = self._maximo(quiz_id)

            if maximos[quiz_id] == 0:
                continue
            
            evolucao.append({
                    "data": tentativa["data"],
                    "quiz": tentativa["quiz_titulo"],
                    "percentual_pontuacao": tentativa["pontuacao"] / maximos[quiz_id],
                    "pontuacao": tentativa["pontuacao"],    
                    "tempo_total": tentativa["tempo_total"]
                })


        return evolucao
    