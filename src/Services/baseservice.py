from src.configmanager import ConfigManager

class BaseService:
    def __init__(self):
        self.config = ConfigManager()