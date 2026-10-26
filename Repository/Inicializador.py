import sqlite3
from pathlib import Path
from contextlib import closing
from .sqlite_base import SQLiteBase

class InicializarDataBase(SQLiteBase):
    def __init__(self, caminho_db) -> None:
        super().__init__(caminho_db)
        self.caminho.parent.mkdir(parents=True, exist_ok=True)
        self.inicializar()

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row
        return conn

    def inicializar(self):
        with closing(self.conectar()) as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS usuario(
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL)""")

            conn.execute("""CREATE TABLE IF NOT EXISTS quiz(
            id TEXT PRIMARY KEY,
            titulo TEXT NOT NULL,
            tempo_limite INTEGER NOT NULL,
            limite_tentativas INTEGER NOT NULL)""")

            conn.execute("""CREATE TABLE IF NOT EXISTS tema(
            id TEXT PRIMARY KEY,
            nome TEXT UNIQUE NOT NULL)""")

            conn.execute("""CREATE TABLE IF NOT EXISTS tentativa(
            id TEXT PRIMARY KEY,
            id_quiz TEXT NOT NULL,
            id_usuario TEXT NOT NULL,
            data TEXT NOT NULL,
            pontuacao REAL NOT NULL,
            tempo_total INTEGER NOT NULL,
            status_conclusao INTEGER NOT NULL,
            
            FOREIGN KEY (id_quiz) REFERENCES quiz(id),
            FOREIGN KEY (id_usuario) REFERENCES usuario(id))""")

            conn.execute("""CREATE TABLE IF NOT EXISTS pergunta(
            id TEXT PRIMARY KEY,
            id_tema TEXT NOT NULL,
            enunciado TEXT NOT NULL,
            indice_resposta INTEGER NOT NULL,
            dificuldade TEXT NOT NULL,

            UNIQUE (id_tema, enunciado),
            
            FOREIGN KEY (id_tema) REFERENCES tema(id))""")

            conn.execute("""CREATE TABLE IF NOT EXISTS alternativa(
            id TEXT PRIMARY KEY,
            id_pergunta TEXT NOT NULL,
            enunciado TEXT NOT NULL,
            posicao INTEGER NOT NULL,
            
            UNIQUE (id_pergunta, posicao),

            FOREIGN KEY (id_pergunta) REFERENCES pergunta(id) ON DELETE CASCADE)""")

            conn.execute("""CREATE TABLE IF NOT EXISTS respostas_tentativa(
            id_tentativa TEXT NOT NULL,
            id_pergunta TEXT NOT NULL,
            id_alternativa TEXT,

            PRIMARY KEY (id_tentativa, id_pergunta),
            
            FOREIGN KEY (id_tentativa) REFERENCES tentativa(id) ON DELETE CASCADE,
            FOREIGN KEY (id_pergunta) REFERENCES pergunta(id),
            FOREIGN KEY (id_alternativa) REFERENCES alternativa(id))""")

            conn.execute("""CREATE TABLE IF NOT EXISTS quiz_pergunta(
            id_quiz TEXT NOT NULL,
            id_pergunta TEXT NOT NULL,
            
            PRIMARY KEY (id_quiz, id_pergunta),
            
            FOREIGN KEY (id_quiz) REFERENCES quiz(id) ON DELETE CASCADE,
            FOREIGN KEY (id_pergunta) REFERENCES pergunta(id) ON DELETE CASCADE)""")
            conn.commit()