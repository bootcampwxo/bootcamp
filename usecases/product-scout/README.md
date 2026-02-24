# Sumário
- [Sumário](#sumário)
- [🛒 Explorador de Produtos Alimentícios](#-explorador-de-produtos-alimentícios)
- [🤔 O Problema](#-o-problema)
- [🎯 Objetivo](#-objetivo)
- [📈 Valor de Negócio](#-valor-de-negócio)
  - [Para Clientes](#para-clientes)
  - [Para o Varejista](#para-o-varejista)
- [🏛️ Arquitetura](#-arquitetura)
- [🎥 Demonstração](#-demonstração)
- [📝 Laboratório prático passo a passo](#-laboratório-prático-passo-a-passo)

# 🛒 Explorador de Produtos Alimentícios

![FreshLane Markets](images/store.png)

Neste laboratório, você vai construir e interagir com um **Agente Explorador de Produtos** (Product Scout Agent), projetado para ajudar consumidores a tomar decisões mais seguras e informadas ao comprar produtos alimentícios online. Usaremos a **FreshLane Markets**, uma rede de supermercados fictícia, como a empresa que desenvolve esta solução agêntica.

## 🤔 O Problema

**Cenário**: Imagine um cliente navegando em uma loja de supermercado online. Ele quer saber mais sobre um produto antes de adicioná-lo ao carrinho — especificamente se contém ingredientes que podem causar reações alérgicas e se há recalls ativos sobre o produto.

Para apoiar isso, a loja oferece um agente de IA que automatiza a busca de informações em nome do cliente. Em vez de verificar manualmente vários sites, o cliente pode confiar no agente para rapidamente apresentar detalhes críticos sobre conteúdo nutricional, alérgenos e questões de segurança.

**Contexto de Negócio**: Para um varejista, oferecer esse tipo de assistência com IA agêntica reduz o risco para o cliente, melhora a confiança e aprimora a experiência geral de compra. Também pode reduzir a carga sobre as equipes de suporte ao cliente, que de outra forma gastariam tempo significativo respondendo perguntas sobre segurança de produtos.

Idealmente, a loja integraria sua própria biblioteca de produtos em tal agente. Para este exercício prático, no entanto, simularemos a mesma funcionalidade usando uma consulta à Open Food Foundation (OFF) para recuperar informações de produtos.

## 🎯 Objetivo

Criar um sistema multiagente inteligente que permita aos clientes:

✅ **Buscar informações detalhadas** sobre produtos alimentícios

✅ **Verificar alérgenos** e ingredientes potencialmente problemáticos

✅ **Consultar recalls ativos** da FDA (Food and Drug Administration)

✅ **Entender valores nutricionais** e diretrizes alimentares

✅ **Obter explicações** sobre classificações nutricionais

Tudo isso através de uma interface conversacional simples e natural, integrada ao site da loja.

## 📈 Valor de Negócio

### Para Clientes
- **Decisões mais seguras**: Informações completas sobre alérgenos e recalls
- **Compra informada**: Acesso rápido a dados nutricionais e ingredientes
- **Confiança aumentada**: Transparência sobre produtos antes da compra
- **Experiência simplificada**: Uma única interface para todas as consultas

### Para o Varejista
- **Redução de riscos**: Menos problemas com produtos inadequados
- **Confiança do cliente**: Transparência gera fidelidade
- **Suporte otimizado**: Menos carga sobre equipes de atendimento
- **Diferenciação competitiva**: Experiência de compra superior

## 🏛️ Arquitetura

A solução utiliza uma arquitetura multiagente com **watsonx Orchestrate**, onde agentes especializados colaboram para atender às solicitações dos clientes:

![Arquitetura](./images/Product%20Scout%20Agent%20Architecture.png)

### Componentes da Arquitetura

**1. Agente Open Food Foundation**
- Busca produtos na base da Open Food Foundation (organização sem fins lucrativos que mantém um banco de dados aberto de produtos alimentícios)
- Recupera detalhes completos incluindo ingredientes e informações nutricionais
- Usa ferramentas: `off_search_tool` e `off_product_tool`

**2. Agente Recalls FDA**
- Consulta recalls (recolhimentos) ativos da FDA (Administração de Alimentos e Medicamentos dos EUA)
- Verifica segurança de produtos específicos
- Usa ferramenta: `fda_recalls_tool`

**3. Agente Nutricao**
- Fornece explicações sobre classificações nutricionais (nutrition scores)
- Oferece diretrizes alimentares
- Usa base de conhecimento (RAG) com documentos sobre nutrição

**4. FreshLaneMarket Product Scout** (Agente Orquestrador)
- Coordena os três agentes especializados
- Interpreta solicitações dos clientes
- Combina informações de múltiplas fontes
- Fornece respostas completas e contextualizadas

### Fluxo de Trabalho

1. Cliente faz pergunta sobre um produto
2. Agente orquestrador analisa a solicitação
3. Delega tarefas aos agentes especializados apropriados
4. Agentes especializados executam suas ferramentas/buscas
5. Orquestrador combina resultados
6. Resposta completa é apresentada ao cliente

## 🎥 Demonstração

Veja o vídeo completo que demonstra todo o cenário:

[▶️ Assistir demonstração do Product Scout](https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/13654/c722ea5e-5f7b-442c-93d2-e3ec7d13de6f)

## 📝 Laboratório prático passo a passo

👉👉👉 [Clique aqui](./hands-on-lab.md) para acessar as instruções detalhadas e implementar este caso de uso.

Neste laboratório você vai:

1. **Criar o Agente Open Food Foundation** - Para buscar informações de produtos da base de dados aberta
2. **Criar o Agente Recalls FDA** - Para verificar recolhimentos ativos da FDA
3. **Criar o Agente Nutricao** - Para informações nutricionais e diretrizes alimentares
4. **Criar o Agente Orquestrador** - Para coordenar todos os agentes especializados
5. **Integrar com website** - Adicionar chat widget ao site da FreshLane Markets

**Tempo estimado**: 60-90 minutos

**Pré-requisitos**:
- Acesso ao watsonx Orchestrate
- Navegador web
- Editor de texto (para personalizar HTML)

---

> [!IMPORTANT]
> Este laboratório usa APIs públicas da Open Food Foundation e FDA. Em um ambiente de produção, você integraria com o catálogo de produtos da própria loja e sistemas internos de gestão de qualidade.

**Features demonstradas**: `RAG` `Multi-agent orchestration` `Backend connection` `No code` `Embedded chat`