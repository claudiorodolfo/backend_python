# Nível 8 - Testes e Deploy

Este nível adiciona testes automatizados e preparação para deploy em produção.

## 🧪 Testes

- Testes unitários dos modelos
- Testes de views
- Testes de formulários
- Testes de API (se aplicável)
- Cobertura de código

## 🚀 Deploy

- Configurações de produção
- Variáveis de ambiente
- Arquivos estáticos
- Banco de dados de produção
- Servidor WSGI (Gunicorn)

## 📦 Dependências de Produção

```bash
pip install gunicorn
pip install whitenoise
pip install dj-database-url
pip install python-decouple
```

## 📝 Arquivos de Deploy

- `Procfile` - Para Heroku
- `runtime.txt` - Versão do Python
- `.env.example` - Exemplo de variáveis
- `settings/production.py` - Settings de produção

## ✅ Checklist de Deploy

- [ ] DEBUG = False
- [ ] SECRET_KEY em variável de ambiente
- [ ] ALLOWED_HOSTS configurado
- [ ] Banco de dados de produção
- [ ] Arquivos estáticos coletados
- [ ] Migrations aplicadas
- [ ] Testes passando
- [ ] Logging configurado
