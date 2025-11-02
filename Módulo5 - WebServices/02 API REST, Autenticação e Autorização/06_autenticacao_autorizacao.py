"""
06 - Autenticação e Autorização
==================================
Diferenças entre autenticação e autorização e conceitos fundamentais
"""

print("=" * 60)
print("AUTENTICAÇÃO E AUTORIZAÇÃO")
print("=" * 60)

# ============================================
# 1. DIFERENÇA ENTRE AUTENTICAÇÃO E AUTORIZAÇÃO
# ============================================

"""
Autenticação (Authentication):
-------------------------------
"Quem você é?"
- Processo de verificar a identidade do usuário
- Confirma que o usuário é quem diz ser
- Exemplos: login, senha, token

Autorização (Authorization):
-----------------------------
"O que você pode fazer?"
- Processo de verificar permissões do usuário
- Determina quais recursos/operações o usuário pode acessar
- Exemplos: permissões, roles, níveis de acesso

Analogy (Analogia):
-------------------
- Autenticação: Verificar seu ID na entrada (quem você é)
- Autorização: Verificar se você tem permissão para acessar determinada área (o que pode fazer)
"""

print("\n" + "=" * 60)
print("AUTENTICAÇÃO vs AUTORIZAÇÃO")
print("=" * 60)

exemplos = {
    "Autenticação": {
        "Pergunta": "Quem você é?",
        "Exemplos": [
            "Login com usuário e senha",
            "Token de autenticação",
            "Biometria",
            "Certificado digital"
        ],
        "Resultado": "Confirma identidade do usuário"
    },
    "Autorização": {
        "Pergunta": "O que você pode fazer?",
        "Exemplos": [
            "Usuário comum pode ler posts, mas não deletar",
            "Admin pode acessar painel administrativo",
            "Editor pode editar artigos, mas não publicar",
            "Apenas proprietário pode deletar seu próprio recurso"
        ],
        "Resultado": "Define permissões e acesso"
    }
}

for conceito, info in exemplos.items():
    print(f"\n{conceito}:")
    print(f"  {info['Pergunta']}")
    print(f"  Exemplos:")
    for exemplo in info['Exemplos']:
        print(f"    - {exemplo}")
    print(f"  Resultado: {info['Resultado']}")


# ============================================
# 2. FLUXO DE AUTENTICAÇÃO E AUTORIZAÇÃO
# ============================================

print("\n" + "=" * 60)
print("FLUXO TÍPICO")
print("=" * 60)

fluxo = """
1. Cliente faz requisição
   ↓
2. Servidor verifica AUTENTICAÇÃO
   - Token válido? ✓ → Continua
   - Token inválido? ✗ → Retorna 401 Unauthorized
   ↓
3. Servidor verifica AUTORIZAÇÃO
   - Usuário tem permissão? ✓ → Processa requisição
   - Sem permissão? ✗ → Retorna 403 Forbidden
   ↓
4. Servidor retorna resposta
"""

print(fluxo)


# ============================================
# 3. MÉTODOS DE AUTENTICAÇÃO
# ============================================

print("\n" + "=" * 60)
print("MÉTODOS DE AUTENTICAÇÃO")
print("=" * 60)

metodos_autenticacao = {
    "Basic Authentication": {
        "descricao": "Usuário e senha em base64 no header",
        "formato": "Authorization: Basic base64(username:password)",
        "vantagens": [
            "Simples de implementar",
            "Padrão HTTP"
        ],
        "desvantagens": [
            "Credenciais em cada requisição",
            "Menos seguro",
            "Adequado apenas para HTTPS"
        ],
        "uso": "APIs simples, desenvolvimento, sistemas internos"
    },
    "Token Authentication": {
        "descricao": "Token gerado após login, enviado em cada requisição",
        "formato": "Authorization: Bearer token123456",
        "vantagens": [
            "Mais seguro que Basic Auth",
            "Token pode expirar",
            "Pode ser revogado"
        ],
        "desvantagens": [
            "Precisa gerenciar tokens",
            "Token pode ser roubado"
        ],
        "uso": "APIs moderadas, aplicações web"
    },
    "JWT (JSON Web Token)": {
        "descricao": "Token auto-contido com informações assinadas",
        "formato": "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
        "vantagens": [
            "Stateless (sem necessidade de armazenar no servidor)",
            "Contém informações do usuário",
            "Escalável",
            "Padrão da indústria"
        ],
        "desvantagens": [
            "Token não pode ser revogado facilmente",
            "Precisa validar assinatura"
        ],
        "uso": "APIs modernas, aplicações distribuídas"
    },
    "OAuth 2.0": {
        "descricao": "Padrão de autorização para acesso a recursos de terceiros",
        "formato": "Fluxo complexo com múltiplas etapas",
        "vantagens": [
            "Padrão da indústria",
            "Suporta refresh tokens",
            "Escopo de permissões",
            "Usado por grandes players (Google, Facebook)"
        ],
        "desvantagens": [
            "Complexo de implementar",
            "Múltiplos fluxos"
        ],
        "uso": "APIs públicas, integrações com terceiros"
    }
}

for metodo, info in metodos_autenticacao.items():
    print(f"\n{metodo}:")
    print(f"  Descrição: {info['descricao']}")
    print(f"  Formato: {info['formato']}")
    print(f"  Vantagens:")
    for vantagem in info['vantagens']:
        print(f"    + {vantagem}")
    print(f"  Desvantagens:")
    for desvantagem in info['desvantagens']:
        print(f"    - {desvantagem}")
    print(f"  Uso: {info['uso']}")


