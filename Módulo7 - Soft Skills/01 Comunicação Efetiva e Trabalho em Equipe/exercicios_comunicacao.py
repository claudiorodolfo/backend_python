"""
Exercícios Práticos: Comunicação Efetiva e Trabalho em Equipe

Estes exercícios ajudam a desenvolver habilidades de comunicação
e trabalho em equipe através de simulações e reflexões.
"""

# ============================================================================
# EXERCÍCIO 1: Analisador de Mensagens
# ============================================================================

class AnalisadorComunicacao:
    """
    Classe para analisar qualidade de mensagens de comunicação.
    Avalia clareza, concisão, completude e tom profissional.
    """
    
    def __init__(self):
        self.criterios = {
            'clareza': 'A mensagem é clara e fácil de entender?',
            'concisao': 'A mensagem vai direto ao ponto?',
            'completude': 'Toda informação necessária está presente?',
            'tom': 'O tom é profissional e apropriado?',
            'jargao': 'Evita jargão técnico desnecessário?',
            'acao': 'Há uma chamada para ação clara?'
        }
    
    def analisar(self, mensagem: str, contexto: str = "geral") -> dict:
        """
        Analisa uma mensagem segundo critérios de comunicação efetiva.
        
        Args:
            mensagem: Texto da mensagem a analisar
            contexto: Contexto da mensagem (email, slack, code_review, etc.)
        
        Returns:
            Dicionário com análise de cada critério
        """
        resultado = {}
        
        # Análise básica
        palavras = mensagem.split()
        resultado['comprimento'] = len(palavras)
        resultado['comprimento_adequado'] = self._avaliar_comprimento(
            len(palavras), contexto
        )
        
        # Verificar critérios
        resultado['clareza'] = self._verificar_clareza(mensagem)
        resultado['concisao'] = self._verificar_concisao(mensagem)
        resultado['completude'] = self._verificar_completude(mensagem)
        resultado['tom'] = self._verificar_tom(mensagem)
        resultado['jargao'] = self._verificar_jargao(mensagem)
        resultado['acao'] = self._verificar_acao(mensagem)
        
        # Score geral
        scores = [
            resultado['clareza'],
            resultado['concisao'],
            resultado['completude'],
            resultado['tom'],
            resultado['jargao'],
            resultado['acao']
        ]
        resultado['score_geral'] = sum(scores) / len(scores)
        
        return resultado
    
    def _avaliar_comprimento(self, num_palavras: int, contexto: str) -> bool:
        """Avalia se o comprimento é adequado para o contexto."""
        limites = {
            'slack': (10, 100),
            'email': (20, 300),
            'code_review': (10, 200),
            'geral': (15, 250)
        }
        min_palavras, max_palavras = limites.get(contexto, limites['geral'])
        return min_palavras <= num_palavras <= max_palavras
    
    def _verificar_clareza(self, mensagem: str) -> float:
        """Verifica clareza da mensagem (0.0 a 1.0)."""
        # Palavras que indicam clareza
        indicadores_positivos = ['porque', 'exemplo', 'especificamente', 'detalhes']
        indicadores_negativos = ['talvez', 'possivelmente', 'tipo', 'sei lá']
        
        score = 0.5  # Base
        
        for palavra in indicadores_positivos:
            if palavra in mensagem.lower():
                score += 0.1
        
        for palavra in indicadores_negativos:
            if palavra in mensagem.lower():
                score -= 0.1
        
        return max(0.0, min(1.0, score))
    
    def _verificar_concisao(self, mensagem: str) -> float:
        """Verifica se mensagem é concisa (0.0 a 1.0)."""
        palavras = mensagem.split()
        
        # Mensagens muito longas sem estrutura perdem pontos
        if len(palavras) > 200:
            return 0.3
        
        # Verificar repetições
        palavras_unicas = len(set(palavras))
        razao_unico = palavras_unicas / len(palavras) if palavras else 0
        
        return min(1.0, razao_unico * 1.2)
    
    def _verificar_completude(self, mensagem: str) -> float:
        """Verifica se mensagem contém informação completa (0.0 a 1.0)."""
        elementos_importantes = ['quem', 'o que', 'quando', 'onde', 'por que']
        
        # Verificar se há detalhes específicos
        tem_numeros = any(char.isdigit() for char in mensagem)
        tem_datas = any(
            palavra in mensagem.lower() 
            for palavra in ['hoje', 'amanhã', 'deadline', 'prazo']
        )
        tem_detalhes = len(mensagem.split()) > 15
        
        score = 0.0
        if tem_numeros:
            score += 0.2
        if tem_datas:
            score += 0.2
        if tem_detalhes:
            score += 0.3
        
        # Verificar perguntas (indica busca por completude)
        if '?' in mensagem:
            score += 0.3
        
        return min(1.0, score)
    
    def _verificar_tom(self, mensagem: str) -> float:
        """Verifica tom profissional (0.0 a 1.0)."""
        score = 0.7  # Base
        
        # Palavras profissionais
        palavras_profissionais = [
            'obrigado', 'por favor', 'agradeço', 'favorável',
            'colaboração', 'sugestão', 'oportunidade'
        ]
        
        # Palavras não profissionais
        palavras_improprias = [
            'putz', 'caramba', 'cara', 'mano', 'beleza',
            'foda-se', 'chato', 'idiota'
        ]
        
        mensagem_lower = mensagem.lower()
        
        for palavra in palavras_profissionais:
            if palavra in mensagem_lower:
                score += 0.05
        
        for palavra in palavras_improprias:
            if palavra in mensagem_lower:
                score -= 0.3
        
        # Verificar excesso de exclamações
        if mensagem.count('!') > 2:
            score -= 0.1
        
        return max(0.0, min(1.0, score))
    
    def _verificar_jargao(self, mensagem: str) -> float:
        """Verifica uso apropriado de jargão (0.0 a 1.0)."""
        # Lista de jargão técnico comum
        jargoes_comuns = [
            'async', 'sync', 'callback', 'closure', 'singleton',
            'factory', 'decorator', 'middleware', 'endpoint', 'payload'
        ]
        
        jargoes_encontrados = [
            j for j in jargoes_comuns 
            if j.lower() in mensagem.lower()
        ]
        
        # Algum jargão é OK, muito jargão sem explicação é ruim
        if len(jargoes_encontrados) == 0:
            return 1.0  # Sem jargão
        elif len(jargoes_encontrados) <= 2:
            return 0.8  # Jargão moderado
        else:
            return 0.4  # Muito jargão
    
    def _verificar_acao(self, mensagem: str) -> float:
        """Verifica se há chamada para ação clara (0.0 a 1.0)."""
        verbos_acao = [
            'fazer', 'criar', 'enviar', 'revisar', 'completar',
            'atualizar', 'corrigir', 'implementar', 'deployar'
        ]
        
        perguntas = mensagem.count('?')
        imperativos = any(verbo in mensagem.lower() for verbo in verbos_acao)
        
        score = 0.0
        if perguntas > 0:
            score += 0.3
        if imperativos:
            score += 0.4
        if 'deadline' in mensagem.lower() or 'prazo' in mensagem.lower():
            score += 0.3
        
        return min(1.0, score)
    
    def gerar_sugestoes(self, analise: dict) -> list:
        """Gera sugestões de melhoria baseado na análise."""
        sugestoes = []
        
        if analise['clareza'] < 0.6:
            sugestoes.append(
                "Melhore a clareza: use exemplos concretos e evite ambiguidade"
            )
        
        if analise['concisao'] < 0.6:
            sugestoes.append(
                "Seja mais conciso: remova informações desnecessárias"
            )
        
        if analise['completude'] < 0.6:
            sugestoes.append(
                "Adicione mais contexto: inclua detalhes sobre quando, onde, como"
            )
        
        if analise['tom'] < 0.6:
            sugestoes.append(
                "Ajuste o tom: use linguagem mais profissional e respeitosa"
            )
        
        if analise['jargao'] < 0.6:
            sugestoes.append(
                "Reduza jargão técnico ou explique termos técnicos usados"
            )
        
        if analise['acao'] < 0.5:
            sugestoes.append(
                "Adicione chamada para ação clara: o que precisa ser feito?"
            )
        
        return sugestoes


