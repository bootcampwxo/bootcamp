# 🛒 Laboratório Hands-on: Análise de Prateleira de Varejo

> **Nota**: Este caso de uso utiliza o watsonx Orchestrate ADK (Agent Developer Kit) e requer configuração avançada de ambiente de desenvolvimento. O laboratório completo em inglês está disponível em [`retail.md`](./retail.md) com 846 linhas de instruções detalhadas.

## 📋 Visão Geral

Este laboratório demonstra como criar uma solução multi-agente para análise de prateleiras de varejo usando:
- **Modelos de Visão**: Análise de imagens de prateleiras
- **Busca na Web**: Pesquisa de tendências de mercado
- **Múltiplos Agentes**: Colaboração entre agentes especializados
- **watsonx Orchestrate ADK**: Desenvolvimento e teste local

## 🎯 Objetivos do Laboratório

1. Criar ferramentas customizadas (imagem para texto e busca web)
2. Desenvolver 3 agentes colaborativos:
   - **Internet Research Agent**: Interpreta imagens e busca tendências
   - **Market Analyst Agent**: Analisa tendências e cria recomendações
   - **Retail Market Agent**: Agente supervisor que coordena os outros
3. Testar a solução localmente com ADK
4. (Opcional) Fazer deploy em instância SaaS
5. (Opcional) Criar agente "headless" acionado por eventos

## 🔧 Pré-requisitos

- watsonx Orchestrate ADK instalado e configurado
- Acesso ao watsonx.ai com modelo de visão (llama-3-2-90b-vision-instruct)
- Chave de API Tavily para busca na web
- Python 3.x e Docker/Docker Compose
- VS Code para desenvolvimento

## 📚 Estrutura do Laboratório

### Parte 1: Criação de Ferramentas
- **Ferramenta de Imagem para Texto**: Usa watsonx.ai vision model
- **Ferramenta de Busca Web**: Integração com Tavily via Langchain

### Parte 2: Desenvolvimento de Agentes
- Configuração de conexões e credenciais
- Criação de agentes via UI e YAML
- Definição de comportamentos e instruções
- Testes e validação

### Parte 3: Deploy e Integração
- Upload para instância SaaS (opcional)
- Criação de agente headless (opcional)
- Integração via REST API

## 🚀 Início Rápido

### 1. Configurar Ambiente

```bash
# Iniciar ADK local
orchestrate chat start --env-file .env

# Importar conexões
orchestrate connections import -f ./usecases/retail/src/connections/watsonxai.yaml
orchestrate connections import -f ./usecases/retail/src/connections/tavily.yaml
```

### 2. Importar Ferramentas

```bash
# Ferramenta de descrição de imagem
orchestrate tools import -k python \
  -f ./usecases/retail/src/tools/generate_description_from_image.py \
  -r ./usecases/retail/src/tools/requirements.txt \
  -a watsonxai

# Ferramenta de busca web
orchestrate tools import -k python \
  -f ./usecases/retail/src/tools/web_search.py \
  -r ./usecases/retail/src/tools/requirements.txt \
  -a tavily
```

### 3. Importar Agentes

```bash
# Importar todos os agentes
orchestrate agents import -f ./usecases/retail/src/agents/internet_research_agent.yaml
orchestrate agents import -f ./usecases/retail/src/agents/market_analyst_agent.yaml
orchestrate agents import -f ./usecases/retail/src/agents/retail_market_agent.yaml
```

### 4. Testar Solução

Acesse a UI do watsonx Orchestrate e teste com prompts como:

```
Please look at the image at https://i.imgur.com/qfiugNJ.jpeg. 
Based on market trends for the products in the image, can you make 
recommendations for any rearrangement of the products on the shelf?
```

## 📖 Documentação Completa

Para instruções detalhadas passo a passo, incluindo:
- Explicação completa do código das ferramentas
- Configuração de conexões e credenciais
- Criação interativa de agentes via UI
- Deploy em ambiente SaaS
- Implementação de agente headless
- Troubleshooting e dicas avançadas

**Consulte o laboratório completo em inglês**: [`retail.md`](./retail.md)

## 🏗️ Arquitetura da Solução

```
┌─────────────────────────────────────────────────────────────┐
│                    Retail Market Agent                       │
│                   (Agente Supervisor)                        │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┐
        │                         │
┌───────▼──────────┐    ┌────────▼─────────────┐
│ Internet Research│    │  Market Analyst      │
│     Agent        │    │      Agent           │
└───────┬──────────┘    └──────────────────────┘
        │
   ┌────┴────┐
   │         │
┌──▼──┐  ┌──▼──────┐
│Image│  │Web      │
│Tool │  │Search   │
└─────┘  └─────────┘
```

## 🎓 Conceitos Aprendidos

- **Multi-agent Orchestration**: Coordenação entre agentes especializados
- **Vision Models**: Processamento de imagens com IA
- **Tool Creation**: Desenvolvimento de ferramentas customizadas
- **ADK Development**: Ciclo completo de desenvolvimento local
- **REST API Integration**: Integração programática com agentes
- **Event-driven Architecture**: Agentes acionados por eventos

## 📁 Arquivos do Projeto

```
usecases/retail/
├── README.md                          # Visão geral do caso de uso
├── retail.md                          # Laboratório completo (846 linhas)
├── hands-on-lab.md                    # Este arquivo (resumo)
├── src/
│   ├── connections/
│   │   ├── watsonxai.yaml            # Conexão watsonx.ai
│   │   └── tavily.yaml               # Conexão Tavily
│   ├── tools/
│   │   ├── generate_description_from_image.py
│   │   ├── web_search.py
│   │   └── requirements.txt
│   ├── agents/
│   │   ├── internet_research_agent.yaml
│   │   ├── market_analyst_agent.yaml
│   │   └── retail_market_agent.yaml
│   ├── app/
│   │   └── image_listener.py         # Agente headless
│   ├── import-all.sh                 # Script de importação
│   └── set-credentials.sh            # Script de credenciais
└── images/                            # Screenshots do laboratório
```

## 💡 Dicas

1. **Teste Local Primeiro**: Use o ADK para desenvolvimento e testes antes de fazer deploy
2. **Conexões**: Configure as credenciais corretamente antes de importar ferramentas
3. **Modelos**: Experimente diferentes modelos para otimizar performance
4. **Prompts**: Ajuste as instruções dos agentes para melhorar resultados
5. **Logs**: Use `Show reasoning` na UI para debug

## 🔗 Recursos Adicionais

- [watsonx Orchestrate ADK Documentation](https://developer.watson-orchestrate.ibm.com/)
- [Langchain IBM Integration](https://python.langchain.com/api_reference/ibm/index.html)
- [Tavily Search API](https://www.tavily.com/)

## ⚠️ Notas Importantes

- Este laboratório requer conhecimento avançado de Python e Docker
- O ADK deve estar configurado e rodando localmente
- As chaves de API (watsonx.ai e Tavily) devem estar válidas
- O laboratório completo leva aproximadamente 2-3 horas para completar

---

**Para instruções detalhadas e completas, consulte**: [`retail.md`](./retail.md)
