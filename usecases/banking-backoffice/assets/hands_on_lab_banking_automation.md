# Transforming Banking with Intelligent Agents - Lab <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

- [🔍Introdução](#-introdução)
- [📊 Operações Bancárias](#-operações-bancárias)
  - [Cenário do Usuário Atual](#Cenário-do-Usuário-Atual)
  - [Futuro com Agentic AI](#Futuro-com-Agenticai)
- [🏗️ Target Architecture with Agentic AI](#%EF%B8%8F-arquitetura-de-destino-com-agentic-ai)
- [🔧 Instruções de Laboratório](#-Instruções-de-Laboratório)
  - [Pré-requisitos](#pré-requisitos)
  - [Visão Geral das Etapas do Laboratório](#Visão-Geral-das-Etapas-do-Laboratório)
- [Conecte-se à sua instância atribuída do Watsonx Orchestrate](#Conecte-se-à-sua-instância-atribuída-do-Watsonx-Orchestrate)
- [Agente de Back Office GFM](#Agente-de-Back-Office-GFM)
  - [Crie o Agente de Back Office GFM](#Crie-o-Agente-de-Back-Office-GFM)
  - [Teste e implante o Agente de Back Office GFM](#Teste-e-implante-o-Agente-de-Back-Office-GFM)
- [Agente de caixa GFM](#Agente-de-caixa-GFM)
  - [Criar Agente de Caixa GFM](#Criar-Agente-de-Caixa-GFM)
  - [Teste e implante o Agente de Caixa GFM](#Teste-e-implante-o-Agente-de-Caixa-GFM)
- [Agente de Informações sobre Produtos GFM](#Agente-de-Informações-sobre-Produtos-GFM)
  - [Criar Agente de Informações do Produtos GFM](#Criar-Agente-de-Informações-sobre-Produtos-GFM)
  - [Teste e implante o Agente de Informações do Produto GFM](#Teste-e-implante-o-Agente-de-Informações-do-Produto-GFM)
- [Agente Orquestrador do Banco GFM](#Agente-Orquestrador-do-Banco-GFM)
  - [Criar Agente de Orquestra do Banco GFM](#Crie-o-Agente-Orquestrador-do-Banco-GFM)
  - [Adicione Agentes colaborativos](#Adicione-Agentes-colaborativos)
  - [Teste e implante o Agente Orquestrador do Banco GFM](#Teste-e-implante-o-Agente-Orquestrador-do-Banco-GFM)
- [Teste Sua Solução Bancária De Agentic IA](#Teste-Sua-Solução-Bancária-De-Agentic-AI)
- [🎉 Parabéns. Você completou o laboratório](#-Parabéns)
- [📚 Recursos](#-recursos)
- [📄 Isenção de responsabilidade do código de amostra da IBM](#-ibm-sample-code-disclaimer)

## 🔍 Introdução

Bem-vindo ao Laboratório de IA Agentic do GFM Bank! Neste workshop prático, você transformará um aplicativo bancário tradicional em uma solução moderna e alimentada por IA usando o **watsonx Orchestrate**. O setor bancário está passando por uma rápida transformação digital, e o GFM Bank está liderando o caminho implementando agentes de IA inovadores para lidar com as interações com os clientes.

O GFM Bank enfrenta desafios com as operações tradicionais de caixa e back-office que são manuais, demoradas e muitas vezes resultam em longos tempos de espera do cliente. Ao implementar uma solução de IA Agentic, o banco pretende:

  - Fornecer suporte ao cliente 24 horas por dia, 7 dias por semana, para operações bancárias comuns
  - Reduza os tempos de espera para transações e aprovações
  - Manter a estrita conformidade com os regulamentos bancários
  - Melhore a satisfação do cliente através de um serviço mais rápido
  - Libere a equipe humana para lidar com necessidades mais complexas do cliente

Neste laboratório, você construirá um sistema de agentes de IA colaboradores que podem lidar com operações bancárias, incluindo:

  - Consultas sobre o saldo da conta
  - Transferências de dinheiro entre contas
  - Aprovações de limite de cheque especial
  - Reversões de taxas
  - Solicitações de informações sobre o produto

## 📊 Operações Bancárias

Atualmente, o GFM Bank conta com caixas humanos para transações básicas e equipe de back-office para aprovações, levando a atrasos e experiências inconsistentes com os clientes na alta temporada.*

### Cenário do Usuário Atual
John, um cliente do GFM Bank, precisa fazer um pagamento urgente de €8.000, mas ele só tem €5.000 em sua conta. 

1. John visita a agência bancária e espera na fila para falar com um caixa
2. O caixa verifica seu saldo e o informa que ele não tem fundos suficientes
3. John solicita um cheque especial de €3.000
4. O caixa deve encaminhar a solicitação para um gerente de back-office
5. John espera novamente pela aprovação
6. Uma vez aprovado, ele retorna ao caixa para concluir a transferência
7. Se John perceber que enviou muito dinheiro, ele precisa solicitar uma reversão, o que requer outro processo de aprovação

Esse processo normalmente leva de 1 a 2 horas do tempo de John e envolve vários membros da equipe.

### Futuro com IA Agentic
Com o sistema alimentado por IA, você construirá hoje:

1. John envia uma mensagem para o Agente Orquestrador do Banco GFM
2. Ele pede para transferir €8.000
3. O Agente de Caixa verifica seu saldo e o informa sobre fundos insuficientes
4. John solicita um cheque especial
5. O Agente de Caixa encaminha esta solicitação para o Agente de Back Office
6. Após a aprovação (se a solicitação for inferior a € 10.000) do Agente de Back Office, o Agente de Caixa conclui a transferência
7. Se John precisar de uma reversão, ela é tratada rapidamente dentro da mesma conversa. 

Todo o processo leva minutos em vez de horas, e John nunca precisa sair de casa.

## 🏗️ Arquitetura de destino com Agentic AI

![Architecture](banking-backoffice-architecture.png)

## 🔧 Instruções de Laboratório

Neste laboratório, você construirá uma solução completa de IA Agentic para o GFM Bank usando o watsonx Orchestrate. Você criará vários agentes especializados que trabalham juntos para lidar com solicitações de clientes.

### Pré-requisitos
- Compreensão básica das operações bancárias (por exemplo, transferência, verificação de saldo, cheque especial...)
- Familiaridade com conceitos de agentes de IA (por exemplo, instruções, ferramentas, colaboradores...)

### Visão Geral das Etapas do Laboratório

1. Conecte-se ao **watsonx Orchestrate**
2. Crie o Agente de Back Office GFM
3. Crie o Agente de Caixa GFM
4. Crie o Agente de Informações do Produto GFM
5. Crie o Agente Orquestrador do Banco GFM
6. Teste a solução completa

### 🚀🚀🚀 Vamos começar! 🚀🚀🚀 <!-- omit in toc -->

### Conecte-se à sua instância atribuída do Watsonx Orchestrate

- Faça login no IBM Cloud (cloud.ibm.com). Navegue até o menu de hambúrguer superior esquerdo e, em seguida, até a Lista de Recursos. Abra a seção AI/Aprendizagem de Máquina. Você deve ver um serviço **watsonx Orchestrate**, clique para abrir

  ![Watsonx Orchestrate service](./images/i1.png)

- Clique no botão **Launch watsonx Orchestrate** 

  ![Launch Watsonx Orchestrate](./images/i2.png)

- Bem-vindo ao watsonx Orchestrate. Abra o menu de hambúrguer, clique em **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

### Agente de Back Office GFM

Este Agente lida com operações bancárias especiais para o GFM Bank que exigem privilégios elevados, como aprovação de cheque especial e processamento de reversões de taxas. Opera a partir do centro de operações do GFM Bank.

#### Crie o Agente de Back Office GFM

- Clique em **Create Agent**

  ![Create Agent](./backoffice_ag_imgs/i1.png)

- Siga os passos de acordo com a captura de tela abaixo.
  - Selecione **Create from scratch**
  - Nomeie o Agente:
    ```
    Agente de Back Office do GFM Bank
    ```
  - Adicione o seguinte ao **Description**:  

```
  Você é o Agente de Back Office do GFM Bank, responsável por lidar com operações bancárias especiais que exigem privilégios elevados. Você trabalha no centro de operações do GFM Bank e tem autoridade para aprovar saques a descoberto e processar estornos de taxas.

  Suas competências:
1. Aprovar limites de saque a descoberto usando a ferramenta `approve-overdraft` com IBAN e valor (0-10.000 EUR)
2. Processar estornos de taxas usando a ferramenta `fee-reversal` com IBAN e valor
3. Exceções ou ajustes especiais
4. Quaisquer operações que exijam privilégios elevados
5. Fornecer reembolsos, se solicitado
```
    
  - Clique **Create**
 
    ![Back Office Agent Description](./backoffice_ag_imgs/i2.png)

- Na página Agente de Back Office do GFM Bank, selecione o modelo "llama-3-405b-instruct" no menu suspenso no meio superior da página.

  ![Select Model](./backoffice_ag_imgs/i15.png)

- Mantenha os padrões para as seções **Profile**, **Voice modality**, and **Knowledge**.
- Na seção **Toolset**, clique no botão **Add tool**.

  ![Add Tool](./backoffice_ag_imgs/i3.png)

- Clique em **Import**.

  ![Import file](./backoffice_ag_imgs/i4.png)

- Clique em  **Import from file**

  ![Import from file](./backoffice_ag_imgs/i16.png)

- Faça Upload do arquivo de API `bank.json` API (o arquivo está disponível na pasta "6. Banking Backoffice" gerada após a descompactação do arquivo LABS.zip). Arraste e solte o arquivo na área designada.

  ![Upload spec file](./images/i38.png)

- Assim que o arquivo for carregado, selecione **Next**. Seleciona as **Operações**  the "Processar uma reversão de taxa para uma conta" and Aprovar ou modificar o limite de cheque especial para uma conta" **Operations** e clique em **Done**

  ![Select Tools](./backoffice_ag_imgs/i7.png)

- Você deve ver o seguinte em **Tools**:

  ![Loaded tools](./backoffice_ag_imgs/i9.png)

- Na seção **Behavior** . Adicione o seguinte texto às **Instruções**: 
```
  Instruções Principais:
- Execute somente operações explicitamente solicitadas pelos clientes
- Verifique os detalhes antes de realizar qualquer operação
- Confirme todas as operações concluídas
- Explique quaisquer erros ou limitações claramente

Regras e Limitações:
- Os limites de cheque especial devem estar entre 1.000 e 10.000 euros
- Processe estornos de taxas somente quando o cliente apresentar uma justificativa comercial clara
- Sempre verifique o IBAN antes de processar qualquer operação
- Mantenha uma postura profissional e eficiente

Diretrizes de Resposta:
- Para aprovações de cheque especial: Confirme quando o cheque especial foi aprovado ou negado e exiba o novo limite e os detalhes da conta
Exemplo de resposta:
Seu cheque especial no valor de 2.000 euros foi aprovado
- Para estornos de taxas: Confirme o valor estornado e o novo saldo da conta
- Em caso de erros: Explique o problema claramente e sugira soluções alternativas quando apropriado
- Sempre use uma linguagem clara e concisa que explique o que foi feito

Mantenha um tom profissional com a formalidade apropriada para um representante bancário com privilégios elevados.
```

  
- Como este agente será um agente colaborador e será invocado pelo GFM Bank Orchestrator, não queremos habilitá-lo para bate-papo direto na página inicial do bate-papo. Desatile o recurso **Show agent** na seção **Channels**.

  ![Instructions](./backoffice_ag_imgs/i11.png)

#### Teste e implante o Agente de Back Office GFM

- Na janela de visualização à direita, teste com a seguinte consulta:
  ```
  Quero solicitar um saldo negativo de 1000 EUROS para minha conta IBAN DE89320895326389021994
  ```

- Clique em **Deploy** 

  ![Deploy](./backoffice_ag_imgs/i10.png)

- Na página **Deploy Agent**, clique em **Deploy**

  ![Deploy agent](./backoffice_ag_imgs/i13.png)

### Agente de caixa GFM

Este Agente auxilia os clientes com tarefas bancárias diárias, como consultas de saldo e transferências de dinheiro. Responde apenas ao que é perguntado, evitando suposições ou ações proativas.

#### Criar Agente de Caixa GFM

- Clique no menu de hambúrguer, depois em  **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- Clique em **Create Agent**

  ![Create Agent](./teller_ag_imgs/i2.png)

- Siga os passos de acordo com a captura de tela abaixo.
  - Selecione **Create from scratch**
  - Nomeie o Agente
    ```
    Agente de caixa GFM
    ```
  - Adicione o seguinte à Descrição: **Description**:
    ```
    Você é um Agente de Caixa do Banco GFM, responsável por fornecer assistência precisa e profissional em transações bancárias, como consultas de saldo e transferências. Você responde estritamente às solicitações do cliente, sem suposições ou sugestões.

    Você pode:

    Verificar saldos de contas usando a ferramenta de consulta de saldo com um IBAN

    Processar transferências de dinheiro usando a ferramenta de transferência iban com IBAN de origem, IBAN de destino e valor

    Você formata as respostas de saldo usando uma saída estruturada, incluindo uma lista ou tabela limpa de transações recentes para melhorar a legibilidade.

    Encaminhar para o Agente de Back Office quando:
    O cliente solicitar aprovação ou alterações de cheque especial

    O cliente solicitar estornos ou reembolsos de taxas

    O cliente precisar de exceções ou ajustes especiais

    A intenção envolve operações que exigem privilégios elevados

    O cliente usa frases de exemplo: "precisa de um cheque especial", "estornar uma taxa", "solicitar um reembolso"
    ```
  - Clique **Create**
 
    ![Create agent](./teller_ag_imgs/i5.png)

- Na página do `Agente de Caixa GFM`, selecione o modelo "llama-3-405b-instruct" no menu suspenso no meio superior da página.

  ![Select model](./teller_ag_imgs/i20.png)

- Use os padrões para as seções **Profile**, **Voice modality**, e **Knowledge**. Na seção **Toolset**, clique no botão **Add tool**.

  ![Add Tool](./teller_ag_imgs/i6.png)

- Clique em **Import**.

  ![Import](./teller_ag_imgs/i7.png)

- Clique em **Import from file**.

  ![Import from file](./teller_ag_imgs/i21.png)

- Faça Upload do arquivo de API `bank.json` API (o arquivo está disponível na pasta "6. Banking Backoffice" gerada após a descompactação do arquivo LABS.zip). Arraste e solte o arquivo na área designada e clique em **Next**.
  
  ![Upload spec file](./images/i38.png)

- Selecione as **operações** "Verificar saldo da conta por IBAN" e "Transferir dinheiro entre IBANs" e clique **Done**.

  ![Select Operations](./teller_ag_imgs/i10.png)

- Você deve ver o seguinte em  **Tools**:
  
  ![Uploaded tools](./teller_ag_imgs/i12.png)

- Na seção **Agents**, clique em **Add Agent**

  ![Uploaded tools](./teller_ag_imgs/i16.png)

- Clique **Add from local instance**

  ![Uploaded tools](./teller_ag_imgs/i17.png)

- Selecione **GFM Backoffice** e depois **Add to Agent button**

  ![Uploaded tools](./teller_ag_imgs/i18.png)

  ![Uploaded tools](./teller_ag_imgs/i19.png)

- Vá para a seção **Behavior**. Adicione o seguinte em **Instructions**:

  ```
  Responda apenas ao que o cliente solicitar explicitamente — nunca antecipe ou sugira os próximos passos.

  Para consultas de saldo:

  Exiba o saldo atual

  Exiba o limite de cheque especial, se disponível

  Exiba as transações recentes formatadas como uma tabela ou lista com marcadores

  Encerre a resposta — não sugira outras ações

  Para solicitações de transferência:

  Confirme e processe a transferência

  Relate o sucesso ou a falha, incluindo o novo saldo, se bem-sucedido

  Em caso de fundos insuficientes, informe a falha sem sugerir cheque especial, a menos que explicitamente solicitado

  Não presuma intenção — peça esclarecimentos se a solicitação não for clara

  Use linguagem clara e concisa, com um tom profissional

  Ao apresentar transações recentes, use o seguinte formato:

  Formato de Resposta de Exemplo (para Consulta de Saldo)
  Cliente: "Qual é o saldo da minha conta para o IBAN DE12345678?"
  Agente:
  Seu saldo atual é de 500 EUR.
  Seu limite de cheque especial é de 200 EUR.

  Transações Recentes:
  | Data       | Tipo     | Total   | Descrição         |
  |------------|----------|---------|----------------------|
  | May 16     | Withdrawal | -50 EUR | ATM Withdrawal       |
  | May 15     | Deposit   | +200 EUR | Direct Deposit       |
  | May 13     | Purchase  | -30 EUR | Grocery Store        |
  ```

- Como este agente será um agente colaborador e será invocado pelo Agente Orquestrador do GFM Bank, não queremos habilitá-lo para bate-papo direto na página inicial do bate-papo. Desatile o recurso **Show agent**.

  ![Show agent toggle](./teller_ag_imgs/i14.png)

#### Teste e implante o Agente de Caixa GFM

- Na janela de visualização à direita, teste com a seguinte consulta:
```
Qual é o saldo do IBAN da minha conta DE89320895326389021994
```

- Clique em **Deploy** 

  ![Deploy](./teller_ag_imgs/i13.png)

- Na tela de **Deploy Agent**, clique em **Deploy**. O Agente agora está disponível para que outras pessoas interajam.

  ![Deploy agent](./teller_ag_imgs/i1.png)
  
### Agente de Informações sobre Produtos GFM

Este Agente atua como especialista confiável em todos os produtos e serviços bancários oferecidos pelo GFM Bank. Ajuda os clientes a explorar e entender as soluções financeiras disponíveis com clareza e precisão.

#### Criar Agente de Informações sobre Produtos GFM

- Clique no menu de hambúrguer, depois em **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- Na próxima tela, clique em **Create Agent**

  ![Create Agent](./prod_info_ag_imgs/i1.png)

- Siga os passos de acordo com a captura de tela abaixo
  - Selecione **Create from scratch**
  - Nomeie o agente
    ```
    Informações do Produto GFM
    ```
  - Adicione o seguinte em **Description**:
    
    ```
    Você é o Especialista em Produtos do GFM Bank, o recurso especializado para todos os produtos e serviços bancários oferecidos pelo GFM Bank. Sua função é fornecer informações precisas e úteis sobre soluções bancárias, proporcionando uma experiência excepcional ao cliente.

Sua expertise abrange:
1. Produtos de Conta – Recursos, tarifas, taxas de juros e requisitos para contas correntes, poupança, CDBs, mercado monetário e contas para jovens.

2. Produtos de Empréstimo – Informações sobre empréstimos pessoais, financiamentos imobiliários, financiamentos para veículos, financiamento imobiliário e empréstimos para construção de crédito, incluindo termos, taxas e elegibilidade.

3. Serviços de Cartão – Detalhes sobre cartões de crédito, débito, com garantia e empresariais, além de opções de proteção contra cheque especial.

4. Banco Digital – Ferramentas bancárias móveis e online, carteiras digitais, alertas e recursos de segurança.

5. Serviços Especializados – Serviços bancários internacionais, gestão de patrimônio, serviços bancários para empresas, seguros e planejamento financeiro.
    ```
    
  - Clique **Create**
  ![Prod Agent Description](./prod_info_ag_imgs/i2.png)

- Na página do `Informações do Produto GFMe, selecione o modelo "llama-3-405b-instruct" no menu suspenso na parte superior central da página.

  ![Select model](./prod_info_ag_imgs/i14.png)

- Na seção **Knowledge**. clique em **Choose knowledge**.

  ![Choose knowledge](./prod_info_ag_imgs/i13.png)

- Clique em **Upload files** e depois **Next**.

  ![Choose knowledge](./prod_info_ag_imgs/i12.png)

- Carregue os documentos listados abaixo fornecidos pelo instrutor e clique **Next**

  ```
  lista-de-precos-e-servicos.pdf
  ser-termos-condicoes-cartoes-de-debito.pdf
  FAQ sobre serviços de cheque especial.docx
  ```
  
  ![Upload Documents](./prod_info_ag_imgs/i11.png)

- Na seção **Description**, adicione o seguinte e depois  **Save**:

```
  Esta base de conhecimento abrangente contém informações detalhadas sobre os produtos, serviços, taxas e procedimentos operacionais do GFM Bank, organizados nas seguintes categorias:

1. Contas Bancárias Pessoais
- Contas Correntes: Tipos, recursos, saldos mínimos, taxas mensais, condições de isenção de taxas
- Contas Poupança: Taxas de juros, limites de saque, requisitos de depósito mínimo
- Conta Pessoal para Cheque Especial: Elegibilidade, limites, processo de solicitação, taxas, condições de pagamento
- Contas para Jovens e Estudantes: Requisitos de idade, recursos especiais, transição para contas para adultos
- Requisitos para Abertura de Conta: Documentação, critérios de elegibilidade, processos online vs. na agência

2. Produtos e Serviços de Cartão
- Cartões de Débito: Recursos, medidas de segurança, recursos de pagamento por aproximação
- Termos e Condições do Cartão de Débito: Contrato completo do titular do cartão, responsabilidades, resolução de disputas
- Proteção contra Cheque Especial do Cartão: Requisitos de adesão, limites de cobertura, taxas associadas
- Limites de Transações do Cartão: Limites diários de saque em caixas eletrônicos, limites de compra, procedimentos de ajuste
- Segurança do Cartão: Gerenciamento de PIN, substituição do cartão, medidas de proteção contra fraudes
Cartão Perdido/Roubado Procedimentos: Processo de denúncia, substituição emergencial, limitações de responsabilidade

3. Serviços de Banco Digital
- Banco Móvel: Recursos do aplicativo, compatibilidade de dispositivos, medidas de segurança
- Banco Online: Gerenciamento de contas, serviços de pagamento de contas, recursos de transferência
- Recursos de Segurança: Métodos de autenticação, prevenção de fraudes, garantias de proteção ao cliente

4. Taxas e Estrutura de Preços
- Tabela de Tarifas Abrangente: Taxas de serviço, taxas de transação, multas
- Programas de Isenção de Tarifas: Requisitos para evitar taxas mensais de manutenção
- Estrutura de Tarifas de Caixas Eletrônicos: Taxas dentro da rede vs. fora da rede, custos de uso de caixas eletrônicos internacionais
- Preços de Serviços de Investimento: Tabelas de comissões, taxas de administração, valores mínimos de conta
- Considerações Especiais sobre Tarifas: Descontos para militares, benefícios para idosos, isenções para estudantes

5. Produtos de Empréstimo
- Empréstimos Pessoais: Taxas, termos, requisitos para solicitação, prazos de aprovação
- Empréstimos Imobiliários: Opções de hipoteca, linhas de crédito, oportunidades de refinanciamento
- Empréstimos para Veículos: Financiamento de veículos novos e usados, estruturas de taxas, processo de pré-aprovação
- Produtos de Construção de Crédito: Crédito com Garantia Opções de Contas de Investimento, Programas de Melhoria de Crédito

6. Bancos Internacionais
- Serviços em Moeda Estrangeira: Taxas de câmbio, disponibilidade de moeda, procedimentos para solicitação
- Transferências Eletrônicas Internacionais: Taxas, tempo de processamento, informações necessárias
- Políticas de Transações Estrangeiras: Uso do cartão no exterior, taxas internacionais, taxas de conversão de moeda
- Acesso a Caixas Eletrônicos Estrangeiros: Parcerias com redes globais de caixas eletrônicos, limites de saque e taxas associadas

7. Serviços de Investimento
- Opções de Contas de Investimento: Contas individuais, contas de aposentadoria, poupança para educação
- Produtos de Investimento: Fundos mútuos, títulos, ações, certificados de depósito
- Serviços de Consultoria: Opções de contas administradas, recursos de planejamento financeiro
- Estrutura de Taxas de Investimento: Taxas de administração, custos de transação, requisitos de saldo mínimo

8. Recursos de Suporte ao Cliente
- Informações da Central de Atendimento: Números de contato, horário de funcionamento, procedimentos de escalonamento
- Detalhes Bancários da Agência: Locais, horário de funcionamento, serviços disponíveis
- Agendamento de Consultas: Processo para reunião com especialistas, preparação necessária

Cada tópico inclui informações atualizadas, divulgações regulatórias, quando aplicável, e referências cruzadas internas a produtos ou serviços relacionados para facilitar o atendimento completo ao cliente.
```

    ![Prod Agent Knowledge Description](./prod_info_ag_imgs/i10.png)

- Todos os arquivos e a descrição enviados serão assim:

  ![Prod Agent Knowledge Description](./prod_info_ag_imgs/i9.png)

- Na seção **Behavior**, adicione em **Instructions**:
  ```
  Diretrizes de Resposta:
Ao descrever produtos:
- Comece com os principais benefícios e recursos mais relevantes para os clientes
- Explique claramente as estruturas de taxas e como elas podem ser isentas
- Forneça faixas de taxas de juros precisas com os avisos de isenção de responsabilidade apropriados
- Compare produtos quando for útil (por exemplo, "Ao contrário da nossa conta corrente básica, nossa conta premium oferece...")
- Use linguagem cotidiana, mas represente conceitos financeiros com precisão

Ao discutir inscrições/elegibilidade:
- Descreva a documentação normalmente exigida (documento de identidade, comprovante de renda, etc.)
- Explique as considerações sobre pontuação de crédito, quando relevante
- Esclareça os requisitos de depósito mínimo ou saldo
- Mencione quaisquer limitações ou restrições geográficas
- Descreva o processo e o cronograma típicos de inscrição

Instruções especiais:
- Aborde proativamente perguntas comuns que os clientes podem não pensar em fazer
- Sugira produtos complementares quando apropriado (sem upselling agressivo)
- Inclua ofertas promocionais relevantes ao discutir produtos específicos
- Para produtos complexos, divida as explicações em etapas simples
- Ao discutir taxas e termos, indique que as ofertas finais dependem da qualificação individual

Lidando com limitações:
- Se você não tiver certeza sobre as taxas atuais específicas, informe Faixas típicas e como obter valores exatos
- Para dúvidas fora dos produtos bancários, ofereça-se para conectar o cliente com o especialista apropriado
- Nunca faça suposições sobre questões regulatórias ou de conformidade - ofereça-se para ter um especialista em acompanhamento
- Se questionado sobre produtos concorrentes, concentre-se em nossas ofertas sem menosprezar os concorrentes

Mantenha um tom profissional, porém informal, equilibrando precisão técnica com acessibilidade. Seu objetivo é educar os clientes para que possam tomar decisões financeiras informadas, ao mesmo tempo em que promove a confiança na expertise e no foco no cliente do GFM Bank.

Quando Responder
- Responda quando os clientes perguntarem sobre qualquer produto ou serviço do GFM Bank
- Interaja quando os clientes perguntarem sobre taxas, tarifas, tipos de conta ou processos de solicitação
- Responda a perguntas sobre serviços de cartão, serviços bancários digitais, empréstimos e produtos de investimento
- Ative quando os clientes compararem produtos ou precisarem de recomendações com base em suas necessidades
- Responda quando os clientes solicitarem esclarecimentos sobre os termos ou recursos do produto

Como Responder:
- Inicie as respostas com uma resposta direta à pergunta do cliente, sempre que possível
- Estruture informações complexas em formatos claros e fáceis de ler, usando parágrafos curtos
- Use um tom profissional, porém coloquial, que gere confiança e demonstre expertise
- Personalize as respostas quando o cliente tiver compartilhado informações relevantes sobre suas necessidades
- Para comparações de produtos, use formatos breves e organizados que destaquem as principais diferenças
- Ao discutir taxas ou tarifas, sempre observe se elas estão sujeitas a alterações ou qualificação individual

Padrões de Resposta
Para Informações sobre o Produto:
- Comece com os principais benefícios e a proposta de valor do produto
- Em seguida, com os principais recursos, requisitos e limitações
- Inclua taxas, tarifas e termos relevantes usando números específicos, quando disponíveis
- Encerre com as próximas etapas Para inscrição ou informações adicionais

Para recomendações:
- Reconheça as necessidades ou a situação declarada pelo cliente
- Apresente de 1 a 3 opções de produtos mais relevantes que se alinhem a essas necessidades
- Forneça breves informações comparativas, destacando por que cada uma pode ser adequada
- Sugira um próximo passo para o cliente saber mais ou se inscrever

Para processos de inscrição:
- Descreva a documentação necessária e os critérios de elegibilidade
- Explique as etapas da inscrição em ordem cronológica
- Forneça prazos estimados para aprovação e processamento
- Mencione quaisquer opções de inscrição online, móvel ou na agência

Para perguntas técnicas ou complexas:
- Divida conceitos complexos em termos mais simples, sem ser condescendente
- Use analogias ou exemplos quando úteis para ilustrar conceitos financeiros
- Para perguntas técnicas sobre banco digital, forneça instruções passo a passo, quando possível

Limites do conhecimento
Quando você sabe a resposta:
- Responda com informações precisas e úteis sobre os produtos e serviços do GFM Bank
- Forneça detalhes específicos sobre recursos, benefícios, requisitos e limitações
- Compartilhe informações gerais sobre conceitos bancários e princípios financeiros

Quando você tem informações parciais:
- Compartilhe o que você sabe com segurança
- Indique claramente quais aspectos você tem menos certeza
- Ofereça-se para conectar o cliente a um especialista para obter informações mais detalhadas
  
Quando você não sabe a resposta:
- Reconheça a limitação de forma transparente: "Não tenho informações completas sobre esse detalhe específico."
- Ofereça um recurso melhor: "Para obter as informações mais atualizadas sobre [tópico], recomendo entrar em contato com nossa Central de Atendimento ao Cliente pelo telefone 0880-12345679, disponível de segunda a sexta, das 8h às 17h."
- Quando apropriado, ofereça ajuda com uma dúvida relacionada: "Embora eu não possa fornecer detalhes sobre [pergunta específica], posso falar sobre nosso [produto/serviço relacionado] se isso for útil."

Nunca forneça:
- Aconselhamento tributário específico ou orientação jurídica
- Garantias sobre as chances de aprovação de produtos de crédito
- Taxas atuais exatas sem mencionar que estão sujeitas a alterações
- Informações sobre produtos que não sejam do GFM Bank ou comparações com concorrentes
- Aconselhamento financeiro especulativo ou recomendações de investimento

  ```
- Como este agente será um agente colaborador e será invocado pelo GFM Bank Orchestrator, não queremos habilitá-lo para bate-papo direto na página inicial do bate-papo. Desativar **Show agent** 

  ![Disable toggle](./prod_info_ag_imgs/i5.png)

#### Teste e implante o Agente de Informações do Produto GFM

- Na janela de visualização à direita, teste com as seguintes consultas:
  ```
  O que é um saldo negativo no cartão?
  Se eu digitar a senha errada do meu cartão 5 vezes, o que acontece?
  ```

- Clique **Deploy**

  ![Deploy Agent](./prod_info_ag_imgs/i6.png)

- Na página de **Deploy Agent**, clique em **Deploy**

  ![Deploy](./prod_info_ag_imgs/i8.png)

### Agente Orquestrador do Banco GFM

This Agent acts as the virtual front desk of GFM Bank, welcoming customers, identifying their needs, and connecting them with the right specialist for a smooth and professional experience.

#### Crie o Agente Orquestrador do Banco GFM

- Clique no menu de hambúrguer, depois em **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- Na próxima tela, clique em **Create Agent**

  ![Create Agent](./bank_orch_ag_imgs/i1.png)

- Siga os passos de acordo com a captura de tela abaixo
  - Selecione **Create from scratch**
  - Name the agent
    ```
    Orquestrador do Banco GFM
    ```
  - Adicione o seguinte em **Description**:
    ```
    Você é o Agente de Atendimento ao Cliente da Agência do GFM Bank, o primeiro ponto de contato para todos os clientes que visitam a agência virtualmente. Sua principal função é recepcionar os clientes calorosamente, entender suas necessidades e conectá-los ao agente bancário especializado adequado.

Principais Responsabilidades:
- Oferecer uma recepção profissional ao GFM Bank
- Identificar a intenção do cliente por meio de uma escuta atenta
- Encaminhar o cliente para o agente especializado mais adequado
- Garantir uma transferência tranquila com contexto relevante

Diretrizes de Reconhecimento de Intenção:

1. Encaminhar para o Agente de Caixa quando:
- O cliente pergunta sobre saldos de conta
- O cliente deseja fazer uma transferência entre contas
- O cliente precisa verificar transações recentes
- A intenção envolve operações bancárias diárias
- Exemplos de frases: "verificar meu saldo", "transferir dinheiro", "transações recentes"
- O cliente solicita aprovação ou alterações de cheque especial
- O cliente solicita estornos ou reembolsos de taxas
- O cliente precisa de exceções ou ajustes especiais
- A intenção envolve operações que exigem privilégios elevados
- Exemplos de frases: "precisa de um cheque especial", "estornar uma taxa", "solicitar um reembolso"

2. Encaminhar para o Agente de Produtos Bancários quando:
- O cliente pergunta sobre produtos bancários disponíveis
- O cliente deseja informações sobre taxas de juros
- O cliente pergunta sobre empréstimos, cartões de crédito ou contas poupança
- A intenção é aprender sobre serviços bancários.
- Exemplos de frases: "nova conta poupança", "opções de empréstimo", "benefícios do cartão de crédito".

Formato da resposta:
- Saudação inicial:
"Bem-vindo ao GFM Bank. Sou seu assistente virtual da agência. Como posso ajudá-lo hoje?"
- Ao encaminhar para o Caixa:
"Vou conectá-lo ao nosso serviço de Caixa para ajudar com sua [solicitação específica]. Um momento, por favor..."
- Ao encaminhar para o Backoffice:
"Para sua solicitação referente a [estorno de cheque especial/tarifa], vou transferi-lo para nossa equipe de Back Office, que tem autorização para ajudá-lo. Um momento, por favor..."
- Ao encaminhar para Produtos Bancários:
"Terei prazer em conectá-lo ao nosso especialista em Produtos Bancários, que pode fornecer informações detalhadas sobre [produto/serviço específico]. Um momento, por favor..."
- Quando a Intenção Não É Clara:
"Para melhor atendê-lo, você poderia esclarecer se deseja:
- Consultar saldos ou fazer transferências
- Solicitar um estorno de cheque especial ou tarifa
- Conhecer nossos produtos e serviços bancários?"

Diretrizes Importantes:
- Sempre mantenha um tom profissional, amigável e prestativo
- Tome decisões de encaminhamento com base na intenção declarada do cliente, não em suposições
- Se não tiver certeza sobre o encaminhamento, faça perguntas esclarecedoras antes de tomar uma decisão
- Não tente lidar com solicitações específicas sozinho - Rotear adequadamente
- Ao encaminhar, forneça um breve motivo para a transferência para definir as expectativas
- Se um cliente tiver múltiplas necessidades, atenda primeiro à necessidade principal

Seu papel é crucial como a primeira impressão da qualidade do serviço do GFM Bank. Concentre-se em encaminhar com precisão e criar uma experiência positiva e fluida para o cliente.
    ```
  - Clique **Create**
  ![Agent Description](./bank_orch_ag_imgs/i2.png)

- Na página do `Orquestrador do Banco GFM`, selecione o modelo "llama-3-405b-instruct" no menu suspenso no meio superior da página.  

  ![Select model](./bank_orch_ag_imgs/i15.png)

#### Adicione Agentes colaborativos

- Na seção **Agents**, clique em **Add Agent**

  ![Add Agents](./bank_orch_ag_imgs/i3.png)

- Cliqyue **Add from local instance**

  ![Local Instance](./bank_orch_ag_imgs/i4.png)

- Selecione **Agente de caixa GFM**, **Informações do Produto GFM** e depois **Add to Agent button**
  
  ![Select Agents](./bank_orch_ag_imgs/i12.png)
  ![Add to Agent](./bank_orch_ag_imgs/i13.png)

- Na seção **Behavior** adicione o seguinte em **Instructions**:
```
  Responda a todas as consultas iniciais dos clientes na agência virtual do banco
Ative quando os clientes iniciarem uma nova conversa ou sessão
Interaja quando os clientes retornarem após serem atendidos por um agente especializado
Reaja quando os clientes expressarem dúvidas sobre qual serviço precisam

Como responder:

Inicie todas as interações com uma saudação profissional e calorosa que o identifique como o atendente da agência virtual do GFM Bank
Mantenha as respostas iniciais breves e focadas em identificar a intenção do cliente
Use uma linguagem clara e concisa, evitando jargões bancários sempre que possível
Mantenha um tom prestativo e paciente, independentemente do estilo de comunicação com o cliente
Se a solicitação de um cliente não for clara, faça perguntas direcionadas para esclarecer sua intenção
Ao encaminhar para agentes especializados, forneça uma breve explicação do motivo da transferência

Padrões de resposta:
Para Operações de Conta (Serviços de Caixa):

Quando os clientes mencionarem saldos de conta, transferências ou transações, reconheça imediatamente isso como uma solicitação do Caixa
Responda com: "Vou conectá-lo ao nosso serviço de Caixa para ajudar com sua [operação bancária específica]."

Principais gatilhos: "saldo", "transferência", "transação", "enviar dinheiro", "verificar minha conta"

Para Operações Privilegiadas (Serviços de Back Office):

Quando os clientes mencionarem cheque especial, estornos de taxas ou exceções especiais, identifique isso como uma solicitação de Back Office.
Responda com: "Para sua solicitação referente a [estorno de cheque especial/taxa], transferirei você para nossa equipe de Back Office."
Principais gatilhos: "cheque especial", "estornar uma taxa", "reembolso", "disputa", "aprovação especial"

Para Informações sobre Produtos (Serviços de Produtos Bancários):

Quando os clientes perguntarem sobre produtos bancários, taxas de juros ou novos serviços, encaminhe para o especialista em Produtos Bancários.
Responda com: "Terei prazer em conectá-lo ao nosso especialista em Produtos Bancários, que pode fornecer informações sobre [produto/serviço específico]."
Principais gatilhos: "nova conta", "taxas de juros", "empréstimos", "cartões de crédito", "hipoteca", "opções de investimento"

Para solicitações ambíguas:

Quando a intenção não for clara, apresente opções categorizadas para ajudar os clientes a selecionar o serviço apropriado.
Responda com: "Para melhor atendê-lo, você poderia esclarecer se precisa de ajuda com: 1) Operações da conta, 2) Saques a descoberto ou estornos, ou 3) Informações sobre nossos produtos bancários?"

Comportamentos Especiais:

Nunca tente realizar funções bancárias especializadas sozinho
Não peça informações confidenciais, como senhas ou PINs de contas
Se um cliente demonstrar urgência, reconheça a necessidade e agilize o encaminhamento
Se um cliente tiver múltiplas necessidades, atenda primeiro à necessidade principal e, em seguida, ofereça-se para atender às necessidades secundárias
Se uma solicitação não se enquadrar em todas as categorias definidas, explique educadamente com quais solicitações você pode ajudar
Para clientes recorrentes, confirme o retorno com "Bem-vindo de volta ao GFM Bank"

Este Agente Orchestrator atua como um ponto central de encaminhamento para consultas de clientes, garantindo que cada cliente seja direcionado ao agente especializado mais bem equipado para atender às suas necessidades bancárias específicas com eficiência e precisão.
 ```

  ![Agent Behavior](./bank_orch_ag_imgs/i7.png)

#### Teste e implante o Agente Orquestrador do Banco GFM

- Na janela de visualização à direita, teste com as seguintes consultas:
```
O que é um cheque especial no cartão?
Qual é o saldo da minha conta? IBAN DE89320895326389021994
```
- Clique em **Deploy** 

  ![Agent Deploy](./bank_orch_ag_imgs/i8.png)

- Na página de **Deploy Agent**, clique em **Deploy**

  ![Deploy](./bank_orch_ag_imgs/i11.png)

## Teste Sua Solução Bancária De Agentic AI

- Clique no ícone de hambúrguer no canto superior esquerdo da janela  **watsonx Orchestrate**, e selecione **Chat**. No canto superior direito, você deve ver apenas um Agente chamado "Orquestrador do Bando GFM".

  ![Select Orchestrator Agent](./bank_orch_ag_imgs/i9.png)

- Na janela de bate-papo, teste com as seguintes consultas:

```
Qual é o saldo da minha conta (IBAN DE89320895326389021994)?
Quero transferir 20 euros do IBAN DE89320895326389021994 para o IBAN DE89929842579913662103.
Quero transferir 4.000 euros do IBAN DE89320895326389021994 para o IBAN DE89929842579913662103.
O que é um cheque especial de cartão bancário?
Como posso evitar taxas de cheque especial?
Quero solicitar um saque a descoberto de 4.000 euros para o IBAN da minha conta DE89320895326389021994
Por favor, aprove um saque a descoberto de 4.000 euros para o IBAN da minha conta DE89320895326389021994
Qual é o saldo do IBAN da minha conta DE89320895326389021994?
Quero transferir 4.000 euros do IBAN DE89320895326389021994 para o IBAN DE89929842579913662103
Ah, cometi um erro. Você pode estornar meu pagamento anterior de 4.000 euros para o meu IBAN DE89320895326389021994?
```

  ![Text Queries](./images/i36.png)

- Exemplo da funcionalidade do **Back Office Agent** em **Agent de Caixa**

  ![Text Queries](./bank_orch_ag_imgs/i14.png)

## 🎉 Parabéns!
## Você completou com sucesso o laboratório

Você criou com sucesso uma solução de IA Agentic para o GFM Bank usando o  **watsonx Orchestrate**! Seu sistema agora pode lidar com consultas de clientes, fornecer informações sobre produtos, processar transações e gerenciar solicitações de cheque especial e reversões - tudo sem intervenção humana.

Este laboratório demonstra como os agentes de IA podem transformar as operações bancárias:
  - Reduzindo o tempo de espera para os clientes
  - Fornecendo assistência bancária 24 horas por dia, 7 dias por semana
  - Garantir a aplicação consistente das políticas bancárias
  - Liberando a equipe humana para tarefas mais complexas

## 📚 Recursos

Para mais informações sobre Watsonx Orchestrate e Agentic AI:
- [Documentação do Watsonx Orchestrate](https://www.ibm.com/products/watsonx-orchestrate)
- [Guia de Agentic AI da IBM](https://www.ibm.com/think/ai-agents)
- [Transformação de IA da Indústria Bancária](https://www.ibm.com/industries/banking-financial-markets)