# ============================================================================
# EXERCÍCIO 2: Gerador de Feedback Construtivo (Modelo SBI)
# ============================================================================

class GeradorFeedbackSBI:
    """
    Classe para criar feedback construtivo usando o modelo SBI:
    Situation (Situação), Behavior (Comportamento), Impact (Impacto)
    """
    
    def criar_feedback(
        self, 
        situacao: str, 
        comportamento: str, 
        impacto_positivo: str = None,
        impacto_negativo: str = None,
        sugestao: str = None
    ) -> str:
        """
        Cria feedback usando modelo SBI.
        
        Args:
            situacao: Contexto onde o comportamento ocorreu
            comportamento: Comportamento observável
            impacto_positivo: Impacto positivo (para feedback positivo)
            impacto_negativo: Impacto negativo (para feedback corretivo)
            sugestao: Sugestão de melhoria (opcional)
        
        Returns:
            Feedback formatado
        """
        feedback = f"Situação: {situacao}\n"
        feedback += f"Comportamento: {comportamento}\n"
        
        if impacto_positivo:
            feedback += f"Impacto Positivo: {impacto_positivo}\n"
        
        if impacto_negativo:
            feedback += f"Impacto Negativo: {impacto_negativo}\n"
        
        if sugestao:
            feedback += f"Sugestão: {sugestao}"
        
        return feedback
    
    def feedback_code_review(
        self,
        pr_numero: int,
        arquivo: str,
        linha: int,
        comentario: str,
        tipo: str = "corretivo"  # "positivo" ou "corretivo"
    ) -> str:
        """
        Cria feedback específico para code review.
        
        Args:
            pr_numero: Número do Pull Request
            arquivo: Nome do arquivo
            linha: Número da linha (opcional)
            comentario: Comentário técnico
            tipo: Tipo de feedback ("positivo" ou "corretivo")
        """
        situacao = f"No PR #{pr_numero}, arquivo {arquivo}"
        if linha:
            situacao += f", linha {linha}"
        
        comportamento = comentario
        
        if tipo == "positivo":
            impacto = (
                "Isso torna o código mais legível e fácil de manter. "
                "Boa prática!"
            )
        else:
            impacto = (
                "Isso pode causar problemas de manutenção no futuro. "
                "Vamos melhorar?"
            )
        
        return self.criar_feedback(situacao, comportamento, 
                                  impacto_positivo=impacto if tipo == "positivo" else None,
                                  impacto_negativo=impacto if tipo == "corretivo" else None)


