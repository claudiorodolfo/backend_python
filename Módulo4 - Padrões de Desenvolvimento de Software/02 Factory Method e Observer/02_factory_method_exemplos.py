"""
02 - EXEMPLOS PRÁTICOS DO FACTORY METHOD
=========================================

Casos de uso reais:
1. Criação de diferentes tipos de notificações
2. Factory para diferentes formatos de exportação
3. Factory para diferentes estratégias de pagamento
4. Factory para diferentes tipos de autenticação
"""

# EXEMPLO 1: Factory para Notificações
# ======================================

from abc import ABC, abstractmethod

class Notificacao(ABC):
    """Interface para notificações"""
    
    @abstractmethod
    def enviar(self, destinatario, mensagem):
        pass

class EmailNotificacao(Notificacao):
    def enviar(self, destinatario, mensagem):
        return f"Email enviado para {destinatario}: {mensagem}"

class SMSNotificacao(Notificacao):
    def enviar(self, destinatario, mensagem):
        return f"SMS enviado para {destinatario}: {mensagem}"

class PushNotificacao(Notificacao):
    def enviar(self, destinatario, mensagem):
        return f"Push enviado para {destinatario}: {mensagem}"

class NotificacaoFactory(ABC):
    """Factory para criar notificações"""
    
    @abstractmethod
    def criar_notificacao(self, tipo) -> Notificacao:
        pass
    
    def enviar_notificacao(self, tipo, destinatario, mensagem):
        """Método helper que usa o factory"""
        notificacao = self.criar_notificacao(tipo)
        return notificacao.enviar(destinatario, mensagem)

class SistemaNotificacaoFactory(NotificacaoFactory):
    """Implementação concreta do factory"""
    
    def criar_notificacao(self, tipo) -> Notificacao:
        tipos = {
            "email": EmailNotificacao(),
            "sms": SMSNotificacao(),
            "push": PushNotificacao()
        }
        
        if tipo not in tipos:
            raise ValueError(f"Tipo de notificação não suportado: {tipo}")
        
        return tipos[tipo]


# EXEMPLO 2: Factory para Exportação de Dados
# ============================================

class Exportador(ABC):
    """Interface para exportadores"""
    
    @abstractmethod
    def exportar(self, dados, nome_arquivo):
        pass

class CSVExportador(Exportador):
    def exportar(self, dados, nome_arquivo):
        # Simulação
        return f"Exportando {len(dados)} registros para {nome_arquivo}.csv"

class JSONExportador(Exportador):
    def exportar(self, dados, nome_arquivo):
        return f"Exportando {len(dados)} registros para {nome_arquivo}.json"

class ExcelExportador(Exportador):
    def exportar(self, dados, nome_arquivo):
        return f"Exportando {len(dados)} registros para {nome_arquivo}.xlsx"

class ExportadorFactory(ABC):
    """Factory para exportadores"""
    
    @abstractmethod
    def criar_exportador(self, formato) -> Exportador:
        pass

class RelatorioFactory(ExportadorFactory):
    """Factory para exportação de relatórios"""
    
    def criar_exportador(self, formato) -> Exportador:
        exportadores = {
            "csv": CSVExportador(),
            "json": JSONExportador(),
            "excel": ExcelExportador()
        }
        
        if formato not in exportadores:
            raise ValueError(f"Formato não suportado: {formato}")
        
        return exportadores[formato]
    
    def exportar_relatorio(self, formato, dados, nome):
        """Método helper"""
        exportador = self.criar_exportador(formato)
        return exportador.exportar(dados, nome)


# EXEMPLO 3: Factory para Estratégias de Pagamento
# ==================================================

class Pagamento(ABC):
    """Interface para métodos de pagamento"""
    
    @abstractmethod
    def processar(self, valor):
        pass
    
    @abstractmethod
    def validar(self):
        pass

class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao
    
    def processar(self, valor):
        return f"Processando pagamento de R${valor} via cartão {self.numero_cartao[-4:]}"
    
    def validar(self):
        return len(self.numero_cartao) == 16

class PagamentoBoleto(Pagamento):
    def processar(self, valor):
        return f"Gerando boleto de R${valor}"
    
    def validar(self):
        return True  # Boleto sempre válido

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix):
        self.chave_pix = chave_pix
    
    def processar(self, valor):
        return f"Processando PIX de R${valor} para {self.chave_pix}"
    
    def validar(self):
        return self.chave_pix is not None

class PagamentoFactory(ABC):
    """Factory para métodos de pagamento"""
    
    @abstractmethod
    def criar_pagamento(self, tipo, **kwargs) -> Pagamento:
        pass

class ProcessadorPagamentoFactory(PagamentoFactory):
    """Factory para processamento de pagamentos"""
    
    def criar_pagamento(self, tipo, **kwargs) -> Pagamento:
        if tipo == "cartao":
            if "numero_cartao" not in kwargs:
                raise ValueError("Número do cartão necessário")
            return PagamentoCartao(kwargs["numero_cartao"])
        elif tipo == "boleto":
            return PagamentoBoleto()
        elif tipo == "pix":
            if "chave_pix" not in kwargs:
                raise ValueError("Chave PIX necessária")
            return PagamentoPix(kwargs["chave_pix"])
        else:
            raise ValueError(f"Método de pagamento não suportado: {tipo}")


