"""
04 - CASOS PRÁTICOS DE USO DO OBSERVER
=======================================

Exemplos reais:
1. Sistema de notificações de usuário
2. Monitoramento de mudanças em dados
3. Sistema de cache invalidation
4. Editor de texto com múltiplas visualizações
5. Sistema de eventos de pedidos
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any

# CASO DE USO 1: Sistema de Notificações de Usuário
# ===================================================

class UsuarioObserver(ABC):
    """Observer para eventos de usuário"""
    
    @abstractmethod
    def notificar(self, evento: str, dados: Dict[str, Any]):
        pass


class EmailNotificacaoObserver(UsuarioObserver):
    """Envia notificações por email"""
    
    def __init__(self, email):
        self.email = email
    
    def notificar(self, evento: str, dados: Dict[str, Any]):
        if evento == "novo_pedido":
            print(f"[EMAIL {self.email}] Novo pedido #{dados['pedido_id']} criado")
        elif evento == "pedido_entregue":
            print(f"[EMAIL {self.email}] Pedido #{dados['pedido_id']} foi entregue")
        elif evento == "promocao":
            print(f"[EMAIL {self.email}] Nova promoção: {dados['titulo']}")


class PushNotificacaoObserver(UsuarioObserver):
    """Envia notificações push"""
    
    def __init__(self, device_id):
        self.device_id = device_id
    
    def notificar(self, evento: str, dados: Dict[str, Any]):
        print(f"[PUSH {self.device_id}] Notificação: {evento}")


class SistemaUsuario:
    """Subject que gerencia eventos de usuário"""
    
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id
        self._observers: List[UsuarioObserver] = []
        self._pedidos = []
    
    def adicionar_observer(self, observer: UsuarioObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remover_observer(self, observer: UsuarioObserver):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def _notificar(self, evento: str, dados: Dict[str, Any]):
        """Notifica todos os observers"""
        for observer in self._observers:
            observer.notificar(evento, dados)
    
    def criar_pedido(self, pedido_id):
        """Cria pedido e notifica"""
        self._pedidos.append(pedido_id)
        self._notificar("novo_pedido", {"pedido_id": pedido_id})
    
    def marcar_entregue(self, pedido_id):
        """Marca pedido como entregue e notifica"""
        self._notificar("pedido_entregue", {"pedido_id": pedido_id})
    
    def enviar_promocao(self, titulo):
        """Envia promoção e notifica"""
        self._notificar("promocao", {"titulo": titulo})


# CASO DE USO 2: Monitoramento de Mudanças em Dados
# ===================================================

class DadosObserver(ABC):
    """Observer para mudanças em dados"""
    
    @abstractmethod
    def on_dados_atualizados(self, campo, valor_antigo, valor_novo):
        pass


class AuditoriaObserver(DadosObserver):
    """Registra mudanças para auditoria"""
    
    def __init__(self):
        self.registros = []
    
    def on_dados_atualizados(self, campo, valor_antigo, valor_novo):
        registro = {
            "campo": campo,
            "valor_antigo": valor_antigo,
            "valor_novo": valor_novo,
            "timestamp": "2024-01-01 10:00:00"  # Simplificado
        }
        self.registros.append(registro)
        print(f"[AUDITORIA] {campo} alterado: {valor_antigo} -> {valor_novo}")


class CacheObserver(DadosObserver):
    """Invalidates cache quando dados mudam"""
    
    def __init__(self):
        self.cache = {}
    
    def on_dados_atualizados(self, campo, valor_antigo, valor_novo):
        # Remove do cache quando há mudanças
        if campo in self.cache:
            del self.cache[campo]
            print(f"[CACHE] Cache invalidado para campo: {campo}")


class ModeloDados:
    """Subject que mantém dados observáveis"""
    
    def __init__(self):
        self._observers: List[DadosObserver] = []
        self._dados = {}
    
    def adicionar_observer(self, observer: DadosObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self, campo, valor_antigo, valor_novo):
        for observer in self._observers:
            observer.on_dados_atualizados(campo, valor_antigo, valor_novo)
    
    def set_valor(self, campo, valor):
        """Define valor e notifica mudanças"""
        valor_antigo = self._dados.get(campo)
        self._dados[campo] = valor
        
        if valor_antigo != valor:
            self._notificar(campo, valor_antigo, valor)
    
    def get_valor(self, campo):
        return self._dados.get(campo)


# CASO DE USO 3: Sistema de Eventos de Pedidos (E-commerce)
# ===========================================================

class PedidoObserver(ABC):
    """Observer para eventos de pedidos"""
    
    @abstractmethod
    def on_pedido_evento(self, evento: str, pedido_info: Dict):
        pass


class EstoqueObserver(PedidoObserver):
    """Atualiza estoque quando pedido é criado"""
    
    def __init__(self):
        self.estoque = {"produto1": 100, "produto2": 50}
    
    def on_pedido_evento(self, evento: str, pedido_info: Dict):
        if evento == "pedido_criado":
            produtos = pedido_info.get("produtos", [])
            for produto in produtos:
                prod_id = produto["id"]
                qtd = produto["quantidade"]
                if prod_id in self.estoque:
                    self.estoque[prod_id] -= qtd
                    print(f"[ESTOQUE] {prod_id}: {self.estoque[prod_id]} unidades restantes")


class FinanceiroObserver(PedidoObserver):
    """Registra transações financeiras"""
    
    def __init__(self):
        self.transacoes = []
    
    def on_pedido_evento(self, evento: str, pedido_info: Dict):
        if evento == "pedido_criado":
            valor = pedido_info.get("valor_total", 0)
            self.transacoes.append({
                "pedido_id": pedido_info["id"],
                "valor": valor,
                "tipo": "entrada"
            })
            print(f"[FINANCEIRO] Receita registrada: R${valor:.2f}")


class LogisticaObserver(PedidoObserver):
    """Gerencia logística do pedido"""
    
    def on_pedido_evento(self, evento: str, pedido_info: Dict):
        if evento == "pedido_criado":
            print(f"[LOGÍSTICA] Preparando envio do pedido #{pedido_info['id']}")
        elif evento == "pedido_enviado":
            print(f"[LOGÍSTICA] Pedido #{pedido_info['id']} enviado!")


class Pedido:
    """Subject que representa um pedido"""
    
    def __init__(self, pedido_id):
        self.pedido_id = pedido_id
        self._observers: List[PedidoObserver] = []
        self.produtos = []
        self.valor_total = 0
        self.status = "pendente"
    
    def adicionar_observer(self, observer: PedidoObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self, evento: str):
        pedido_info = {
            "id": self.pedido_id,
            "produtos": self.produtos,
            "valor_total": self.valor_total,
            "status": self.status
        }
        for observer in self._observers:
            observer.on_pedido_evento(evento, pedido_info)
    
    def adicionar_produto(self, produto_id, quantidade, preco):
        """Adiciona produto ao pedido"""
        self.produtos.append({
            "id": produto_id,
            "quantidade": quantidade,
            "preco": preco
        })
        self.valor_total += quantidade * preco
    
    def finalizar(self):
        """Finaliza o pedido e notifica"""
        self.status = "finalizado"
        self._notificar("pedido_criado")
    
    def marcar_enviado(self):
        """Marca pedido como enviado e notifica"""
        self.status = "enviado"
        self._notificar("pedido_enviado")


# CASO DE USO 4: Editor de Texto com Múltiplas Visualizações
# ============================================================

class VisualizacaoObserver(ABC):
    """Observer para atualizações de visualização"""
    
    @abstractmethod
    def atualizar(self, texto):
        pass


class VisualizacaoTexto(VisualizacaoObserver):
    """Visualização em texto puro"""
    
    def atualizar(self, texto):
        print(f"[TEXTO] {texto}")


class VisualizacaoEstatisticas(VisualizacaoObserver):
    """Visualização de estatísticas do texto"""
    
    def atualizar(self, texto):
        palavras = len(texto.split())
        caracteres = len(texto)
        print(f"[STATS] Palavras: {palavras}, Caracteres: {caracteres}")


class VisualizacaoPreview(VisualizacaoObserver):
    """Preview formatado do texto"""
    
    def atualizar(self, texto):
        preview = texto[:50] + "..." if len(texto) > 50 else texto
        print(f"[PREVIEW] {preview}")


class EditorTexto:
    """Subject que mantém o texto editado"""
    
    def __init__(self):
        self._observers: List[VisualizacaoObserver] = []
        self._texto = ""
    
    def adicionar_visualizacao(self, observer: VisualizacaoObserver):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def _notificar(self):
        """Notifica todas as visualizações"""
        for observer in self._observers:
            observer.atualizar(self._texto)
    
    def escrever(self, texto):
        """Atualiza texto e notifica observers"""
        self._texto = texto
        self._notificar()
    
    def get_texto(self):
        return self._texto


# EXEMPLO COMPLETO: Sistema Integrado
# ====================================

def exemplo_sistema_integrado():
    """Demonstra múltiplos casos de uso do Observer"""
    print("\n" + "=" * 60)
    print("SISTEMA INTEGRADO - OBSERVER PATTERN")
    print("=" * 60)
    
    # 1. Sistema de Usuário
    print("\n1. Sistema de Notificações de Usuário:")
    usuario = SistemaUsuario("user123")
    email_obs = EmailNotificacaoObserver("user@email.com")
    push_obs = PushNotificacaoObserver("device123")
    
    usuario.adicionar_observer(email_obs)
    usuario.adicionar_observer(push_obs)
    
    usuario.criar_pedido("PED001")
    usuario.marcar_entregue("PED001")
    
    # 2. Monitoramento de Dados
    print("\n2. Monitoramento de Mudanças:")
    modelo = ModeloDados()
    auditoria = AuditoriaObserver()
    cache = CacheObserver()
    
    modelo.adicionar_observer(auditoria)
    modelo.adicionar_observer(cache)
    
    modelo.set_valor("nome", "João")
    modelo.set_valor("idade", 30)
    modelo.set_valor("nome", "João Silva")  # Mudança
    
    # 3. Sistema de Pedidos
    print("\n3. Sistema de Pedidos (E-commerce):")
    pedido = Pedido("PED002")
    
    estoque_obs = EstoqueObserver()
    financeiro_obs = FinanceiroObserver()
    logistica_obs = LogisticaObserver()
    
    pedido.adicionar_observer(estoque_obs)
    pedido.adicionar_observer(financeiro_obs)
    pedido.adicionar_observer(logistica_obs)
    
    pedido.adicionar_produto("produto1", 2, 100.00)
    pedido.adicionar_produto("produto2", 1, 50.00)
    pedido.finalizar()
    pedido.marcar_enviado()
    
    # 4. Editor de Texto
    print("\n4. Editor de Texto com Múltiplas Visualizações:")
    editor = EditorTexto()
    
    texto_obs = VisualizacaoTexto()
    stats_obs = VisualizacaoEstatisticas()
    preview_obs = VisualizacaoPreview()
    
    editor.adicionar_visualizacao(texto_obs)
    editor.adicionar_visualizacao(stats_obs)
    editor.adicionar_visualizacao(preview_obs)
    
    editor.escrever("Este é um exemplo de texto sendo editado no editor")
    editor.escrever("Agora atualizado com mais conteúdo para demonstrar o Observer")


if __name__ == "__main__":
    print("=" * 60)
    print("CASOS PRÁTICOS - OBSERVER PATTERN")
    print("=" * 60)
    
    # Exemplos individuais já executados acima
    # Exemplo completo integrado
    exemplo_sistema_integrado()

