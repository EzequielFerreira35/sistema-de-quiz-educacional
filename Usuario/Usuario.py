class Usuario:
    def __init__(self, id: int, username: str, email: str, senha: str, tentativas: list):
        self.id = id
        self.username = username
        self.email = email
        self.senha = senha
        self.tentativas = tentativas

class Tentativa:
    def __init__(self):
        pass
    