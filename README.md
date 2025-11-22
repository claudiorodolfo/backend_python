# Backend com Python - Curso Completo

Repositório educacional completo para aprendizado de desenvolvimento backend com Python. Este curso abrange desde os fundamentos de programação até frameworks avançados como Django, passando por bancos de dados, padrões de design, WebServices e muito mais.

## 📚 Sobre o Curso

Este curso foi desenvolvido para fornecer uma base sólida e completa em desenvolvimento backend com Python. O conteúdo está organizado em módulos progressivos, cada um construindo sobre os conhecimentos anteriores, garantindo um aprendizado estruturado e eficiente.

### Objetivo do Curso

Ao final deste curso, você será capaz de:
- Desenvolver aplicações backend completas e profissionais em Python
- Trabalhar com diferentes bancos de dados relacionais (SQLite, MySQL, PostgreSQL)
- Criar APIs RESTful robustas e seguras
- Aplicar padrões de design e princípios SOLID
- Desenvolver aplicações web completas com Django
- Gerenciar projetos com Git e GitHub
- Aplicar soft skills essenciais no desenvolvimento de software

## 🎯 Estrutura do Curso

O curso está dividido em 8 módulos principais:

### [Módulo 1 - Lógica de Programação](./Módulo1%20-%20Lógica%20de%20Programação/)
Fundamentos essenciais de programação em Python.

**Conteúdo:**
- Variáveis, tipos de dados e entrada de dados
- Operadores e estruturas condicionais
- Estruturas de repetição e listas
- Tuplas, dicionários e funções
- Strings e tratamento de erros e exceções

**Pré-requisitos:** Nenhum (curso começa do zero)

---

### [Módulo 2 - Banco de Dados](./Módulo2%20-%20Banco%20de%20Dados/)
Trabalho com bancos de dados relacionais utilizando Python.

**Conteúdo:**
- Introdução a SQL – Comandos Básicos
- Comandos de Atualização, Remoção, modelagem e normalização
- Joins, Consultas Avançadas e Conexão com BD
- Projetos práticos com SQLite, MySQL e PostgreSQL

**Pré-requisitos:** Módulo 1

---

### [Módulo 3 - Programação Orientada a Objetos](./Módulo3%20-%20Programação%20Orientada%20a%20Objetos/)
Conceitos fundamentais de POO aplicados em Python.

**Conteúdo:**
- Fundamentos de POO (classes, objetos, métodos)
- Encapsulamento, Herança e Polimorfismo
- Composição, Associação e Tratamento de Exceções
- Projeto prático: SQLite + POO

**Pré-requisitos:** Módulo 1 e 2

---

### [Módulo 4 - Padrões de Desenvolvimento de Software](./Módulo4%20-%20Padrões%20de%20Desenvolvimento%20de%20Software/)
Padrões de design e princípios SOLID para código profissional.

**Conteúdo:**
- Padrões Criacionais: Singleton, Factories (Simple Factory, Factory Method, Abstract Method), Builder, Prototype
- Padrões Estruturais: Adapter, Decorator, Facade, Proxy, DAO, Composite, Bridge, Flyweight
- Padrões Comportamentais: Observer, Strategy, State, Memento, Command, Template Method, Visitor, Iterator, Mediator, Chain of Responsability
- Padrões Arquiteturais: MVC, Repository, Service Layer
- Princípios SOLID, Clean Code

**Pré-requisitos:** Módulo 3

---

### [Módulo 5 - WebServices](./Módulo5%20-%20WebServices/)
Desenvolvimento de APIs RESTful com Python.

**Conteúdo:**
- Fundamentos e RESTful Web Services
- API REST, Autenticação e Autorização
- Erros, Logs e WebSockets, Comunicação em Tempo Real
- Frameworks: Flask, FastAPI, Django REST Framework

**Pré-requisitos:** Módulos 2, 3 e 4

---

### [Módulo 6 - Django](./Módulo6%20-%20Django/)
Framework web completo para desenvolvimento backend profissional.

**Conteúdo:**
- Introdução, Modelos e Migrations
- Views, Templates, URLs e Rotas
- Formulário, Validação de Dados, Autenticação e Autorização
- Testes Automatizados e Deploy

