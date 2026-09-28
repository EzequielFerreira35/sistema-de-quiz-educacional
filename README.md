# Descrição do Problema
O Sistema de Quiz Educacional é um projeto que permite que os Usuários respondam e criem quizzes com título, perguntas, número máximo de tentativas e tempo limite. O Usuário poderá cadastrar perguntas de múltipla escolha, cada uma com um enunciado, alternativas, nível de dificuldade (Fácil, Médio e Difícil) e tema. Além disso, o Usuário poderá gerar diferentes tipos de relatórios que podem fornecer o seu desempenho no Quiz, ranking de usuários e evolução do desempenho do Usuário.

# Objetivo
Desenvolver um sistema que permita que Usuários possam criar, gerenciar e responder quizzes com perguntas de múltipla escolha, fornecendo pontuação, desempenho e evolução.

# Classes Geral

## 1.Tema
    - id: int
    - nome: str

## 2.Quiz
    - id: int
    - titulo: str
    - tempo_limite: int
    - limite_tentativas: int
    - lista_perguntas: list

    + calcular_pontuacao_maxima() -> float

## 3.Pergunta
    - id: int
    - tema: Tema
    - enunciado: str
    - alternativas: list[str]
    - indice_respota: int
    - dificuldade: str

    + verificar_resposta() -> bool
    + verificar_duplicata() -> bool
    + verificar_qtd_resposta() -> bool
    + peso() -> int

## 4.Usuário
    - id: int
    - username: str
    - email: str
    - senha: str
    - tentativas: lista

## 5.Tentativa
    - id: int
    - usuario: Usuario
    - quiz: Quiz
    - repostas: list
    - pontuacao: int
    - tempo_total: int  
    - status_conclusao: bool

    + calcular_pontuacao() -> float
    + taxa_acerto() -> float

## 6.Relatório
    data: str
    nome: str
    tipo: str
    conteudo: dict

# Classes de Serviço

## 1. QuizService
    + criar_quiz() -> Quiz
    + listar_quizzes() -> list
    + adicionar_pergunta() -> bool
    + buscar_por_id() -> Quiz

## 2. TemaService
    + criar_tema() -> Tema
    + listar_temas() -> list
    + buscar_por_id() -> Tema

## 3. UsuarioService
    + cadastrar() -> Usuario
    + atualizar_email() -> bool
    + listar_usuario() -> list
    + buscar_por_id() -> Usuario
    + buscar_por_email() -> Usuario

## 4. PerguntaService
    + criar_pergunta() -> Pergunta
    + listar_pergunta() -> list
    + listar_por_tema() -> list
    + buscar_por_id() -> list

## 5. TentativaService
    + reponder_quiz() -> Quiz
    + listar_por_usuario() -> list
    + listar_por_usuario_e_quiz() -> list

## 6. RelatorioService
    + calcular_taxa_aprovacao() -> float
    + gerar_distribuicao_notas() -> dict
    + gerar_ranking_usuarios() -> list
    + gerar_desempenho_usuario() -> dict
    + gerar_questoes_mais_erradas() -> list
    + evolucaoo_usuario() -> list

## 7. AuthService 
    + login() -> bool
    + logout() -> bool
