"""
Exercícios Práticos: Gestão de Tempo e Produtividade

Estes exercícios ajudam a desenvolver habilidades de gestão de tempo
e produtividade através de ferramentas e simulações práticas.
"""

from datetime import datetime, timedelta
from typing import List, Dict, Tuple, Optional
from enum import Enum
import json


# ============================================================================
# EXERCÍCIO 1: Implementação da Técnica Pomodoro
# ============================================================================

class EstadoPomodoro(Enum):
    """Estados possíveis de um Pomodoro."""
    TRABALHO = "trabalho"
    PAUSA_CURTA = "pausa_curta"
    PAUSA_LONGA = "pausa_longa"
    PARADO = "parado"


class PomodoroTracker:
    """
    Classe para rastrear e gerenciar sessões Pomodoro.
    """
    
    def __init__(self, duracao_trabalho: int = 25, duracao_pausa: int = 5):
        """
        Inicializa tracker de Pomodoro.
        
        Args:
            duracao_trabalho: Duração do Pomodoro em minutos (padrão: 25)
            duracao_pausa: Duração da pausa em minutos (padrão: 5)
        """
        self.duracao_trabalho = duracao_trabalho
        self.duracao_pausa = duracao_pausa
        self.duracao_pausa_longa = 15
        self.pomodoros_completos = 0
        self.estado_atual = EstadoPomodoro.PARADO
        self.inicio_sessao = None
        self.tarefa_atual = None
        self.historico = []
    
    def iniciar_pomodoro(self, tarefa: str = "Trabalho focado"):
        """
        Inicia um novo Pomodoro.
        
        Args:
            tarefa: Descrição da tarefa sendo trabalhada
        """
        if self.estado_atual == EstadoPomodoro.TRABALHO:
            print("⚠️ Já existe um Pomodoro em andamento!")
            return
        
        self.estado_atual = EstadoPomodoro.TRABALHO
        self.inicio_sessao = datetime.now()
        self.tarefa_atual = tarefa
        
        print(f"🍅 Pomodoro iniciado: {tarefa}")
        print(f"⏰ Duração: {self.duracao_trabalho} minutos")
        print(f"📝 Foco total! Evite interrupções.")
    
    def finalizar_pomodoro(self) -> bool:
        """
        Finaliza o Pomodoro atual.
        
        Returns:
            True se completou com sucesso, False se ainda não terminou
        """
        if self.estado_atual != EstadoPomodoro.TRABALHO:
            print("⚠️ Nenhum Pomodoro de trabalho em andamento!")
            return False
        
        tempo_decorrido = (datetime.now() - self.inicio_sessao).total_seconds() / 60
        tempo_esperado = self.duracao_trabalho
        
        if tempo_decorrido < tempo_esperado * 0.8:  # Menos de 80% do tempo
            print(f"⚠️ Pomodoro finalizado prematuramente ({tempo_decorrido:.1f}min)")
        else:
            self.pomodoros_completos += 1
            print(f"✅ Pomodoro completo! ({self.pomodoros_completos} completos hoje)")
            
            # Registrar no histórico
            self.historico.append({
                'tarefa': self.tarefa_atual,
                'duracao': tempo_decorrido,
                'timestamp': datetime.now().isoformat()
            })
        
        # Determinar próximo estado
        if self.pomodoros_completos % 4 == 0:
            self.estado_atual = EstadoPomodoro.PAUSA_LONGA
            duracao_pausa = self.duracao_pausa_longa
            print(f"🛋️ Hora da pausa longa! {duracao_pausa} minutos")
        else:
            self.estado_atual = EstadoPomodoro.PAUSA_CURTA
            duracao_pausa = self.duracao_pausa
            print(f"☕ Pausa! {duracao_pausa} minutos")
        
        self.tarefa_atual = None
        return True
    
    def tempo_restante(self) -> Optional[float]:
        """
        Retorna tempo restante do Pomodoro atual em minutos.
        
        Returns:
            Minutos restantes ou None se não houver Pomodoro ativo
        """
        if self.estado_atual != EstadoPomodoro.TRABALHO or not self.inicio_sessao:
            return None
        
        tempo_decorrido = (datetime.now() - self.inicio_sessao).total_seconds() / 60
        tempo_restante = self.duracao_trabalho - tempo_decorrido
        
        return max(0, tempo_restante)
    
    def estatisticas(self) -> Dict:
        """
        Retorna estatísticas do tracker.
        
        Returns:
            Dicionário com estatísticas
        """
        total_minutos = sum(h['duracao'] for h in self.historico)
        
        # Agrupar por tarefa
        tarefas = {}
        for h in self.historico:
            tarefa = h['tarefa']
            if tarefa not in tarefas:
                tarefas[tarefa] = 0
            tarefas[tarefa] += h['duracao']
        
        return {
            'pomodoros_completos': self.pomodoros_completos,
            'total_minutos': total_minutos,
            'total_horas': total_minutos / 60,
            'tarefas': tarefas,
            'pomodoro_atual': self.tarefa_atual,
            'tempo_restante': self.tempo_restante()
        }


