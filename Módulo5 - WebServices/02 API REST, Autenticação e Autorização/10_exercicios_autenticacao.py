"""
10 - Exercícios Práticos de Autenticação
==========================================
Exercícios para praticar implementação de autenticação
"""

print("=" * 60)
print("EXERCÍCIOS DE AUTENTICAÇÃO")
print("=" * 60)

# ============================================
# EXERCÍCIO 1: IMPLEMENTAR BASIC AUTH
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIO 1: BASIC AUTH COMPLETO")
print("=" * 60)

print("""
Tarefa: Criar uma API com Basic Auth que:

1. Tenha rota pública /api/public
2. Tenha rotas protegidas:
   - GET /api/protected - Requer autenticação
   - GET /api/admin - Requer autenticação E role 'admin'

3. Banco de usuários:
   - admin / senha123 (role: admin)
   - user / senha456 (role: user)

4. Testar:
   - Acessar rota pública sem auth ✓
   - Acessar protegida sem auth ✗ (401)
   - Acessar protegida com credenciais inválidas ✗ (401)
   - Acessar protegida com credenciais válidas ✓
   - Acessar admin com user ✗ (403)
   - Acessar admin com admin ✓

Implementação sugerida:
- Função para decodificar Basic Auth
- Decorador @requer_autenticacao
- Decorador @requer_role(role)
- Rotas implementadas
""")


# ============================================
# EXERCÍCIO 2: IMPLEMENTAR TOKEN AUTH
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIO 2: TOKEN AUTH COMPLETO")
print("=" * 60)

print("""
Tarefa: Criar uma API com Token Auth que:

1. Endpoints:
   - POST /api/login - Recebe username/password, retorna token
   - POST /api/logout - Revoga token
   - GET /api/protected - Requer token válido
   - GET /api/tokens - Lista tokens do usuário (requer token)

2. Funcionalidades:
   - Tokens expiram após 1 hora
   - Tokens podem ser revogados no logout
   - Tokens armazenados com timestamp de criação

3. Testar:
   - Login com credenciais válidas → Recebe token ✓
   - Login com credenciais inválidas → Erro ✗
   - Acessar protegida sem token → 401 ✗
   - Acessar protegida com token válido → Sucesso ✓
   - Acessar protegida com token expirado → 401 ✗
   - Logout → Token revogado ✓

Implementação sugerida:
- Função gerar_token()
- Função verificar_token()
- Função revogar_token()
- Decorador @requer_token
""")


# ============================================
# EXERCÍCIO 3: IMPLEMENTAR JWT
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIO 3: JWT COMPLETO")
print("=" * 60)

print("""
Tarefa: Criar uma API com JWT que:

1. Endpoints:
   - POST /api/login - Retorna JWT
   - GET /api/protected - Requer JWT válido
   - GET /api/token/info - Decodifica e retorna payload do token
   - POST /api/token/refresh - Gera novo token (opcional)

2. Payload do JWT deve conter:
   - user_id
   - username
   - role
   - iat (issued at)
   - exp (expiration)

3. Testar:
   - Login → Recebe JWT ✓
   - Decodificar JWT → Ver payload ✓
   - Acessar com JWT válido → Sucesso ✓
   - Acessar com JWT expirado → 401 ✗

Implementação sugerida:
- Função gerar_jwt(payload)
- Função verificar_jwt(token)
- Decorador @requer_jwt
""")


# ============================================
# EXERCÍCIO 4: SISTEMA DE PERMISSÕES
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIO 4: SISTEMA DE PERMISSÕES")
print("=" * 60)

print("""
Tarefa: Criar sistema de permissões baseado em roles

1. Roles e permissões:
   - admin: todas as permissões
   - editor: pode criar/editar posts, comentar
   - user: pode ler posts, comentar
   - guest: pode apenas ler posts públicos

2. Endpoints:
   - GET /api/posts - Todos podem ler
   - POST /api/posts - Apenas editor/admin
   - PUT /api/posts/{id} - Apenas editor/admin
   - DELETE /api/posts/{id} - Apenas admin
   - POST /api/comments - Apenas user/editor/admin

3. Implementar:
   - Decorador @requer_permissao(permissao)
   - Verificação de role vs permissão necessária

Testar:
- Guest tenta criar post → 403 ✗
- User tenta criar post → 403 ✗
- Editor cria post → Sucesso ✓
- Admin deleta post → Sucesso ✓
""")


