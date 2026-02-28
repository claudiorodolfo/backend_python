# Projeto Django - Gestão de Pessoas

Este projeto é um sistema completo de gestão de pessoas desenvolvido com Django, organizado por níveis de complexidade crescente. Ideal para aprendizado progressivo do framework Django.

## 📁 Estrutura do Projeto

O projeto está organizado em 8 níveis de complexidade, cada um adicionando novas funcionalidades:

### ✅ Nível 1: Estrutura Base
- Projeto Django básico
- Configurações iniciais
- Sistema de admin do Django
- **Status**: Completo e funcional

### ✅ Nível 2: Modelos de Dados
- App `pessoas` criado
- Modelo `Pessoa` completo com validações
- Configuração do admin
- Migrations do banco de dados
- **Status**: Completo e funcional

### ✅ Nível 3: Views e Templates
- Views para listar e detalhar pessoas
- Templates HTML com design moderno
- Sistema de busca
- Interface web amigável
- **Status**: Completo e funcional

### 📝 Nível 4: Formulários e CRUD
- Formulários Django
- CRUD completo (Create, Read, Update, Delete)
- Validação de formulários
- Mensagens de feedback
- **Status**: Documentado (ver README do nível)

### 📝 Nível 5: Admin Personalizado
- Actions customizadas
- Filtros avançados
- Interface admin melhorada
- **Status**: Documentado (ver README do nível)

### 📝 Nível 6: API REST
- Django REST Framework
- API REST completa
- Serializers
- Documentação automática
- **Status**: Documentado (ver README do nível)

### 📝 Nível 7: Autenticação
- Sistema de login/logout
- Controle de acesso
- Permissões customizadas
- **Status**: Documentado (ver README do nível)

### 📝 Nível 8: Testes e Deploy
- Testes automatizados
- Preparação para produção
- Configurações de deploy
- **Status**: Documentado (ver README do nível)

## 🚀 Início Rápido

### 1. Escolha um Nível

Comece pelo **Nível 1** se você é iniciante, ou escolha o nível que corresponde ao seu conhecimento atual.

### 2. Configure o Ambiente

```bash
# Navegue até o nível escolhido
cd Nivel1_Estrutura_Base  # ou outro nível

# Crie e ative ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate      # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configure o Banco de Dados

```bash
# Crie as migrations
python manage.py makemigrations

# Aplique as migrations
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser
```

### 4. Execute o Servidor

```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

## 📋 Pré-requisitos

- **Python 3.8+**
- **pip** (gerenciador de pacotes Python)
- **virtualenv** (recomendado para isolar dependências)

## 📚 Documentação Adicional

- **[COMANDOS.md](COMANDOS.md)** - Todos os comandos Django úteis
- **[GUIA_IMPLEMENTACAO.md](GUIA_IMPLEMENTACAO.md)** - Guia detalhado de implementação de cada nível
- Cada nível possui seu próprio **README.md** com instruções específicas

## 🎯 Objetivos de Aprendizado

Ao completar este projeto, você terá aprendido:

1. ✅ Estrutura de um projeto Django
2. ✅ Criação de modelos e migrations
3. ✅ Views e templates
4. ✅ Formulários Django
5. ✅ CRUD completo
6. ✅ Admin personalizado
7. ✅ API REST com DRF
8. ✅ Autenticação e permissões
9. ✅ Testes automatizados
10. ✅ Deploy em produção

## 🔧 Tecnologias Utilizadas

- **Django 4.2** - Framework web
- **SQLite** - Banco de dados (desenvolvimento)
- **Django REST Framework** - API REST (Nível 6+)
- **HTML/CSS** - Templates e estilos
- **Python 3.8+** - Linguagem de programação

## 📖 Recursos de Aprendizado

- [Documentação Oficial do Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Tutorial Django](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

## 🤝 Contribuindo

Este é um projeto educacional. Sinta-se livre para:
- Adicionar novos níveis
- Melhorar a documentação
- Corrigir bugs
- Adicionar funcionalidades

## 📝 Licença

Este projeto é para fins educacionais.

## 🎓 Estrutura de Aprendizado

```
Nível 1 → Nível 2 → Nível 3 → Nível 4 → Nível 5 → Nível 6 → Nível 7 → Nível 8
  ↓         ↓         ↓         ↓         ↓         ↓         ↓         ↓
Base    Modelos   Views    Formulários  Admin   API REST  Auth    Testes
```

Cada nível constrói sobre o anterior, permitindo aprendizado progressivo e incremental.
