# Adicionando Agentes Externos

## Visão Geral

Este guia de laboratório orienta você no processo de integração de agentes externos ao seu ambiente watsonx Orchestrate. Você aprenderá como conectar um agente LangGraph de terceiros que realiza buscas no Google, criar um agente orquestrador mestre para rotear consultas de forma inteligente e testar o sistema multi-agente completo. Ao final deste laboratório, você terá um assistente de compra de carros totalmente funcional que combina informações do catálogo com pesquisa web em tempo real.

> [!NOTE]
> **Pré-requisito:** Este laboratório assume que você já completou o laboratório **Data Poisoning** e criou o **Dealership Support Agent** com a base de conhecimento do catálogo de veículos. O agente criado naquele laboratório será usado aqui como o agente de pesquisa do catálogo (Car Research Agent).

## Índice

- [Adicionando Agentes Externos](#adicionando-agentes-externos)
  - [Visão Geral](#visão-geral)
  - [Índice](#índice)
- [Adicionando Agentes Externos](#adicionando-agentes-externos-1)
    - [Parte 1: Conectar Agente de Busca Google de Terceiros](#parte-1-conectar-agente-de-busca-google-de-terceiros)
    - [Parte 2: Criar Agente Mestre de Compra de Carros](#parte-2-criar-agente-mestre-de-compra-de-carros)
    - [Parte 3: Testar Seus Agentes](#parte-3-testar-seus-agentes)

---

# Adicionando Agentes Externos

### Parte 1: Conectar Agente de Busca Google de Terceiros

Agora vamos conectar o agente LangGraph externo que realiza buscas no Google por informações sobre carros, avaliações e dados de mercado.

> [!TIP]
> Este agente usa o protocolo Agent-to-Agent (A2A) para se comunicar com o watsonx Orchestrate. O instrutor já implantou este agente para você.

1. Clique no link **Manage Agents** no menu breadcrumb no canto superior esquerdo.


2. Clique no botão **Create agent**.

   ![Create agent](../agentic-monitoring/assets/google_search_create.png)

3. Selecione **Create from scratch**.
   
   **Name**:
   ```
   Google Search Agent
   ```
   
   **Description**:
   ```
   This agent searches Google for real-time information such as user reviews, ratings, and market comparisons, but only for cars that are in our catalog. It should not provide information for vehicles not sold by our dealership.
   ```
   > *Este agente pesquisa no Google informações em tempo real, como avaliações de usuários, classificações e comparações de mercado, mas apenas para carros que estão em nosso catálogo. Não deve fornecer informações sobre veículos não vendidos pela nossa concessionária.*

   > [!NOTE]
   > O **Name** e a **Description** do agente são mantidos em inglês. Eles são usados pelo agente mestre para tomar decisões de roteamento — manter em inglês garante consistência e precisão na orquestração multi-agente.

   Clique no botão **Create**.

   ![Create search agent](../agentic-monitoring/assets/google_search_create_agent.png)

4. Na seção **Agents**, clique no botão **Add agent**.

   ![Add agent](../agentic-monitoring/assets/google_search_add_agent.png)

5. Clique em **Import** e depois em **Add from external source**.

   ![Import agent](../agentic-monitoring/assets/google_search_import_agent.png)

   ![Add external](../agentic-monitoring/assets/google_search_add_external.png)

6. Selecione **External agent via A2A standard**.

7. Preencha os detalhes de conexão fornecidos pelo seu instrutor:

   **Endpoint URL**: (Obtenha do instrutor)

   **Authentication Type**: Selecione **API Key**

   **API Key Value**: (Obtenha do instrutor)

   ![A2A configuration](../agentic-monitoring/assets/google_search_a2a_config.png)

   Role para baixo até a seção **Define new agent** e preencha os detalhes:

   **Name**:
   ```
   Web Search Agent
   ```

   **Description**:
   ```
   This agent connects to the Tavily service to perform a web search and return the top results.
   ```
   > *Este agente se conecta ao serviço Tavily para realizar uma busca na web e retornar os principais resultados.*

   > [!NOTE]
   > O **Name** e a **Description** do agente importado são mantidos em inglês, pois identificam o agente dentro do sistema multi-agente.

   ![Define new agent](../agentic-monitoring/assets/google_search_define_agent.png)

   Então clique em "Import Agent"

8. Na seção **Behavior**, adicione as seguintes instruções:

    ```
    You are a car research specialist with access to real-time Google Search. You may use Google Search only for cars that are in our catalog.

    1. User reviews and ratings for cars in our catalog: Search for owner experiences, common complaints, and satisfaction ratings.

    2. Market comparisons for cars in our catalog: Find competitive information and industry reviews when the question is about one of our catalog vehicles.

    3. Latest information for cars in our catalog: Search for recent news, recalls, or updates about specific catalog models.

    4. The vehicles in the catalog are: Nissan Versa, Hyundai Kona Electric, Alfa Romeo Spider, Porsche 911 Carrera GTS, and Kia Nero. If the user asks about a vehicle that is not in our catalog, do not search the web. Respond with:
    "I'm sorry, our dealership does not sell that car, so I can't provide information on that vehicle."

    Always provide the source URLs for the information you find. Format search results clearly with:
    - Title of the source
    - Key information or summary
    - Source URL

    If search returns no results for a catalog vehicle, inform the user and suggest alternative search terms.
    ```

    ![Search agent behavior](../agentic-monitoring/assets/google_search_behavior.png)

9. Teste o agente com estas consultas:

    ```
    O que os proprietários dizem sobre o Porsche 911?
    ```

    ```
    Encontre avaliações de usuários para o Toyota Camry
    ```

    ![Test search agent](../agentic-monitoring/assets/google_test_porsche.png)
    ![Test search agent](../agentic-monitoring/assets/google_test_camry.png)



### Parte 2: Criar Agente Mestre de Compra de Carros

Agora vamos criar um agente orquestrador que roteia consultas de forma inteligente para o agente especializado apropriado.

1. Clique em **Manage Agents** e depois em **Create agent**.

   ![Create Agent](../agentic-monitoring/assets/comp_create.png)

   Clique no botão **Create from scratch**.

   ![Create from scratch](../agentic-monitoring/assets/comp_create_from_scratch.png)


2. Digite os seguintes detalhes

   **Name**:
   ```
   Master Car Buying Agent
   ```
   
   **Description**:
   ```
   Intelligent car buying assistant that routes queries to specialized agents. Provides comprehensive information from both our catalog and external market research.
   ```
   > *Assistente inteligente de compra de carros que roteia consultas para agentes especializados. Fornece informações abrangentes tanto do nosso catálogo quanto de pesquisas externas de mercado.*

   > [!NOTE]
   > O **Name** e a **Description** do agente mestre são mantidos em inglês. As instruções de **Behavior** também permanecem em inglês para garantir que a lógica de roteamento funcione de forma confiável.

   Clique no botão **Create**.

   ![Create master agent](../agentic-monitoring/assets/master_create_agent.png)

3. Na seção **Agents**, clique no botão **Add agent**.

   ![Add agents](../agentic-monitoring/assets/master_add_agent.png)

4. Clique em **Add from local instance**.

   ![Add local](../agentic-monitoring/assets/master_add_local.png)

5. Selecione tanto o **Dealership Support Agent** (criado no laboratório de Data Poisoning — este é o agente de pesquisa do catálogo de carros) quanto o **Google Search Agent** (criado na Parte 1 acima), depois clique em **Add to Agent**.

   > [!NOTE]
   > O **Dealership Support Agent** foi criado no laboratório anterior (Data Poisoning) e possui a base de conhecimento com o catálogo de veículos da ABC Dealership. Ele atuará como o agente especializado em pesquisa do catálogo neste sistema multi-agente.

   ![Select agents](../agentic-monitoring/assets/master_add_agents.png)

6. Na seção **Behavior**, adicione a seguinte lógica de roteamento:

    ```
    You are the Master Car Buying Assistant. Your role is to route user queries to the appropriate specialized agent and synthesize responses.

    ROUTING RULES:

    1. CATALOG QUERIES → Dealership Support Agent
       - "Show me your sedans/SUVs/trucks"
       - "What's the price of [car in catalog]?"
       - "Compare [catalog car] and [catalog car]"
       - "Give me specifications for [catalog car]"
       - Any query about cars in our inventory

    2. EXTERNAL RESEARCH → Google Search Agent
       - "What do owners say about [catalog car]?"
       - "Find reviews for [catalog car]"
       - "Are there any recent recalls for [catalog car]?"
       - "What are reviewers saying about [catalog car]?"
       - Any query requiring market research or user reviews for a car in our catalog

    3. HYBRID QUERIES → Both Agents
       - "How does [our catalog car] compare to market leaders?"
       - "What do reviewers say about [our catalog car], and what are its specs?"
       - First get catalog info, then get market research for that same catalog car, then synthesize

    4. NON-CATALOG CARS → Do not use Google Search Agent
       - If the user asks about a car that is not in our catalog, do not answer with generated details and do not search the web.
       - Respond with: "I'm sorry, our dealership does not sell that car, so I can't provide information on that vehicle."

    RESPONSE GUIDELINES:
    - The vehicles in the catalog are: Nissan Versa, Hyundai Kona Electric, Alfa Romeo Spider, Porsche 911 Carrera GTS, and Kia Nero.
    - Always determine whether the vehicle is in our catalog before routing
    - Only use Dealership Support Agent and Google Search Agent for cars in our catalog
    - Always identify which agent(s) you're using
    - For comparisons, create clear tables with all relevant features
    - Cite sources for external information
    - If a query is ambiguous, ask for clarification
    - Do not speculate about vehicles outside our catalog
    - Provide comprehensive, helpful responses for supported vehicles
    

    
![Master behavior](../agentic-monitoring/assets/master_behavior.png)

7. Teste o agente mestre com várias consultas:

    ```
    Compare o Kia Nero com o Hyundai Kona Electric
    ```

    ```
    As avaliações dos proprietários são mais positivas para o Alfa Romeo Spider ou para o Porsche 911?
    ```

    ```
    Mostre-me avaliações de usuários para o Tesla Model Y
    ```


    ![Test master agent](../agentic-monitoring/assets/test_master_compare.png)
    ![Test master agent](../agentic-monitoring/assets/test_master_reviews.png)
    ![Test master agent](../agentic-monitoring/assets/test_master_tesla.png)



8. Clique em **Deploy** para tornar o agente ativo.

    ![Deploy master](../agentic-monitoring/assets/master_deploy.png)
    ![Deploy](../agentic-monitoring/assets/master_deploy_agent.png)

    Seu agente agora está **Live**!

9. Clique em **Activate agent monitoring** quando solicitado.

    ![Activate monitoring](../agentic-monitoring/assets/activate_monitoring.png)

### Parte 3: Testar Seus Agentes

Agora vamos testar o sistema completo através da interface de chat.

1. Clique em **IBM watsonx Orchestrate** no canto superior esquerdo da sua janela.


2. Selecione o **Master Car Buying Agent** no menu dropdown.

   ![Select master](../agentic-monitoring/assets/chat_master.png)

3. Experimente estes cenários de teste abrangentes:

   **Cenário 1: Pesquisa de Catálogo**
   ```
   Mostre-me todos os veículos elétricos do catálogo
   ```
   ![test all](../agentic-monitoring/assets/test_scenario1.png)

   **Cenário 2: Pesquisa Externa**
   ```
   O que os proprietários dizem sobre o Nissan Versa?
   ```
   ![test all](../agentic-monitoring/assets/test_scenario2a.png)
   
   ```
   O que os proprietários dizem sobre o BMW X5 2024?
   ```

   ![test all](../agentic-monitoring/assets/test_scenario2b.png)


   **Cenário 3: Consulta Híbrida Catálogo + Avaliação**
   ```
   O que os avaliadores dizem sobre o Porsche 911 e quais são suas especificações principais?
   ```
   ![test all](../agentic-monitoring/assets/test_scenario3.png)

   **Cenário 4: Consulta Complexa**
   ```
   Estou procurando um SUV familiar abaixo de $40.000 com bom consumo de combustível. O que você recomenda do catálogo e como eles se comparam aos líderes de mercado?
   ```
   ![test all](../agentic-monitoring/assets/test_scenario4.png)

-----

<b>➜</b> ![Clique aqui para acessar o próximo laboratório - Proteja Contra Vazamento de PII com Controles no watsonx Orchestrate]([https://github.com/bootcampwxo/bootcamp/blob/main/usecases/acp/lab_guides/4_adding_external_agents.md](https://github.com/bootcampwxo/bootcamp/blob/main/usecases/acp/controls/README.md)))
