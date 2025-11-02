"""
03 - Criação e Execução de Migrations
======================================

Este arquivo demonstra como trabalhar com migrations no Django.
"""

# ============================================================================
# O QUE SÃO MIGRATIONS?
# ============================================================================

"""
Migrations são arquivos Python que descrevem mudanças nos models do Django.
Eles permitem:
- Versionar mudanças no banco de dados
- Aplicar mudanças em diferentes ambientes
- Reverter mudanças quando necessário
- Trabalhar em equipe de forma sincronizada
"""

# ============================================================================
# COMANDOS DE MIGRATION
# ============================================================================

"""
# 1. Criar migrations (após modificar models)
python manage.py makemigrations
python manage.py makemigrations minha_app  # Para app específico

# 2. Ver o SQL que será executado (sem aplicar)
python manage.py sqlmigrate minha_app 0001

# 3. Aplicar migrations
python manage.py migrate
python manage.py migrate minha_app  # Para app específico
python manage.py migrate minha_app 0001  # Migration específica

# 4. Reverter migrations
python manage.py migrate minha_app 0002  # Voltar para migration anterior
python manage.py migrate minha_app zero  # Reverter todas as migrations

# 5. Ver status das migrations
python manage.py showmigrations
python manage.py showmigrations minha_app

# 6. Marcar migrations como aplicadas (sem executar)
python manage.py migrate --fake minha_app 0001

# 7. Marcar migrations como não aplicadas
python manage.py migrate --fake minha_app zero
"""

# ============================================================================
# EXEMPLO DE ARQUIVO DE MIGRATION GERADO
# ============================================================================

"""
# 0001_initial.py (gerado automaticamente)

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('descricao', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=2)),
                ('quantidade', models.IntegerField(default=0)),
                ('categoria', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='produtos',
                    to='minha_app.categoria'
                )),
            ],
        ),
    ]
"""

# ============================================================================
# MIGRATIONS CUSTOMIZADAS
# ============================================================================

"""
Às vezes você precisa criar migrations customizadas para:
- Migrar dados existentes
- Fazer transformações complexas
- Renomear campos/tabelas

# Criar migration vazia para customizar
python manage.py makemigrations --empty minha_app
"""

# Exemplo de migration customizada:

"""
# 0002_migrate_dados.py

from django.db import migrations


def migrar_dados(apps, schema_editor):
    '''
    Função para migrar dados durante a migration.
    Use apps.get_model() ao invés de import direto.
    '''
    Produto = apps.get_model('minha_app', 'Produto')
    Categoria = apps.get_model('minha_app', 'Categoria')
    
    # Criar categoria padrão
    categoria_default, _ = Categoria.objects.get_or_create(
        nome='Sem Categoria',
        defaults={'descricao': 'Categoria padrão'}
    )
    
    # Atribuir categoria padrão para produtos sem categoria
    Produto.objects.filter(categoria__isnull=True).update(
        categoria=categoria_default
    )


def reverter_migracao(apps, schema_editor):
    '''Função para reverter a migration'''
    # Implementar lógica de reversão se necessário
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('minha_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrar_dados, reverter_migracao),
    ]
"""

# ============================================================================
# BOAS PRÁTICAS COM MIGRATIONS
# ============================================================================

"""
1. NUNCA edite migrations que já foram aplicadas em produção
   - Crie uma nova migration ao invés disso

2. Sempre teste migrations em ambiente de desenvolvimento primeiro

3. Faça backup do banco antes de aplicar migrations em produção

4. Commit migrations no controle de versão junto com o código

5. Use --fake com cuidado (apenas quando realmente necessário)

6. Se precisar resetar completamente:
   - Deletar banco de dados (SQLite)
   - Deletar pasta migrations (exceto __init__.py)
   - Recriar migrations do zero

7. Para renomear um model:
   - Criar novo model com novo nome
   - Criar migration customizada para copiar dados
   - Deletar model antigo

8. Para mudar tipo de campo que pode perder dados:
   - Criar novo campo temporário
   - Migrar dados
   - Deletar campo antigo
   - Renomear novo campo
"""

# ============================================================================
# EXEMPLO PRÁTICO: CENÁRIOS COMUNS
# ============================================================================

"""
# CENÁRIO 1: Adicionar novo campo a model existente

# 1. Adicionar campo no model
class Produto(models.Model):
    # ... campos existentes ...
    codigo_barras = models.CharField(max_length=50, blank=True)  # NOVO

# 2. Criar migration
python manage.py makemigrations

# 3. Aplicar migration
python manage.py migrate


# CENÁRIO 2: Alterar campo existente (ex: max_length)

# 1. Alterar no model
class Produto(models.Model):
    nome = models.CharField(max_length=200)  # Era 100, agora é 200

# 2. Criar e aplicar migration
python manage.py makemigrations
python manage.py migrate


# CENÁRIO 3: Deletar campo

# 1. Remover campo do model
# codigo_barras = models.CharField(...)  # REMOVIDO

# 2. Criar e aplicar migration
python manage.py makemigrations
python manage.py migrate


# CENÁRIO 4: Adicionar relacionamento ForeignKey

# 1. Adicionar ForeignKey no model
class Produto(models.Model):
    # ... campos existentes ...
    fornecedor = models.ForeignKey(
        'Fornecedor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

# 2. Criar Fornecedor model primeiro
class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)

# 3. Criar e aplicar migrations
python manage.py makemigrations
python manage.py migrate
"""

# ============================================================================
# RESOLVENDO CONFLITOS DE MIGRATIONS
# ============================================================================

"""
Se você trabalha em equipe e houver conflitos de migrations:

1. Ver quais migrations estão conflitando:
   python manage.py showmigrations

2. Se duas branches criaram migrations diferentes:
   - Merge das branches pode criar dependências conflitantes
   - Resolva manualmente editando dependencies nas migrations

3. Se migration foi aplicada mas não existe no repositório:
   - Use --fake para marcar como aplicada
   - Ou recrie a migration com mesmo número

4. Se migration não foi aplicada mas já existe:
   - Aplique a migration normalmente
   - Ou remova do repositório se ainda não foi commitada
"""

# ============================================================================
# DETECTAR PROBLEMAS NAS MIGRATIONS
# ============================================================================

"""
# Ver estado das migrations
python manage.py showmigrations

# Output exemplo:
minha_app
 [X] 0001_initial
 [ ] 0002_add_campo_novo
 [X] 0003_alter_produto

# [X] = aplicada
# [ ] = não aplicada

# Ver SQL específico de uma migration
python manage.py sqlmigrate minha_app 0002

# Verificar inconsistências
python manage.py migrate --plan
"""

print("Arquivo de referência: Migrations no Django")
print("Execute 'python manage.py makemigrations' após modificar models")
print("Execute 'python manage.py migrate' para aplicar as migrations")

