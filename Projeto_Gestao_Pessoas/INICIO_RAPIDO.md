# 🚀 Início Rápido - Projeto Gestão de Pessoas

Guia rápido para começar a usar o projeto Django de Gestão de Pessoas.

## ⚡ Passo a Passo Rápido

### 1. Escolha um Nível

Recomendamos começar pelo **Nível 1** se você é iniciante.

```bash
cd Nivel1_Estrutura_Base
```

### 2. Configure o Ambiente Virtual

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar (Linux/Mac)
source venv/bin/activate

# Ativar (Windows)
venv\Scripts\activate
```

### 3. Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados

```bash
# Criar migrations
python manage.py makemigrations

# Aplicar migrations
python manage.py migrate
```

### 5. Crie um Superusuário (Opcional)

```bash
python manage.py createsuperuser
```

Siga as instruções para criar um usuário admin.

### 6. Execute o Servidor

```bash
python manage.py runserver
```

### 7. Acesse a Aplicação

- **Home/Lista**: http://127.0.0.1:8000/
- **Admin**: http://127.0.0.1:8000/admin/

## 📝 Para Outros Níveis

O processo é o mesmo, apenas mude o diretório:

```bash
cd Nivel2_Modelos      # ou Nivel3_Views_Templates, etc.
```

## 🎯 Níveis Disponíveis

| Nível | Nome | Status | Descrição |
|-------|------|--------|-----------|
| 1 | Estrutura Base | ✅ Completo | Projeto Django básico |
| 2 | Modelos | ✅ Completo | Modelo Pessoa completo |
| 3 | Views e Templates | ✅ Completo | Interface web |
| 4 | Formulários CRUD | 📝 Documentado | CRUD completo |
| 5 | Admin Personalizado | 📝 Documentado | Admin avançado |
| 6 | API REST | 📝 Documentado | API com DRF |
| 7 | Autenticação | 📝 Documentado | Login e permissões |
| 8 | Testes e Deploy | 📝 Documentado | Testes e produção |

## ❓ Problemas Comuns

### Django não encontrado
```bash
# Certifique-se de que o ambiente virtual está ativado
# E que o Django está instalado
pip install django
```

### Erro de migrations
```bash
# Delete o banco de dados e recrie
rm db.sqlite3
python manage.py migrate
```

### Porta já em uso
```bash
# Use outra porta
python manage.py runserver 8080
```

## 📚 Próximos Passos

1. Leia o **README.md** do nível escolhido
2. Consulte **COMANDOS.md** para comandos úteis
3. Veja **GUIA_IMPLEMENTACAO.md** para implementar níveis avançados

## 🎓 Dica

Comece pelo **Nível 1** e vá progredindo gradualmente. Cada nível adiciona novas funcionalidades e conceitos importantes do Django.
