# Nível 4 - Formulários e CRUD Completo

Este nível adiciona formulários Django e funcionalidades completas de CRUD (Create, Read, Update, Delete) através da interface web.

## 📁 Estrutura Adicional

```
Nivel4_Formularios_CRUD/
├── pessoas/
│   ├── forms.py              # Formulários Django
│   ├── views.py              # Views com CRUD completo
│   └── ...
└── templates/
    └── pessoas/
        ├── form.html         # Formulário de criação/edição
        └── confirmar_exclusao.html  # Confirmação de exclusão
```

## 🚀 Como Executar

Siga os mesmos passos do Nível 3, mas agora você terá acesso a:

- **Criar pessoa**: `/criar/`
- **Editar pessoa**: `/<id>/editar/`
- **Excluir pessoa**: `/<id>/excluir/`

## 🎯 Funcionalidades Adicionadas

### 1. Formulários Django
- Validação automática de campos
- Widgets customizados
- Mensagens de erro/sucesso

### 2. CRUD Completo
- **Create**: Criar novas pessoas
- **Read**: Listar e visualizar pessoas
- **Update**: Editar pessoas existentes
- **Delete**: Excluir pessoas

### 3. Melhorias na Interface
- Formulários estilizados
- Confirmação antes de excluir
- Mensagens de feedback
- Validação em tempo real

## 📝 Arquivos a Criar

### pessoas/forms.py
```python
from django import forms
from .models import Pessoa

class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 4}),
        }
```

### pessoas/views.py (atualizar)
Adicionar views:
- `criar_pessoa(request)`
- `editar_pessoa(request, pessoa_id)`
- `excluir_pessoa(request, pessoa_id)`

### pessoas/urls.py (atualizar)
Adicionar rotas:
- `criar/` → criar_pessoa
- `<id>/editar/` → editar_pessoa
- `<id>/excluir/` → excluir_pessoa

### templates/pessoas/form.html
Template para formulário de criação/edição

### templates/pessoas/confirmar_exclusao.html
Template para confirmação de exclusão

## ➡️ Próximo Nível

No **Nível 5**, vamos personalizar ainda mais o admin do Django com funcionalidades avançadas.
