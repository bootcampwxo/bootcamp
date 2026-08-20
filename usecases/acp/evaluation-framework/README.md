# Sumário
- [🧪 Evaluation Framework](#-evaluation-framework)
  - [🤔 O Problema](#-o-problema)
  - [🎯 Objetivo](#-objetivo)
  - [📈 Valor de Negócio](#-valor-de-negócio)
  - [🏛️ Arquitetura](#-arquitetura)
  - [📝 Laboratório prático passo a passo](#-laboratório-prático-passo-a-passo)

# 🧪 Evaluation Framework

Um agente de IA pode parecer funcionar bem durante os testes manuais e mesmo assim falhar silenciosamente em produção — chamando a ferramenta errada, ignorando parâmetros obrigatórios ou cedendo a um usuário mal-intencionado que o manipula com prompts adversariais.

O **Evaluation Framework** do watsonx Orchestrate ADK foi desenvolvido para eliminar essa incerteza: ele transforma a validação de agentes de uma atividade subjetiva e manual em um processo **sistemático, quantitativo e repetível**.

## 🤔 O Problema

As equipes de IA da **TechCorp Inc.** e da **ABC Robots** construíram agentes sofisticados — o **AskHR** para operações de RH e o **Master Agent** para análise competitiva. Antes de liberar esses agentes para os usuários finais, os times precisam responder a perguntas críticas:

- O agente chama as ferramentas certas, na sequência correta e com os parâmetros corretos?
- Quando um usuário mal-intencionado tenta manipulá-lo, o agente resiste?
- Se mudarmos as instruções do agente, como sabemos que não quebramos algo que funcionava?

Sem um framework de avaliação, essas perguntas só têm resposta depois que o problema acontece em produção.

## 🎯 Objetivo

Neste laboratório, você vai aplicar o **Evaluation Framework** do ADK sobre os dois agentes já construídos nos laboratórios anteriores, percorrendo o ciclo completo:

1. **`generate`** — Gera datasets de ground truth automaticamente a partir de estórias de usuário escritas em linguagem natural e das definições de ferramentas Python
2. **`evaluate`** — Simula interações reais, compara com o ground truth e produz métricas quantitativas de desempenho
3. **`analyze`** — Detalha onde e por que o agente falhou, com sugestões de melhoria para instruções e docstrings de ferramentas
4. **`red-teaming`** — Executa ataques adversariais baseados no **OWASP Top 10 for LLM Applications** para mapear as vulnerabilidades de segurança do agente

## 📈 Valor de Negócio

**Para as equipes de desenvolvimento:**
- Detectar regressões de comportamento antes do deploy, não depois
- Reduzir tempo gasto em testes manuais e revisões subjetivas de qualidade
- Ter evidências quantitativas para comparar versões de agentes (A/B de modelos, instruções, ferramentas)

**Para as equipes de segurança e compliance:**
- Mapear vulnerabilidades com base no padrão OWASP, o mesmo referencial usado em auditorias de segurança de IA
- Criar histórico auditável de testes de segurança para cada versão do agente
- Demonstrar conformidade com frameworks regulatórios que exigem testes adversariais em sistemas de IA

**Para o negócio:**
- Reduzir o risco de incidentes de segurança que comprometam dados de colaboradores (AskHR) ou informações estratégicas da empresa (Análise Competitiva)
- Aumentar a confiança dos stakeholders com métricas objetivas de qualidade e segurança antes de cada liberação

## 🏛️ Arquitetura

O Evaluation Framework opera em quatro etapas encadeadas, todas acessíveis via CLI do ADK:

```
  Estórias de Usuário (CSV)
  + Definições de Ferramentas (Python)
            │
            ▼
       [ generate ] ──► ground truth (test_cases/)
            │
            ▼
       [ evaluate ] ──► métricas de desempenho (summary_metrics.csv)
            │
            ▼
       [ analyze  ] ──► diagnóstico por test case
            │
            ▼
  [ red-teaming plan + run ] ──► mapa de vulnerabilidades OWASP
```

**Casos de uso avaliados neste lab:**

| Agente | Ferramentas avaliadas |
|--------|-----------------------|
| `Agente de RH` (AskHR) | `get_time_off_balance`, `post_request_time_off`, `get_user_profile_details` |
| `Master Agent` (Análise Competitiva) | `get_product_catalog`, `get_product_specifications`, `search_and_review_high_rated_products` |

## 📝 Laboratório prático passo a passo

👉👉👉 [Clique aqui](hands-on-lab-evaluation-framework.md) para acessar as instruções detalhadas.

**Tempo estimado:** 60–90 minutos

---

**Features demonstradas:** `Evaluation Framework` `generate` `evaluate` `analyze` `red-teaming` `OWASP Top 10 for LLMs` `CLI`
