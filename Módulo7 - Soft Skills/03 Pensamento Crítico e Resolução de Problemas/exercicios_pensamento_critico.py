"""
Exercícios Práticos: Pensamento Crítico e Resolução de Problemas

Estes exercícios ajudam a desenvolver habilidades de pensamento crítico
e resolução estruturada de problemas através de técnicas e práticas.
"""

from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import json


# ============================================================================
# EXERCÍCIO 1: Análise de Causa Raiz (5 Porquês)
# ============================================================================

class AnalisadorCausaRaiz:
    """
    Ferramenta para análise de causa raiz usando técnica dos 5 Porquês.
    """
    
    def __init__(self):
        self.analises = []
    
    def analisar_problema(self, problema: str) -> Dict:
        """
        Inicia análise de problema usando 5 Porquês.
        
        Args:
            problema: Descrição do problema
        
        Returns:
            Dicionário com estrutura de análise
        """
        analise = {
            'problema': problema,
            'porques': [],
            'causa_raiz': None,
            'solucoes': []
        }
        
        return analise
    
    def adicionar_porque(self, analise: Dict, porque: str, nivel: int) -> Dict:
        """
        Adiciona um "por quê?" à análise.
        
        Args:
            analise: Dicionário de análise
            porque: Resposta ao "por quê?"
            nivel: Nível do porquê (1-5)
        
        Returns:
            Analise atualizada
        """
        analise['porques'].append({
            'nivel': nivel,
            'porque': porque
        })
        
        # Se chegou ao 5º porquê ou resposta indica causa raiz
        if nivel >= 5 or self._eh_causa_raiz(porque):
            analise['causa_raiz'] = porque
            analise['nivel_final'] = nivel
        
        return analise
    
    def _eh_causa_raiz(self, resposta: str) -> bool:
        """
        Tenta identificar se resposta indica causa raiz.
        Causa raiz geralmente é sobre processo, política ou sistema.
        """
        indicadores = [
            'processo', 'política', 'sistema', 'arquitetura',
            'design', 'requisito', 'documentação', 'falta de'
        ]
        
        resposta_lower = resposta.lower()
        return any(ind in resposta_lower for ind in indicadores)
    
    def gerar_solucoes(self, analise: Dict) -> List[str]:
        """
        Gera soluções potenciais baseadas na causa raiz identificada.
        
        Args:
            analise: Dicionário de análise
        
        Returns:
            Lista de soluções potenciais
        """
        causa_raiz = analise['causa_raiz']
        if not causa_raiz:
            return ["Causa raiz não identificada - continue análise"]
        
        solucoes = []
        
        # Soluções genéricas baseadas no tipo de causa
        if 'processo' in causa_raiz.lower():
            solucoes.append("Revisar e melhorar processo atual")
            solucoes.append("Documentar processo corretamente")
            solucoes.append("Treinar equipe no processo")
        
        if 'política' in causa_raiz.lower():
            solucoes.append("Revisar política existente")
            solucoes.append("Criar nova política se necessário")
            solucoes.append("Comunicar política claramente")
        
        if 'sistema' in causa_raiz.lower() or 'arquitetura' in causa_raiz.lower():
            solucoes.append("Refatorar arquitetura/sistema")
            solucoes.append("Adicionar monitoramento/logging")
            solucoes.append("Implementar testes adequados")
        
        if 'falta de' in causa_raiz.lower():
            solucoes.append("Implementar o que está faltando")
            solucoes.append("Documentar necessidade claramente")
            solucoes.append("Priorizar em backlog")
        
        # Solução sempre presente
        solucoes.append(f"Endereçar causa raiz: {causa_raiz}")
        
        analise['solucoes'] = solucoes
        return solucoes
    
    def visualizar_analise(self, analise: Dict) -> str:
        """
        Retorna representação visual da análise.
        
        Args:
            analise: Dicionário de análise
        
        Returns:
            String formatada
        """
        output = "\n" + "=" * 70 + "\n"
        output += "ANÁLISE DE CAUSA RAIZ (5 PORQUÊS)\n"
        output += "=" * 70 + "\n\n"
        
        output += f"Problema: {analise['problema']}\n\n"
        
        output += "Análise:\n"
        output += "-" * 70 + "\n"
        
        for i, pq in enumerate(analise['porques'], 1):
            output += f"{i}. Por quê? → {pq['porque']}\n"
        
        output += "\n" + "-" * 70 + "\n"
        output += f"Causa Raiz Identificada: {analise['causa_raiz']}\n"
        
        if analise['solucoes']:
            output += "\nSoluções Propostas:\n"
            for i, sol in enumerate(analise['solucoes'], 1):
                output += f"  {i}. {sol}\n"
        
        return output


