# Classes Geral

## 1.Tema
    - id: int
    - nome: str

## 2.Quiz
    - id: int
    - titulo: str
    - dificuldade: str
    - tema_id: int
    - pontuacao_maxima: int
    - tempo_limite: int
    - limite_tentativas: int
    - lista_perguntas: list

## 3.Pergunta
    - id: int
    - tema_id: int
    - enunciado: str
    - alternativas: list
    - indice_respota: int
    
## 4.Usuário
    - id: int
    - username: str
    - email: str
    - senha: str
    - status: bool

## 5.Tentativa
    - id: int
    - usuario_id: int
    - quiz_id: int
    - pontuacao: int
    - tempo: int
    - acertos: int
    - perguntas_acertadas: list
    
## 6.Estatística
    - acertos: int

# Classes de Serviço

## 1. QuizService
    + criar_quiz()
    + listar_quizzes()
    + listar_por_tema_e_usuario()
    + adicionar_pergunta()
    + buscar_por_id()

## 2. TemaService
    + criar_tema()
    + listar_temas()

## 3. UsuarioService
    + cadastrar()
    + atualizar_email()
    + remover()
    + listar_usuario()
    + buscar_por_id()
    + buscar_por_email()

## 4. PerguntaService
    + criar_pergunta()
    + listar_pergunta()

## 5. TentativaService
    + reponder_quiz()
    + listar_por_usuario()
    + listar_por_usuario_e_quiz()

## 5. AuthService 
    + login()
    + logout()

# Classes de Dados

## 1. Repository
    + salvar()
    + buscar_por_id()
    + deletar()
    + listar_todos()

## 2. UsuarioRepository
    + buscar_por_email()

## 3. QuizRepository
    + listar_por_tema()
    + listar_por_tema_e_usuario()

## 4. TemaRepository

## 5. RelatorioRepository
    + listar_por_usuario()
    + listar_por_usuario_e_quiz()

## 6. TentativaRepository
    + listar_por_usuario()
    + listar_por_usuario_e_quiz()

# Classes de Relatórios

## 1.Relatório
### 1.1 Relatorio   Quiz
### 1.2 RelatorioTema
### 1.3 RelatorioUsuario
### 1.4 RelatorioTentativa

# Classes Customizadas Para tratamento de Erro
