import sqlite3
from contextlib import contextmanager
from pathlib import Path

class SQLiteBase:
    """Classe base dos repositórios SQLite.
    Responsável por abrir a conexão e fazer commit
    """

    def __init__(self, caminho_db) -> None:
        self.caminho = Path(caminho_db)

    @contextmanager
    def conexao(self):
        conn = sqlite3.connect(self.caminho)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            with conn:
                yield conn
        finally:
            conn.close()