**Pré-requisitos:** Módulos 2, 3, 4 e 5

---

### [Módulo 7 - Soft Skills](./Módulo7%20-%20Soft%20Skills/)
Habilidades interpessoais essenciais para desenvolvedores.

**Conteúdo:**
- Comunicação Efetiva e Trabalho em Equipe
- Gestão de Tempo e Produtividade
- Pensamento Crítico e Resolução de Problemas

**Pré-requisitos:** Nenhum (pode ser estudado em paralelo)

---

### [Módulo 8 - Git](./Módulo8%20-%20Git/)
Controle de versão e colaboração em projetos de software.

**Conteúdo:**
- Introdução ao Git e Controle de Versão
- Fluxo de Trabalho com Branches e GitHub
- Fluxos de Trabalho com Git

**Pré-requisitos:** Nenhum (recomendado desde o início)

## 🚀 Como Começar

### Pré-requisitos do Sistema

1. **Python 3.7 ou superior**
   ```bash
   # Verificar versão instalada
   python3 --version
   
   # Instalar Python (se necessário)
   # macOS: brew install python3
   # Ubuntu/Debian: sudo apt install python3
   # Windows: Baixar de python.org
   ```

2. **Git** (para o Módulo 8 e controle de versão)
   ```bash
   # Verificar instalação
   git --version
   
   # Instalar Git (se necessário)
   # macOS: brew install git
   # Ubuntu/Debian: sudo apt install git
   # Windows: Baixar de git-scm.com
   ```

3. **Editor de Código**
   - Recomendado: [VS Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), ou qualquer editor de sua preferência

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd backend_python
   ```

2. **Crie um ambiente virtual (recomendado):**
   ```bash
   # Criar ambiente virtual
   python3 -m venv venv
   
   # Ativar ambiente virtual
   # macOS/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```

3. **Instale as dependências conforme necessário:**
   Cada módulo pode ter suas próprias dependências. Consulte o `requirements.txt` de cada módulo quando necessário.

## 📖 Como Utilizar Este Repositório

### Ordem Recomendada de Estudo

1. **Módulo 1** → Comece aqui se você é iniciante em programação
2. **Módulo 2** → Aprenda a trabalhar com bancos de dados
3. **Módulo 3** → Entenda Programação Orientada a Objetos
4. **Módulo 4** → Aplique padrões de design profissionais
5. **Módulo 5** → Crie APIs RESTful
6. **Módulo 6** → Desenvolva aplicações completas com Django
7. **Módulo 7** → Desenvolva soft skills (pode ser estudado em paralelo)
8. **Módulo 8** → Aprenda Git (recomendado desde o início)

### Abordagem de Aprendizado

1. **Leia o README de cada módulo** antes de começar
2. **Siga a ordem dos arquivos** dentro de cada módulo
3. **Execute os exemplos** e experimente modificá-los
4. **Complete os exercícios** para fixar o aprendizado
5. **Crie projetos próprios** aplicando os conceitos aprendidos

### Estrutura de Cada Módulo

Cada módulo contém:
- **README.md**: Documentação completa do módulo
- **Arquivos de exemplo**: Código Python com exemplos práticos
- **Exercícios**: Práticas para fixar o aprendizado
- **Slides**: Material de apoio (quando disponível)
- **Projetos**: Projetos práticos completos

## 🔧 Tecnologias e Ferramentas

### Linguagens e Frameworks
- **Python 3.7+**: Linguagem principal
- **Flask**: Framework web minimalista
- **FastAPI**: Framework moderno de alta performance
- **Django**: Framework web completo
- **Django REST Framework**: Framework para APIs REST

### Bancos de Dados
- **SQLite**: Banco embutido para desenvolvimento
- **MySQL**: SGBD popular para aplicações web
- **PostgreSQL**: SGBD avançado e robusto

### Ferramentas de Desenvolvimento
- **Git**: Controle de versão
- **GitHub**: Plataforma de colaboração
- **Postman/Insomnia**: Teste de APIs
- **SQLite Browser**: Interface gráfica para SQLite
- **MySQL Workbench**: Interface para MySQL
- **pgAdmin**: Interface para PostgreSQL

