"""
02 - Protocolos e Formatos de Dados
=====================================
Exploração detalhada dos protocolos HTTP/HTTPS e formatos XML/JSON
"""

import json
import urllib.request
import urllib.error
import ssl
from typing import Dict, Any

print("=" * 60)
print("PROTOCOLOS HTTP E HTTPS - DETALHES")
print("=" * 60)


# ============================================
# 1. PROTOCOLO HTTP - DETALHAMENTO
# ============================================

"""
Estrutura de uma Requisição HTTP:
-----------------------------------
GET /api/users HTTP/1.1
Host: example.com
Accept: application/json
User-Agent: Python-urllib/3.9

Estrutura de uma Resposta HTTP:
--------------------------------
HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 150

{"status": "success", "data": [...]}
"""

def demonstrar_estrutura_http():
    """Demonstra a estrutura de requisições e respostas HTTP"""
    
    print("\nEstrutura de uma Requisição HTTP:")
    print("-" * 40)
    requisicao_exemplo = """GET /api/users/123 HTTP/1.1
Host: api.example.com
Accept: application/json
User-Agent: Python-Client/1.0
Authorization: Bearer token123"""
    print(requisicao_exemplo)
    
    print("\nEstrutura de uma Resposta HTTP:")
    print("-" * 40)
    resposta_exemplo = """HTTP/1.1 200 OK
Content-Type: application/json
Content-Length: 89
Date: Mon, 01 Jan 2024 12:00:00 GMT

{
  "id": 123,
  "nome": "João Silva",
  "email": "joao@example.com"
}"""
    print(resposta_exemplo)


# ============================================
# 2. MÉTODOS HTTP EM AÇÃO
# ============================================

"""
Métodos HTTP e seus significados:
----------------------------------
GET    - Recuperar dados (idempotente, seguro)
POST   - Criar novo recurso (não idempotente)
PUT    - Atualizar recurso completo (idempotente)
PATCH  - Atualização parcial (não idempotente)
DELETE - Remover recurso (idempotente)
HEAD   - Obter apenas headers (sem corpo)
OPTIONS - Descobrir métodos permitidos
"""

class HTTPMethodDemo:
    """Demonstra diferentes métodos HTTP"""
    
    def __init__(self):
        self.recursos = {}
        self.contador_id = 1
    
    def simular_get(self, recurso_id: int) -> Dict[str, Any]:
        """Simula GET - Recuperar recurso"""
        if recurso_id in self.recursos:
            return {
                "method": "GET",
                "status": 200,
                "data": self.recursos[recurso_id]
            }
        else:
            return {
                "method": "GET",
                "status": 404,
                "error": "Recurso não encontrado"
            }
    
    def simular_post(self, dados: Dict[str, Any]) -> Dict[str, Any]:
        """Simula POST - Criar novo recurso"""
        novo_id = self.contador_id
        self.contador_id += 1
        self.recursos[novo_id] = dados
        return {
            "method": "POST",
            "status": 201,
            "data": {"id": novo_id, **dados},
            "message": "Recurso criado com sucesso"
        }
    
    def simular_put(self, recurso_id: int, dados: Dict[str, Any]) -> Dict[str, Any]:
        """Simula PUT - Atualizar recurso completo"""
        if recurso_id in self.recursos:
            self.recursos[recurso_id] = dados
            return {
                "method": "PUT",
                "status": 200,
                "data": {"id": recurso_id, **dados},
                "message": "Recurso atualizado completamente"
            }
        else:
            return {
                "method": "PUT",
                "status": 404,
                "error": "Recurso não encontrado"
            }
    
    def simular_patch(self, recurso_id: int, dados_parciais: Dict[str, Any]) -> Dict[str, Any]:
        """Simula PATCH - Atualização parcial"""
        if recurso_id in self.recursos:
            self.recursos[recurso_id].update(dados_parciais)
            return {
                "method": "PATCH",
                "status": 200,
                "data": {"id": recurso_id, **self.recursos[recurso_id]},
                "message": "Recurso atualizado parcialmente"
            }
        else:
            return {
                "method": "PATCH",
                "status": 404,
                "error": "Recurso não encontrado"
            }
    
    def simular_delete(self, recurso_id: int) -> Dict[str, Any]:
        """Simula DELETE - Remover recurso"""
        if recurso_id in self.recursos:
            del self.recursos[recurso_id]
            return {
                "method": "DELETE",
                "status": 204,
                "message": "Recurso deletado com sucesso"
            }
        else:
            return {
                "method": "DELETE",
                "status": 404,
                "error": "Recurso não encontrado"
            }