# ============================================================================
# EXERCÍCIO 2: Matriz de Eisenhower
# ============================================================================

class Urgencia(Enum):
    URGENTE = "urgente"
    NAO_URGENTE = "nao_urgente"


class Importancia(Enum):
    IMPORTANTE = "importante"
    NAO_IMPORTANTE = "nao_importante"


class QuadranteEisenhower(Enum):
    Q1_FAZER_AGORA = "q1_fazer_agora"
    Q2_AGENDAR = "q2_agendar"
    Q3_DELEGAR = "q3_delegar"
    Q4_ELIMINAR = "q4_eliminar"


class MatrizEisenhower:
    """
    Classe para categorizar tarefas usando Matriz de Eisenhower.
    """
    
    def __init__(self):
        self.tarefas = {
            QuadranteEisenhower.Q1_FAZER_AGORA: [],
            QuadranteEisenhower.Q2_AGENDAR: [],
            QuadranteEisenhower.Q3_DELEGAR: [],
            QuadranteEisenhower.Q4_ELIMINAR: []
        }
    
    def categorizar(
        self, 
        tarefa: str, 
        importancia: Importancia, 
        urgencia: Urgencia
    ) -> QuadranteEisenhower:
        """
        Categoriza tarefa em um dos 4 quadrantes.
        
        Args:
            tarefa: Descrição da tarefa
            importancia: Nível de importância
            urgencia: Nível de urgência
        
        Returns:
            Quadrante correspondente
        """
        if importancia == Importancia.IMPORTANTE:
            if urgencia == Urgencia.URGENTE:
                quadrante = QuadranteEisenhower.Q1_FAZER_AGORA
            else:
                quadrante = QuadranteEisenhower.Q2_AGENDAR
        else:
            if urgencia == Urgencia.URGENTE:
                quadrante = QuadranteEisenhower.Q3_DELEGAR
            else:
                quadrante = QuadranteEisenhower.Q4_ELIMINAR
        
        self.tarefas[quadrante].append({
            'tarefa': tarefa,
            'importancia': importancia.value,
            'urgencia': urgencia.value,
            'categoria': quadrante.value
        })
        
        return quadrante
    
    def adicionar_tarefa(
        self,
        tarefa: str,
        importante: bool,
        urgente: bool
    ) -> QuadranteEisenhower:
        """
        Adiciona tarefa usando valores booleanos.
        
        Args:
            tarefa: Descrição da tarefa
            importante: Se a tarefa é importante
            urgente: Se a tarefa é urgente
        
        Returns:
            Quadrante correspondente
        """
        importancia = Importancia.IMPORTANTE if importante else Importancia.NAO_IMPORTANTE
        urgencia = Urgencia.URGENTE if urgente else Urgencia.NAO_URGENTE
        
        return self.categorizar(tarefa, importancia, urgencia)
    
    def visualizar_matriz(self) -> str:
        """
        Retorna representação visual da matriz.
        
        Returns:
            String formatada com matriz
        """
        output = "\n" + "=" * 70 + "\n"
        output += "MATRIZ DE EISENHOWER\n"
        output += "=" * 70 + "\n\n"
        
        output += "                    URGENTE              NÃO URGENTE\n"
        output += "IMPORTANTE     │ Quadrante 1        │ Quadrante 2\n"
        output += "               │ FAZER AGORA        │ AGENDAR\n"
        output += f"               │ ({len(self.tarefas[QuadranteEisenhower.Q1_FAZER_AGORA])} tarefas)        │ ({len(self.tarefas[QuadranteEisenhower.Q2_AGENDAR])} tarefas)\n"
        output += "\n"
        output += "NÃO IMPORTANTE │ Quadrante 3        │ Quadrante 4\n"
        output += "               │ DELEGAR/REJEITAR   │ ELIMINAR\n"
        output += f"               │ ({len(self.tarefas[QuadranteEisenhower.Q3_DELEGAR])} tarefas)        │ ({len(self.tarefas[QuadranteEisenhower.Q4_ELIMINAR])} tarefas)\n"
        
        output += "\n" + "-" * 70 + "\n"
        output += "DETALHES:\n"
        output += "-" * 70 + "\n\n"
        
        quadrante_nomes = {
            QuadranteEisenhower.Q1_FAZER_AGORA: "Q1 - FAZER AGORA",
            QuadranteEisenhower.Q2_AGENDAR: "Q2 - AGENDAR",
            QuadranteEisenhower.Q3_DELEGAR: "Q3 - DELEGAR",
            QuadranteEisenhower.Q4_ELIMINAR: "Q4 - ELIMINAR"
        }
        
        for quadrante, nome in quadrante_nomes.items():
            output += f"\n{nome}:\n"
            tarefas_quad = self.tarefas[quadrante]
            if tarefas_quad:
                for i, t in enumerate(tarefas_quad, 1):
                    output += f"  {i}. {t['tarefa']}\n"
            else:
                output += "  (nenhuma tarefa)\n"
        
        return output
    
    def analise_distribuicao(self) -> Dict:
        """
        Analisa distribuição de tarefas entre quadrantes.
        
        Returns:
            Dicionário com análise
        """
        total = sum(len(tarefas) for tarefas in self.tarefas.values())
        
        if total == 0:
            return {'total': 0, 'distribuicao': {}, 'recomendacao': 'Nenhuma tarefa ainda'}
        
        distribuicao = {
            'q1_percentual': len(self.tarefas[QuadranteEisenhower.Q1_FAZER_AGORA]) / total * 100,
            'q2_percentual': len(self.tarefas[QuadranteEisenhower.Q2_AGENDAR]) / total * 100,
            'q3_percentual': len(self.tarefas[QuadranteEisenhower.Q3_DELEGAR]) / total * 100,
            'q4_percentual': len(self.tarefas[QuadranteEisenhower.Q4_ELIMINAR]) / total * 100,
        }
        
        recomendacoes = []
        
        if distribuicao['q1_percentual'] > 40:
            recomendacoes.append(
                "⚠️ Muitas tarefas no Q1 (Fazer Agora). "
                "Isso indica falta de planejamento. Tente mover tarefas para Q2."
            )
        
        if distribuicao['q2_percentual'] < 30:
            recomendacoes.append(
                "💡 Poucas tarefas no Q2 (Agendar). "
                "Idealmente, maioria do tempo deve estar no Q2 (importante não urgente)."
            )
        
        if distribuicao['q3_percentual'] > 20:
            recomendacoes.append(
                "⚠️ Muitas tarefas no Q3 (Delegar). "
                "Avalie se essas tarefas realmente precisam ser feitas ou podem ser eliminadas."
            )
        
        if distribuicao['q4_percentual'] > 10:
            recomendacoes.append(
                "⚠️ Tarefas no Q4 (Eliminar). "
                "Remova essas tarefas - são desperdício de tempo."
            )
        
        return {
            'total': total,
            'distribuicao': distribuicao,
            'recomendacoes': recomendacoes if recomendacoes else ['✅ Distribuição parece equilibrada']
        }