# ============================================
# EXERCÍCIO 5: API COMPLETA COM AUTH
# ============================================

print("\n" + "=" * 60)
print("EXERCÍCIO 5: API COMPLETA")
print("=" * 60)

print("""
Tarefa: Criar API completa de blog com autenticação

1. Modelo de dados:
   - Users (id, username, email, password_hash, role)
   - Posts (id, title, content, author_id, created_at)
   - Comments (id, post_id, user_id, content, created_at)

2. Endpoints públicos:
   - GET /api/posts - Lista posts públicos
   - GET /api/posts/{id} - Detalhe do post

3. Endpoints protegidos (requer JWT):
   - POST /api/login - Login
   - GET /api/profile - Perfil do usuário autenticado
   - POST /api/posts - Criar post (editor/admin)
   - PUT /api/posts/{id} - Editar post (author/editor/admin)
   - DELETE /api/posts/{id} - Deletar post (author/admin)
   - POST /api/posts/{id}/comments - Comentar (user/editor/admin)
   - DELETE /api/comments/{id} - Deletar comentário (author/admin)

4. Regras de negócio:
   - Usuário só pode editar/deletar seus próprios posts/comentários
   - Editor pode editar qualquer post
   - Admin pode tudo

Implementar:
- JWT authentication
- Sistema de permissões
- Validação de ownership
- CRUD completo
""")


# ============================================
# DESAFIO: REFRESH TOKEN
# ============================================

print("\n" + "=" * 60)
print("DESAFIO: REFRESH TOKEN")
print("=" * 60)

print("""
Implementar sistema de Refresh Token:

1. Dois tipos de tokens:
   - Access Token: JWT de curta duração (15 minutos)
   - Refresh Token: Token de longa duração (7 dias)

2. Fluxo:
   - Login retorna access_token e refresh_token
   - Cliente usa access_token para requisições
   - Quando access_token expira, usar refresh_token para obter novo
   - Refresh token armazenado no servidor (pode ser revogado)

3. Endpoints:
   - POST /api/login → {access_token, refresh_token}
   - POST /api/refresh → Recebe refresh_token, retorna novo access_token
   - POST /api/logout → Revoga ambos os tokens

4. Segurança:
   - Refresh token só pode ser usado uma vez
   - Após uso, gerar novo refresh token
   - Refresh token revogado no logout
""")


# ============================================
# CHECKLIST DE IMPLEMENTAÇÃO
# ============================================

print("\n" + "=" * 60)
print("CHECKLIST DE IMPLEMENTAÇÃO")
print("=" * 60)

checklist = """
Para cada exercício, certifique-se de:

✓ Validação de entrada (username, password)
✓ Hash de senhas (nunca em texto plano)
✓ Mensagens de erro claras
✓ Status codes apropriados (401, 403, etc.)
✓ Headers corretos (Authorization: Bearer token)
✓ Expiração de tokens
✓ Tratamento de tokens inválidos/expirados
✓ Logs adequados (sem expor senhas/tokens)
✓ Testes com curl/Postman
✓ Documentação dos endpoints
"""

print(checklist)


# ============================================
# RESUMO
# ============================================

print("\n" + "=" * 60)
print("RESUMO - EXERCÍCIOS DE AUTENTICAÇÃO")
print("=" * 60)
print("""
Exercícios propostos:

1. Basic Auth completo
2. Token Authentication
3. JWT Authentication
4. Sistema de permissões
5. API completa com auth
6. Desafio: Refresh Token

Objetivos:
- Praticar implementação de diferentes métodos de auth
- Entender fluxo de autenticação/autorização
- Implementar sistema de permissões
- Criar API completa e segura

Boas práticas:
- Sempre hash de senhas
- Tokens com expiração
- Validação de entrada
- Mensagens de erro claras
- Status codes apropriados
- Testes completos
""")

