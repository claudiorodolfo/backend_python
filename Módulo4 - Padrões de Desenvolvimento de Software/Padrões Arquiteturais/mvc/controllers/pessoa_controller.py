from typing import Dict, Optional
from models.repository.repositorio_pessoa import RepositorioPessoas
from models.entities.pessoa import Pessoa


class PessoaController:
    """
    Controller Pattern - Camada de controle e lógica de negócio
    Responsável por coordenar View e Repository
    Contém validações, regras de negócio e formatação de dados
    
    Recebe dados da View via dicionário (desacopla View das entidades)
    Faz conversão de tipos quando necessário (string -> int/float)
    Cria entidades internamente para persistência
    """
    def __init__(self, repository: RepositorioPessoas):
        self.repository = repository

    def __validarCampos(self, pessoaObj: Pessoa):
        """Valida as regras de negócio da pessoa (valores já convertidos)"""
        if pessoaObj.nome is not None:
            if not pessoaObj.nome.strip():
                raise ValueError('Campo Nome Incorreto!')
        
        if pessoaObj.idade is not None:
            if pessoaObj.idade < 0:
                raise ValueError('Campo Idade Incorreto! Idade não pode ser negativa!')

        if pessoaObj.altura is not None:
            if pessoaObj.altura <= 0:
                raise ValueError('Campo Altura Incorreto! Altura deve ser maior que zero!')

    def __formatarResposta(self, pessoa: Pessoa) -> Dict:
        """Formata a resposta no padrão da API com head e body separados"""
        return {
            "head": {
                "count": 1,
                "type": "Pessoa"
            },
            "body": {
                "email": pessoa.email,
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "altura": pessoa.altura
            }
        }

    def cadastrarPessoa(self, dados_pessoa: Dict) -> Dict:
        """
        Coordena o cadastro de uma pessoa
        Recebe dicionário da View, converte tipos, cria entidade, valida, persiste e retorna resposta padronizada
        """
        try:
            # Conversão de tipos e criação da entidade
            email = dados_pessoa.get("email", "").strip() if dados_pessoa.get("email") else ""
            if not email:
                raise ValueError('Campo Email é obrigatório!')
            
            nome = dados_pessoa.get("nome", "").strip() if dados_pessoa.get("nome") else None
            idade = None
            altura = None
            
            if dados_pessoa.get("idade"):
                try:
                    idade = int(dados_pessoa["idade"])
                except (ValueError, TypeError):
                    raise ValueError('Campo Idade Incorreto! Deve ser um número inteiro!')
            
            if dados_pessoa.get("altura"):
                try:
                    altura = float(dados_pessoa["altura"])
                except (ValueError, TypeError):
                    raise ValueError('Campo Altura Incorreto! Deve ser um número!')
            
            # Criação da entidade Pessoa
            pessoa = Pessoa(email, nome, idade, altura)
            
            # Validação
            self.__validarCampos(pessoa)
            
            # Persistência
            pessoaCriada = self.repository.criar(pessoa)
            
            # Formatação da resposta
            dados = self.__formatarResposta(pessoaCriada)
            
            return {
                "success": True,
                "data": dados
            }
        except Exception as excecao:
            dados = {
                "head": {
                    "code": 0,
                },
                "body": {
                    "error": str(excecao)
                }
            }
            return {
                "success": False,
                "error": dados
            }

    def buscarPorEmail(self, email: str) -> Dict:
        """
        Coordena a busca de uma pessoa por email
        Recebe string diretamente da View (padrão simples de frameworks)
        """
        try:
            if not email or not email.strip():
                raise ValueError('E-mail não pode ser vazio!')
            
            pessoa_busca = Pessoa(email.strip())
            pessoa = self.repository.buscarPorEmail(pessoa_busca)
            
            if not pessoa:
                raise ValueError('Pessoa não encontrada!')
            
            dados = self.__formatarResposta(pessoa)
            
            return {
                "success": True,
                "data": dados
            }
        except Exception as excecao:
            dados = {
                "head": {
                    "code": 0,
                },
                "body": {
                    "error": str(excecao)
                }
            }
            return {
                "success": False,
                "error": dados
            }

    def atualizarPessoa(self, dados_pessoa: Dict) -> Dict:
        """
        Coordena a atualização de uma pessoa
        Recebe dicionário da View, converte tipos, cria entidade, valida, atualiza e retorna resposta padronizada
        """
        try:
            # Conversão de tipos e criação da entidade
            email = dados_pessoa.get("email", "").strip() if dados_pessoa.get("email") else ""
            if not email:
                raise ValueError('Campo Email é obrigatório!')
            
            nome = dados_pessoa.get("nome", "").strip() if dados_pessoa.get("nome") else None
            idade = None
            altura = None
            
            if dados_pessoa.get("idade"):
                try:
                    idade = int(dados_pessoa["idade"])
                except (ValueError, TypeError):
                    raise ValueError('Campo Idade Incorreto! Deve ser um número inteiro!')
            
            if dados_pessoa.get("altura"):
                try:
                    altura = float(dados_pessoa["altura"])
                except (ValueError, TypeError):
                    raise ValueError('Campo Altura Incorreto! Deve ser um número!')
            
            # Criação da entidade Pessoa
            pessoa = Pessoa(email, nome, idade, altura)
            
            # Validação
            self.__validarCampos(pessoa)
            
            # Persistência
            pessoaAtualizada = self.repository.atualizar(pessoa)
            
            if not pessoaAtualizada:
                raise ValueError('Pessoa não encontrada para atualização!')
            
            # Formatação da resposta
            dados = self.__formatarResposta(pessoaAtualizada)
            
            return {
                "success": True,
                "data": dados
            }
        except Exception as excecao:
            dados = {
                "head": {
                    "code": 0,
                },
                "body": {
                    "error": str(excecao)
                }
            }
            return {
                "success": False,
                "error": dados
            }

    def apagarPessoa(self, dados_pessoa: Dict) -> Dict:
        """
        Coordena a exclusão de uma pessoa
        Recebe dicionário da View, cria entidade temporária para busca e apaga
        """
        try:
            email = dados_pessoa.get("email", "").strip() if dados_pessoa.get("email") else ""
            if not email:
                raise ValueError('Campo Email é obrigatório!')
            
            # Criação da entidade Pessoa apenas com email para busca
            pessoa = Pessoa(email)
            
            # Persistência
            sucesso = self.repository.apagar(pessoa)
            
            if not sucesso:
                raise ValueError('Pessoa não encontrada para exclusão!')
            
            # Formatação da resposta
            dados = {
                "head": {
                    "count": 1,
                    "type": "Pessoa"
                },
                "body": {
                    "email": email
                }
            }
            
            return {
                "success": True,
                "data": dados
            }
        except Exception as excecao:
            dados = {
                "head": {
                    "code": 0,
                },
                "body": {
                    "error": str(excecao)
                }
            }
            return {
                "success": False,
                "error": dados
            }