# ============================================================================
# EXERCÍCIO 3: Simulador de Resolução de Conflitos
# ============================================================================

class ResolvedorConflitos:
    """
    Classe para guiar processo de resolução de conflitos.
    """
    
    def __init__(self):
        self.estrategias = {
            'colaboracao': 'Buscar solução win-win que satisfaça todos',
            'compromisso': 'Ambas partes cedem algo para chegar a solução',
            'acomodacao': 'Uma parte cede para satisfazer a outra',
            'competicao': 'Uma parte ganha, outra perde',
            'evitacao': 'Ignorar ou adiar o conflito'
        }
    
    def analisar_conflito(
        self,
        tipo: str,
        importancia: str,  # "alta", "media", "baixa"
        urgencia: str,  # "alta", "media", "baixa"
        relacionamento: str  # "importante", "neutro", "baixo"
    ) -> dict:
        """
        Analisa conflito e sugere estratégia apropriada.
        
        Returns:
            Dicionário com análise e recomendação
        """
        recomendacao = self._recomendar_estrategia(
            importancia, urgencia, relacionamento
        )
        
        return {
            'tipo': tipo,
            'importancia': importancia,
            'urgencia': urgencia,
            'relacionamento': relacionamento,
            'estrategia_recomendada': recomendacao,
            'descricao': self.estrategias[recomendacao],
            'passos': self._gerar_passos(recomendacao)
        }
    
    def _recomendar_estrategia(
        self, 
        importancia: str, 
        urgencia: str, 
        relacionamento: str
    ) -> str:
        """Recomenda estratégia baseado em características do conflito."""
        # Alta importância + relacionamento importante = colaboração
        if importancia == "alta" and relacionamento == "importante":
            return "colaboracao"
        
        # Alta urgência + baixa importância = compromisso
        if urgencia == "alta" and importancia == "baixa":
            return "compromisso"
        
        # Alta importância + baixo relacionamento = competição (se necessário)
        if importancia == "alta" and relacionamento == "baixo":
            return "colaboracao"  # Sempre tentar colaboração primeiro
        
        # Baixa importância = acomodação ou evitamento
        if importancia == "baixa":
            if relacionamento == "importante":
                return "acomodacao"
            else:
                return "compromisso"
        
        # Default: colaboração
        return "colaboracao"
    
    def _gerar_passos(self, estrategia: str) -> list:
        """Gera passos para implementar estratégia."""
        passos_base = [
            "1. Identifique o conflito claramente",
            "2. Entenda todas as perspectivas envolvidas",
            "3. Identifique interesses subjacentes (não só posições)"
        ]
        
        passos_estrategia = {
            'colaboracao': [
                "4. Brainstorm soluções que atendam todos os interesses",
                "5. Avalie opções juntos",
                "6. Escolha solução que maximize valor para todos",
                "7. Implemente e acompanhe"
            ],
            'compromisso': [
                "4. Identifique o que cada parte pode ceder",
                "5. Negocie termos aceitáveis para ambos",
                "6. Documente acordo",
                "7. Implemente compromisso"
            ],
            'acomodacao': [
                "4. Identifique se você pode ceder sem prejudicar objetivos principais",
                "5. Comunique sua decisão de ceder",
                "6. Busque reciprocidade futura se apropriado"
            ],
            'competicao': [
                "4. Use apenas se for crítico e urgente",
                "5. Explique razões objetivas",
                "6. Minimize danos ao relacionamento",
                "7. Busque reparação depois se necessário"
            ],
            'evitacao': [
                "4. Considere se conflito vai se resolver sozinho",
                "5. Avalie custo de não resolver agora",
                "6. Planeje abordar depois se necessário"
            ]
        }
        
        return passos_base + passos_estrategia.get(estrategia, [])