# ============================================================================
# EXERCÍCIO 3: Metas SMART
# ============================================================================

class MetaSMART:
    """
    Classe para criar e validar metas SMART.
    """
    
    def __init__(
        self,
        descricao: str,
        especifica: bool = False,
        mensuravel: bool = False,
        alcancavel: bool = False,
        relevante: bool = False,
        prazo: Optional[datetime] = None
    ):
        """
        Inicializa meta SMART.
        
        Args:
            descricao: Descrição da meta
            especifica: Se a meta é específica (S)
            mensuravel: Se a meta é mensurável (M)
            alcancavel: Se a meta é alcançável (A)
            relevante: Se a meta é relevante (R)
            prazo: Prazo da meta (T)
        """
        self.descricao = descricao
        self.especifica = especifica
        self.mensuravel = mensuravel
        self.alcancavel = alcancavel
        self.relevante = relevante
        self.prazo = prazo
        self.progresso = 0.0  # 0.0 a 1.0
        self.completa = False
    
    def validar(self) -> Tuple[bool, List[str]]:
        """
        Valida se meta atende todos critérios SMART.
        
        Returns:
            Tuple (é válida, lista de problemas)
        """
        problemas = []
        
        if not self.especifica:
            problemas.append("❌ S (Specific): Meta não é específica o suficiente")
        
        if not self.mensuravel:
            problemas.append("❌ M (Measurable): Meta não é mensurável")
        
        if not self.alcancavel:
            problemas.append("❌ A (Achievable): Meta pode não ser alcançável")
        
        if not self.relevante:
            problemas.append("❌ R (Relevant): Meta pode não ser relevante")
        
        if not self.prazo:
            problemas.append("❌ T (Time-bound): Meta não tem prazo definido")
        elif self.prazo < datetime.now():
            problemas.append("❌ T (Time-bound): Prazo já passou")
        
        return len(problemas) == 0, problemas
    
    def atualizar_progresso(self, progresso: float):
        """
        Atualiza progresso da meta (0.0 a 1.0).
        
        Args:
            progresso: Progresso entre 0.0 (0%) e 1.0 (100%)
        """
        self.progresso = max(0.0, min(1.0, progresso))
        
        if self.progresso >= 1.0:
            self.completa = True
    
    def tempo_restante(self) -> Optional[timedelta]:
        """
        Retorna tempo restante até prazo.
        
        Returns:
            Timedelta ou None se não houver prazo
        """
        if not self.prazo:
            return None
        
        return self.prazo - datetime.now()
    
    def status(self) -> str:
        """
        Retorna status da meta.
        
        Returns:
            String com status
        """
        if self.completa:
            return "✅ Completa"
        
        if not self.prazo:
            return f"🔄 Em progresso ({self.progresso*100:.0f}%)"
        
        tempo_rest = self.tempo_restante()
        
        if tempo_rest.total_seconds() < 0:
            return "⚠️ Prazo vencido"
        elif tempo_rest.days < 7:
            return f"⏰ Urgente ({tempo_rest.days} dias restantes)"
        else:
            return f"📅 Em andamento ({tempo_rest.days} dias restantes)"
    
    def __str__(self) -> str:
        """Representação string da meta."""
        output = f"Meta: {self.descricao}\n"
        output += f"Status: {self.status()}\n"
        
        valida, problemas = self.validar()
        if valida:
            output += "✅ Meta SMART válida\n"
        else:
            output += "⚠️ Meta não atende todos critérios SMART:\n"
            for problema in problemas:
                output += f"  {problema}\n"
        
        if self.prazo:
            output += f"Prazo: {self.prazo.strftime('%d/%m/%Y')}\n"
        
        output += f"Progresso: {self.progresso*100:.0f}%"
        
        return output


