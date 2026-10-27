import sqlite3
from contextlib import contextmanager
from pathlib import Path

class SQLiteBase:
    """Classe base dos repositórios SQLite.
    Responsável por abrir a conexão e fazer commit
    """
    _CAMINHO_DB = Path(__file__).parent / "Database" / "SistemaData.db"

    def __init__(self) -> None:
        self.caminho = self._CAMINHO_DB

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