# ============================================================================
# EXERCÍCIO 2: Decomposição de Problemas
# ============================================================================

@dataclass
class Subproblema:
    """Representa um subproblema na decomposição."""
    nome: str
    descricao: str
    subproblemas: List['Subproblema'] = field(default_factory=list)
    dependencias: List[str] = field(default_factory=list)
    prioridade: int = 5  # 1-10, 10 = mais importante


class DecompostorProblemas:
    """
    Ferramenta para decompor problemas complexos em subproblemas.
    """
    
    def __init__(self):
        self.problemas = {}
    
    def criar_problema(self, nome: str, descricao: str) -> Subproblema:
        """
        Cria novo problema raiz.
        
        Args:
            nome: Nome do problema
            descricao: Descrição detalhada
        
        Returns:
            Objeto Subproblema
        """
        problema = Subproblema(nome=nome, descricao=descricao)
        self.problemas[nome] = problema
        return problema
    
    def adicionar_subproblema(
        self,
        problema_pai: Subproblema,
        nome: str,
        descricao: str,
        dependencias: List[str] = None,
        prioridade: int = 5
    ) -> Subproblema:
        """
        Adiciona subproblema a um problema existente.
        
        Args:
            problema_pai: Problema pai
            nome: Nome do subproblema
            descricao: Descrição
            dependencias: Lista de nomes de subproblemas dos quais depende
            prioridade: Prioridade (1-10)
        
        Returns:
            Subproblema criado
        """
        subproblema = Subproblema(
            nome=nome,
            descricao=descricao,
            dependencias=dependencias or [],
            prioridade=prioridade
        )
        
        problema_pai.subproblemas.append(subproblema)
        return subproblema
    
    def visualizar_decomposicao(self, problema: Subproblema, nivel: int = 0) -> str:
        """
        Retorna representação visual da decomposição.
        
        Args:
            problema: Problema raiz
            nivel: Nível atual de indentação
        
        Returns:
            String formatada
        """
        indent = "  " * nivel
        output = f"{indent}├─ {problema.nome}\n"
        output += f"{indent}│  {problema.descricao}\n"
        
        if problema.dependencias:
            output += f"{indent}│  Dependências: {', '.join(problema.dependencias)}\n"
        
        if problema.subproblemas:
            for i, sub in enumerate(problema.subproblemas, 1):
                is_last = i == len(problema.subproblemas)
                prefix = "└─" if is_last else "├─"
                output += f"{indent}{prefix} {sub.nome}\n"
                output += f"{indent}│  {sub.descricao}\n"
                
                if sub.dependencias:
                    output += f"{indent}│  Depends on: {', '.join(sub.dependencias)}\n"
                
                if sub.subproblemas:
                    output += self.visualizar_decomposicao(sub, nivel + 2)
        
        return output
    
    def ordenar_por_dependencias(self, problema: Subproblema) -> List[str]:
        """
        Retorna ordem de execução baseada em dependências.
        
        Args:
            problema: Problema raiz
        
        Returns:
            Lista de nomes de subproblemas em ordem de execução
        """
        # Topological sort simplificado
        ordenados = []
        visitados = set()
        
        def visitar(sub: Subproblema):
            if sub.nome in visitados:
                return
            
            # Visitar dependências primeiro
            for dep_nome in sub.dependencias:
                # Encontrar subproblema da dependência
                for sub_prob in problema.subproblemas:
                    if sub_prob.nome == dep_nome:
                        visitar(sub_prob)
                        break
            
            visitados.add(sub.nome)
            ordenados.append(sub.nome)
        
        for sub in problema.subproblemas:
            visitar(sub)
        
        return ordenados


# ============================================================================
# EXERCÍCIO 3: Brainstorming de Soluções
# ============================================================================