# ============================================================================
# EXERCÍCIO 4: Análise de Produtividade
# ============================================================================

class AnalisadorProdutividade:
    """
    Classe para analisar padrões de produtividade.
    """
    
    def __init__(self):
        self.registros = []  # Lista de registros de tempo gasto
    
    def registrar_atividade(
        self,
        atividade: str,
        categoria: str,
        duracao_minutos: float,
        data: Optional[datetime] = None
    ):
        """
        Registra tempo gasto em uma atividade.
        
        Args:
            atividade: Nome da atividade
            categoria: Categoria (coding, meetings, emails, etc.)
            duracao_minutos: Duração em minutos
            data: Data da atividade (padrão: hoje)
        """
        if data is None:
            data = datetime.now()
        
        self.registros.append({
            'atividade': atividade,
            'categoria': categoria,
            'duracao_minutos': duracao_minutos,
            'data': data
        })
    
    def tempo_por_categoria(self, dias: int = 7) -> Dict[str, float]:
        """
        Retorna tempo total gasto por categoria.
        
        Args:
            dias: Número de dias para analisar (padrão: 7)
        
        Returns:
            Dicionário {categoria: total_minutos}
        """
        data_limite = datetime.now() - timedelta(days=dias)
        
        registros_recentes = [
            r for r in self.registros
            if r['data'] >= data_limite
        ]
        
        tempo_por_cat = {}
        for reg in registros_recentes:
            cat = reg['categoria']
            if cat not in tempo_por_cat:
                tempo_por_cat[cat] = 0
            tempo_por_cat[cat] += reg['duracao_minutos']
        
        return tempo_por_cat
    
    def analise_semanal(self) -> Dict:
        """
        Analisa padrões de produtividade da semana.
        
        Returns:
            Dicionário com análise
        """
        tempo_por_cat = self.tempo_por_categoria(dias=7)
        
        total_minutos = sum(tempo_por_cat.values())
        total_horas = total_minutos / 60
        
        # Recomendações
        recomendacoes = []
        
        if 'meetings' in tempo_por_cat:
            pct_meetings = tempo_por_cat['meetings'] / total_minutos * 100
            if pct_meetings > 30:
                recomendacoes.append(
                    f"⚠️ Muito tempo em reuniões ({pct_meetings:.1f}%). "
                    "Considere reduzir reuniões ou torná-las mais curtas."
                )
        
        if 'coding' in tempo_por_cat:
            pct_coding = tempo_por_cat['coding'] / total_minutos * 100
            if pct_coding < 40:
                recomendacoes.append(
                    f"💡 Pouco tempo codando ({pct_coding:.1f}%). "
                    "Desenvolvedores geralmente precisam de 40-60% do tempo codando."
                )
        
        if 'distracoes' in tempo_por_cat:
            pct_dist = tempo_por_cat['distracoes'] / total_minutos * 100
            if pct_dist > 10:
                recomendacoes.append(
                    f"⚠️ Muito tempo em distrações ({pct_dist:.1f}%). "
                    "Considere estratégias para reduzir."
                )
        
        return {
            'total_horas': total_horas,
            'tempo_por_categoria': tempo_por_cat,
            'distribuicao_percentual': {
                cat: (tempo / total_minutos * 100) 
                for cat, tempo in tempo_por_cat.items()
            },
            'recomendacoes': recomendacoes
        }