# EXEMPLO 4: Factory para Autenticação
# =====================================

class Autenticador(ABC):
    """Interface para autenticadores"""
    
    @abstractmethod
    def autenticar(self, credenciais):
        pass

class AutenticadorLDAP(Autenticador):
    def autenticar(self, credenciais):
        usuario = credenciais.get("usuario")
        senha = credenciais.get("senha")
        # Simulação
        return f"Autenticado via LDAP: {usuario}"

class AutenticadorOAuth(Autenticador):
    def autenticar(self, credenciais):
        token = credenciais.get("token")
        # Simulação
        return f"Autenticado via OAuth com token: {token[:10]}..."

class AutenticadorDatabase(Autenticador):
    def autenticar(self, credenciais):
        usuario = credenciais.get("usuario")
        senha = credenciais.get("senha")
        # Simulação
        return f"Autenticado via Database: {usuario}"

class AutenticadorFactory(ABC):
    """Factory para autenticadores"""
    
    @abstractmethod
    def criar_autenticador(self, tipo) -> Autenticador:
        pass

class SistemaAutenticacaoFactory(AutenticadorFactory):
    """Factory para sistema de autenticação"""
    
    def criar_autenticador(self, tipo) -> Autenticador:
        autenticadores = {
            "ldap": AutenticadorLDAP(),
            "oauth": AutenticadorOAuth(),
            "database": AutenticadorDatabase()
        }
        
        if tipo not in autenticadores:
            raise ValueError(f"Tipo de autenticação não suportado: {tipo}")
        
        return autenticadores[tipo]
    
    def autenticar_usuario(self, tipo, credenciais):
        """Método helper"""
        autenticador = self.criar_autenticador(tipo)
        return autenticador.autenticar(credenciais)


# EXEMPLO 5: Factory Combinado - Sistema Completo
# =================================================

def exemplo_sistema_completo():
    """Demonstra uso de múltiplos factories em um sistema"""
    print("\n" + "=" * 60)
    print("SISTEMA COMPLETO USANDO FACTORY METHOD")
    print("=" * 60)
    
    # 1. Sistema de Notificações
    notif_factory = SistemaNotificacaoFactory()
    print("\n1. Notificações:")
    print(f"   {notif_factory.enviar_notificacao('email', 'user@email.com', 'Bem-vindo!')}")
    print(f"   {notif_factory.enviar_notificacao('sms', '11999999999', 'Código: 1234')}")
    
    # 2. Exportação de Dados
    export_factory = RelatorioFactory()
    dados = [{"id": 1}, {"id": 2}, {"id": 3}]
    print("\n2. Exportação:")
    print(f"   {export_factory.exportar_relatorio('csv', dados, 'relatorio')}")
    print(f"   {export_factory.exportar_relatorio('json', dados, 'relatorio')}")
    
    # 3. Processamento de Pagamento
    pagamento_factory = ProcessadorPagamentoFactory()
    print("\n3. Pagamentos:")
    pagamento1 = pagamento_factory.criar_pagamento("cartao", numero_cartao="1234567890123456")
    print(f"   {pagamento1.processar(100.00)}")
    
    pagamento2 = pagamento_factory.criar_pagamento("pix", chave_pix="user@email.com")
    print(f"   {pagamento2.processar(50.00)}")
    
    # 4. Autenticação
    auth_factory = SistemaAutenticacaoFactory()
    print("\n4. Autenticação:")
    resultado = auth_factory.autenticar_usuario("database", {
        "usuario": "admin",
        "senha": "senha123"
    })
    print(f"   {resultado}")


if __name__ == "__main__":
    print("=" * 60)
    print("EXEMPLOS PRÁTICOS - FACTORY METHOD")
    print("=" * 60)
    
    # Exemplos individuais
    print("\n1. Notificações:")
    notif_factory = SistemaNotificacaoFactory()
    notif = notif_factory.criar_notificacao("email")
    print(f"   {notif.enviar('user@email.com', 'Mensagem importante')}")
    
    print("\n2. Exportação:")
    export_factory = RelatorioFactory()
    exportador = export_factory.criar_exportador("csv")
    print(f"   {exportador.exportar([1, 2, 3], 'dados')}")
    
    print("\n3. Pagamento:")
    pagamento_factory = ProcessadorPagamentoFactory()
    pagamento = pagamento_factory.criar_pagamento("boleto")
    print(f"   {pagamento.processar(150.00)}")
    
    print("\n4. Autenticação:")
    auth_factory = SistemaAutenticacaoFactory()
    autenticador = auth_factory.criar_autenticador("oauth")
    resultado = autenticador.autenticar({"token": "abc123xyz789"})
    print(f"   {resultado}")
    
    # Exemplo completo
    exemplo_sistema_completo()

