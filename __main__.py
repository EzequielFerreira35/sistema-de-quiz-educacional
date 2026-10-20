from Repository.Inicializador import InicializarDataBase
from Entidades.usuario import Usuario
from pathlib import Path

def main():
    InicializarDataBase("Database/SistemaData.db")


if __name__ == "__main__":
    main()