# ============================================================================
# EXERCÍCIOS PRÁTICOS - DEMONSTRAÇÃO
# ============================================================================

def demonstracao_pomodoro():
    """Demonstra uso do Pomodoro tracker."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 1: Técnica Pomodoro")
    print("=" * 70)
    
    tracker = PomodoroTracker(duracao_trabalho=25, duracao_pausa=5)
    
    print("\n--- Simulando alguns Pomodoros ---\n")
    
    # Simular Pomodoros completos
    tarefas = [
        "Implementar função de autenticação",
        "Code review do PR #42",
        "Escrever testes unitários"
    ]
    
    for tarefa in tarefas:
        tracker.iniciar_pomodoro(tarefa)
        # Simular conclusão
        tracker.finalizar_pomodoro()
        print()
    
    print("\n--- Estatísticas ---")
    stats = tracker.estatisticas()
    print(f"Pomodoros completos: {stats['pomodoros_completos']}")
    print(f"Total de horas: {stats['total_horas']:.2f}")
    print("\nTempo por tarefa:")
    for tarefa, minutos in stats['tarefas'].items():
        print(f"  {tarefa}: {minutos:.1f} minutos")


def demonstracao_eisenhower():
    """Demonstra uso da Matriz de Eisenhower."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 2: Matriz de Eisenhower")
    print("=" * 70)
    
    matriz = MatrizEisenhower()
    
    # Exemplos de tarefas de desenvolvimento
    tarefas_exemplo = [
        ("Bug crítico em produção", True, True),
        ("Refatorar código legado", True, False),
        ("Aprender nova tecnologia", True, False),
        ("Responder email não urgente", False, True),
        ("Ver redes sociais", False, False),
        ("Implementar feature solicitada", True, True),
        ("Melhorar documentação", True, False),
        ("Reunião desnecessária", False, True),
        ("Planejamento arquitetural", True, False),
        ("Corrigir teste quebrado", True, True),
    ]
    
    print("\n--- Categorizando Tarefas ---\n")
    
    for tarefa, importante, urgente in tarefas_exemplo:
        quadrante = matriz.adicionar_tarefa(tarefa, importante, urgente)
        print(f"'{tarefa}' → {quadrante.value}")
    
    print("\n--- Matriz Completa ---")
    print(matriz.visualizar_matriz())
    
    print("\n--- Análise de Distribuição ---")
    analise = matriz.analise_distribuicao()
    print(f"Total de tarefas: {analise['total']}")
    print("\nDistribuição:")
    for cat, pct in analise['distribuicao'].items():
        print(f"  {cat}: {pct:.1f}%")
    
    print("\nRecomendações:")
    for rec in analise['recomendacoes']:
        print(f"  {rec}")