# ============================================
# 4. PERMISSÕES E ROLES
# ============================================

print("\n" + "=" * 60)
print("PERMISSÕES E ROLES")
print("=" * 60)

class Role:
    """Representa um papel/role de usuário"""
    def __init__(self, nome, descricao, permissoes):
        self.nome = nome
        self.descricao = descricao
        self.permissoes = permissoes
    
    def tem_permissao(self, permissao):
        """Verifica se role tem uma permissão"""
        return permissao in self.permissoes


roles_exemplo = {
    "admin": Role("admin", "Administrador completo", [
        "users:read", "users:write", "users:delete",
        "posts:read", "posts:write", "posts:delete",
        "system:admin"
    ]),
    "editor": Role("editor", "Editor de conteúdo", [
        "posts:read", "posts:write",
        "comments:read", "comments:write"
    ]),
    "user": Role("user", "Usuário comum", [
        "posts:read",
        "comments:read", "comments:write"
    ]),
    "guest": Role("guest", "Visitante", [
        "posts:read"
    ])
}

print("\nExemplos de Roles e Permissões:")
for nome, role in roles_exemplo.items():
    print(f"\n  {role.nome.upper()} ({role.descricao}):")
    for permissao in role.permissoes:
        print(f"    - {permissao}")


# ============================================
# 5. IMPORTÂNCIA DA SEGURANÇA
# ============================================

print("\n" + "=" * 60)
print("IMPORTÂNCIA DA SEGURANÇA")
print("=" * 60)

boas_praticas = {
    "1. Sempre use HTTPS em produção": {
        "porque": "Protege dados em trânsito",
        "o_que": "Criptografa comunicação"
    },
    "2. Nunca exponha credenciais": {
        "porque": "Credenciais são sensíveis",
        "o_que": "Use variáveis de ambiente, não hardcode"
    },
    "3. Valide e sanitize entrada": {
        "porque": "Previne ataques (SQL injection, XSS)",
        "o_que": "Sempre valide dados do cliente"
    },
    "4. Use tokens com expiração": {
        "porque": "Limita janela de ataque se token for roubado",
        "o_que": "Tokens devem expirar após tempo determinado"
    },
    "5. Implemente rate limiting": {
        "porque": "Previne abuso e ataques DDoS",
        "o_que": "Limite requisições por IP/usuário"
    },
    "6. Hash de senhas": {
        "porque": "Senhas nunca devem ser armazenadas em texto plano",
        "o_que": "Use bcrypt, argon2 ou similar"
    },
    "7. Logs cuidadosos": {
        "porque": "Não exponha informações sensíveis",
        "o_que": "Nunca logue senhas ou tokens"
    },
    "8. CORS adequado": {
        "porque": "Previne acesso não autorizado de outros domínios",
        "o_que": "Configure CORS apropriadamente"
    }
}

print("\nBoas Práticas de Segurança:")
for numero, pratica in boas_praticas.items():
    print(f"\n{numero}")
    print(f"  Por quê: {pratica['porque']}")
    print(f"  O que fazer: {pratica['o_que']}")


# ============================================
# 6. CENÁRIOS DE USO
# ============================================

print("\n" + "=" * 60)
print("CENÁRIOS DE USO")
print("=" * 60)

cenarios = [
    {
        "situacao": "Usuário tenta acessar sem token",
        "autenticacao": "✗ Falha",
        "autorizacao": "Não chega aqui",
        "resposta": "401 Unauthorized"
    },
    {
        "situacao": "Usuário comum tenta deletar post de outro",
        "autenticacao": "✓ Passa (tem token válido)",
        "autorizacao": "✗ Falha (sem permissão)",
        "resposta": "403 Forbidden"
    },
    {
        "situacao": "Admin acessa painel administrativo",
        "autenticacao": "✓ Passa",
        "autorizacao": "✓ Passa (tem role admin)",
        "resposta": "200 OK"
    },
    {
        "situacao": "Usuário cria seu próprio post",
        "autenticacao": "✓ Passa",
        "autorizacao": "✓ Passa (pode criar próprios posts)",
        "resposta": "201 Created"
    }
]

print("\nCenários:")
for i, cenario in enumerate(cenarios, 1):
    print(f"\n{i}. {cenario['situacao']}:")
    print(f"   Autenticação: {cenario['autenticacao']}")
    print(f"   Autorização: {cenario['autorizacao']}")
    print(f"   Resposta: {cenario['resposta']}")


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - AUTENTICAÇÃO E AUTORIZAÇÃO")
print("=" * 60)
print("""
Conceitos fundamentais:

1. Autenticação:
   - Verifica identidade (quem você é)
   - Login, senha, token
   - Sem autenticação → 401 Unauthorized

2. Autorização:
   - Verifica permissões (o que pode fazer)
   - Roles, permissões, scopes
   - Sem autorização → 403 Forbidden

3. Métodos comuns:
   - Basic Auth: Simples, menos seguro
   - Token Auth: Mais seguro, tokens gerenciados
   - JWT: Stateless, escalável, padrão moderno
   - OAuth 2.0: Padrão para integrações

4. Segurança:
   - Sempre HTTPS em produção
   - Valide entrada
   - Tokens com expiração
   - Rate limiting
   - Hash de senhas

Próximos arquivos:
- 07_basic_auth.py - Implementação Basic Auth
- 08_token_auth.py - Implementação Token Auth
- 09_jwt_auth.py - Implementação JWT
""")

