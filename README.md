## Descrição do Problema
O Sistema de Quiz Educacional é um projeto que permite que os Usuários respondam e criem quizzes com título, perguntas, número máximo de tentativas e tempo limite. O Usuário poderá cadastrar perguntas de múltipla escolha, cada uma com um enunciado, alternativas, nível de dificuldade (Fácil, Médio e Difícil) e tema. Além disso, o Usuário poderá gerar diferentes tipos de relatórios que podem fornecer o seu desempenho no Quiz, ranking de usuários e evolução do desempenho do Usuário.

## Objetivo
Desenvolver um sistema que permita que Usuários possam criar, gerenciar e responder quizzes com perguntas de múltipla escolha, fornecendo pontuação, desempenho e evolução.

# Diagrama de Classes

```mermaid
classDiagram
    class Tema{
        - id: int
        - nome: str
    }

    class Quiz {
        - id: int
        + titulo: str
        + tempo_limite: int
        + limite_tentativas: int
        - lista_perguntas: list
         + calcular_pontuacao_maxima() -> float
    }

    class Pergunta {
        - id: int
        + tema: Tema
        + enunciado: str
        + alternativas: list[str]
        - indice_resposta: int
        + dificuldade: str

        + verificar_resposta() -> bool
        + verificar_duplicata() -> bool
        + verificar_qtd_resposta() -> bool
        + peso() -> int
        }

    class Usuario {    
        - id: int
        + username: str
        + email: str
        - senha: str
        - tentativas: lista
    }

    class Tentativa {
        - id: int
        + usuario: Usuario
        + quiz: Quiz
        + respostas: list
        + pontuacao: int
        + tempo_total: int  
        + status_conclusao: bool

        + calcular_pontuacao() -> float
        + taxa_acerto() -> float
        }
    
    class Relatorio {
        + data: str
        + nome: str
        + tipo: str
        + conteudo: dict
    }

    class QuizService {
        + criar_quiz() -> Quiz
        + listar_quizzes() -> list
        + adicionar_pergunta() -> bool
        + buscar_por_id() -> Quiz
        }

    class TemaService {
        + criar_tema() -> Tema
        + listar_temas() -> list
        + buscar_por_id() -> Tema
        }

    class UsuarioService {
        + cadastrar() -> Usuario
        + atualizar_email() -> bool
        + listar_usuario() -> list
        + buscar_por_id() -> Usuario
        + buscar_por_email() -> Usuario
        }

    class PerguntaService {
        + criar_pergunta() -> Pergunta
        + listar_pergunta() -> list
        + listar_por_tema() -> list
        + buscar_por_id() -> list }

    class TentativaService {
        + reponder_quiz() -> Quiz
        + listar_por_usuario() -> list
        + listar_por_usuario_e_quiz() -> list 
        }

    class RelatorioService {
        + calcular_taxa_aprovacao() -> float
        + gerar_distribuicao_notas() -> dict
        + gerar_ranking_usuarios() -> list
        + gerar_desempenho_usuario() -> dict
        + gerar_questoes_mais_erradas() -> list
        + evolucao_usuario() -> list
        }

    class AuthService {
        + login() -> bool
        + logout() -> bool
        }

    UsuarioService ..> Usuario 
    QuizService ..> Quiz
    TemaService ..> Tema
    PerguntaService ..>  Pergunta
    TentativaService ..> Tentativa
    RelatorioService ..> Relatorio
    AuthService ..> Usuario

    Quiz "1" *-- "*" Pergunta
    Pergunta "*" o-- "*" Tema
    Tentativa "*" --> "1" Quiz
    Usuario "1" *-- "*" Tentativa

```


# Lista das Classes

* Tema
* Quiz
* Pergunta
* Usuário
* Tentativa
* Relatório
* QuizService
* TemaService
* UsuarioService
* PerguntaService
* TentativaService
* RelatorioService
* AuthService 
