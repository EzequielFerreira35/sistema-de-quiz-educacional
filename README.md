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
    + peso() -> int

## 4.Usuário
    - id: int
    - username: str
    - email: str
    - senha: str
    - tentativas: list(tentativas)    

## 5.Tentativa
    - id: int
    - usuario: Usuario
    - quiz: Quiz
    - repostas: list[int]
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
    + listar_quizzes() -> list[Quiz]
    + adicionar_pergunta() -> bool
    + buscar_por_id() -> Quiz

## 2. TemaService
    + criar_tema() -> Tema
    + listar_temas() -> list[Tema]
    + buscar_por_id() -> Tema

## 3. UsuarioService
    + cadastrar() -> Usuario
    + atualizar_email() -> bool
    + listar_usuario() -> list[Usuario]
    + buscar_por_id() -> Usuario
    + buscar_por_email() -> Usuario

## 4. PerguntaService
    + criar_pergunta() -> Pergunta
    + listar_pergunta() -> list[Pergunta]
    + listar_por_tema() -> list[Pergunta]
    + buscar_por_id() -: list[Pergunta]

## 5. TentativaService
    + reponder_quiz() -> Quiz
    + listar_por_usuario() -> list[Tentativa]
    + listar_por_usuario_e_quiz() -> list[Tentativa]

## 6. RelatorioService
    + gerar_taxa_aprovacao() -> float
    + gerar_distribuicao_notas() -> dict
    + gerar_ranking_usuarios() -> list
    + gerar_desempenho_usuario() -> dict
    + gerar_questoes_mais_erradas() -> list

## 6. AuthService 
    + login() -> bool
    + logout() -> bool
