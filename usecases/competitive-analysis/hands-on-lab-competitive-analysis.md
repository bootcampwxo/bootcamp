# 👨🏻‍💻 Caso de Uso: Análise Competitiva

## Índice
- [Arquitetura](#-arquitetura)
- [Descrição do Caso de Uso](#descrição-do-caso-de-uso)
- [Pré-requisitos](#pré-requisitos)
- [Visão Geral das Etapas do Lab](#visão-geral-das-etapas-do-lab)
- [Instruções do Laboratório](#instruções-do-laboratório)
  - [Conectar à sua instância do Watsonx Orchestrate](#conectar-à-sua-instância-do-watsonx-orchestrate)
  - [Criar Agente Identificador](#criar-agente-identificador)
  - [Criar Agente de Análise Competitiva](#criar-agente-de-análise-competitiva)
  - [Criar Agente ABC Robots](#criar-agente-abc-robots)
  - [Criar Agente Master](#criar-agente-master)
  - [Experimente os Agentes em Ação](#experimente-os-agentes-em-ação)

## 🏛️ Arquitetura

![Competitive Analysis Architecture drawio](https://github.ibm.com/user-attachments/assets/39d11294-f75d-482d-a94d-80e0511a5aa7)

## Descrição do Caso de Uso

A ABC Robots planeja implementar um Sistema de Inteligência Competitiva alimentado por IA para automatizar pesquisa de mercado e análise de concorrentes. Este sistema ajudará equipes de vendas a rapidamente identificar e posicionar seus produtos contra concorrentes, superando as ineficiências de pesquisa manual e insights desatualizados. O objetivo é criar um sistema habilitado por IA que suporte análise competitiva e pesquisa de mercado através de:

- Extração de produtos do catálogo de produtos da empresa
- Identificação e extração de características-chave de cada produto
- Busca por produtos concorrentes baseada em atributos-chave
- Geração de tabela de comparação competitiva estruturada com preço, características e diferenciais

Ao automatizar essas tarefas, a empresa visa acelerar processos de vendas, melhorar precisão de dados e habilitar equipes de vendas a tomar decisões informadas mais rapidamente.

## Pré-requisitos

**Instrutores:**
- Consulte o [guia do instrutor](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/tree/main/usecase-setup/competitive-analysis) correspondente para configurar todos os ambientes e serviços backend
- Forneça a URL para o servidor MCP deployado

**Participantes:**
- Valide que você tem acesso ao ambiente TechZone correto para este laboratório
- Complete o guia de [configuração de ambiente](../../environment-setup) para passos sobre criação de chave de API e configuração de projeto
- Certifique-se de que o instrutor forneceu a URL para conectar ao servidor MCP
- Certifique-se de que seu instrutor forneceu o arquivo `Vaccum_cleaners_v2.docx` para ser carregado como conhecimento
- Certifique-se de que seu instrutor forneceu o arquivo `abc-robots-website-final.zip` para incorporar seu chat em um website
- Certifique-se de que seu instrutor forneceu todas as credenciais necessárias

## Visão Geral das Etapas do Lab

1. Conectar ao watsonx Orchestrate
2. Criar o Agente Identificador - usa ferramenta MCP extract_from_image
3. Criar o Agente de Análise Competitiva - usa ferramenta MCP search_and_review_high_rated_products
4. Criar o Agente ABC Robots - agente RAG
5. Criar o Agente Master - agente orquestrador

Vamos começar.

## Instruções do Laboratório

### Conectar à sua instância do Watsonx Orchestrate

1. Faça login no IBM Cloud (cloud.ibm.com). Navegue até o menu hambúrguer no canto superior esquerdo, depois para **Resource List**. Abra a seção **AI/Machine Learning**. Você deve ver um serviço **watsonx Orchestrate**. Clique para abri-lo.

   ![Watsonx Orchestrate service](./assets/i1.png)

2. Clique no botão **Launch watsonx Orchestrate**:

   ![Launch Watsonx Orchestrate](./assets/i2.png)

### Criar Agente Identificador

O Agente Identificador reconhece um produto a partir de uma imagem. Ele depende de um serviço pré-deployado em um servidor MCP que invoca um modelo multi-modal hospedado no watsonx.ai para reconhecimento de imagem. Vamos integrar este serviço em um agente do watsonx Orchestrate.

> [!TIP]
> Um servidor MCP é um deployment ativo de uma implementação do Model Context Protocol (MCP), que fornece acesso padronizado a ferramentas externas, dados e serviços de forma segura e consistente.

1. Vá para a página inicial do watsonx Orchestrate, clique no menu hambúrguer (☰), selecione **Build** e depois **Agent Builder**.

   ![Agent Builder](assets/BAP_1.png)

2. Clique no botão **Create agent**.

   ![Create Agent](assets/BAP_2.png)

3. Selecione **Create from scratch**, adicione as seguintes informações:
   
   **Name**:
   ```
   Identifier Agent
   ```
   **Description**:
   ```
   This agent will extract the brand name and product name from the image.
   ```

   Clique no botão **Create**.

   ![Create from scratch](assets/id_create.png)

4. Vá para a seção **Toolset** e clique em **Add tool**:

   ![Add tool](assets/id_tool.png)

5. Selecione **Add from file or MCP server**:

   ![Add MCP Server](assets/id_add_mcp.png)

6. Selecione **Import from MCP server**:

   ![Import from MCP Server](assets/id_import_mcp.png)

7. Na janela **Import or remove tools from MCP server**, clique em **Add MCP server**:

   ![Add MCP Server](assets/id_add_mcp_button.png)

8. Na janela **Add MCP server**, adicione os seguintes parâmetros e depois clique em **Connect**:

   - Server Name:
     ```
     mcp-competitive-tools
     ```
   - Obtenha a URL do servidor MCP do seu instrutor e preencha no comando Install da seguinte forma:
     ```
     uvx mcp-proxy [MCP-SERVER-URL]/sse
     ```
     > ex: `uvx mcp-proxy https://remote-mcp-tools.20sp7brq6u6i.us-south.codeengine.appdomain.cloud/sse`

   ![Server Details](assets/id_server_details.png)

9. Você deve ver uma mensagem `Connection successful` abaixo. Clique em **Done**:

   ![Connection Successful](assets/id_connect.png)

10. Na janela **Import or remove tools from MCP server**, ative o toggle da ferramenta `extract_from_image` para **On** e depois feche a janela.

    ![Toogle tool](assets/id_image_toggle.png)

11. Agora vamos definir o que o agente deve fazer na seção **Behavior**. Vamos ser específicos em termos do formato que queremos obter do agente de reconhecimento de imagem. Experimente as seguintes **Instructions**:

    ```
    I will share an image URL. Please use the extract_from_image tool to parse the content. From the extracted text or context, identify the exact product name and brand name from the reference image. This information will be used by the Competitive Analysis Agent.

    Return the result in this format:

    Brand Name :
   
    Product Name:
    ```
    ![Behavior](assets/id_behavior.png)

12. Vamos testar o agente imediatamente carregando a seguinte imagem. Passaremos a URL correspondente para o agente reconhecer o produto:

    <img src="https://m.media-amazon.com/images/I/613mvDKX1hL._AC_SL1500_.jpg" width="400">

13. Digite a seguinte query no chat do lado direito na janela **Preview**:

    ```
    Tell me what product is in this image https://m.media-amazon.com/images/I/613mvDKX1hL._AC_SL1500_.jpg
    ```
   
    ![Behavior](assets/id_test.png)

14. Agora você pode deployar o agente. Clique no botão **Deploy** e depois em **Deploy** novamente na janela **Pre-deployment summary**:

    ![Deploy](assets/id_deploy.png)
    ![Deploy](assets/id_deploy_2.png)

    Você verá agora que seu agente está **Live** e você pode conversar com ele diretamente. Demonstraremos isso mais tarde no laboratório.

    ![Deploy](assets/id_live.png)

### Criar Agente de Análise Competitiva

Agora, vamos criar o Agente de Análise Competitiva. Este permite obter informações de produtos no mercado usando APIs do Google Search e Google Shopping.

Usamos o SerpAPI para invocar esses serviços e depois os expusemos como ferramentas no servidor MCP para invocação mais fácil do Agente no watsonx Orchestrate.

1. Clique no link **Manage Agents** no menu breadcrumb no canto superior esquerdo.

   ![Manage Agent](assets/id_manage_agent.png)

2. Selecione o botão **Create agent**.

   ![Create Agent](assets/comp_create.png)

3. Selecione **Create from scratch**.
   
   **Name**:
   ```
   Comp Analysis Agent
   ```
   **Description**:
   ```
   Provides elaborate, very detailed analysis using a tool.
   ```

   Clique no botão **Create**.

4. Configure o modelo para `llama-3-405b-instruct`. Este modelo é mais apropriado para lidar com queries do que o de visão.

   ![Create from scratch](assets/comp_model.png)

5. Vá para a seção **Toolset** e clique no botão **Add tool**.

   ![Add tool](assets/comp_tool.png)

6. Selecione **Add from file or MCP server**.

   ![Add MCP Server](assets/comp_add_mcp.png)

7. Selecione **Import from MCP server**.

   ![Import MCP Server](assets/comp_import_mcp.png)

8. Como conectamos o servidor MCP nas etapas do Agente anterior, você agora terá a opção de escolher seu servidor MCP. Na janela **Import or remove tools from MCP server**, escolha o dropdown **Select MCP server** e selecione o servidor `mcp-competitive-tools`.

   ![Select MCP Server](assets/comp_select_mcp.png)

9. Uma vez que as ferramentas disponíveis sejam exibidas, ative o toggle da ferramenta `search_and_review_high_rated_products` para **On** e depois feche a janela.

   ![Toogle tool](assets/comp_search_toggle.png)

10. Na seção **Behavior**, adicione o seguinte ao campo de texto **Instructions**:

    ```
    When given a product name, use the search_and_review_high_rated_products tool to retrieve the content for the user's query.
    ```
    ![Behavior](assets/comp_behavior.png)

11. Agora você pode testar seu agente. Adicione a seguinte query na caixa de entrada de texto no canto inferior direito da janela **Preview**:

    ```
    Give me details of the Dreame L10 Pro.
    ```

12. Clique no botão **Deploy** no canto superior direito para deployar o agente no ambiente live. Clique no botão **Deploy** novamente na janela **Pre-deployment summary**.

    ![Deploy](assets/comp_deploy_2.png)

    Você verá agora que seu agente está **Live** e você pode conversar com ele diretamente.

    ![Live](assets/comp_live.png)

### Criar Agente ABC Robots

Este agente extrairá informações do catálogo de produtos da ABC Robots. Na vida real, informações de produtos podem estar em um banco de dados ou outro tipo de repositório empresarial. Para simplicidade, faremos upload de um PDF com o catálogo de produtos. Os seguintes produtos estão no catálogo:

<br>
<br>

<img width="1187" alt="Screenshot 2025-10-01 at 10 58 12 AM" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/37dbc688-a5b7-4835-8564-07637ea5a57b">

<br>
<br>

1. Clique no link **Manage Agents** no menu breadcrumb no canto superior esquerdo.

   ![Manage Agent](assets/comp_manage.png)

2. Selecione o botão **Create agent**.

   ![Create Agent](assets/abc_create_agent.png)

3. Selecione **Create from scratch**.
   
   **Name**:
   ```
   ABC Robots Agent
   ```
   **Description**:
   ```
   This agent will answer questions using the uploaded knowledge base. Always interpret the user's input as a query to the knowledge base. The user will ask queries related to robotic vacuum cleaners only as the knowledge base contains that information.
   ```

   Clique no botão **Create**.

4. Na seção **Knowledge Source**, clique no botão **Choose knowledge**.

   ![Knowledge](assets/abc_knowledge.png)

5. Após clicar no botão **Choose knowledge**, uma janela pop-up aparecerá. Selecione **Upload files** e depois clique em **Next**.

   ![Knowledge](assets/abc_upload.png)

6. Faça upload do documento fornecido [Vacuum_cleaners_v2.docx](assets/Vaccum_cleaners_v2.docx) e clique no botão **Next**.

   ![Knowledge](assets/abc_file_upload.png)

7. Adicione a descrição abaixo no campo **Description** e depois clique em **Save**.

   **Description:**
   ```
   This knowledge document contains all the product-related information for ABC Robots. All queries related to the product will be addressed using this document as the primary source.
   ```
   ![Knowledge](assets/abc_knowledge_source.png)

8. Após completar todos os passos acima, sua fonte de conhecimento será adicionada e aparecerá como mostrado na imagem abaixo.

   ![Upload file](assets/abc_knowledge_results.png)

9. Clique no botão **Edit Knowledge Settings** e mude o **Response** para **Dynamic (Preview)** e o **Maximum Search Results** para 10, depois clique no botão **Save**.

   ![settings](assets/abc_knowledge_settings.png)

10. Na seção **Behavior**, adicione o seguinte ao campo de texto **Instructions**:

    ```
    Specs query → Structured summary of that product from KB (exact text, no paraphrasing).
    Comparison query → Generate a side-by-side comparison from KB. Each distinct function, feature, or specification must be presented as a separate row in the table (e.g., individual rows for "Cleaning Modes", "Battery Life", "Navigation System", "Dustbin Capacity", etc.). Do not consolidate multiple features into grouped rows like "Core Functions" or "Main Features".
    Competitive analysis vs KB → Compare a given product (if in KB) vs all KB products.
    No relevant data → Output strictly:
    
    The information required cannot be found in the current knowledge base. Please upload the relevant data in a supported format (e.g., CSV, TSV, or text document).
    ```
    ![Upload file](assets/abc_behavior.png)

11. Agora você pode testar seu agente. Faça perguntas sobre produtos ABC robots, ou informações específicas para qualquer produto.

    ```
    Give me the list of products for ABC robots
    ```

    ```
    Give me information for the Nimbus S7
    ```

12. Clique no botão **Deploy** no canto superior direito para deployar o agente no ambiente live. Clique no botão **Deploy** novamente na janela **Pre-deployment summary**:

    ![Deploy](assets/abc_deploy_2.png)

    Você verá agora que seu agente está **Live** e você pode conversar com ele diretamente.

### Criar Agente Master

1. Clique no link **Manage Agents** no menu breadcrumb no canto superior esquerdo.

2. Selecione o botão **Create agent**.

3. Selecione **Create from scratch**.
   
   **Name**:
   ```
   Master Agent
   ```
   **Description**:
   ```
   You are an intelligent assistant; you have the capability of choosing agents based on the user's request. Ensure to follow the behavior strictly.
   ```

   Clique no botão **Create**.

   ![Create from scratch](assets/master_create_agent.png)

4. Configure o modelo para `llama-3-405b-instruct`.

   ![Model](assets/master_model.png)

5. Na seção **Agents**, clique no botão **Add agent**.

   ![Add Agent](./assets/master_add_agent.png)

6. Clique em **Add from local instance**.

   ![Add Agent](./assets/master_add_local.png)

7. Selecione o **ABC Robots Agent**, o **Comp Analysis Agent** e o **Identifier Agent**, depois clique no botão **Add to Agent**.

   ![Add Agents](./assets/master_add_agents.png)

8. Na seção **Behavior**, adicione o seguinte ao campo de texto **Instructions**:

    ```
    The Master Agent does not answer queries directly. Its only responsibility is to route queries to the appropriate specialised agents, manage state between interactions, and ensure downstream queries are context-aware.
    Routing Rules
    Image-based Product Identification:
    If a user query contains an image or explicitly asks "Tell me what product is in the image," route the query to the Identifier Agent.
    After the response is received from the Identifier Agent, display the brand name and model name and ask the user - "Would you like me to pull information for this product?".
    If the user answers "Yes," provide the output from the Identifier Agent to the comp-analysis-ag and, from the response received, analyze and understand the response to provide a detailed and very long answer, divided into specifications, features, and reviews only. Ensure there is no none response in the headers.
    Customer Perception Summary:
    If a user queries "Give me the summary of how this product is perceived by customers, broken down into good and bad," then provide a detailed breakdown of reviews divided into good and bad from the response already received from comp-analysis-ag.
    Competitive Analysis against Knowledge Base:
    If a user queries "Do a competitive analysis of this product against the knowledge base," then a detailed comparison needs to be done between the response already received from comp-analysis-ag and the knowledge base from ABC Robots (all the products). Extract all information from the knowledge base and compare all features, price, and ratings against comp-analysis-ag. Understand and analyze, then provide that response in a detailed and long tabular manner. Decide on columns nicely for its table, making sure all comparisons are under one table.
    Product-specific Queries (ABC Robots):
    If a user queries "Give me a comparison between Aerowash X1 and Nimbus S7," or "Give me the specifications of Aerowash X1," "Give me the products of ABC robots" (in products of ABC, just provide a list of products and the table should be nicely proportionate), or similar queries like this with other product names too, then redirect it to ABC Robots.
    Display features, pricing, or any other relevant detailed answers along with their respective sub-headings in a detailed and a long tabular manner vertically.
    The answer should start with "Based on the knowledge base, here is the comparison between HydraClean V9 and Nimbus S7" (or relevant products), in a tabular format vertically only for other products too. Analyze the products and then provide columns and their rows of comparison nicely.
    At the end, give your detailed and a long comparison analysis too after the tabular comparison.
    Competitive Analysis with Top Competitors:
    If a user queries "Give me a competitive analysis of HydraClean v9 and the top competitors in the market" (there can be any product instead of HydraClean v9), route the query to comp-analysis-ag and pass this query "HydraClean v9 and top competitors in the market" only.
    Once a response is received, understand and analyze it, and provide a new tabular response (decide on columns and rows smartly). In the end, give your detailed analysis.
    ```

9. Clique no botão **Deploy** no canto superior direito para deployar o agente no ambiente live:

   ![Steps](assets/master_deploy.png)

10. Clique no botão **Deploy** novamente na janela **Pre-deployment summary**:

    ![Deploy](assets/master_deploy_agent.png)

    Você verá agora que seu agente está **Live** e você pode conversar com ele diretamente.

### Experimente os Agentes em Ação

Siga os passos acima e depois tente interagir com o caso de uso usando estas queries de exemplo:

1. Vá para o menu hambúrguer e selecione **Chat**.

   ![chat](assets/chat.png)

2. Selecione o **Master Agent** do menu dropdown, e você estará pronto para começar.

   ![Master Agent](assets/chat_master.png)

3. Faça as seguintes queries que devem ser roteadas para o ABC Robots Agent:

   ```
   Show me the list of products by ABC robots
   ```
   ![ABC Agent Response](assets/chat_q1.png)

   ```
   Give me the specifications of Aerowash X1
   ```
   ![ABC Agent Response](assets/chat_q2.png)

   ```
   Give me a comparison table between Aerowash X1 and HydraClean v9 broken down into individual features
   ```

   <img width="684" alt="Screenshot 2025-10-04 at 11 21 08 AM" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/1555eefe-73fb-4812-94b7-452bc8e22123">

### Agora clique no ícone azul para criar um Novo Chat e iniciar uma nova conversa:

![New Chat Image](assets/image41.png)

4. Para identificar informações de produto a partir de uma imagem, pergunte:

   ```
   Tell me what product is in this image https://m.media-amazon.com/images/I/613mvDKX1hL._AC_SL1500_.jpg
   ```
   
   Você será perguntado "Would you like me to pull information for this model?". Responda com `yes`:
   
   ![Comparison Agent Response](assets/chat_q5.png)

5. Para fazer alguma análise competitiva, experimente estes prompts:

   ```
   Give me the specifications of the product in the image
   ```

   ```
   Give me a summary of how this product is perceived by customers
   ```
   ![ABC Agent Response](assets/chat_q7.png)

   ```
   Give me a competitive analysis of the product in the image against each of the products in the catalog for ABC robots. Break it down by individual features in a table. Include Laundry and Dishwashing as well. Put it all together into a single table.
   ```

   <img width="685" alt="Screenshot 2025-10-04 at 11 26 16 AM" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/cdde7a14-cd88-4f2a-bdcd-7c8869d9ee53">

## Deployment

Agora você vai deployar este chat no website interno da ABC Robots para que os funcionários da ABC Robots possam realizar análise competitiva.

1. Vá para **Manage Agents** e depois para seu Master Agent.

2. Role para baixo até **Channels** e clique em **Embedded Agent**.

   <img width="700" alt="embedding" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/0a57a2ec-53ee-4266-bb4d-4fefd5bafd48">

3. Copie o código clicando no botão **Copy to Clipboard** no canto superior direito do bloco de código que começa com `<script>`.

4. Extraia o arquivo ZIP do website ABC Robots fornecido pelo seu instrutor.

5. Edite o arquivo **index.html** usando seu editor de texto favorito ou ferramenta de desenvolvimento.

   <img width="700" alt="deployment-code" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/f2d323bc-f693-4d83-a8f2-71bd485de941">

6. Role até o final e cole-o logo antes da tag `</body>`.

7. Salve suas mudanças e abra o arquivo **index.html** com seu navegador. Você verá algo assim:

   <img width="700" alt="robots-website" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/0a9dc956-5898-4ce1-89cd-6600d869d508">

Clique no ícone do watsonx Orchestrate no canto inferior direito e comece a conversar com seu agente.