### Bibliotecas Python Principais
- `sqlite3`: Biblioteca padrão para SQLite
- `mysql-connector-python` / `pymysql`: Conectores MySQL
- `psycopg2`: Conector PostgreSQL
- `requests`: Cliente HTTP
- `pydantic`: Validação de dados
- `PyJWT`: Autenticação JWT
- `pytest`: Framework de testes

## 📚 Recursos Adicionais

### Documentação Oficial
- [Python Documentation](https://docs.python.org/3/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

### Cursos e Tutoriais Online
- [Real Python](https://realpython.com/) - Tutoriais Python de alta qualidade
- [Python.org Tutorial](https://docs.python.org/3/tutorial/) - Tutorial oficial
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) - Tutorial oficial Django
- [REST API Tutorial](https://restfulapi.net/) - Guia completo sobre REST

### Comunidades
- [Python Brasil](https://python.org.br/) - Comunidade Python no Brasil
- [Stack Overflow - Python](https://stackoverflow.com/questions/tagged/python)
- [r/Python](https://www.reddit.com/r/Python/) - Subreddit Python
- [Django Forum](https://forum.djangoproject.com/) - Fórum oficial Django

## 🎓 Metodologia de Ensino

Este curso segue uma abordagem prática e progressiva:

1. **Teoria com Prática**: Cada conceito é explicado e imediatamente aplicado em código
2. **Exemplos Progressivos**: Começamos simples e aumentamos a complexidade gradualmente
3. **Projetos Reais**: Projetos práticos que simulam situações reais de desenvolvimento
4. **Boas Práticas**: Aprendizado de melhores práticas desde o início
5. **Exercícios Práticos**: Exercícios para fixar o aprendizado

## 🔐 Boas Práticas

### Segurança
- Nunca commite credenciais ou informações sensíveis
- Use variáveis de ambiente para configurações
- Valide sempre dados de entrada
- Use prepared statements para prevenir SQL injection
- Implemente autenticação adequada em APIs

### Código
- Siga o PEP 8 (guia de estilo Python)
- Escreva código legível e bem documentado
- Use nomes descritivos para variáveis e funções
- Aplique princípios SOLID
- Escreva testes para código crítico

### Versionamento
- Use Git desde o início
- Faça commits frequentes e descritivos
- Use branches para features e correções
- Mantenha o repositório organizado

## 📝 Contribuindo

Este é um repositório educacional. Se você encontrar erros, tiver sugestões ou quiser contribuir:

1. Abra uma issue descrevendo o problema ou sugestão
2. Para correções, crie um pull request
3. Siga as boas práticas de código Python
4. Documente suas mudanças

## ⚠️ Importante

### Sobre os Exercícios
- Complete todos os exercícios para fixar o aprendizado
- Não pule etapas - cada módulo constrói sobre os anteriores
- Experimente modificar os exemplos para entender melhor

### Sobre Prática
- A programação é aprendida fazendo, não apenas lendo
- Crie seus próprios projetos além dos exemplos
- Pratique regularmente para manter o conhecimento

### Sobre Dúvidas
- Consulte a documentação oficial quando tiver dúvidas
- Use comunidades online para buscar ajuda
- Revise módulos anteriores se necessário

## 🏆 Certificação e Conclusão

Ao completar todos os módulos, você terá:
- Conhecimento sólido de Python para backend
- Habilidade para criar APIs RESTful profissionais
- Experiência com frameworks modernos (Django, FastAPI, Flask)
- Conhecimento de bancos de dados relacionais
- Compreensão de padrões de design e arquitetura
- Habilidades de versionamento com Git
- Soft skills essenciais para desenvolvimento

## 📞 Suporte

Para dúvidas, sugestões ou problemas:
- Abra uma issue no repositório
- Consulte a documentação de cada módulo
- Revise os READMEs específicos de cada seção

## 📄 Licença

Este material educacional está disponível para fins de aprendizado. Consulte a licença do repositório para mais detalhes.

## 🌟 Agradecimentos

Este curso foi desenvolvido com o objetivo de fornecer uma base sólida e completa em desenvolvimento backend com Python. Esperamos que este material seja útil em sua jornada de aprendizado!

---

**Boa sorte em sua jornada de aprendizado! 🚀**

*Última atualização: 2024*

