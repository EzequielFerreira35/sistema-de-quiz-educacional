from Repository.Inicializador import InicializarDataBase
from pathlib import Path

CAMINHO_DB = Path(__file__).parent / "Database" / "SistemaData.db"

def main():
    InicializarDataBase(CAMINHO_DB)


if __name__ == "__main__":
    main()