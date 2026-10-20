import sqlite3
from pathlib import Path

class InicizalizarDataBase:
    def __init__(self, db_path: str) -> None:
        self.caminho = Path(db_path)
        self.inicializar()

    def conectar(self):
        conn = sqlite3.connect(self.caminho)
        conn.execute("PRAGMA foreign_keys = OK")
        conn.row_factory = sqlite3.Row
        return conn

    def inicializar(self):
        with self.conectar() as conn:
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
            id TEXTE PRIMARY KEY,
            nome TEXT NOT NULL)""")

            conn.execute("""CREATE TABLE IF NOT EXISTS tentativa(
            id TEXT PRIMARY KEY,
            id_quiz TEXT NOT NULL,
            id_usuario TEXT NOT NULL,
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
            
            FOREIGN KEY (id_tema) REFERENCES tema(id))""")

            conn.execute("""CREATE TABLE IF NOT EXISTS alternativa(
            id TEXT PRIMARY KEY,
            id_pergunta TEXT NOT NULL,
            enunciado TEXT NOT NULL,
            
            FOREIGN KEY (id_pergunta) REFERENCES pegunta(id))""")

            conn.execute("""CREATE TABLE IF NOT EXISTS respostas_tentativa(
            id TEXT PRIMARY KEY,
            id_tentativa TEXT NOT NULL,
            id_pergunta TEXT NOT NULL,
            id_alternativa TEXT NOT NULL,
            
            FOREIGN KEY (id_tentativa) REFERENCES tentativa(id),
            FOREIGN KEY (id_pergunta) REFERENCES pergunta(id))""")
        conn.close()