class Brainstorming:
    """
    Ferramenta para brainstorming de soluções.
    """
    
    def __init__(self):
        self.sessoes = []
    
    def iniciar_sessao(self, problema: str) -> Dict:
        """
        Inicia sessão de brainstorming.
        
        Args:
            problema: Problema a ser resolvido
        
        Returns:
            Dicionário da sessão
        """
        sessao = {
            'problema': problema,
            'ideias': [],
            'categorias': {},
            'filtrada': False
        }
        self.sessoes.append(sessao)
        return sessao
    
    def adicionar_ideia(self, sessao: Dict, ideia: str, categoria: str = "geral"):
        """
        Adiciona ideia à sessão (sem julgamento durante brainstorming).
        
        Args:
            sessao: Sessão de brainstorming
            ideia: Ideia proposta
            categoria: Categoria da ideia
        """
        sessao['ideias'].append({
            'ideia': ideia,
            'categoria': categoria
        })
        
        if categoria not in sessao['categorias']:
            sessao['categorias'][categoria] = []
        sessao['categorias'][categoria].append(ideia)
    
    def avaliar_ideias(
        self,
        sessao: Dict,
        criterios: List[str] = None
    ) -> Dict:
        """
        Avalia ideias após brainstorming.
        
        Args:
            sessao: Sessão de brainstorming
            criterios: Lista de critérios de avaliação
        
        Returns:
            Dicionário com avaliação
        """
        if criterios is None:
            criterios = ['viabilidade', 'impacto', 'custo', 'tempo']
        
        avaliacao = {
            'criterios': criterios,
            'ideias_avaliadas': []
        }
        
        for ideia_info in sessao['ideias']:
            ideia = ideia_info['ideia']
            # Simulação: cada ideia recebe score 1-10 em cada critério
            # Na prática, você faria avaliação manual
            scores = {criterio: 5 for criterio in criterios}  # Placeholder
            total = sum(scores.values())
            
            avaliacao['ideias_avaliadas'].append({
                'ideia': ideia,
                'categoria': ideia_info['categoria'],
                'scores': scores,
                'total': total
            })
        
        # Ordenar por score total
        avaliacao['ideias_avaliadas'].sort(key=lambda x: x['total'], reverse=True)
        sessao['filtrada'] = True
        
        return avaliacao
    
    def top_ideias(self, sessao: Dict, n: int = 5) -> List[str]:
        """
        Retorna top N ideias da sessão.
        
        Args:
            sessao: Sessão de brainstorming
            n: Número de ideias
        
        Returns:
            Lista de top ideias
        """
        if not sessao.get('filtrada'):
            return sessao['ideias'][:n]
        
        # Retornar top do último resultado de avaliação
        # Isso requer que avaliar_ideias tenha sido chamado
        return [ideia['ideia'] for ideia in sessao['ideias'][:n]]


# ============================================================================
# EXERCÍCIO 4: Análise de Trade-offs
# ============================================================================

@dataclass
class Opcao:
    """Representa uma opção em análise de trade-offs."""
    nome: str
    descricao: str
    criterios: Dict[str, float] = field(default_factory=dict)  # critério: score


