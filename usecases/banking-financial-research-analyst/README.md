# Sumário
- [Sumário](#sumário)
  - [🥇 Agente Analista Financeiro](#-agente-analista-financeiro)
  - [🤔 O Problema](#-o-problema)
  - [🎯 Objetivo](#-objetivo)
  - [📈 Valor para o Negócio](#-valor-para-o-negócio)
  - [🏛️ Arquitetura](#-arquitetura)
  - [📝 Laboratório Prático Passo a Passo](#-laboratório-prático-passo-a-passo)
  - [🎥 Vídeo de Demonstração](#-vídeo-de-demonstração)


## 🥇 Agente Analista Financeiro

![Agente Analista Financeiro](images/blue_aurum_img.png)

## 🤔 O Problema

A <b>Blue Aurum Financial</b> está em busca de expandir e escalar seus investimentos para gerar mais valor aos acionistas. Porém, a equipe de analistas enfrenta dificuldades para identificar novas oportunidades com agilidade, devido ao tempo elevado necessário para pesquisa e análise detalhada dos potenciais investimentos.

Hoje, o processo é majoritariamente manual: os analistas precisam revisar relatórios financeiros das empresas de interesse, compará-los com outras do mesmo setor ou já presentes no portfólio da Blue Aurum. Depois, criam um resumo comparativo, realizam buscas online para obter informações adicionais sobre a empresa, sua equipe de gestão, relatórios recentes de analistas e notícias atuais. Além disso, utilizam ferramentas internas de modelagem financeira para projetar retornos.

<b>Principais desafios enfrentados pelos analistas:</b>

- A pesquisa manual atrasa a identificação de novas oportunidades de investimento.

- O processo exige esforço significativo, envolvendo ferramentas internas, busca por dados públicos e análise de relatórios financeiros.

- A volatilidade do mercado e mudanças no sentimento dos investidores exigem revisões constantes das análises e recomendações.

## 🎯 Objetivo

A <b>Blue Aurum Financial</b> pretende implementar um Agente de Pesquisa Financeira com IA para apoiar sua equipe de analistas, acelerando a pesquisa e identificando oportunidades de investimento de alto valor.
O objetivo é criar uma solução baseada em agentes que ajude os analistas nas seguintes tarefas:

- Analisar relatórios financeiros e gerar comparativos entre empresas do mesmo setor.
  
- Buscar informações externas sobre empresas, equipes de gestão, notícias e relatórios recentes.

- Integrar dados internos com ferramentas de modelagem financeira para projeções de retorno.
  
- Reduzir o tempo de pesquisa manual, oferecendo respostas rápidas e confiáveis.

Ao automatizar essas tarefas, a empresa quer tornar o processo de pesquisa muito mais ágil, acelerando a identificação de novas oportunidades de investimento.

## 📈 Valor para o Negócio

✅  Reduz o tempo gasto em pesquisas manuais, acelerando a identificação de oportunidades.

✅ Mantém os analistas atualizados em tempo real, com notícias, dados de mercado e relatórios de especialistas.

✅  Gera recomendações mais precisas, baseadas em pesquisa automatizada e diligência inteligente.

## 🏛️ Arquitetura

Para agilizar o processo de pesquisa, a Blue Aurum Financial fez parceria com a IBM para desenvolver uma solução de Pesquisa Financeira Multiagente, baseada no [watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate)

A arquitetura abaixo mostra os diferentes agentes de IA envolvidos e as ferramentas utilizadas para executar as tarefas.

Essa arquitetura é composta por agentes especializados, que trabalham de forma colaborativa para desempenhar funções-chave, garantindo eficiência e inteligência no processo.

`Agente de Busca Web`: Responsável por realizar pesquisas na internet e trazer informações atualizadas. Ele utiliza diferentes mecanismos de busca, como DuckDuckGo e Brave, agregando os resultados para entregar respostas completas e coerentes.

`Agente de API Financeira`: Especializado em recuperar informações financeiras. Usa ferramentas como Glossário (para explicar termos) e Dados de Mercado. Neste bootcamp, essa ferramenta demonstra como o agente pode buscar dados de mercado, mas na prática é possível adicionar outras, incluindo APIs internas para modelagem financeira.

`Agente Analista Financeiro`: É o agente orquestrador principal, que responde às consultas dos analistas. Ele é capaz de raciocinar com base na entrada do usuário e decidir a melhor forma de responder. Pode usar uma base de conhecimento interna seguindo o padrão RAG (Geração Aumentada por Recuperação) ou delegar a outro agente para atender melhor à solicitação.

Este sistema aproveita o poder do [watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate), a plataforma da IBM de no-code/low-code/pro-code para soluções com agentes de IA, e do [watsonx.ai](https://www.ibm.com/products/watsonx-ai), a plataforma da IBM para hospedagem de modelos de base como LLMs (Modelos de Linguagem de Grande Escala).

![Arquitetura - Agente Analista Financeiro](images/banking-fra-architecture.png)

------

Neste bootcamp, você vai aprender a usar os recursos do <b>watsonx Orchestrate</b> para criar múltiplos agentes e ferramentas, desenvolvendo um agente de pesquisa financeira capaz de acelerar a análise de investimentos.

Esse agente terá habilidades como:

✅ Interpretar documentos (por exemplo, relatórios de lucros)

✅ Realizar análises comparativas entre empresas

✅ Buscar notícias recentes na web

✅ Recuperar dados de mercado

Tudo isso para ajudar os analistas a encontrar informações relevantes rapidamente e fazer recomendações de investimento com mais confiança.

## 📝 Laboratório Prático Passo a Passo

👉👉👉 [Clique aqui](hands-on-lab-banking.md) para acessar as instruções detalhadas e implementar este caso de uso.

**Tempo estimado**: 60-90 minutos

**Pré-requisitos**:
- Acesso ao watsonx Orchestrate
- Conclusão do guia de configuração de ambiente
- Familiaridade com conceitos financeiros básicos

## 🎥 Demonstração

Veja o vídeo completo que demonstra a solução:

[▶️ Assistir demonstração do Financial Research Analyst](https://bucket-wxo.s3.us-south.cloud-object-storage.appdomain.cloud/Banking%20Financial%20Research%20Analyst.mp4)

---

**Features demonstradas**: `RAG` `Multi-agent orchestration` `Backend connection` `No code`
