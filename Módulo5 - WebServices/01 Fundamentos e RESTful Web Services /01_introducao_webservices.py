"""
01 - Introdução a WebServices
====================================
Este arquivo introduz os conceitos fundamentais de WebServices,
incluindo definições, tipos e exemplos práticos.
"""

# ============================================
# 1. DEFINIÇÃO E FUNÇÃO DE WEBSERVICES
# ============================================

"""
WebService (Serviço Web):
---------------------------
Um WebService é uma aplicação que fornece funcionalidades através de 
protocolos web padrão (principalmente HTTP/HTTPS), permitindo que 
diferentes sistemas se comuniquem entre si de forma padronizada.

Funções principais:
- Comunicar dados entre sistemas diferentes
- Disponibilizar funcionalidades remotamente
- Integrar sistemas heterogêneos
- Permitir reutilização de código e funcionalidades
- Suportar arquiteturas distribuídas
"""

print("=" * 60)
print("INTRODUÇÃO A WEBSERVICES")
print("=" * 60)

# Exemplo conceitual: Simulando comunicação entre sistemas
class WebService:
    """
    Representação conceitual de um WebService
    """
    def __init__(self, nome, url_base):
        self.nome = nome
        self.url_base = url_base
        self.funcionalidades = []
    
    def adicionar_funcionalidade(self, nome_func, descricao):
        """Adiciona uma funcionalidade ao serviço"""
        self.funcionalidades.append({
            'nome': nome_func,
            'descricao': descricao
        })
    
    def listar_funcionalidades(self):
        """Lista todas as funcionalidades disponíveis"""
        print(f"\nFuncionalidades de {self.nome}:")
        for func in self.funcionalidades:
            print(f"  - {func['nome']}: {func['descricao']}")


# Exemplo prático: Criando um serviço de consulta de CEP
servico_cep = WebService(
    "Consulta CEP",
    "https://viacep.com.br/ws/"
)
servico_cep.adicionar_funcionalidade(
    "buscar_cep",
    "Retorna endereço completo a partir de um CEP"
)
servico_cep.listar_funcionalidades()


# ============================================
# 2. TIPOS DE WEBSERVICES: SOAP vs REST
# ============================================

"""
SOAP (Simple Object Access Protocol):
---------------------------------------
- Protocolo baseado em XML
- Mais rígido e complexo
- Usa WSDL (Web Services Description Language) para descrição
- Suporta transações e segurança avançada
- Overhead maior (mais verboso)
- Melhor para sistemas enterprise complexos

REST (Representational State Transfer):
----------------------------------------
- Arquitetura baseada em recursos
- Mais simples e leve
- Usa JSON (mais comum) ou XML
- Stateless (sem estado)
- Menor overhead
- Melhor para web e mobile apps
"""

print("\n" + "=" * 60)
print("SOAP vs REST - COMPARAÇÃO")
print("=" * 60)

# Exemplo de requisição SOAP (simulado)
soap_request = """
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
        <getUser xmlns="http://example.com/userservice">
            <userId>123</userId>
        </getUser>
    </soap:Body>
</soap:Envelope>
"""

# Exemplo de requisição REST (simulado)
rest_request = {
    "method": "GET",
    "url": "http://example.com/api/users/123",
    "headers": {
        "Accept": "application/json"
    }
}

print("\nSOAP Request (XML):")
print("Tamanho:", len(soap_request), "caracteres")
print(soap_request[:200] + "...")

print("\nREST Request (JSON):")
print("Tamanho:", len(str(rest_request)), "caracteres")
print(rest_request)


# ============================================
# 3. PROTOCOLOS: HTTP E HTTPS
# ============================================

"""
HTTP (HyperText Transfer Protocol):
-------------------------------------
- Protocolo de comunicação na web
- Porta padrão: 80
- Não criptografado
- Mais rápido
- Adequado para dados não sensíveis

HTTPS (HTTP Secure):
--------------------
- HTTP sobre SSL/TLS
- Porta padrão: 443
- Criptografado
- Mais seguro
- Obrigatório para dados sensíveis (senhas, tokens, etc.)
"""

import urllib.request
import urllib.parse

print("\n" + "=" * 60)
print("PROTOCOLOS HTTP E HTTPS")
print("=" * 60)

def verificar_protocolo(url):
    """Verifica qual protocolo uma URL usa"""
    if url.startswith("https://"):
        return "HTTPS (Seguro)"
    elif url.startswith("http://"):
        return "HTTP (Não seguro)"
    else:
        return "Protocolo não identificado"