class AnalisadorTradeoffs:
    """
    Ferramenta para análise de trade-offs entre opções.
    """
    
    def __init__(self):
        self.analises = []
    
    def criar_analise(self, decisao: str) -> Dict:
        """
        Cria nova análise de trade-offs.
        
        Args:
            decisao: Descrição da decisão a ser tomada
        
        Returns:
            Dicionário de análise
        """
        analise = {
            'decisao': decisao,
            'criterios': {},  # critério: peso (1-10)
            'opcoes': []
        }
        self.analises.append(analise)
        return analise
    
    def adicionar_criterio(self, analise: Dict, nome: str, peso: float = 5.0):
        """
        Adiciona critério de avaliação.
        
        Args:
            analise: Análise de trade-offs
            nome: Nome do critério
            peso: Peso do critério (1-10)
        """
        analise['criterios'][nome] = peso
    
    def adicionar_opcao(self, analise: Dict, nome: str, descricao: str) -> Opcao:
        """
        Adiciona opção a ser avaliada.
        
        Args:
            analise: Análise de trade-offs
            nome: Nome da opção
            descricao: Descrição da opção
        
        Returns:
            Opção criada
        """
        opcao = Opcao(nome=nome, descricao=descricao)
        analise['opcoes'].append(opcao)
        return opcao
    
    def avaliar_opcao(self, opcao: Opcao, criterio: str, score: float):
        """
        Avalia opção em um critério.
        
        Args:
            opcao: Opção a avaliar
            criterio: Nome do critério
            score: Score (0-10)
        """
        opcao.criterios[criterio] = max(0.0, min(10.0, score))
    
    def calcular_scores_ponderados(self, analise: Dict) -> Dict[str, float]:
        """
        Calcula scores ponderados de cada opção.
        
        Args:
            analise: Análise de trade-offs
        
        Returns:
            Dicionário {nome_opcao: score_ponderado}
        """
        scores = {}
        
        for opcao in analise['opcoes']:
            score_total = 0.0
            peso_total = 0.0
            
            for criterio, peso in analise['criterios'].items():
                score = opcao.criterios.get(criterio, 0.0)
                score_total += score * peso
                peso_total += peso
            
            if peso_total > 0:
                scores[opcao.nome] = score_total / peso_total
            else:
                scores[opcao.nome] = 0.0
        
        return scores
    
    def recomendar(self, analise: Dict) -> Tuple[str, float]:
        """
        Recomenda opção com maior score ponderado.
        
        Args:
            analise: Análise de trade-offs
        
        Returns:
            Tuple (nome_opcao_recomendada, score)
        """
        scores = self.calcular_scores_ponderados(analise)
        
        if not scores:
            return None, 0.0
        
        melhor = max(scores.items(), key=lambda x: x[1])
        return melhor[0], melhor[1]
    
    def visualizar_analise(self, analise: Dict) -> str:
        """
        Retorna representação visual da análise.
        
        Args:
            analise: Análise de trade-offs
        
        Returns:
            String formatada
        """
        output = "\n" + "=" * 70 + "\n"
        output += "ANÁLISE DE TRADE-OFFS\n"
        output += "=" * 70 + "\n\n"
        
        output += f"Decisão: {analise['decisao']}\n\n"
        
        output += "Critérios (pesos):\n"
        for criterio, peso in analise['criterios'].items():
            output += f"  • {criterio}: {peso}\n"
        
        output += "\n" + "-" * 70 + "\n"
        output += "Opções:\n"
        output += "-" * 70 + "\n\n"
        
        scores = self.calcular_scores_ponderados(analise)
        
        for opcao in analise['opcoes']:
            output += f"{opcao.nome}:\n"
            output += f"  Descrição: {opcao.descricao}\n"
            output += "  Scores por critério:\n"
            
            for criterio, peso in analise['criterios'].items():
                score = opcao.criterios.get(criterio, 0.0)
                output += f"    {criterio}: {score:.1f}/10 (peso: {peso})\n"
            
            score_final = scores[opcao.nome]
            output += f"  Score Final (ponderado): {score_final:.2f}/10\n\n"
        
        recomendacao, score = self.recomendar(analise)
        if recomendacao:
            output += "-" * 70 + "\n"
            output += f"✨ Recomendação: {recomendacao} (score: {score:.2f}/10)\n"
        
        return output


# ============================================================================
# EXERCÍCIO 5: Resolução Estruturada de Problemas
# ============================================================================

