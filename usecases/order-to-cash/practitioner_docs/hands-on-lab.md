
# 👨🏻‍💻 Caso de Uso: Order to Cash  

## Índice
- [👨🏻‍💻 Caso de Uso: Order to Cash](#-caso-de-uso-order-to-cash)
  - [Índice](#índice)
  - [Descrição do caso de uso](#descrição-do-caso-de-uso)
  - [Arquitetura  ](#arquitetura--)
  - [Pré requisitos](#pré-requisitos)
  - [watsonx Orchestrate](#watsonx-orchestrate)
    - [Acessando o watsonx Orchestrate](#acessando-o-watsonx-orchestrate)
  - [Criação do Agente Order-to-Cash](#criação-do-agente-order-to-cash)
    - [Configuração do agente com base de conhecimento](#configuração-do-agente-com-base-de-conhecimento)
  - [Criação e configuração do agente de suporte ao cliente](#criação-e-configuração-do-agente-de-suporte-ao-cliente)
  - [Criação e configuração do agente de gerenciamento de pedidos](#criação-e-configuração-do-agente-de-gerenciamento-de-pedidos)
  - [Juntando tudo - Colaboração completa dos agentes](#juntando-tudo---colaboração-completa-dos-agentes)
  - [Experimente os agentes em ação no watsonx Orchestrate](#experimente-os-agentes-em-ação-no-watsonx-orchestrate)
  - [Conclusão](#conclusão)

## Descrição do caso de uso

Este caso de uso foca na **transformação do processo Order-to-Cash (O2C) de ponta a ponta** usando o **watsonx Orchestrate**, conforme ilustrado no diagrama de arquitetura.  

A solução tem como objetivo:

- Automatizar as principais etapas do ciclo O2C — da colocação do pedido ao faturamento.
- Aumentar a satisfação do cliente.
- Acelerar o fluxo de caixa.
- Gerar impacto mensurável nos resultados financeiros por meio da integração de **agentes inteligentes** e **sistemas corporativos**.


<b>O que você fará neste laboratório?</b>

Você construirá um **Agente O2C no watsonx Orchestrate** que simula interações com funções essenciais do negócio, como:

- **Suporte ao cliente**.
- **Gerenciamento de pedidos**.

Esse agente irá:

- Otimizar o gerenciamento de pedidos.
- Reduzir o esforço manual.
- Acelerar o processamento de faturas.
- Impulsionar a conversão de caixa mais rapidamente.

Tudo isso contribui para **melhorar a eficiência operacional** e **aumentar a satisfação do cliente**.

## Arquitetura  <a id="architecture"></a>

<img width="900" alt="image" src="./images/arch.png">

## Pré requisitos

Para executar as etapas desta parte do laboratório prático do bootcamp, você precisa ter acesso ao <b>watsonx Orchestrate</b> que são fornecidos a você como parte da preparação para este bootcamp.

## watsonx Orchestrate

Conforme detalhado na Arquitetura da solução, a maior parte dos agentes será construída e implementada no <b>watsonx Orchestrate</b>.

Os **agentes de IA** são entidades autônomas capazes de executar tarefas, tomar decisões e interagir com seu ambiente.  
No <b>watsonx Orchestrate</b>, eles são um componente-chave da nossa estrutura de **IA agêntica**, permitindo criar sistemas complexos e dinâmicos que se adaptam e respondem a condições em constante mudança.

### Acessando o watsonx Orchestrate

Se você ainda não estiver conectado à sua conta do IBM Cloud, navegue no seu navegador preferido até https://cloud.ibm.com e efetue login com suas credenciais (que você usou para sua reserva no TechZone).

Na página inicial do IBM Cloud:

1 - Clique no menu de navegação superior esquerdo (menu de hambúrguer) e selecione **Resource list**.

*Observação: se você for membro de várias contas do IBM Cloud, certifique-se de estar trabalhando na conta correta, que possui os serviços necessários disponíveis.

![IBM Cloud Resource List](./images/ibm_cloud_resources.png) 

2 - Na página Lista de recursos, expanda a seção **AI / Machine Learning** e clique no nome do serviço <b>watsonx Orchestrate</b>
![IBM Cloud wxo](./images/ibm_cloud_wxo.png) 

3 - Clique no botão azul, em `Launch watsonx Orchestrate`

![wxo launch](./images/wxo-launch.png) 

Essa é a página inicial do <b>watsonx Orchestrate</b>, conforme ilustrado na figura abaixo. Você verá uma interface de conversação intuitiva com um campo de bate-papo onde poderá digitar qualquer texto para começar a interagir com o <b>watsonx Orchestrate.</b>

Navegue no ícone do menu (ícone de hamburguer) ao lado esquerdo da trela, clique em `Agent Builder`

![wxo agent builder](./images/wxo-nav-menu-agent-builder.png) 
  
## Criação do Agente Order-to-Cash

A página **Gerenciar agentes** estará inicialmente **em branco**, pois nenhum agente foi criado ainda.  

À medida que você cria **agentes de IA capazes de raciocinar e agir**, essa página será preenchida com os agentes disponíveis, permitindo que você visualize, edite e gerencie cada um deles.

1 - Clique no botão `Create agent +` para começar a criar seu primeiro agente.
   
![wxo create agent](./images/wxo-create-agent-manage-agents-empty.png) 

2 - Na página Criar um agente, selecione **Create from scratch**, forneça um **Nome** e **Descrição** para o agente e clique em **Create**.

<b>Nome</b>

```Agente Order-to-Cash```

<b>Descrição:</b>
```
Este Agente Supervisor orquestra e gerencia o fluxo de conversas, encaminhando de forma inteligente as consultas dos usuários para os agentes especializados apropriados, com base no contexto.
O Agente Supervisor supervisiona dois agentes específicos de domínio:
1. Agente de Gerenciamento de Pedidos
2. Agente de Suporte ao Cliente
Ele também lida com consultas gerais, encaminhando-as para uma base de conhecimento.
```

O <b>watsonx Orchestrate</b> permite a criação de um agente do zero ou a partir de um modelo, o que envolve navegar por um catálogo de agentes existentes e usar atributos de outro agente como modelo para o novo agente. Neste laboratório, você criará agentes do zero.

![wxo order to cash agent](./images/img20.png) 

### Configuração do agente com base de conhecimento

4 - Após criar o agente de IA, nesta seção você realizará a **configuração necessária** para que ele funcione corretamente. O processo inclui:

- **Adicionar conhecimento**: Integrar informações da base de conhecimento para que o agente possa responder às consultas com precisão.
- **Configurar ferramentas**: Habilitar recursos que permitam ao agente executar tarefas de forma automatizada.

A página do <b>watsonx Orchestrate </b> é divida em duas partes. A metade direita é uma interface de chat de **Preview** que permite testar o comportamento do seu agente. A metade esquerda da página consiste em quatro seções principais que você pode usar para configurar seu agente.

Vamos dar uma olhada em cada elemento presente:
<br>
- <b>Profile: </b> A seção **Profile** contém a descrição do agente que você forneceu ao criá-lo. Você pode acessar esta seção para editar e refinar a descrição do agente conforme necessário.
<br>
- <b>Welcome Message:</b> Ainda durante a etapa de definição do tipo de agente, você também pode configurar uma mensagem de boas vindas que será exibida na interface para o usuário, como mostrado na imagem abaixo. Essa etapa é opcional e você pode definir algo como: Bem vindo ao Agente X
<br>
- <b>Quick start Prompts:</b> Esse passo também é opcional. Nessa sessão podemos definir atalhos para o usuário, essas mensagens serão exibidas para o usuário como botões na interface. Você pode criar esses botões clicando em `Add prompt +` e removê-los clicando no ícone de lixeira.  Para que essas opções apareçam na telinha de preview do lado direito da tela, use o ícone de restart para atualizar a interface. <b>Não é necessário sair da página.</b>
<br>
- <b>Knowledge:</b> A seção **Knowledge** é onde você pode adicionar conhecimento ao agente. Adicionar conhecimento aos agentes desempenha um papel crucial no aprimoramento de suas capacidades de conversação, fornecendo-lhes as informações necessárias para gerar respostas precisas e contextualmente relevantes para casos de uso específicos. Você pode enviar arquivos diretamente para o agente ou conectar-se a uma instância do <b>Milvus</b>, </b>Elasticsearch, AstraDB ou algum outro banco de dados vetorial da sua preferência, como um repositório de conteúdo. Por meio dessa interface de  **Knowledge**, você pode habilitar seus agentes de IA para implementar o padrão de Geração Aumentada de Recuperação (RAG), um padrão de IA muito popular para fundamentar respostas em uma fonte confiável de dados, como uma base de conhecimento empresarial.  
<br>
- <b>Toolset:</b> Enquanto *Knowledge* é como você capacita os agentes com uma base de conhecimento confiável, **Toolset** é como você capacita os agentes a agir, fornecendo-lhes Ferramentas e Agentes . Os agentes podem realizar tarefas usando **Tools** ou delegar tarefas a outros **Agentes** que sejam profundamente qualificados nessas tarefas.
<br> 
- <b>Behavior:</b> A seção **Behavior** do agente é onde você fornece instruções ao agente para definir como ele responde às solicitações e situações do usuário. Você pode configurar regras que determinam quando e como o agente deve agir. Essas regras ajudam o agente a se comportar de maneira previsível e consistente, proporcionando uma experiência perfeita ao usuário.
<br>
- <b>Channels:</b> A seção **Channels** é onde você pode conectar seu agente aos canais que sua equipe usa para se comunicar (em pré-visualização). Você pode habilitar seu agente para se comunicar via equipes, WhatsApp com Twilio, Facebook Messenger e Genesys Bot Connector, e etc.

Por fim, após concluir a configuração do agente e testar seu desempenho, você pode **implantar** o agente para disponibilizá-lo no canal selecionado.

![wxo create agent config](./images/img21.png) 

5 - Na página de configuração do agente, revise a *Descrição* do agente na seção  **Profile** e mantenha-a como está (sem necessidade de edição).

6 - Em seguida, role para baixo até a seção **Knowledge**, ou clique no atalho **Knowledge**. Na seção Knowledge adicione uma descrição para informar o agente sobre o conteúdo do conhecimento. Para este laboratório, adicione a seguinte descrição, pois forneceremos ao agente um documento de Perguntas Frequentes (FAQ) sobre o processo Order to Cash.

Descrição: 

```Este conhecimento aborda todas as dúvidas relacionadas ao processo Order to Cash.```

7 - Na etapa de **knowledge**, o <b>watsonx Orchestrate</b> oferece duas formas atualizadas de adicionar conhecimento:

`Upload de Arquivos`

Você pode enviar documentos diretamente pela interface:

- **Tipos suportados**:
  - `.docx`, `.pdf`, `.pptx`, `.xlsx`: até 25 MB cada
  - `.csv`, `.html`, `.txt`: até 5 MB cada [1](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-uploading-files-as-knowledge-source)[2](https://developer.watson-orchestrate.ibm.com/knowledge_base/build_kb)
- **Limites**:
  - Até 20 arquivos por lote
  - Total máximo de 30 MB por upload [1](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-uploading-files-as-knowledge-source)[2](https://developer.watson-orchestrate.ibm.com/knowledge_base/build_kb)
- **Recursos adicionais**:
  - Inclua URLs para consulta da fonte original
  - Dados armazenados com segurança na região do cluster [1](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-uploading-files-as-knowledge-source)

`Integração com Repositórios Externos`

Ideal para conteúdo dinâmico e frequentemente atualizado:

- **Suporte a Milvus, Elasticsearch, Astra DB ou serviços customizados** [3](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-adding-knowledge)[4](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-building-knowledge-source)
- Permite criar fontes reutilizáveis e conectar múltiplos agentes [4](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-building-knowledge-source)[2](https://developer.watson-orchestrate.ibm.com/knowledge_base/build_kb)
- A configuração pode ser feita via interface ou usando o ADK (CLI) [2](https://developer.watson-orchestrate.ibm.com/knowledge_base/build_kb)[5](https://developer.watson-orchestrate.ibm.com/knowledge_base/deploy_kb)

**No laboratório**: clique em **Upload files**

![wxo agent config knowledge](./images/img35.png) 

8 - Arraste e solte o arquivos PDF "Order to Cash FAQs pt_BR.pdf" para enviar ao conhecimento do agente (O arquivo `Order to Cash FAQs pt_BR.pdf` está disponível na pasta "7. Automation do Order to Cash" gerada após a descompactação do arquivo LABS.zip)

9 - Após o upload de todos os arquivos para a base de conhecimento, você pode começar a testar o agente para validar como ele responde a perguntas usando essa base de conhecimento. Os arquivos enviados são processados ​​e preparados para serem utilizados pelo agente. Após a conclusão do upload, teste o agente fazendo algumas perguntas, como:

```O que devo fazer se houver um problema com a entrega do meu pedido, como atrasos ou produtos danificados? ```

```Quais métodos de pagamento são aceitos?```

10 - Você deverá ver as respostas sendo recuperadas dos documentos enviados e, em seguida, a resposta final gerada pelo agente, conforme ilustrado na figura abaixo.

![wxo agent knowledge test](./images/img37.png) 

**NÃO é NECESSÁRIO NEM FAZER IMPLANTAR/FAZER DEPLOY NESTE MOMENTO**

Neste momento, vale a pena refletir sobre o que você desenvolveu até agora. Você projetou um agente e o capacitou com uma base de conhecimento para que ele possa responder a consultas em contexto usando sua base de conhecimento. *Parabéns!*

## Criação e configuração do agente de suporte ao cliente

Nesta seção, você irá criar o **Agente de Suporte ao Cliente**, um agente colaborador projetado para:

- **Atender dúvidas dos clientes**.
- **Recuperar conversas de e-mail relevantes**.
- **Fornecer atualizações de pedidos em tempo real**.

<b>Como o agente funciona?</b>

Este agente é alimentado por uma combinação de ferramentas:

- **Ferramenta de Recuperação de E-mails**: acessa mensagens enviadas pelos clientes.
- **Ferramenta de Consulta de Pedidos**: obtém o status atualizado dos pedidos.

O agente espelha processos reais de suporte, permitindo:

- Selecionar respostas adequadas.
- Opcionalmente, enviar e-mails aos clientes.
- Executar tudo dentro de um **fluxo de conversa guiado**.

11 - Retorne para a página de criação e gerenciamentos de agentes e clique em  **Create agent** para começar a desenvolver um novo agente, o Agente de Suporte ao Cliente.

![wxo landing page create agent](./images/wxo-landing-page-create-agent.png) 

12 - Na página de criação de um agente/Create new agent, selecione o bloco `Create from scratch` forneça um  **Nome** e uma **Descrição** para o agente e clique em `Create`

<b>Nome:</b>
```Agente de Suporte ao Cliente```

Descrição: 
```
Este agente é útil para todas as consultas de suporte ao cliente. Ele busca todos os endereços de e-mail dos usuários, recupera atualizações de pedidos com base na entrada do usuário (ID do pedido) na ferramenta e envia um e-mail relevante ao usuário com a respectiva atualização do pedido.
```
A descrição de um agente é importante, pois ela é aproveitada pela solução de agente para encaminhar mensagens do usuário ao agente certo e qualificado para atender à solicitação.

![wxo create customer support agent](./images/img1.png) 

13 -  Na página de configuração do agente, role para baixo até a seção **Toolset** ou clique no atalho. Em seguida, clique no botão **Add tool** para abrir a janela para adicionar ferramentas ao agente.

![wxo agent tools](./images/img3.png) 

14 - Na janela _pop up_ de opções da ferramenta, selecione **Import** conforme ilustrado na figura abaixo.

![wxo tool options](./images/img4.png) 
![wxo tool options](./images/img4.1.png) 

O <b>watsonx Orchestrate</b> oferece suporte a diversas abordagens para adicionar ferramentas aos agentes:

- Adicionar do catálogo: A opção **Add from catalog** permite adicionar uma ferramenta de um amplo catálogo de ferramentas predefinidas. O catálogo de ferramentas está sendo desenvolvido ativamente para facilitar ainda mais a adição de ferramentas aos agentes.

- Adicionar da instância local: A opção **Add from local instance** opermite que você adicione uma ferramenta de um conjunto existente de ferramentas já carregadas na instância local do watsonx Orchestrate.

- Importar: A opção **Import** permite que você importe uma ferramenta externa usando uma especificação **OpenAPI** e selecionando quais operações você deseja importar como ferramentas.

- Criar um novo fluxo: A opção **Create a new flow** fornece uma interface de criação de ferramentas de arrastar e soltar para criar uma sequência de etapas que utilizam controles e atividades condicionais.

Para fins do Agente Order-to-Cash, você usará a opção **Import** e, em seguida **Import from file** tpara importar uma especificação OpenAPI e definir quais operações importar como ferramentas. Você precisará de um arquivo de especificação OpenAPI, que está disponível na pasta "7. Automation do Order to Cash" gerada após a descompactação do arquivo LABS.zip.

15 - Na página da ferramenta Importar, arraste e solte o arquivo de especificação **customer_support.yml** (disponível na pasta "7. Automation do Order to Cash" gerada após a descompactação do arquivo LABS.zip.) e clique em **Next**.

![wxo tool import openapi](./images/img2.png) 

16 - Em seguida, marque as caixas de seleção para as operações **Obter detalhes do pedido** , **Obter todos os pedidos** e **Obter todos os e-mails** e clique em **Done**.

![wxo tool import operations](./images/img5.png) 

17 - Neste ponto, você verá as três ferramentas importadas na subseção Ferramentas, o que significa que elas estão disponíveis para o **Agente de Suporte ao Cliente** usar essas ferramentas na execução de tarefas.

18 - Em seguida, role mais para baixo até a seção **Behavior** ou clique no atalho **Behavior** e adicione as seguintes instruções para orientar o agente em seu raciocínio e orquestração.

<b>Instruções de comportamento do Agente </b>

`````````````````````````````````````````````````
### **Condição de Acionamento**
Quando um usuário inicia uma conversa ou faz uma pergunta contendo a palavra-chave
```mostrar todos os meus e-mails, atendimento ao cliente, lista de clientes ou frases relacionadas```

### **Etapa 1**: Exibir todos os e-mails de clientes
* **Ação**: Acionar a ferramenta get_all_mails para buscar todos os dados do e-mail
* **Formato de Resposta**: Apresentar a tabela com todas as colunas-chave: nome do e-mail, endereço, cc, bcc, assunto, a partir dos dados buscados.
* **Prompt**:
```Aqui está a lista de todos os e-mails disponíveis.     
| Para o Nome             | Para endereço de email                                             |
| --------------------------- | ------------------------------------------------------------- |
| Acme Corp - John Smith      | [john.smith@acmecorp.com](mailto:john.smith@acmecorp.com)     |
| Globex Ltd - Maria Gonzales | [maria.gonzales@globex.com](mailto:maria.gonzales@globex.com) |

    Por favor selecione o nome ou e-mail do cliente.
    ```

### **Etapa 2**: Entrada e Validação de E-mail
* **Ação**: Aguarde o usuário inserir um nome ou e-mail.
* **Validação**:
* Caso não encontre, responda com:
```O endereço de e-mail selecionado não está na lista. Escolha um válido entre os acima.```
* Se válido, prossiga para a próxima etapa.

### **Etapa 3**: Exiba todos os pedidos de 'obter Todos os Pedidos(2)' primeiro e peça ao usuário o ID do Pedido na lista exibida para obter a atualização do pedido.
* **Solicitação**:
```Aqui está a lista de IDs de pedidos. Selecione o ID do Pedido cuja atualização você deseja verificar.```
* **Ação**: Exiba todos os IDs de pedidos e aguarde a entrada do usuário.

### **Etapa 4**: Exibir Atualização do Pedido
* **Ação**: Acione a ferramenta get_order_details com o ID do Pedido fornecido.
* **Formato de Resposta**: Exiba a atualização do pedido de forma organizada em formato de tabela.

### **Etapa 5**: Peça para entrar em contato com o cliente
* **Solicitação**:
```Você gostaria de entrar em contato com este cliente sobre este pedido? (sim/não)```

### **Etapa 6**: Solicitar Curadoria de E-mail
* **Solicitação**:
```Deseja que eu redija um e-mail com a atualização do pedido acima para o cliente selecionado? (sim/não)```

### **Etapa 7**: Redigir E-mail
* **Condição de Acionamento**: Se o usuário responder sim.
* **Ação**: Gerar e-mail automaticamente.
* **Formato do E-mail**:
    ```Para: abc@acmecorp.com
    Assunto: Atualização do seu Pedido xyzzy
    Prezado abc,
    Agradecemos o seu contato. Aqui estão os detalhes do seu pedido:
    - ID do Pedido: xyzzy
    - Data do Pedido: 25/01/2025

    O pedido está atrasado porque a quantidade solicitada não está disponível no estoque atual.
    Data de entrega atualizada: 25/01/2025

    Caso tenha alguma dúvida ou precise de mais assistência, entre em contato conosco.

    Atenciosamente,
    Equipe de Suporte ao Cliente```
* **Solicitação**:
```Deseja enviar o e-mail acima ao cliente agora? (sim/não)```

### **Etapa 8**: Enviar o e-mail
* **Condição de gatilho**: Se o usuário selecionar "sim" para enviar o e-mail.
* **Resposta:
```E-mail enviado com sucesso para john.smith@acmecorp.com.```

### **Princípios de design**
* Interação passo a passo limpa e intuitiva
* Validação de entrada para reduzir erros
* Prompts claros em cada etapa para orientar o usuário
* Formatação estruturada para facilitar a leitura
* Segue um fluxo de trabalho de suporte do mundo real
`````````````````````````````````````````````````

![wxo customer support agent behavior](./images/img6.png)

19 - Agora que você concluiu a criação do agente e adicionou as ferramentas necessárias, teste as ferramentas na seção **Preview** fazendo uma pergunta de exemplo, como:

```mostrar todos os e-mails```

```lista de clientes```

Observe a resposta baseada nas informações retornadas pela ferramenta de e-mail. Para verificar isso, clique no link **Show Reasoning** para expandir o raciocínio do agente. Observe que o agente está chamando corretamente a ferramenta **Obter Todos os E-mails** e que ela mostra tanto a entrada quanto a saída da chamada da ferramenta.

![wxo tool mails](./images/img7.png) 
![wxo tool mails](./images/img8.png) 

20 - Digite um dos nome de clientes da lista retornada pelo Agente (Ex: Globex Ltd - Maria Gonzales) para listar os ids de pedidos. Em seguida digite um dos ids retornados pelo agente para obter os detalhes do pedido e depois entrar em contato com o cliente, redigir e enviar um e-mail.

Novamente, observe a resposta e expanda o link **Show Reasoning** para rastrear o raciocínio do agente, que neste caso acionou corretamente a ferramenta **Obter detalhes do pedido**.

![wxo tool order](./images/img9.png)  
![wxo tool order](./images/img10.png)

21 - Neste ponto, você está pronto para implantar seu agente. Para isso, role até o final da página de configuração e certifique-se de que a barra deslizante ao lado de **Show agent** esteja desabilitada. Clique no botão **Deploy** para implantar o agente e torná-lo disponível para uso como um agente colaborador.

![wxo order managemen agent deploy](./images/show-chat.png)
![wxo o2c deploy](./images/img11.png) 

*Parabéns! Você acabou de concluir o desenvolvimento do **Agente de Suporte ao Cliente** , equipado com ferramentas para retornar dados de e-mail e atualizações de pedidos.

## Criação e configuração do agente de gerenciamento de pedidos

Nesta seção, você criará o **Agente de Gerenciamento de Pedidos** , um agente colaborador essencial responsável por gerenciar o fluxo de ponta a ponta de pedidos de compra (POs) dentro do ciclo de vida do Pedido ao Pagamento (O2C). Este agente foi projetado para otimizar o processamento de pedidos interagindo com sistemas externos, como bancos de dados e plataformas ERP (por exemplo, SAP), ajudando os usuários a recuperar detalhes de POs e cotações, validar entradas e fazer pedidos com eficiência. Neste laboratório, o agente estará equipado com ferramentas como **Buscar Todos as ordens de pedidos** , **Obter Detalhes da ordem de pedido** , **Obter Detalhes da Cotação** e **Exibir Confirmação** para simular a automação empresarial do mundo real.

22 - Navegue novamente para a página de criação/gerenciamento de agentes, clique em `Create new agent +` para começar a criar o agente de gerenciamento de pedidos.

23 - Clique em `Create from scratch` novamente

Defina o seguinte:

<b>Nome:</b>

```Agente de Gerenciamento de Pedidos```

<b>Descrição:</b> 

```
Este agente foi projetado para lidar com consultas de usuários relacionadas ao gerenciamento de pedidos. Ele recupera os detalhes do pedido de compra (PO) juntamente com as informações de cotação correspondentes, garantindo que os usuários recebam dados precisos e atualizados. Assim que as informações são recuperadas, o agente responde com uma mensagem de confirmação: "Seu pedido foi feito com sucesso."
```

![wxo create order management agent](./images/img12.png)

24 - Na página de configuração do agente, role para baixo até a seção **Toolset** ou clique no atalho **Toolset**e, em seguida, clique em **Add tool**.

25 - Como explicado anteriormente, o Watsonx Orchestrate oferece suporte a diversas abordagens para adicionar ferramentas aos agentes. Para o Agente de Gerenciamento de Pedidos, você utilizará a funcionalidade de **Import**, como fez anteriormente. Clique no bloco **Import from file**.

26 - Na página da ferramenta Importar, arraste e solte o arquivo de especificação **order_management.yml** fornecido pelo seu instrutor e clique em **Next**. (O arquivo order_management.yml" está disponível na pasta "7. Automation do Order to Cash" gerada após a descompactação do arquivo LABS.zip)

![wxo order managemen agent tool import openapi](./images/img13.png) 

27 - Em seguida, marque as caixas de seleção para as operações **Buscar todos os pedidos de compra** , **Obter detalhes do pedido de compra** , **Obter detalhes da cotação**, **Obter detalhes correspondentes** e **Exibir confirmação** e clique em **Done**.

![wxo order management agent tool import operations](./images/img38.png) 

28 - Neste ponto, você verá a ferramenta importada na subseção Ferramentas, o que significa que ela está disponível para o **Agente de Gerenciamento de Pedidos** .


29 - Role a página para baixo até a seção **Behavior** na configuração do agente e adicione as seguintes **instruções** para orientar o comportamento do agente:

- **Defina o tom e estilo de comunicação**: Por exemplo, amigável, profissional ou objetivo.
- **Inclua diretrizes para tomada de decisão**: Como priorizar respostas, quando solicitar mais informações e como lidar com casos ambíguos.
- **Especifique limites e escopo**: Indique quais tipos de perguntas o agente deve responder e quais devem ser encaminhadas para um humano.
- **Adicione instruções para uso das ferramentas**: Explique quando e como utilizar recursos como recuperação de e-mails ou consulta de pedidos.
- **Inclua boas práticas de privacidade e segurança**: Como evitar compartilhar dados sensíveis ou informações não autorizadas.

Essas instruções ajudam a garantir que o agente siga um comportamento consistente e alinhado às necessidades do negócio.


<b>Instruções de comportamento do Agente</b>

`````````````````````````````````````````````````````
### **Condição de Acionamento**
Quando um usuário inicia uma conversa ou faz uma pergunta contendo a palavra-chave
```mostrar todos os pedidos ou gerenciamento de pedidos ou gerenciar pedidos ou frases relacionadas.```

### **Etapa 1: Buscar e Exibir Todos os Pedidos de Compra**
* **Ação**: Acionar automaticamente a ferramenta `fetch_all_pos`.
* **Formato de Resposta (Exemplo)**:
```Aqui está uma lista de todos os pedidos de compra:
  | PO Number   | POM ID | Submetido por    | User ID           |
  |-------------|--------|------------------|-------------------|
  | 4300016793  | 4697   | Sailendu Patra   | sailendu.patra    |
  | 4200054529  | 3426   | Tannavi Snehal   | tannavi.snehal    |
  Insira o número do pedido que você gostaria de visualizar ou gerenciar.```

### **Etapa 2: Entrada e Validação do Número da Ordem de Compra**
* **Ação**: Aguarde a entrada do usuário (número da Ordem de Compra).
* **Validação**:
  * Se não encontrado:
    ```
    Nenhum detalhe da Ordem de Compra encontrado para o número da Ordem de Compra informado. Tente novamente ou verifique sua entrada.
    ```
  * Se válido: Prossiga para a Etapa 3.

### **Etapa 3: Obter e exibir os detalhes da OC em formato de tabela**
* **Ação**: Chamar a ferramenta `get_po_details(po_number)`.
* **Exemplo de resposta**:

  ```Confirme os detalhes da OC mostrados acima. Deseja prosseguir com esta OC? (Sim/Não)```

### **Etapa 4: Obter e exibir os detalhes da cotação em formato de tabela**
* **Condição de gatilho**: Se o usuário confirmar a OC.
* **Ação**: Extrair `quotation_number` dos detalhes da OC e chamar a ferramenta `get_quotation_details(quotation_number)`.
* **Exemplo de resposta**:

    ```Confirme os detalhes da cotação. Podemos prosseguir com a realização do pedido? (Sim/Não)```

### **Etapa 5: Confirmar e Fazer o Pedido**
* **Condição de Acionamento**: Se o usuário confirmar o orçamento.
* **Ação**: Chamar a ferramenta `display_confirmation`.
* **Exemplo de Resposta**:

    ```O pedido foi feito com sucesso. Você pode acompanhar seu pedido com o ID do Pedido: #710004927```

### **Princípios de Design**
* Garanta **uma confirmação por vez** — primeiro o pedido, depois o orçamento.
* Evite sobrecarregar o usuário com muitas informações de uma só vez.
* Valide as entradas do usuário e forneça prompts de recuperação amigáveis ​​caso algo dê errado.
* Formate as mensagens de forma clara com tabelas e destaques limpos em estilo markdown.
`````````````````````````````````````````````````````

Em seguida, teste a funcionalidade do agente fazendo uma pergunta como

```Gerenciar pedidos```

```Mostrar todos os pedidos```
  
-> Selecione um pedido, cotinue conversando com o agente e observe a resposta do agente. Clique no link **Show Reasoning** e observe como o agente está invocando corretamente as funções **Obter Todos os Detalhes da PO**, **Obter Detalhes da PO**, **Obter Detalhes da Cotação**, **Obter Detalhes da Correspondência** e **Exibir Confirmação** para recuperar informações relevantes.

![wxo order management agent behavior](./images/img16.png) 
![wxo order management agent behavior](./images/img17.png)
![wxo order management agent behavior](./images/img18.png)
![wxo chat q3 reasoning](./images/img34.0.png)

30 - Neste ponto, você está pronto para **implantar seu agente**. Para isso:

1. Role até o final da página de configuração.
2. Certifique-se de que a barra deslizante ao lado de **Show agent** esteja **desabilitada**.
3. Clique no botão `Deploy` para publicar o agente e torná-lo disponível como um **agente colaborador**.

Após a implantação, o agente estará pronto para ser utilizado nos fluxos de trabalho definidos.

![wxo order managemen agent deploy](./images/show-chat.png)
![wxo order managemen agent deploy](./images/img19.png) 

*Parabéns!* Você acabou de concluir o desenvolvimento do **Agente de Gerenciamento de Pedidos** equipado com ferramentas para ajudar os usuários a recuperar detalhes de PO e cotação, validar entradas e fazer pedidos de forma eficiente.

## Juntando tudo - Colaboração completa dos agentes

Agora que você desenvolveu todos os agentes e ferramentas, nesta seção, você trabalhará no processo de integração dos agentes colaboradores, testando e implantando o agente. **Agente Order-to-Cash**.

31 - Se você não estiver na página inicial do watsonx Orchestrate (interface de bate-papo), repita as etapas anteriores para garantir que você esteja conectado ao IBM Cloud, localize o serviço watsonx Orchestrate e inicie-o para acessar a página inicial.

32 - Na página Gerenciar agentes, selecione o **Manage agents**.

![wxo landing page manage agents](./images/wxo-landing-page-manage-agents.png) 

33 - Na página Gerenciar agentes, selecione o **Agente Order-to-Cash**.

![wxo collaborator agents](./images/img39.png) 

34 - Na página de configuração do **Agente Order-to-Cash**, role até a seção **Toolset** ou clique no atalho **Toolset** e você utilizará a funcionalidade **Add from local instance** como fez anteriormente e selecionará todas as ferramentas relevantes de ambos os agentes conforme abaixo:

![wxo collaborator agents](./images/img39.1.png) 

35 - Na janela _pop up_, selecione **Add from local instance**. Para referência, o Watsonx Orchestrate oferece suporte a diversas abordagens para adicionar agentes colaboradores.

![wxo collaborator agents](./images/img22.png)  

36 - Marque a caixa de seleção ao lado do **Agente de Suporte ao Cliente** e do **Agente de Gerenciamento de Pedidos** e clique no botão  **Add to agent**

![wxo financial analyst add collaborators](./images/img23.png) 

37 - Role mais para baixo até a seção **Behavior** ou clique no atalho  **Behavior** e adicione as seguintes **instruções** para orientar o agente em seu raciocínio e orquestração.

<b>Instruções de comportamento do Agente</b>

````````````````````````````````````````````
## **Função do Agente: Agente Supervisor**
- Este **Agente Supervisor** orquestra e gerencia o fluxo da conversa, encaminhando de forma inteligente as consultas dos usuários para os agentes especializados apropriados, com base no contexto.
---

### **Responsabilidades e Comportamento**
O Agente Supervisor supervisiona dois agentes específicos de domínio:
1. **Agente de Gerenciamento de Pedidos**
2. **Agente de Suporte ao Cliente**
---

### **Lógica de Acionamento**
* **Consultas de Gerenciamento de Pedidos**
*Condição de Acionamento*: Quando um usuário inicia uma conversa ou faz uma pergunta contendo as palavras-chave `mostrar todos os pedidos`, `gerenciar pedidos` ou frases relacionadas.
*Ação*: Delega automaticamente a conversa para o **Agente de Gerenciamento de Pedidos**, que segue um fluxo de trabalho estruturado passo a passo para buscar e gerenciar pedidos de compra e cotações.

* **Consultas de Suporte ao Cliente**
*Condição de Acionamento*: Quando o usuário solicita ajuda usando a palavra-chave 'mostrar todos os e-mails', `suporte ao cliente` ou intenção relacionada.
*Ação*: Passa o controle para o **Agente de Suporte ao Cliente**, que lida com consultas por e-mail, atualizações de pedidos e fluxos de trabalho de comunicação com o cliente.
---

### **Comportamento de Retorno para Consultas Gerais**
* **Consultas Não Específicas de Domínio (por exemplo, perguntas O2C)**
*Condição de Acionamento*: Quando a consulta do usuário não está relacionada ao gerenciamento de pedidos ou ao suporte ao cliente.
*Ação*: O Agente Supervisor encaminha a consulta para um **sistema de recuperação de conhecimento** e retorna a resposta mais relevante **diretamente, sem especificar o contexto de retorno**.
---

### **Princípios de Design**
* **Reconhecimento de Intenção Primeiro**: Detecte e encaminhe claramente com base no contexto de entrada do usuário.
* **Delegação, não duplicação**: Não lida com tarefas detalhadas, mas garante que o agente certo seja ativado.
* **Fluxo de interação natural**: Transições suaves sem interromper a experiência do usuário.
* **Sem sobreposição entre agentes**: Mantém limites claros para evitar confusão.
* **Respostas diretas para O2C e outros tópicos**: Sem enquadramento ou isenções de responsabilidade extras — apenas a resposta relevante.
````````````````````````````````````````````

Teste o comportamento do agente na seção **Preview** fazendo a seguinte pergunta de exemplo:

```Mostrar todos os e-mails de atendimento ao cliente```

``` Lista de clientes```

Expanda os links **Show Reasoning** e **Step 1** para revisar o raciocínio do agente. Observe que ele está recuperando as informações corretamente, pois faz referência à ferramenta **Agente de Suporte ao Cliente**.

![wxo knowledge base test](./images/img25.png) 

38 - Continue testando seu agente agora, enfatizando a funcionalidade do agente de gerenciamento de pedidos e a Base de conhecimento. 

Para isso, faça a seguinte perguntas:

```Mostrar todos os detalhes do pedido```

```Gerenciar pedidos```

39 - Neste ponto, você está pronto para implementar seu **Agente Order-to-Cash** . Para isso, role até o final da página de configuração e certifique-se de que a barra deslizante ao lado de **Show agent** esteja habilitada (verde) para tornar o **Agente Order-to-Cash** acessível na interface de chat. Clique no botão **Deploy** para implementar seu agente.


![wxo  agent deploy](./images/img24.png)

*Parabéns!* Você acabou de desenvolver e implantar o **Agente Order-to-Cash**.

## Experimente os agentes em ação no watsonx Orchestrate

Agora que você implantou seu **Order-to-Cash Agent**, você pode interagir com o agente usando a <b>watsonx Orchestrate</b> Conversational Interface.

40 - Clique no menu de navegação superior esquerdo e selecione **Chat** para acessar a interface de conversação.

![wxo chat ui](./images/wxo-chat-ui.png)

41 - Na interface do **Chat**, observe que agora você tem o **Order-to-Cash** como um dos agentes disponíveis para conversar. À medida que você adiciona mais agentes, pode selecionar com qual agente deseja interagir selecionando a lista suspensa de agentes.
Com o **Order-to-Cash** selecionado, tente interagir fazendo a seguintes perguntas e observe a resposta.

```Mostrar todos os e-mails de atendimento ao cliente```

``` Lista de clientes```

![wxo chat q1](./images/img26.png)

42 -  Expanda as seções **Show Reasoning** e **Step 1** para investigar o raciocínio do agente ao recuperar a resposta da ferramenta **Agente de suporte ao cliente** e continuar a conversar com o fluxo de trabalho de suporte ao cliente.

![wxo chat q1 reasoning](./images/img26copy.png)
![wxo chat q1](./images/img27.png)
![wxo chat q1](./images/img27.1.png)

43 - Em seguida, faça a seguinte pergunta para obter uma resposta da base de conhecimento.
Pergunta:

```O que devo fazer se houver algum problema com a entrega do meu pedido, como atrasos ou produtos danificados?``

```Quais métodos de pagamento são aceitos?```

Expanda as seções **Show Reasoning** e **Step 1** para investigar o raciocínio do agente ao recuperar a resposta. Nesse caso, o agente utiliza a **knowledge base** para recuperar a resposta.

![wxo chat q2](./images/img28.png)

44 - Em seguida, tente outra pergunta para recuperar os detalhes do pedido.
Pergunta:

```Mostre-me todos os pedidos```

Expanda a seção `Show Reasoning` e observe que o agente tomou 2 passos para recuperar a resposta para esta pergunta.

45 -  Agora, vamos tentar explorar quais são as etapas executadas. Expanda as seções **Step 1** e **Step 2** e observe o agente transferindo a solicitação ao **Agente de Gerenciamento de Pedidos** para fornecer os detalhes do pedido de um usuário específico.

![wxo chat q3 reasoning](./images/img31.png)
![wxo chat q3 reasoning](./images/img32.png)
![wxo chat q3 reasoning](./images/img33.png)


> 💡 Dica: Teste diferentes cenários para entender como os agentes se adaptam às suas necessidades.

## Conclusão

**Parabéns** por concluir a parte prática do laboratório do bootcamp.

Recapitulando, você utilizou a funcionalidade sem código do <b>watsonx Orchestrate</b> para desenvolver o **Agente Order-to-Cash** especializado em auxiliar na colocação de pedidos, faturamento, aumento da satisfação do cliente, aceleração do fluxo de caixa e impacto mensurável nos resultados financeiros, integrando agentes inteligentes e sistemas corporativos. Em seguida, você adicionou conhecimento ao agente, enviando documentos de conhecimento em formato PDF que capturam informações O2C.

Em seguida, você ampliou os recursos do **Agente Order-to-Cash** desenvolvendo dois outros agentes, o **Agente de gerenciamento de pedidos** e o **Agente de suporte ao cliente**, que são equipados com ferramentas para executar consultas de gerenciamento de pedidos e também recuperar informações do suporte ao cliente sobre seu pedido.