# Demonstração prática
print("\n" + "=" * 60)
print("DEMONSTRAÇÃO DE MÉTODOS HTTP")
print("=" * 60)

demo = HTTPMethodDemo()

# POST - Criar recurso
print("\n1. POST - Criar usuário:")
resultado_post = demo.simular_post({
    "nome": "Maria Santos",
    "email": "maria@example.com",
    "idade": 25
})
print(json.dumps(resultado_post, indent=2, ensure_ascii=False))

# GET - Recuperar recurso
print("\n2. GET - Buscar usuário ID 1:")
resultado_get = demo.simular_get(1)
print(json.dumps(resultado_get, indent=2, ensure_ascii=False))

# PUT - Atualizar completamente
print("\n3. PUT - Atualizar usuário completamente:")
resultado_put = demo.simular_put(1, {
    "nome": "Maria Santos Silva",
    "email": "maria.silva@example.com",
    "idade": 26,
    "cidade": "São Paulo"
})
print(json.dumps(resultado_put, indent=2, ensure_ascii=False))

# PATCH - Atualizar parcialmente
print("\n4. PATCH - Atualizar apenas idade:")
resultado_patch = demo.simular_patch(1, {"idade": 27})
print(json.dumps(resultado_patch, indent=2, ensure_ascii=False))

# DELETE - Remover recurso
print("\n5. DELETE - Remover usuário:")
resultado_delete = demo.simular_delete(1)
print(json.dumps(resultado_delete, indent=2, ensure_ascii=False))


# ============================================
# 3. FORMATO JSON - DETALHAMENTO
# ============================================

print("\n" + "=" * 60)
print("FORMATO JSON - OPERAÇÕES")
print("=" * 60)

def demonstrar_json():
    """Demonstra operações com JSON"""
    
    # Dados complexos em Python
    dados_complexos = {
        "usuario": {
            "id": 1,
            "nome": "João Silva",
            "emails": ["joao@example.com", "joao.silva@example.com"],
            "ativo": True,
            "metadata": {
                "criado_em": "2024-01-01",
                "ultimo_acesso": "2024-01-15"
            }
        },
        "preferencias": {
            "tema": "escuro",
            "idioma": "pt-BR",
            "notificacoes": True
        }
    }
    
    print("\n1. Serialização (Python → JSON):")
    json_string = json.dumps(dados_complexos, indent=2, ensure_ascii=False)
    print(json_string)
    
    print("\n2. Desserialização (JSON → Python):")
    dados_reconstruidos = json.loads(json_string)
    print(f"Tipo: {type(dados_reconstruidos)}")
    print(f"Nome do usuário: {dados_reconstruidos['usuario']['nome']}")
    
    print("\n3. Validação de JSON:")
    json_valido = '{"nome": "Teste", "idade": 30}'
    json_invalido = '{"nome": "Teste", "idade": 30'  # Falta fechamento
    
    try:
        dados1 = json.loads(json_valido)
        print(f"  JSON válido: {dados1}")
    except json.JSONDecodeError as e:
        print(f"  Erro: {e}")
    
    try:
        dados2 = json.loads(json_invalido)
        print(f"  JSON válido: {dados2}")
    except json.JSONDecodeError as e:
        print(f"  JSON inválido detectado: {e}")

demonstrar_json()


# ============================================
# 4. FORMATO XML - DETALHAMENTO
# ============================================

print("\n" + "=" * 60)
print("FORMATO XML - OPERAÇÕES")
print("=" * 60)

import xml.etree.ElementTree as ET
from xml.dom import minidom