class ResolvedorEstruturado:
    """
    Ferramenta para guiar resolução estruturada de problemas.
    """
    
    def __init__(self):
        self.problemas = []
    
    def criar_problema(self, descricao: str) -> Dict:
        """
        Cria novo problema para resolver.
        
        Args:
            descricao: Descrição do problema
        
        Returns:
            Dicionário do problema
        """
        problema = {
            'descricao': descricao,
            'entendimento': {},
            'informacoes': [],
            'decomposicao': [],
            'hipoteses': [],
            'testes': [],
            'solucao': None,
            'validacao': None
        }
        self.problemas.append(problema)
        return problema
    
    def documentar_entendimento(
        self,
        problema: Dict,
        comportamento_esperado: str,
        comportamento_atual: str,
        contexto: str = ""
    ):
        """
        Documenta entendimento do problema.
        
        Args:
            problema: Dicionário do problema
            comportamento_esperado: O que deveria acontecer
            comportamento_atual: O que está acontecendo
            contexto: Contexto adicional
        """
        problema['entendimento'] = {
            'esperado': comportamento_esperado,
            'atual': comportamento_atual,
            'contexto': contexto
        }
    
    def adicionar_informacao(self, problema: Dict, info: str, tipo: str = "geral"):
        """
        Adiciona informação coletada.
        
        Args:
            problema: Dicionário do problema
            info: Informação coletada
            tipo: Tipo (log, erro, observação, etc.)
        """
        problema['informacoes'].append({
            'tipo': tipo,
            'info': info
        })
    
    def adicionar_hipotese(self, problema: Dict, hipotese: str, probabilidade: float = 0.5):
        """
        Adiciona hipótese sobre causa.
        
        Args:
            problema: Dicionário do problema
            hipotese: Hipótese sobre causa
            probabilidade: Probabilidade estimada (0.0-1.0)
        """
        problema['hipoteses'].append({
            'hipotese': hipotese,
            'probabilidade': probabilidade,
            'testada': False,
            'resultado': None
        })
        
        # Ordenar por probabilidade
        problema['hipoteses'].sort(key=lambda x: x['probabilidade'], reverse=True)
    
    def testar_hipotese(self, problema: Dict, indice: int, resultado: str, confirmada: bool):
        """
        Registra resultado de teste de hipótese.
        
        Args:
            problema: Dicionário do problema
            indice: Índice da hipótese
            resultado: Descrição do resultado
            confirmada: Se hipótese foi confirmada
        """
        if 0 <= indice < len(problema['hipoteses']):
            hip = problema['hipoteses'][indice]
            hip['testada'] = True
            hip['resultado'] = resultado
            hip['confirmada'] = confirmada
    
    def documentar_solucao(self, problema: Dict, solucao: str, implementacao: str = ""):
        """
        Documenta solução implementada.
        
        Args:
            problema: Dicionário do problema
            solucao: Descrição da solução
            implementacao: Detalhes de implementação
        """
        problema['solucao'] = {
            'descricao': solucao,
            'implementacao': implementacao
        }
    
    def validar_solucao(self, problema: Dict, validada: bool, observacoes: str = ""):
        """
        Valida se solução resolveu problema.
        
        Args:
            problema: Dicionário do problema
            validada: Se solução foi validada
            observacoes: Observações sobre validação
        """
        problema['validacao'] = {
            'validada': validada,
            'observacoes': observacoes
        }
    
    def resumo(self, problema: Dict) -> str:
        """
        Retorna resumo do processo de resolução.
        
        Args:
            problema: Dicionário do problema
        
        Returns:
            String formatada
        """
        output = "\n" + "=" * 70 + "\n"
        output += "RESOLUÇÃO ESTRUTURADA DE PROBLEMA\n"
        output += "=" * 70 + "\n\n"
        
        output += f"Problema: {problema['descricao']}\n\n"
        
        if problema['entendimento']:
            output += "Entendimento:\n"
            output += f"  Esperado: {problema['entendimento']['esperado']}\n"
            output += f"  Atual: {problema['entendimento']['atual']}\n"
            if problema['entendimento']['contexto']:
                output += f"  Contexto: {problema['entendimento']['contexto']}\n"
            output += "\n"
        
        if problema['informacoes']:
            output += f"Informações Coletadas ({len(problema['informacoes'])}):\n"
            for info in problema['informacoes']:
                output += f"  [{info['tipo']}] {info['info']}\n"
            output += "\n"
        
        if problema['hipoteses']:
            output += "Hipóteses:\n"
            for i, hip in enumerate(problema['hipoteses'], 1):
                status = "✓" if hip.get('confirmada') else ("✗" if hip.get('testada') else "?")
                output += f"  {status} {i}. {hip['hipotese']} (prob: {hip['probabilidade']:.0%})\n"
            output += "\n"
        
        if problema['solucao']:
            output += "Solução:\n"
            output += f"  {problema['solucao']['descricao']}\n"
            if problema['solucao']['implementacao']:
                output += f"  Implementação: {problema['solucao']['implementacao']}\n"
            output += "\n"
        
        if problema['validacao']:
            status = "✅ Validada" if problema['validacao']['validada'] else "❌ Não validada"
            output += f"Validação: {status}\n"
            if problema['validacao']['observacoes']:
                output += f"  {problema['validacao']['observacoes']}\n"
        
        return output


# ============================================================================
# EXERCÍCIOS PRÁTICOS - DEMONSTRAÇÃO
# ============================================================================