# ============================================================================
# EXERCÍCIO 4: Praticador de Escuta Ativa
# ============================================================================

class PraticadorEscutaAtiva:
    """
    Ferramenta para praticar técnicas de escuta ativa.
    """
    
    def parafrasear(self, mensagem: str, contexto: str = "") -> str:
        """
        Prática de parafraseamento - reescreve mensagem para confirmar entendimento.
        
        Args:
            mensagem: Mensagem original
            contexto: Contexto adicional para melhorar parafraseamento
        
        Returns:
            Paráfrase da mensagem
        """
        # Esta é uma simulação - na prática, você faria isso mentalmente
        prefixos = [
            "Então você está dizendo que...",
            "Deixe-me confirmar se entendi: você mencionou que...",
            "Pelo que entendi, você quer dizer que...",
            "Você está sugerindo que..."
        ]
        
        import random
        prefixo = random.choice(prefixos)
        
        # Simplificação básica (em prática, você faria isso mentalmente)
        parafrase = mensagem[:len(mensagem)//2] + "... (resumo)"
        
        return f"{prefixo} {parafrase}"
    
    def gerar_perguntas_clarificadoras(self, mensagem: str) -> list:
        """
        Gera perguntas para clarificar entendimento.
        
        Returns:
            Lista de perguntas clarificadoras
        """
        perguntas = [
            "Você pode dar um exemplo concreto disso?",
            "O que você quer dizer especificamente com...?",
            "Como isso se relaciona com...?",
            "Quais são os critérios para...?",
            "Qual é o impacto esperado de...?",
            "Você está se referindo a... ou a...?",
            "Quando você menciona..., você quer dizer...?"
        ]
        
        # Retorna algumas perguntas genéricas úteis
        # Em prática, você faria perguntas específicas baseadas no conteúdo
        return perguntas[:3]
    
    def resumir_pontos_chave(self, pontos: list) -> str:
        """
        Resume pontos-chave de uma conversa.
        
        Args:
            pontos: Lista de pontos principais
        
        Returns:
            Resumo formatado
        """
        resumo = "Para confirmar meu entendimento, os pontos principais são:\n\n"
        
        for i, ponto in enumerate(pontos, 1):
            resumo += f"{i}. {ponto}\n"
        
        resumo += "\nEstá correto? Há algo que eu tenha perdido?"
        
        return resumo


# ============================================================================
# EXERCÍCIOS PRÁTICOS - USO DAS CLASSES
# ============================================================================

def exercicio_1_analisar_mensagem():
    """Exercício 1: Analisar qualidade de mensagem."""
    print("=" * 60)
    print("EXERCÍCIO 1: Análise de Comunicação")
    print("=" * 60)
    
    analisador = AnalisadorComunicacao()
    
    # Exemplo de mensagem
    mensagem = """
    Oi, tipo, aquele código que você fez tá funcionando, mas tipo,
    não sei, acho que poderia ser melhor, sabe? Talvez usar outra
    coisa, não sei exatamente o quê, mas tipo, tem que mudar algo.
    """
    
    print("\nMensagem Original:")
    print(mensagem)
    print("\n" + "-" * 60)
    
    analise = analisador.analisar(mensagem, contexto="slack")
    
    print("\nResultado da Análise:")
    print(f"Score Geral: {analise['score_geral']:.2f}/1.0")
    print(f"\nDetalhes:")
    for criterio, valor in analise.items():
        if criterio != 'score_geral' and isinstance(valor, (int, float)):
            print(f"  {criterio}: {valor:.2f}")
    
    print("\nSugestões de Melhoria:")
    sugestoes = analisador.gerar_sugestoes(analise)
    for i, sugestao in enumerate(sugestoes, 1):
        print(f"  {i}. {sugestao}")


def exercicio_2_feedback_construtivo():
    """Exercício 2: Criar feedback usando modelo SBI."""
    print("\n" + "=" * 60)
    print("EXERCÍCIO 2: Feedback Construtivo (SBI)")
    print("=" * 60)
    
    gerador = GeradorFeedbackSBI()
    
    # Exemplo 1: Feedback positivo
    print("\n--- Exemplo 1: Feedback Positivo ---")
    feedback_positivo = gerador.feedback_code_review(
        pr_numero=42,
        arquivo="validators.py",
        linha=15,
        comentario="Ótimo uso do padrão Strategy para validação!",
        tipo="positivo"
    )
    print(feedback_positivo)
    
    # Exemplo 2: Feedback corretivo
    print("\n--- Exemplo 2: Feedback Corretivo ---")
    feedback_corretivo = gerador.feedback_code_review(
        pr_numero=42,
        arquivo="api.py",
        linha=89,
        comentario="Esta função está muito longa (150+ linhas) e faz muitas coisas",
        tipo="corretivo"
    )
    sugestao = "Sugestão: Quebrar em funções menores, cada uma com responsabilidade única"
    feedback_corretivo += f"\n{sugestao}"
    print(feedback_corretivo)
    
    # Exemplo 3: Feedback geral
    print("\n--- Exemplo 3: Feedback Geral ---")
    feedback_geral = gerador.criar_feedback(
        situacao="Durante a reunião de planejamento do sprint",
        comportamento="Você questionou a estimativa da story e sugeriu dividir em tasks menores",
        impacto_positivo="Isso ajudou a equipe a ter visibilidade melhor do esforço necessário",
        sugestao="Continue fazendo essas perguntas - elas melhoram nosso planejamento"
    )
    print(feedback_geral)


def exercicio_3_resolucao_conflitos():
    """Exercício 3: Resolução de conflitos."""
    print("\n" + "=" * 60)
    print("EXERCÍCIO 3: Resolução de Conflitos")
    print("=" * 60)
    
    resolvedor = ResolvedorConflitos()
    
    # Cenário: Conflito sobre escolha de biblioteca
    print("\n--- Cenário: Escolha de Biblioteca ---")
    print("Você prefere Pydantic, colega prefere Marshmallow")
    print("Ambos têm experiência com suas escolhas")
    print("Decisão é importante para arquitetura do projeto")
    
    analise = resolvedor.analisar_conflito(
        tipo="Conflito Técnico - Escolha de Biblioteca",
        importancia="alta",
        urgencia="media",
        relacionamento="importante"
    )
    
    print(f"\nAnálise do Conflito:")
    print(f"  Tipo: {analise['tipo']}")
    print(f"  Estratégia Recomendada: {analise['estrategia_recomendada']}")
    print(f"  Descrição: {analise['descricao']}")
    
    print(f"\nPassos Recomendados:")
    for passo in analise['passos']:
        print(f"  {passo}")


def exercicio_4_escuta_ativa():
    """Exercício 4: Praticar escuta ativa."""
    print("\n" + "=" * 60)
    print("EXERCÍCIO 4: Escuta Ativa")
    print("=" * 60)
    
    praticador = PraticadorEscutaAtiva()
    
    # Exemplo de mensagem recebida
    mensagem = """
    Acho que precisamos repensar a arquitetura da API. 
    Está ficando muito acoplada e difícil de testar. 
    Talvez devêssemos considerar usar injeção de dependência 
    e separar melhor as camadas.
    """
    
    print("\nMensagem Recebida:")
    print(mensagem)
    
    print("\n--- Técnica 1: Parafrasear ---")
    parafrase = praticador.parafrasear(mensagem)
    print(parafrase)
    
    print("\n--- Técnica 2: Perguntas Clarificadoras ---")
    perguntas = praticador.gerar_perguntas_clarificadoras(mensagem)
    for i, pergunta in enumerate(perguntas, 1):
        print(f"{i}. {pergunta}")
    
    print("\n--- Técnica 3: Resumir Pontos-Chave ---")
    pontos = [
        "Arquitetura atual está com problemas de acoplamento",
        "Dificulta testes",
        "Sugestão: usar injeção de dependência",
        "Sugestão: melhorar separação de camadas"
    ]
    resumo = praticador.resumir_pontos_chave(pontos)
    print(resumo)


# ============================================================================
# MAIN - Executar todos os exercícios
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("EXERCÍCIOS: COMUNICAÇÃO EFETIVA E TRABALHO EM EQUIPE")
    print("=" * 60)
    
    exercicio_1_analisar_mensagem()
    exercicio_2_feedback_construtivo()
    exercicio_3_resolucao_conflitos()
    exercicio_4_escuta_ativa()
    
    print("\n" + "=" * 60)
    print("CONCLUSÃO")
    print("=" * 60)
    print("\nEstes exercícios são simulações. A prática real acontece:")
    print("  - Em conversas reais com colegas")
    print("  - Em code reviews reais")
    print("  - Em reuniões e discussões técnicas")
    print("  - Em escrita de emails e documentação")
    print("\nUse estas ferramentas como guia, mas pratique no dia a dia!")
    print("=" * 60)

