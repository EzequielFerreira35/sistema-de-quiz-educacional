# Sistema de Quiz Educacional

## Descrição do Projeto
O Sistema de Quiz Educacional é um projeto que permite que os Usuários respondam e criem quizzes com título, perguntas, número máximo de tentativas e tempo limite. O Usuário poderá cadastrar perguntas de múltipla escolha, cada uma com um enunciado, alternativas, nível de dificuldade (Fácil, Médio e Difícil) e tema. Além disso, o Usuário poderá gerar diferentes tipos de relatórios que podem fornecer o seu desempenho no Quiz, ranking de usuários e evolução do desempenho do Usuário.

## Objetivo
Desenvolver um sistema que permita que Usuários possam criar, gerenciar e responder quizzes com perguntas de múltipla escolha, fornecendo pontuação, desempenho e evolução.

# Diagrama de Classes

```mermaid
classDiagram
    class Tema{
        - id: str
        - nome: str
    }

    class Quiz {
        - id: str
        + titulo: str
        - tempo_limite: int
        - limite_tentativas: int
        - lista_perguntas: list
        + adicionar_pergunta() -> bool
        + calcular_pontuacao_maxima() -> float
    }

    class Pergunta {
        - id: str
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
        - id: str
        + username: str
        + email: str
        - senha: str
        - tentativas: lista
        + registrar_tentativa() -> bool
    }

    class Tentativa {
        - id: str
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
        + data: datetime
        + nome: str
        + tipo: str
        + conteudo: dict
    }

    class BaseService {
        # itens: list
        + criar()
        + listar() list
        + buscar_por_id()
        + salvar() None
        + carregar() None
    }

    class QuizService {
        + criar_quiz() -> Quiz
        + adicionar_pergunta() -> bool
        }

    class TemaService {
        + criar_tema() -> Tema
        }

    class UsuarioService {
        + cadastrar() -> Usuario
        + atualizar_email() -> bool
        + buscar_por_email() -> Usuario
        }

    class PerguntaService {
        + criar_pergunta() -> Pergunta
        + listar_por_tema() -> list
        }

    class TentativaService {
        + reponder_quiz() -> Tentativa
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
    RelatorioService ..> Tentativa 
    RelatorioService ..> Usuario 


    Quiz "1" *-- "*" Pergunta
    Pergunta "*" o-- "*" Tema
    Tentativa "*" --> "1" Quiz
    Usuario "1" *-- "*" Tentativa

    BaseService <|-- TemaService
    BaseService <|-- QuizService
    BaseService <|-- UsuarioService
    BaseService <|-- PerguntaService
    BaseService <|-- TentativaService


```

# Lista das Classes

* Tema
* Quiz
* Pergunta
* Usuário
* Tentativa
* Relatório
* BaseService
* QuizService
* TemaService
* UsuarioService
* PerguntaService
* TentativaService
* RelatorioService
* AuthService 