def demonstracao_causa_raiz():
    """Demonstra análise de causa raiz."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 1: Análise de Causa Raiz (5 Porquês)")
    print("=" * 70)
    
    analisador = AnalisadorCausaRaiz()
    
    problema = "API retorna erro 500 para alguns usuários"
    analise = analisador.analisar_problema(problema)
    
    analisador.adicionar_porque(analise, "Erro de servidor interno", 1)
    analisador.adicionar_porque(analise, "Exceção não tratada na validação", 2)
    analisador.adicionar_porque(analise, "Dados de alguns usuários têm formato diferente", 3)
    analisador.adicionar_porque(analise, "Validação não cobre todos os casos de edge case", 4)
    analisador.adicionar_porque(analise, "Falta de testes que cubram edge cases no processo de desenvolvimento", 5)
    
    analisador.gerar_solucoes(analise)
    print(analisador.visualizar_analise(analise))


def demonstracao_decomposicao():
    """Demonstra decomposição de problemas."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 2: Decomposição de Problemas")
    print("=" * 70)
    
    decompostor = DecompostorProblemas()
    
    problema = decompostor.criar_problema(
        "Sistema de Autenticação",
        "Criar sistema completo de autenticação com múltiplos métodos"
    )
    
    # Subproblemas
    decompostor.adicionar_subproblema(
        problema, "Modelo de Usuário", "Criar modelo de dados para usuários",
        prioridade=10
    )
    
    decompostor.adicionar_subproblema(
        problema, "Registro", "Permitir que usuários se registrem",
        dependencias=["Modelo de Usuário"],
        prioridade=9
    )
    
    decompostor.adicionar_subproblema(
        problema, "Login JWT", "Implementar login com tokens JWT",
        dependencias=["Modelo de Usuário"],
        prioridade=9
    )
    
    decompostor.adicionar_subproblema(
        problema, "Recuperação de Senha", "Permitir recuperação de senha via email",
        dependencias=["Modelo de Usuário"],
        prioridade=7
    )
    
    decompostor.adicionar_subproblema(
        problema, "OAuth Social", "Login com Google/GitHub",
        dependencias=["Login JWT"],
        prioridade=6
    )
    
    print("\nDecomposição do Problema:")
    print(decompostor.visualizar_decomposicao(problema))
    
    print("\nOrdem Recomendada (por dependências):")
    ordem = decompostor.ordenar_por_dependencias(problema)
    for i, nome in enumerate(ordem, 1):
        print(f"  {i}. {nome}")


def demonstracao_brainstorming():
    """Demonstra brainstorming."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 3: Brainstorming de Soluções")
    print("=" * 70)
    
    brainstorming = Brainstorming()
    
    problema = "Sistema está lento durante picos de tráfego"
    sessao = brainstorming.iniciar_sessao(problema)
    
    # Gerar ideias (sem julgamento)
    ideias = [
        ("Adicionar cache Redis", "infraestrutura"),
        ("Implementar CDN", "infraestrutura"),
        ("Otimizar queries do banco", "código"),
        ("Adicionar mais servidores (scale horizontal)", "infraestrutura"),
        ("Usar load balancer", "infraestrutura"),
        ("Otimizar código Python (profiling)", "código"),
        ("Implementar rate limiting", "código"),
        ("Usar async/await", "código"),
        ("Implementar queue para tarefas pesadas", "arquitetura"),
        ("Adicionar índices no banco", "banco"),
    ]
    
    for ideia, categoria in ideias:
        brainstorming.adicionar_ideia(sessao, ideia, categoria)
    
    print(f"\nProblema: {problema}")
    print(f"\nIdeias Geradas ({len(sessao['ideias'])}):\n")
    
    for categoria, ideias_cat in sessao['categorias'].items():
        print(f"{categoria.upper()}:")
        for ideia in ideias_cat:
            print(f"  • {ideia}")
        print()


def demonstracao_tradeoffs():
    """Demonstra análise de trade-offs."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 4: Análise de Trade-offs")
    print("=" * 70)
    
    analisador = AnalisadorTradeoffs()
    
    decisao = "Escolher entre Monólito e Microserviços"
    analise = analisador.criar_analise(decisao)
    
    # Critérios
    analisador.adicionar_criterio(analise, "Simplicidade", 8)
    analisador.adicionar_criterio(analise, "Escalabilidade", 7)
    analisador.adicionar_criterio(analise, "Manutenibilidade", 6)
    analisador.adicionar_criterio(analise, "Custo de Desenvolvimento", 5)
    analisador.adicionar_criterio(analise, "Performance", 7)
    
    # Opções
    opcao1 = analisador.adicionar_opcao(
        analise, "Monólito", "Aplicação única e monolítica"
    )
    opcao2 = analisador.adicionar_opcao(
        analise, "Microserviços", "Arquitetura de microserviços distribuídos"
    )
    
    # Avaliar Monólito
    analisador.avaliar_opcao(opcao1, "Simplicidade", 9)
    analisador.avaliar_opcao(opcao1, "Escalabilidade", 5)
    analisador.avaliar_opcao(opcao1, "Manutenibilidade", 6)
    analisador.avaliar_opcao(opcao1, "Custo de Desenvolvimento", 9)
    analisador.avaliar_opcao(opcao1, "Performance", 8)
    
    # Avaliar Microserviços
    analisador.avaliar_opcao(opcao2, "Simplicidade", 4)
    analisador.avaliar_opcao(opcao2, "Escalabilidade", 9)
    analisador.avaliar_opcao(opcao2, "Manutenibilidade", 7)
    analisador.avaliar_opcao(opcao2, "Custo de Desenvolvimento", 4)
    analisador.avaliar_opcao(opcao2, "Performance", 6)
    
    print(analisador.visualizar_analise(analise))