def demonstrar_xml():
    """Demonstra operações com XML"""
    
    print("\n1. Criar XML:")
    # Criar estrutura XML
    root = ET.Element("usuarios")
    
    usuario1 = ET.SubElement(root, "usuario")
    ET.SubElement(usuario1, "id").text = "1"
    ET.SubElement(usuario1, "nome").text = "João Silva"
    ET.SubElement(usuario1, "email").text = "joao@example.com"
    ET.SubElement(usuario1, "idade").text = "30"
    
    usuario2 = ET.SubElement(root, "usuario")
    ET.SubElement(usuario2, "id").text = "2"
    ET.SubElement(usuario2, "nome").text = "Maria Santos"
    ET.SubElement(usuario2, "email").text = "maria@example.com"
    ET.SubElement(usuario2, "idade").text = "25"
    
    # Converter para string formatada
    xml_str = ET.tostring(root, encoding='unicode')
    # Formatar com minidom para melhor visualização
    dom = minidom.parseString(ET.tostring(root))
    xml_formatado = dom.toprettyxml(indent="  ")
    print(xml_formatado)
    
    print("\n2. Ler/Parse XML:")
    xml_exemplo = """<?xml version="1.0" ?>
<produtos>
    <produto id="1">
        <nome>Notebook</nome>
        <preco>2500.00</preco>
        <categoria>Eletrônicos</categoria>
    </produto>
    <produto id="2">
        <nome>Mouse</nome>
        <preco>50.00</preco>
        <categoria>Acessórios</categoria>
    </produto>
</produtos>"""
    
    root = ET.fromstring(xml_exemplo)
    print("Produtos encontrados:")
    for produto in root.findall('produto'):
        print(f"  ID: {produto.get('id')}")
        print(f"  Nome: {produto.find('nome').text}")
        print(f"  Preço: {produto.find('preco').text}")
        print(f"  Categoria: {produto.find('categoria').text}")
        print()

demonstrar_xml()


# ============================================
# 5. COMPARAÇÃO JSON vs XML
# ============================================

print("\n" + "=" * 60)
print("COMPARAÇÃO JSON vs XML")
print("=" * 60)

def comparar_formatos():
    """Compara JSON e XML para os mesmos dados"""
    
    dados = {
        "usuarios": [
            {"id": 1, "nome": "João", "email": "joao@example.com"},
            {"id": 2, "nome": "Maria", "email": "maria@example.com"}
        ]
    }
    
    # JSON
    json_data = json.dumps(dados, indent=2, ensure_ascii=False)
    json_size = len(json_data)
    
    # XML equivalente
    root = ET.Element("usuarios")
    for user in dados["usuarios"]:
        usuario = ET.SubElement(root, "usuario")
        ET.SubElement(usuario, "id").text = str(user["id"])
        ET.SubElement(usuario, "nome").text = user["nome"]
        ET.SubElement(usuario, "email").text = user["email"]
    
    xml_data = ET.tostring(root, encoding='unicode')
    xml_size = len(xml_data)
    
    print("\nJSON:")
    print(json_data)
    print(f"Tamanho: {json_size} caracteres")
    
    print("\nXML:")
    print(xml_data)
    print(f"Tamanho: {xml_size} caracteres")
    
    print(f"\nComparação:")
    print(f"  JSON é {xml_size - json_size} caracteres menor")
    print(f"  JSON é {((xml_size - json_size) / xml_size * 100):.1f}% mais compacto")
    print(f"  Legibilidade: JSON é mais fácil de ler")
    print(f"  Uso moderno: JSON é padrão para APIs REST")

comparar_formatos()


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO")
print("=" * 60)
print("""
Conceitos aprendidos:
1. HTTP/HTTPS são protocolos de comunicação web
2. Métodos HTTP: GET, POST, PUT, PATCH, DELETE
3. JSON é mais compacto e legível que XML
4. JSON é o padrão atual para APIs REST
5. XML ainda é usado em SOAP e alguns sistemas legados

Quando usar cada formato:
- JSON: APIs REST, comunicação web moderna, mobile apps
- XML: SOAP, sistemas legados, documentos estruturados complexos
""")

