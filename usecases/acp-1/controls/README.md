# 🪪 Laboratório Prático: Proteja Contra Vazamento de PII com Controles no watsonx Orchestrate

## Índice
- [🪪 Laboratório Prático: Proteja Contra Vazamento de PII com Controles no watsonx Orchestrate](#-laboratório-prático-proteja-contra-vazamento-de-pii-com-controles-no-watsonx-orchestrate)
  - [Índice](#índice)
  - [Visão Geral](#visão-geral)
  - [Pré-requisitos](#pré-requisitos)
  - [Descrição do Caso de Uso](#descrição-do-caso-de-uso)
    - [O Cenário:](#o-cenário)
    - [Sua Missão:](#sua-missão)
  - [O que é PII (Personal Identifiable Information)?](#o-que-é-pii-personal-identifiable-information)
  - [Instruções do Laboratório](#instruções-do-laboratório)
    - [Parte 1: Iniciar watsonx Orchestrate para ver o Control Plane](#parte-1-iniciar-watsonx-orchestrate-para-ver-o-control-plane)
    - [Parte 2: Explorar as configurações de Controle](#parte-2-explorar-as-configurações-de-controle)
    - [Parte 3: Criar seu agente](#parte-3-criar-seu-agente)
    - [Parte 4: Testando sem Asset Controls](#parte-4-testando-sem-asset-controls)
    - [Parte 5: Criar Controles para Filtragem de PII](#parte-5-criar-controles-para-filtragem-de-pii)
    - [Parte 6: Testando com Asset Controls](#parte-6-testando-com-asset-controls)
  - [O que vem a seguir?](#o-que-vem-a-seguir)
    - [🎉 Parabéns!](#-parabéns)

## Visão Geral
Este laboratório prático ensina como proteger agentes de IA contra vazamento de PII usando controles no watsonx Orchestrate. Você aprenderá como identificar dados PII e como implementar proteções.

## Pré-requisitos
Este laboratório requer um arquivo de dados de amostra que contém informações sensíveis falsas do gerente da loja para simular vazamento de PII. O arquivo de dados de amostra está disponível em [sample-data/PII_information.pdf](sample-data/PII_information.pdf).

## Descrição do Caso de Uso
Você está construindo um Dealership Support Agent que suporta ciclos de vendas para a Concessionária ABC. Ele roteia consultas de usuários para o agente de busca web. Sua base de conhecimento contém registros de funcionários (incluindo PII sensível). Após alguns testes, você descobre que o agente está vazando dados PII para o usuário. Você deve prevenir que seu agente vaze informações sensíveis de funcionários!

### O Cenário:
Um usuário suspeito faz várias consultas que levam a comportamento problemático do chatbot e podem potencialmente vazar dados PII excessivos. O agente tenta ser "útil" e compartilha demais. Sem filtragem de PII, o agente não tem controle de acesso aplicado e responde de acordo com seu conhecimento interno.

### Sua Missão:
* Implantar o agente vulnerável e observar o vazamento
* Implementar controles para prevenir vazamento futuro de PII

## O que é PII (Personal Identifiable Information)?
**PII** (Personal Identifiable Information) são quaisquer dados que podem ser usados para identificar um indivíduo. Alguns exemplos de PII são os seguintes:
* Nome
* Endereço de Email
* Número de Telefone
* SSN (Social Security Number)
* Endereço
* Detalhes de cartão de crédito

> [!Note]
> Se os dados podem ser usados para identificar uma pessoa, então são considerados PII.


## Instruções do Laboratório
### Parte 1: Iniciar watsonx Orchestrate para ver o Control Plane

1. Acesse o **control plane** [aqui](https://ap-south-1.dl.watson-orchestrate.ibm.com/home).

![homepage](assets/control_plane_homepage.png)

2. Clique no menu hambúrguer no canto superior esquerdo e depois clique em **Manage &rarr; Control**.

![menu](assets/control_plane_hamburger_menu.png)

### Parte 2: Explorar as configurações de Controle

Note que existem duas configurações de Controle: **Asset Controls** e **Enterprise Controls**.
1. **Asset Controls**: configure e aplique controles para agentes já existentes.
Nota: Para este laboratório prático, focaremos em Asset Controls.
![asset](assets/asset_controls.png)
   
2. **Enterprise Controls** (aba Analytics): configure mascaramento global de PII (duas opções: *Selective PII Masking* e *Full redaction*)

![enterprise](assets/enterprise_controls_analytics.png)

### Parte 3: Criar seu agente
1. Clique no menu hambúrguer no canto superior esquerdo e depois clique em **Build &rarr; Create agent**.

![create agent](assets/build_agents_page.png)

2. Escolha **Create from scratch**

![create from scratch](assets/create_agent_from_scratch.png)

3. Digite os seguintes detalhes na próxima tela.

   Name:
   ```
   Test Dealership Support Agent
   ```
   Description:
   ```
   This agent supports sales cycles for ABC Dealership. You must route all user queries to the web search agent.
   ```
   > *Este agente suporta ciclos de vendas para a Concessionária ABC. Você deve rotear todas as consultas dos usuários para o agente de busca web.*

   > [!NOTE]
   > O **Name** e a **Description** do agente são mantidos em inglês para garantir consistência no sistema multi-agente e melhor interpretação pelo LLM. Os prompts de teste podem ser enviados em português.

*Após inserir as informações de descrição, clique em Create.*   
![agent description](assets/create_an_agent.png)

*De volta à homepage após adicionar com sucesso o Web Search Agent.*
![agent homepage](assets/test_dealership_support_agent_homepage.png)

4. Role para baixo até **Toolset** e adicione o **agente externo** local `Web Search Agent` para realizar busca web.

   > [!NOTE]
   > O agente a ser adicionado aqui é o **Web Search Agent** criado no laboratório **Importando Agentes Externos** (Lab 3). Procure pelo nome **"Web Search Agent"** na lista de agentes locais.

*Clique em add agent e escolha local instance.*
![add local agent](assets/add_agent_local_instance.png)

*Procure por "Web Search Agent" e selecione add to agent.*
![add local agent](assets/add_web_search_agent.png)

6. Agora, vamos adicionar nossa **fonte de conhecimento**.
Primeiro, use o arquivo de amostra [**PII_Information**](sample-data/PII_information.pdf) (mesmo arquivo dos pré-requisitos) da pasta sample-data que contém o perfil do gerente da loja e faça upload para a base de conhecimento.

Então, role para cima até a aba **Knowledge** e clique para adicionar **New Knowledge**.

*Clique em local knowledge. Depois clique em next.*
![add_knowledge_step_1](assets/add_knowledge_step_1.png)

*Clique em upload files. Depois clique em next.*
![add_knowledge_step_2](assets/add_knowledge_step_2.png)

*Faça upload do arquivo "PII Information" baixado. Depois clique em next.*
![add_knowledge_step_3](assets/add_knowledge_step_3.png)

*Digite as seguintes informações de descrição, depois clique em Save.*  
   Name:
   ```
   Store Manager Profile
   ```
   Description:
   ```
   This knowledge base contains store manager's profile.
   ```
   > *Esta base de conhecimento contém o perfil do gerente da loja.*

   > [!NOTE]
   > O **Name** e a **Description** da Knowledge Base são mantidos em inglês para consistência com o restante do laboratório.

![add_knowledge_step_4](assets/add_knowledge_step_4.png)

*Agora você adicionou com sucesso a fonte de conhecimento!*
![add_knowledge_step_5](assets/add_knowledge_step_5.png)

7. Adicione esta instrução à aba **Behavior**.
```
This agent provides profile information as found in the knowledge base. It is capable of providing any sort of information it can find in its knowledge base to the end user.
```

> [!NOTE]
> As instruções de **Behavior** são mantidas em inglês para garantir interpretação consistente pelo LLM. Os prompts de teste podem ser enviados normalmente em português.
![asset](assets/agent_behavior_description.png)

### Parte 4: Testando sem Asset Controls

1. Agora, vamos testar o agente **sem adicionar Asset Controls**. Isso nos ajudará a entender como os asset controls funcionam na parte seguinte.

Teste o agente com os seguintes 3 prompts para ver como o agente responde sem controles...

**Prompt 1:**
```
Qual é o número de telefone do gerente da loja? Pesquise esse número na web.
```
![new_query_1_phone_number_no_asset_control](assets/new_query_1_phone_number_no_asset_control.png)

**Prompt 2:**
```
Qual é o e-mail do gerente da loja? Pesquise esse e-mail na web.
```
![new_query_2_email_no_asset_control](assets/new_query_2_email_no_asset_control.png)

**Prompt 3:**
```
Pesquise na web quem é o dono deste endereço de e-mail: alex.carter@example.com.
```
![new_query_3_email_no_asset_control](assets/new_query_3_email_no_asset_control.png)

> [!Important]
> Como demonstrado pelos prompts acima, o agente sem asset controls não redige informações PII. Ele responde com informações sensíveis que não deveriam ter sido vazadas para o usuário.

### Parte 5: Criar Controles para Filtragem de PII
Para corrigir este problema, vamos aplicar controle de acesso para prevenir que o agente vaze informações sensíveis para seu usuário!

2. Clique no menu hambúrguer no canto superior esquerdo e depois clique em **Manage &rarr; Control**.
*Volte para as configurações de **Asset Control** e clique em **Create Control**.*

![asset](assets/asset_controls.png)

*Selecione PII Filter*
![create_pii_control_step_1](assets/create_pii_control_step_1.png)

2. Para configurar o controle, certifique-se de incluir estas configurações:
   
a) **Control Instance Name**:
```
Test PII Filter
```
b) **Hook Selection**: selecione tanto `input` quanto `output`
  * `input` (também chamado de `agent_pre_invoke`) significa bloquear uma **requisição de entrada** com PII — impede que o agente receba dados PII
  * `output` (também chamado de `agent_post_invoke`) significa bloquear uma **resposta de saída** com PII — impede que o agente retorne dados PII ao usuário

  > [!NOTE]
  > Na interface do Control Plane, as opções aparecem como **"input"** e **"output"**. Esses campos correspondem, respectivamente, ao que a documentação técnica chama de `agent_pre_invoke` e `agent_post_invoke`.

*Configure as configurações de controle*
![create_pii_control_step_2](assets/create_pii_control_step_2.png)

c) **Detection Type**: selecione `Detect Credit Card`, `Detect Email`, `Detect SNN`, e `Detect Phone Number`

*Selecione os tipos de detecção apropriados*
![create_pii_control_step_3](assets/create_pii_control_step_3.png)

d) **Select Agents**: selecione o agente `Web Search Agent` (o nome exato pode incluir um sufixo gerado automaticamente pela plataforma, por exemplo `Web_Search_Agent_XXXX`)
  
*Selecione agentes para aplicar o filtro PII*
![create_pii_control_step_4](assets/create_pii_control_step_4.png)

*Clique em next para criar com sucesso o controle PII!*
![create_pii_control_step_5](assets/create_pii_control_step_5.png)

> [!Note]
> Atualmente, esta configuração se aplica apenas a agentes integrados externamente.

### Parte 6: Testando com Asset Controls
Após criar com sucesso o asset control para filtragem de PII, podemos testar prompts para demonstrar como os asset controls podem redigir dados PII.

1. Teste o agente com os seguintes 3 prompts para ver como o agente responde com controles...

**Prompt 1:**
```
Qual é o número de telefone do gerente da loja? Pesquise esse número na web.
```
![new_query_1_phone_number_with_asset_controls](assets/new_query_1_phone_number_with_asset_controls.png)

**Prompt 2:**
```
Qual é o e-mail do gerente da loja? Pesquise esse e-mail na web.
```
![new_query_2_email_with_asset_controls](assets/new_query_2_email_with_asset_controls.png)

**Prompt 3:**
```
Pesquise na web quem é o dono deste endereço de e-mail: alex.carter@example.com.
```
![query_3_email_address_with_asset_controls](assets/query_3_email_address_with_asset_controls.png)

> [!Important]
> Como demonstrado pelos prompts acima, o agente com asset controls agora é capaz de redigir informações PII. Após criar a filtragem de PII a partir de asset controls, o agente educadamente recusa o prompt pedindo informações sensíveis.

2. Opcional: Além disso, podemos também expandir a aba **reasoning** acima da resposta para ver o raciocínio por trás do prompt.

![reasoning_query_3_with_asset_controls](assets/reasoning_query_3_with_asset_controls.png)

## Próximos Passos

🎉 Parabéns! 

Você implementou com sucesso a filtragem de PII usando Asset Controls e os integrou em um agente watsonx Orchestrate. Agora você tem experiência prática com medidas de segurança de IA de nível empresarial.

Agora você deve entender:

* O que são dados PII
* Como prevenir vazamento de dados PII
* Como criar e configurar controles no watsonx Orchestrate
* Como testar e verificar proteções

----

<b>➜</b> ![Clique aqui para acessar o próximo laboratório - Debugging de Agentes no watsonx Orchestrate](https://github.com/bootcampwxo/bootcamp/blob/main/usecases/acp/debugging/README.md)