def demonstracao_resolucao_estruturada():
    """Demonstra resolução estruturada."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 5: Resolução Estruturada de Problemas")
    print("=" * 70)
    
    resolvedor = ResolvedorEstruturado()
    
    problema = resolvedor.criar_problema(
        "API retorna 404 para endpoint que deveria existir"
    )
    
    # Entendimento
    resolvedor.documentar_entendimento(
        problema,
        comportamento_esperado="GET /api/users retorna lista de usuários",
        comportamento_atual="GET /api/users retorna 404 Not Found",
        contexto="Endpoint funcionava ontem, hoje parou"
    )
    
    # Informações
    resolvedor.adicionar_informacao(problema, "Deploy feito hoje de manhã", "contexto")
    resolvedor.adicionar_informacao(problema, "Rota registrada em urls.py", "código")
    resolvedor.adicionar_informacao(problema, "View existe e está correta", "código")
    
    # Hipóteses
    resolvedor.adicionar_hipotese(problema, "Rota não foi registrada corretamente no deploy", 0.8)
    resolvedor.adicionar_hipotese(problema, "Problema com configuração de URL base", 0.6)
    resolvedor.adicionar_hipotese(problema, "Cache de rotas antigas", 0.4)
    
    # Testar primeira hipótese
    resolvedor.testar_hipotese(problema, 0, "Verificado urls.py - rota existe", False)
    resolvedor.testar_hipotese(problema, 1, "Verificado settings.py - URL_BASE está correto", False)
    resolvedor.testar_hipotese(problema, 2, "Limpado cache - problema resolvido", True)
    
    # Solução
    resolvedor.documentar_solucao(
        problema,
        "Problema era cache de rotas. Limpar cache resolveu.",
        "Executado: python manage.py clear_cache"
    )
    
    # Validação
    resolvedor.validar_solucao(problema, True, "Endpoint funcionando normalmente agora")
    
    print(resolvedor.resumo(problema))


# ============================================================================
# MAIN - Executar todas as demonstrações
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("EXERCÍCIOS: PENSAMENTO CRÍTICO E RESOLUÇÃO DE PROBLEMAS")
    print("=" * 70)
    
    demonstracao_causa_raiz()
    demonstracao_decomposicao()
    demonstracao_brainstorming()
    demonstracao_tradeoffs()
    demonstracao_resolucao_estruturada()
    
    print("\n" + "=" * 70)
    print("CONCLUSÃO")
    print("=" * 70)
    print("\nEstas ferramentas ajudam a estruturar pensamento, mas:")
    print("  1. Pratique com problemas reais")
    print("  2. Adapte técnicas ao seu estilo")
    print("  3. Não seja escravo do processo - use quando ajuda")
    print("  4. Desenvolva intuição através de prática")
    print("\nPensamento crítico é uma habilidade - desenvolve com prática constante!")
    print("=" * 70)