# Exemplos
urls_exemplo = [
    "http://example.com/api/users",
    "https://api.github.com/users",
    "https://secure.example.com/payment"
]

print("\nVerificação de protocolos:")
for url in urls_exemplo:
    protocolo = verificar_protocolo(url)
    print(f"  {url}")
    print(f"    → {protocolo}")


# ============================================
# 4. FORMATOS DE DADOS: XML E JSON
# ============================================

"""
XML (eXtensible Markup Language):
----------------------------------
- Baseado em tags
- Mais verboso
- Melhor para documentos estruturados
- Usado principalmente em SOAP

JSON (JavaScript Object Notation):
-----------------------------------
- Baseado em objetos
- Mais compacto e legível
- Padrão atual para APIs REST
- Mais fácil de processar
"""

import json
import xml.etree.ElementTree as ET

print("\n" + "=" * 60)
print("FORMATOS DE DADOS: XML vs JSON")
print("=" * 60)

# Dados de exemplo
dados_usuario = {
    "id": 1,
    "nome": "João Silva",
    "email": "joao@example.com",
    "idade": 30
}

# Representação em JSON
json_data = json.dumps(dados_usuario, indent=2, ensure_ascii=False)
print("\nJSON:")
print(json_data)
print(f"Tamanho: {len(json_data)} caracteres")

# Representação em XML (simulada)
xml_data = f"""<usuario>
    <id>{dados_usuario['id']}</id>
    <nome>{dados_usuario['nome']}</nome>
    <email>{dados_usuario['email']}</email>
    <idade>{dados_usuario['idade']}</idade>
</usuario>"""
print("\nXML:")
print(xml_data)
print(f"Tamanho: {len(xml_data)} caracteres")

print("\nDiferença de tamanho:")
print(f"  JSON: {len(json_data)} caracteres")
print(f"  XML:  {len(xml_data)} caracteres")
print(f"  Diferença: {len(xml_data) - len(json_data)} caracteres a mais no XML")


# ============================================
# 5. EXEMPLOS PRÁTICOS DE USO EM APLICAÇÕES REAIS
# ============================================

"""
Casos de uso comuns de WebServices:
------------------------------------
1. APIs de Redes Sociais (Twitter, Facebook, Instagram)
2. APIs de Pagamento (Stripe, PayPal)
3. APIs de Mapas (Google Maps, Mapbox)
4. APIs de Clima (OpenWeatherMap)
5. APIs de E-commerce (lojas virtuais)
6. Microserviços em arquiteturas modernas
"""

print("\n" + "=" * 60)
print("EXEMPLOS DE WEBSERVICES REAIS")
print("=" * 60)

exemplos_reais = {
    "Redes Sociais": {
        "Twitter API": "https://api.twitter.com/2",
        "Uso": "Postar tweets, buscar trends, análise de dados"
    },
    "Pagamentos": {
        "Stripe API": "https://api.stripe.com/v1",
        "Uso": "Processar pagamentos, gerenciar assinaturas"
    },
    "Mapas": {
        "Google Maps API": "https://maps.googleapis.com/maps/api",
        "Uso": "Geocodificação, rotas, lugares"
    },
    "Clima": {
        "OpenWeatherMap": "https://api.openweathermap.org/data/2.5",
        "Uso": "Previsão do tempo, dados meteorológicos"
    },
    "E-commerce": {
        "Shopify API": "https://{shop}.myshopify.com/admin/api",
        "Uso": "Gerenciar produtos, pedidos, clientes"
    }
}

for categoria, info in exemplos_reais.items():
    print(f"\n{categoria}:")
    for nome, valor in info.items():
        print(f"  {nome}: {valor}")


# ============================================
# RESUMO E PRÓXIMOS PASSOS
# ============================================

print("\n" + "=" * 60)
print("RESUMO")
print("=" * 60)
print("""
Conceitos aprendidos:
1. WebServices permitem comunicação entre sistemas via web
2. SOAP é mais complexo, REST é mais simples e popular
3. HTTPS é essencial para dados sensíveis
4. JSON é o formato padrão para APIs REST modernas
5. WebServices são usados em inúmeras aplicações reais

Próximos tópicos:
- Conceitos REST detalhados
- Métodos HTTP (GET, POST, PUT, DELETE)
- Status codes HTTP
- Estrutura de URLs RESTful
""")

