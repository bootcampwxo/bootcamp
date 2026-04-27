# Sistema Multi-Agente para Processamento de Sinistros de Seguros

## Sumário

- [Sistema Multi-Agente para Processamento de Sinistros de Seguros](#sistema-multi-agente-para-processamento-de-sinistros-de-seguros)
  - [Sumário](#sumário)
  - [Descrição do caso de uso](#descrição-do-caso-de-uso)
  - [Arquitetura](#arquitetura)
  - [Implementação](#implementação)
    - [⚠️ Agente de Atendimento de Sinistros](#️agente-de-atendimento-de-sinistros)
    - [Pre-requisitos Técnicos](#pre-requisitos-técnicos)
    - [Open Agent Builder](#open-agent-builder)
    - [Agente de Informação](#agente-de-informação)
      - [Crie o Agente de Informação](#crie-o-agente-de-informação)
      - [Teste o Agente de Informação](#teste-o-agente-de-informação)
    - [Agente de sinistro de clientes](#agente-de-sinistro-de-clientes)
      - [Crie o agente de sinistro de clientes](#crie-o-agente-de-sinistro-de-clientes)
      - [Teste o Agente de sinistro de clientes](#teste-o-agente-de-sinistro-de-clientes)
    - [Agente Processador de sinistros](#agente-processador-de-sinistros)
      - [Crie o Agente Processador de sinistros](#crie-o-agente-processador-de-sinistros)
      - [Teste o Agente Processador de sinistros](#teste-o-agente-processador-de-sinistros)
    - [Agente Supervisor](#agente-supervisor)
      - [Crie o Agente Supervisor](#crie-o-agente-supervisor)
    - [Mais testes via chat de IA](#mais-testes-via-chat-de-ia)

## Descrição do caso de uso

Este laboratório demonstra a construção de um **sistema multi-agente completo** para processamento automatizado de sinistros de seguros usando Watsonx Orchestrate. O sistema é composto por três agentes especializados que trabalham em conjunto:

1. **Agente de Informação**: Busca informações externas sobre regulamentações e contexto de acidentes
2. **Agente de Sinistro de Clientes**: Permite que clientes abram e consultem sinistros (construído no laboratório anterior)
3. **Agente Processador de Sinistros**: Analisa sinistros, valida coberturas e gera recomendações fundamentadas
4. **Agente Supervisor**: Orquestra a comunicação entre os agentes e gerencia o fluxo de trabalho

O sistema automatiza o processo de análise de sinistros para processadores, recuperando automaticamente os sinistros abertos, validando-os contra apólices e regulamentações, e gerando recomendações estruturadas para aprovação ou rejeição. Cada recomendação é respaldada por análise detalhada, minimizando erros e acelerando a tomada de decisão.

## Arquitetura

![Arquitetura](Insurance_Autoclaims_Architecture_v2.png)

## Implementação

### ⚠️ Agente de Atendimento de Sinistros

**Caso ainda não tenha realizadoe**, é necessário que você complete primeiro o laboratório do Agente de Atendimento de Sinistros:

👉 **[Agente de Atendimento de Sinistros](../README-customer.md)**


---

### Pre-requisitos Técnicos

- Verifique com seu instrutor se **todos os sistemas** estão funcionando antes de continuar
- Confirme se você tem acesso ao ambiente watsonx Orchestrate para este laboratório
- Certifique-se de que seu instrutor forneceu o seguinte:
   - Especificações OpenAPI para todos os agentes
   - Um nome de usuário de cliente registrado no banco de dados de seguros
   - Arquivos de conhecimento (PDFs) necessários

### Open Agent Builder

- Log in na IBM Cloud (cloud.ibm.com). Navegue até o menu superior esquerdo e, em seguida, até a Lista de Recursos. Abra a seção IA/Aprendizado de Máquina. Você verá o serviço **watsonx Orchestrate**. Clique para abrir.

<img width="1000" alt="image" src="screenshots_hands_on_lab/cloud-resource-list.png">

- Clique no botão "Launch watsonx Orchestrate".

<img width="1000" alt="image" src="screenshots_hands_on_lab/cloud-wxo.png">

- Bem-vindo ao watsonx Orchestrate. Abra o menu de hambúrguer, clique em **Build** -> **Agent Builder**.

<img width="1000" alt="image" src="screenshots_hands_on_lab/wxo-agent-builder.png">

### Agente de Informação

#### Crie o Agente de Informação

- Clique em **Create Agent**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/0.png">

- Siga os passos de acordo com a captura de tela abaixo.
  - Selecione **Create from scratch**
  - Nomeie o agente `information_agent`
  - Use a seguinte descrição:
    ```
    O agente de informações buscará notícias e diferentes artigos e usará essas informações para resumir os resultados e compartilhá-los.
    ```
  - Clique **Create**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/1-ia.png">

  - Mantenha os padrões para **model**, **Profile** e **Knowledge**.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/2-ia.png">

  - Escolha o estilo do agente. Mantenha-o como `default`. Mantenha o Voice Modality como `No voice configuration`.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/3-ia.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/4-ia.png">

- Na seção **Toolset**, clique em **Add tool** para carregar a especificação OpenAPI

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/ia_tool_1.png">

- Clique em **OpenAPI**.

  <img alt="image" src="./screenshots_hands_on_lab/information-agent/step_10_v5.png">

- Faça upload do arquivo `tavily.json` (Arquivo "tavily.json" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip) 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/8-ia.png">

- Selecione **Next**.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/ia_tool_2.png">

- Selecione todas as **Operações** e clique em **Done**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/ia_tool_3.png">

- Na seção **Behavior**, Adicione as seguintes **Instructions**. Isso definirá como o Agente deve se comportar e o que ele deve esperar:

  ```
  O Agente de Informações usará a ferramenta para buscar informações e retornar um resultado resumido.
  ```

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/12-ia.png">

- **Desmarque o Home Page** em Channels.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/13-ia.png">

- Clique em **Deploy**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/14-ia.png">

#### Teste o Agente de Informação

Digite esta consulta:

```
Insurance law fires in California.
```
##### Este é um serviço gratuito de testes que não foi traduzido para o idioma português

<img width="1000" alt="image" src="./screenshots_hands_on_lab/information-agent/15-ia.png">

- Você obterá uma versão resumida de todos os resultados da pesquisa. Clique em **Step 1** e veja os resultados da ferramenta.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/ia-flow-2.png">

### Agente de sinitro de clientes

#### Crie o agente de sinitro de clientes

- Clique no menu de hambúrguer e depois **Build** -> **Agent Builder**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/17.png">

- Clique em **Create Agent**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/0.png">

- Siga os passos de acordo com a captura de tela abaixo
  - Selecione **Create from scratch**
  - Nomeie o agente `Customer_Claims_Agent`
  - Utilize a seguinte descrição:

  ```
  O agente de Reclamações do Cliente permitirá que os clientes consultem o status de suas solicitações de reclamação e criem uma nova solicitação. Você também responderá a perguntas sobre o processo de reclamação e a apólice de seguro, utilizando a base de conhecimento.
  ```

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-1.png">

  - Clique **Create**

- Selecione `Model`. Mantenha-o como o **default**.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-2.png">

- Escolha o estilo do agente. Mantenha-o como `default`.

- Em **Welcome Message:** Ainda durante a etapa de definição do tipo de agente, você também pode configurar uma mensagem de boas vindas que será exibida na interface para o usuário, como mostrado na imagem abaixo. Essa etapa é opcional e você pode definir algo como:
```Bem vindo ao Agente X```

- Em **Quick start Prompts:** Esse passo também é opcional. Nessa sessão podemos definir atalhos para o usuário, essas mensagens serão exibidas para o usuário como botões na interface. Você pode criar esses botões clicando em `Add prompt +` e removê-los clicando no ícone de lixeira. Para que essas opções apareçam na telinha de preview do lado direito da tela, use o ícone de restart para atualizar a interface. **Não é necessário sair da página.**

- Em `Keep Voice Modality` escolha ou mantenha `No voice configuration`.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-3.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-4.png">


- Na seção **Knowledge**:

- Faça o upload do arquivo Automobile Insurance Knowledge Base (Arquivo "Automobile Insurance Knowledge Base.pdf" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip) clicando em **Upload files** em **Documents**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-5.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-6.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-7.png">

- Adicione a seguinte descrição em **Description**:

  ```
  Esta base de conhecimento aborda o tema de seguros e o processo de sinistro. Esta base de conhecimento ajudará o cliente a obter informações sobre o processo de sinistro e as regras e regulamentos de processamento de sinistros de seguro.
  ```

- Na seção **Toolset**, clique em **Add tool** 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-8.png">

- Clique em **Import**. Importe o arquivo `customer_claims_agent_tools.json` (Arquivo "customer_claims_agent_tools.json" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip) 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-9.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-10.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-11.png">

- Selecione **Next**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-13.png">
- Selecione todas as  **Operações** e clique em **Done**
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-14.png">

- Na seção **Behavior**, adicione o seguinte prompt ao **Instructions**:

```
Se o usuário solicitar o envio de uma reclamação, siga estas etapas:

  1. Colete as informações necessárias (sem suposições). Peça ao usuário que forneça os seguintes detalhes:
  - Nome completo (para autenticação)
  - Local do incidente
  - Data do incidente
  - Detalhes e tipo do veículo
  - Uma descrição detalhada do incidente

  Se algum destes estiver faltando, pause e solicite-o antes de continuar.

  2. Solicite todas as seguintes informações adicionais (somente se ainda não tiverem sido fornecidas):
  - O incidente foi reportado à polícia? Em caso afirmativo, qual a data e hora?
  - Houve danos? Qual o custo estimado?
  - Houve despesas médicas? Em caso afirmativo, qual o valor?

  Calcule o custo total estimado somando os danos e as despesas médicas.

  3. Crie a Solicitação de Reclamação. Após coletar todas as informações necessárias:
  - Crie um resumo conciso e estruturado do incidente e dos detalhes relacionados.
  - Use essas informações como claim_request_details na ferramenta "Criar uma Solicitação de Reclamação".

  Se a ferramenta retornar uma reclamação bem-sucedida, siga todos os procedimentos a seguir:
  - Exiba os resultados em uma tabela formatada, com cada detalhe em uma nova linha
  - Destaque o número da reclamação
  - Informe ao usuário: "Você receberá uma confirmação da sua solicitação de reclamação por e-mail."

  Se a ferramenta retornar "cliente não encontrado":
  - Responda com: "Você não está autorizado a enviar uma reclamação."
  - Não exiba nenhuma saída adicional da ferramenta.

Se o usuário perguntar sobre o Status da Reclamação, siga estas etapas:
  1. Pergunte o nome dele
  2. Pergunte o número da reclamação
  3. Use a ferramenta "Verificar Status da Reclamação" para recuperar o status da reclamação
  4. Exiba o resultado em um formato tabular limpo. Cada detalhe deve estar em uma nova linha.
  5. Encerre a conversa após exibir o status da reclamação

Se o usuário tiver dúvidas sobre:
  - Processos de seguro
  - Elegibilidade para sinistros
  - Documentação
  Consulte apenas a base de conhecimento “Automobile Insurance Knowledge Base.pdf”. Se a resposta não estiver na base de conhecimento, responda: “Não sei”.

Não faça referência à base de conhecimento ao interagir com ferramentas.
```
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-15.png">

- Não há necessidade de alterar o `Channels`. Clique em **Deploy**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-16.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/customer/customer-17.png">

#### Teste o Agente de sinitro de clientes

Passo 1. Insira uma consulta básica:

```
Quais são os diferentes tipos de seguro de automóvel?
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claims-flow-1.png">

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claims-flow-2.png">

Etapa 2. Verifique o fluxo para criar uma nova reclamação

Digite o seguinte:
```
Enviar uma nova reclamação
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-3.png">

**OBSERVAÇÃO**: Escolha um dos nomes da planilha de usuários (Arquivo "Insurance_Database_v1.csv" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip)

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-4.png">

Para localização, digite:

`St Mary's Street, San Francisco, California`

ou qualquer outro endereço.

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-5.png">

Para data entre `23-05-2025` ou qualquer outra data

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-6.png">

Para informações sobre o veículo, digite `Toyota Corolla, 2003` ou quaisquer outros detalhes do veículo

<img width="1000" alt="image" src="./screenshots_hands_on_lab/vehicle_details.png">

Para mais detalhes, insira:

```
Eu estava dirigindo para o trabalho quando uma caminhonete vermelha avançou o sinal vermelho e colidiu com a traseira direita do meu veículo no cruzamento. O impacto fez meu carro girar levemente, resultando em danos ao para-choque traseiro, à lanterna traseira direita e um amassado no para-choque traseiro. Eu estava usando cinto de segurança e não sofri ferimentos graves, mas relatei dores leves nas costas e consultei um médico no mesmo dia. As despesas médicas foram de US$ 3.400 e o custo do reparo dos danos foi de US$ 4.500.
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-7.png">

Etapa 3. Verifique o fluxo para o status da reivindicação

Insira a consulta:

```
Verifique o status da reivindicação
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-8.png">

Digite o nome que você escolheu:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-10.png">

Para o número da reclamação, insira o número da reclamação do resumo da reclamação que você acabou de criar:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/claim-flow-11.png">

Você pode criar reivindicações adicionais para o seu nome atribuído para testar o próximo agente.

### Agente Processador de sinistros
#### Crie o Agente Processador de sinistros

- Clique no menu de hambúrguer e depois **Build** -> **Agent Builder**.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/2.png">

- Clique em **Create Agent**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/0.png">

- Siga os passos de acordo com a captura de tela abaixo.
  - Selecione **Create from scratch**
  - Nomeie o agente `Agente_Processamento_Sinistros`
  - Use a seguinte descrição:

  ```
  O Agente de Processamento de Sinistros auxilia o analista na localização de processos em aberto, além de validar, verificar e conferir os dados de cada solicitação.
  O agente atua como suporte à decisão, sugerindo tecnicamente se o sinistro deve ser aprovado ou recusado com base nas regras da apólice.
  ```

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-1.png">

- Verifique o `model`.  


  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-2.png">

- Selecione o estilo do agente como `Default`. Também não são necessárias alterações para a Modalidade de Voz. Mantenha como Configuração Sem Voz.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-3.png">
  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-4.png">

- Na seção **Knowledge** Faça o upload do arquivo de Policy (Arquivo "Policy.pdf" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip) clicando em **Upload files** em **Documents**. 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-5.0.png">

  <img alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-5.1.png">

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-5.2.png">

- Adicione a seguinte  **Description**:
  ```
  Esta base de conhecimento reúne as normas de seguros e as diretrizes operacionais para o tratamento de sinistros.
  Ela fornece o suporte técnico necessário para que o analista processe as solicitações em conformidade com as regras de cobertura e os regulamentos de indenização da seguradora.
  ```

  Esta base pode se chamar (kb de Knowledge Base):
  ```
  Politica_Sinistros-kb
  ```

- Na seção **Toolset** clique em **Add tool**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-6.0.png">

- Clique em **OpenAPI**

  <img alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-6.1.png">

- Faça o Upload do arquivo `claim_processor_agent_tools.json` (Arquivo "claim_processor_agent_tools.json" dentro da pasta "5. Agente de Sinistros de seguros" gerada após descompactar o LABS.zip) 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-8.png">

    <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-10.png">

- Selecione todas as **Operações**. Depois clique em **Done**.

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-11.png">


- Clique em **Add Agent**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-12.png">

- Clique **Add from local instance**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-13.png">

- Selecione **information_agent** e depois **Add to Agent button**

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-14.png">

- Na seção **Behavior** adicione as seguintes **Instructions**:

    ```
  Você começará dando as boas-vindas ao processador de sinistros e exibindo os sinistros em aberto em uma tabela.
  Esta tabela deve incluir o ID do cliente (destacado), número do sinistro, número da apólice, custo estimado, valor segurado e detalhes do veículo. Não exiba duplicatas.

  Peça ao processador de sinistros para selecionar um ID do cliente.

  Se houver vários sinistros para um ID do cliente, peça ao processador de sinistros para selecionar um número.

  Use o número do sinistro e o ID do cliente para buscar detalhes usando a ferramenta Buscar Sinistros Abertos. É muito importante; retornará um erro se não for possível executar a ferramenta.

  Após selecionar um ID do cliente, busque os detalhes do sinistro e da apólice correspondentes a esse ID do cliente e exiba-os em um formato tabular. Em seguida, gere um resumo com base nos seguintes pontos.

  1. Compare o custo estimado com o valor segurado e calcule o valor aprovado do sinistro subtraindo a franquia. Destaque o valor aprovado.

  2. Verifique se a apólice está ativa e se o sinistro se enquadra no período de cobertura.

  3. Classifique o acidente em um dos seguintes tipos: colisão traseira, colisão frontal, impacto lateral, colisão lateral, colisão com um único veículo, colisão com vários veículos, atropelamento, estacionamento, colisão com animais, relacionado ao clima, relacionado a falha mecânica, vandalismo ou roubo.

  4. Determine se o tipo de acidente classificado está coberto pela apólice. Se os detalhes da apólice não estiverem claros, consulte a base de conhecimento para verificar.

  5. É obrigatório usar o information_agent para consultar o tipo de acidente descoberto na etapa 4. Consulte: As regras e regulamentos para o tipo de acidente nos EUA. Use o resultado para verificar se os detalhes do sinistro estão em conformidade.

  6. Forneça uma recomendação clara para aceitar ou rejeitar a solicitação com base nessas verificações.

  7. Destaque o valor total da solicitação (custo estimado menos franquia).

  8. Crie um resumo claro e conciso para o processador da solicitação, enfatizando detalhes importantes como valor aprovado, número da solicitação e número da apólice.

  HIGHLIGHT ALL THE DETAILS IN NEAR FORMAT.

  Por fim, pergunte ao processador da reclamação: "Eles aceitam a reclamação?"
  Não dê os próximos passos.

  Assim que a decisão for tomada, atualize o status da reclamação e envie uma mensagem confirmando que os e-mails foram enviados ao cliente e à equipe financeira.
  ```

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-15.png">

- Mantenha o Channels como está. Clique em **Deploy** 

  <img width="1000" alt="image" src="./screenshots_hands_on_lab/claim_processor_insurance_agent/cp-18.png">

#### Teste o Agente Processador de sinistros

Etapa 1. Insira a consulta básica:

```
Liste todos as reinvidicações em aberto
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/cp-flow-1.png">

Etapa 2. Insira um ID de cliente da lista:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/cp-flow-2-new.png">

Etapa 3. Insira o número da reclamação da lista:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/cp-flow-3.0-new.png">

Etapa 4. Quando solicitado a aceitar a solicitação, responda:

```
Sim
```

<img width="1000" alt="image" src="./screenshots_hands_on_lab/cp-flow-4-new.png">

Etapa 5. Você deverá ver uma confirmação de atualização:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/cp-flow-5-new.png">


### Mais testes via chat de IA

> ***Você também pode testar os agentes pelo chat da IA.***

Navegue até o chat de IA acessando o menu de hambúrguer no canto superior esquerdo e selecione **Chat**.

<img width="1000" alt="image" src="./screenshots_hands_on_lab/39.png">

Em seguida, selecione o agente a ser testado:

<img width="1000" alt="image" src="./screenshots_hands_on_lab/40.png">