def demonstracao_metas_smart():
    """Demonstra criação de metas SMART."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 3: Metas SMART")
    print("=" * 70)
    
    # Exemplo 1: Meta SMART válida
    print("\n--- Exemplo 1: Meta SMART Válida ---")
    meta1 = MetaSMART(
        descricao="Aumentar cobertura de testes de 60% para 80% no módulo de pagamentos",
        especifica=True,  # Específica: módulo de pagamentos
        mensuravel=True,  # Mensurável: 60% → 80%
        alcancavel=True,  # Alcançável
        relevante=True,  # Relevante para qualidade
        prazo=datetime.now() + timedelta(days=30)  # 30 dias
    )
    meta1.atualizar_progresso(0.3)  # 30% completo
    print(meta1)
    
    # Exemplo 2: Meta não SMART
    print("\n--- Exemplo 2: Meta NÃO SMART ---")
    meta2 = MetaSMART(
        descricao="Melhorar código",
        especifica=False,  # Não específica
        mensuravel=False,  # Não mensurável
        alcancavel=True,
        relevante=True,
        prazo=None  # Sem prazo
    )
    print(meta2)
    
    # Exemplo 3: Meta quase SMART
    print("\n--- Exemplo 3: Meta Quase SMART (falta prazo) ---")
    meta3 = MetaSMART(
        descricao="Completar curso de FastAPI e construir 3 APIs de exemplo",
        especifica=True,
        mensuravel=True,  # 3 APIs é mensurável
        alcancavel=True,
        relevante=True,
        prazo=None  # Faltando prazo
    )
    print(meta3)


def demonstracao_produtividade():
    """Demonstra análise de produtividade."""
    print("\n" + "=" * 70)
    print("EXERCÍCIO 4: Análise de Produtividade")
    print("=" * 70)
    
    analisador = AnalisadorProdutividade()
    
    # Simular uma semana de trabalho
    print("\n--- Registrando Atividades da Semana ---\n")
    
    atividades_semana = [
        ("Coding - Feature X", "coding", 120),
        ("Daily Standup", "meetings", 15),
        ("Code Review PR #1", "code_review", 30),
        ("Coding - Feature Y", "coding", 90),
        ("Reunião de Planejamento", "meetings", 60),
        ("Responder emails", "emails", 45),
        ("Coding - Bug Fix", "coding", 60),
        ("Reunião 1:1", "meetings", 30),
        ("Code Review PR #2", "code_review", 45),
        ("Redes Sociais", "distracoes", 20),
        ("Coding - Refatoração", "coding", 90),
        ("Sprint Review", "meetings", 90),
    ]
    
    for atividade, categoria, minutos in atividades_semana:
        analisador.registrar_atividade(atividade, categoria, minutos)
        print(f"✓ {atividade}: {minutos} min ({categoria})")
    
    print("\n--- Análise Semanal ---")
    analise = analisador.analise_semanal()
    
    print(f"\nTotal de horas na semana: {analise['total_horas']:.1f}h")
    
    print("\nTempo por categoria:")
    for cat, minutos in analise['tempo_por_categoria'].items():
        horas = minutos / 60
        pct = analise['distribuicao_percentual'][cat]
        print(f"  {cat}: {horas:.1f}h ({pct:.1f}%)")
    
    print("\nRecomendações:")
    for rec in analise['recomendacoes']:
        print(f"  {rec}")


# ============================================================================
# MAIN - Executar todas as demonstrações
# ============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("EXERCÍCIOS: GESTÃO DE TEMPO E PRODUTIVIDADE")
    print("=" * 70)
    
    demonstracao_pomodoro()
    demonstracao_eisenhower()
    demonstracao_metas_smart()
    demonstracao_produtividade()
    
    print("\n" + "=" * 70)
    print("CONCLUSÃO")
    print("=" * 70)
    print("\nEstas são ferramentas de apoio. O sucesso vem de:")
    print("  1. Experimentar e encontrar o que funciona para você")
    print("  2. Ser consistente no uso")
    print("  3. Ajustar conforme necessário")
    print("  4. Não se culpar por imperfeições - gestão de tempo é prática contínua")
    print("\nComece com uma técnica, domine, depois adicione outras!")
    print("=" * 70)

