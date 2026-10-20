from Repository.UsuarioRepository import UsuarioRepositorySQLite
from Entidades.usuario import Usuario
from pathlib import Path

def main():
    # InicizalizarDataBase("Database/SistemaData.db")
    caminho = Path(__file__).parent / "Database" / "SistemaData.db"
    u1 = Usuario("David", "david@test.com", "123sdl#03SD")
    u2 = Usuario("Ezequiel", "eze@teste.com", "123easd@@$X")

    repo = UsuarioRepositorySQLite(caminho)

    dados = repo.buscar_por_id("47cc318f-e76a-46cf-92f0-cc4e9508f65a")
    dados2= repo.buscar_por_email("eze@teste.com")
    
    print(dados)
    print(dados2)

if __name__ == "__main__":
    main()