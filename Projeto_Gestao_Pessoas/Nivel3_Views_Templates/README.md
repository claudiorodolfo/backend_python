# Nível 3 - Views e Templates

Este nível adiciona views e templates para exibir pessoas através de uma interface web amigável.

## 📁 Estrutura

```
Nivel3_Views_Templates/
├── manage.py
├── gestao_pessoas/
│   ├── settings.py          # Configurações (com templates configurados)
│   ├── urls.py               # URLs principais (inclui app pessoas)
│   └── ...
├── pessoas/
│   ├── models.py             # Modelo Pessoa (do Nível 2)
│   ├── views.py              # Views para listar e detalhar pessoas
│   ├── urls.py               # URLs do app pessoas
│   └── ...
└── templates/                 # Templates HTML
    ├── base.html             # Template base
    └── pessoas/
        ├── lista.html        # Lista de pessoas
        └── detalhe.html     # Detalhes de uma pessoa
```

## 🚀 Como Executar

### 1. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate      # Windows
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Criar e aplicar migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 5. Executar servidor

```bash
python manage.py runserver
```

### 6. Acessar a aplicação

- **Lista de Pessoas**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 🎯 Funcionalidades

### Views

1. **lista_pessoas**: Lista todas as pessoas cadastradas
   - Suporta busca por nome ou CPF
   - Filtra apenas pessoas ativas
   - Ordena por nome

2. **detalhe_pessoa**: Exibe detalhes completos de uma pessoa
   - Mostra todas as informações cadastradas
   - Exibe idade calculada
   - Mostra status (ativo/inativo)

### Templates

1. **base.html**: Template base com:
   - Header com navegação
   - Estilos CSS modernos
   - Sistema de mensagens
   - Footer

2. **lista.html**: Página de listagem com:
   - Tabela de pessoas
   - Campo de busca
   - Link para detalhes de cada pessoa
   - Contador de pessoas cadastradas

3. **detalhe.html**: Página de detalhes com:
   - Informações básicas
   - Dados pessoais
   - Endereço (se cadastrado)
   - Informações do sistema
   - Observações (se houver)
   - Link para edição no admin

## 📊 URLs Disponíveis

- `/` - Lista de pessoas
- `/<id>/` - Detalhes de uma pessoa específica
- `/admin/` - Interface administrativa

## 🎨 Características do Design

- Interface limpa e moderna
- Cores profissionais (azul, cinza)
- Responsivo (funciona em diferentes tamanhos de tela)
- Navegação intuitiva
- Mensagens de feedback visual

## ➡️ Próximo Nível

No **Nível 4**, vamos adicionar formulários e funcionalidades completas de CRUD (Create, Read, Update, Delete) através da interface web.
