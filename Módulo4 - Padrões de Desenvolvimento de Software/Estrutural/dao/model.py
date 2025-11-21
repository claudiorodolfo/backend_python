"""
Model/Entity - Representa a entidade de negócio
"""

class Usuario:
    
    def __init__(self, id: int = None, nome: str = "", email: str = ""):
        self._id = id
        self._nome = nome
        self._email = email
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        self._email = value
    
    def __str__(self):
        return f"Usuario(id={self._id}, nome='{self._nome}', email='{self._email}')"
    