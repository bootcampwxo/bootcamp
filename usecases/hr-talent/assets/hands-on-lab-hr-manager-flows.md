
# 🧑‍💼 Automatizando a aquisição de talentos com fluxos de trabalho agenciados

## Índice

- [Descrição do Caso de Uso](#descrição-do-caso-de-uso)
- [Pré-requisitos](#pré-requisitos)
- [Agente de Aquisição de Talentos com fluxos de trabalho](#-agente-de-aquisição-de-talentos-com-fluxos-de-trabalho)
     - [Criar um novo agente de Talentos](#criar-um-novo-agente)
     - [Etapa 1: Crie um fluxo de trabalho baseado em agentes e configure as entradas e saídas](#etapa-1-crie-um-fluxo-de-trabalho-baseado-em-agentes-e-configure-as-entradas-e-saídas)
     - [Etapa 2: Atividade do usuário para coletar o número de candidatos](#etapa-2-atividade-do-usuário-para-coletar-o-número-de-candidatos)
     - [Etapa 3: Bloco de código para armazenar o número de candidatos](#etapa-3-bloco-de-código-para-armazenar-o-número-de-candidatos)
     - [Etapa 4: Para cada iteração faça o upload dos currículos dos candidatos.](#etapa-4-para-cada-iteração-faça-o-upload-dos-currículos-dos-candidatos.)
     - [Etapa 5: Exibir mensagem para enviar um currículo](#etapa-5-exibir-mensagem-para-enviar-um-currículo)
     - [Etapa 6: Envio de arquivo](#etapa-6-envio-de-arquivo)
     - [Etapa 7: Extrator de documentos para currículos](#etapa-7-extrator-de-documentos-para-currículos)
     - [Etapa 8: Armazene o nome e as habilidades do candidato para uso posterior.](#etapa-8-armazene-o-nome-e-as-habilidades-do-candidato-para-uso-posterior)
     - [Etapa 9: Exibir uma mensagem para enviar a descrição da vaga](#etapa-9-exibir-uma-mensagem-para-enviar-a-descrição-da-vaga)
     - [Etapa 10: Faça o upload da descrição da vaga](#etapa-10-faça-o-upload-da-descrição-da-vaga)
     - [Etapa 11: Extrator de documentos para habilidades da vaga](#etapa-11-extrator-de-documentos-para-habilidades-da-vaga)
     - [Etapa 12: Solicitação generativa - relacionar as habilidades dos candidatos às habilidades da vaga](#etapa-12-solicitação-generativa---relacionar-as-habilidades-dos-candidatos-às-habilidades-da-vaga)
     - [Etapa 13: Exibir resumo da partida - saída do prompt generativo](#etapa-13-exibir-resumo-da-partida---saída-do-prompt-generativo)
     - [Atualizar o comportamento do agente](#atualizar-o-comportamento-do-agente)
     - [Teste o agente](#teste-o-agente)
- [Reunindo tudo](#reunindo-tudo)


## Descrição do Caso de Uso

Na [primeira parte do laboratório de Talentos de RH](./hands-on-lab-hr-manager.md), você usou o recurso **Chat with documents** para carregar vários currículos e uma descrição de vaga. Em seguida, você solicitou ao agente que gerasse uma tabela comparando as habilidades dos candidatos com as habilidades exigidas para a vaga. Nesse caso, o LLM interno do agente realiza todo o trabalho; tudo o que é necessário do usuário é fornecer a solicitação/consulta correta. No entanto, às vezes pode não ser óbvio qual é a solicitação correta, já que os gerentes de RH não são especialistas em programação de prompts. Além disso, podemos querer programar o agente para executar algumas etapas adicionais, como entrar em contato automaticamente com o candidato selecionado, pedir que ele escolha um horário para a entrevista, processar automaticamente a resposta e adicioná-la ao calendário. Nesse caso, podemos querer criar um **agentic workflow**.

Um fluxo de trabalho agêntico representa uma sequência de etapas que utiliza controles e atividades condicionais. Os fluxos de trabalho agênticos permitem criar sequências de tarefas, bem como condições, ramificações e loops. Podemos usar uma variedade de nós, incluindo pequenos blocos de código, entrada do usuário, nós de processamento de documentos para extrair dados de documentos e prompts generativos para criar e configurar prompts LLM com entradas e saídas.

Em vez de lidar com cada etapa individualmente, os agentes podem iniciar um fluxo de trabalho agêntico para gerenciar todo o processo do início ao fim. Os fluxos de trabalho agênticos são ideais para tarefas que exigem coordenação entre sistemas ou múltiplos pontos de decisão.

Por exemplo, um fluxo de trabalho agêntico pode ser criado para lidar com a integração de novos funcionários: coletar informações, criar contas, enviar e-mails de boas-vindas e notificar as equipes internas. Uma vez criado, esse fluxo de trabalho agético pode ser reutilizado em todos os departamentos, acionado pelos agentes sempre que um novo funcionário for contratado — sem a necessidade de coordenar manualmente cada etapa.

Ao usar fluxos de trabalho agéticos, os usuários corporativos obtêm:

- Confiança de que as tarefas são concluídas de forma correta e consistente.

- Agilidade por meio da automação de etapas repetitivas. - Visibilidade de como os processos são executados e onde ocorrem os gargalos.
- Escalabilidade para aplicar a mesma lógica em equipes, regiões ou produtos.

## Pré-requisitos

Você vai precisar dos arquivos baixados durante o laboratório de Gerente de RH:

- [Currículo do Candidato 1](../data/Candidato%201.pdf)
- [Currículo do Candidato 2](../data/Candidato%202.pdf)
- [Currículo do Candidato 3](../data/Candidato%203.pdf)
- [Currículo do Candidato 4](../data/Candidato%204.pdf)
- [Currículo do Candidato 5](../data/Candidato%205.pdf)
- [Descrição do Cargo](../data/Descrição%20do%20Cargo.pdf)

## 🥇 Agente de Aquisição de Talentos com fluxos de trabalho

Nesta parte do laboratório, implementaremos o seguinte fluxo de trabalho:

![alt text](./hands-on-lab-assets/flow_to_build.jpeg)

Agora, vamos orientá-lo passo a passo na criação do fluxo de trabalho acima. Primeiro, criaremos um agente separado para experimentação.

### Criar um novo agente
 
Abra o Construtor de Agentes no Watsonx Orchestrate, caso ainda não esteja aberto -- clique em ***Build** no menu principal (ícone de hambúrguer).

![alt text](./images-lab/builder.png)

Criar um novo agente:

![alt text](./images-lab/create-agent.png)

Selecione **Create from scratch**, dê o nome de **Agente de Seleção** e adicione uma breve descrição. As descrições são usadas para direcionar a consulta do usuário ao agente correto. Você pode usar a descrição abaixo:
```
Este agente ajuda a encontrar candidatos para vagas com base em suas habilidades.
```
![alt text](./images-lab/agent-scratch.png)

Após clicar em **Create**, você será direcionado para esta tela:

![alt text](./images-lab/principal-screen.png)

Vamos manter todas as outras configurações com os valores padrão por enquanto. Role para baixo até a seção **Toolset**. É aqui que adicionaremos nosso fluxo (fluxo de trabalho com agentes). Clique em **Add Tool**.

![alt text](./images-lab/add-tool-flows.png)

Selecione **Create an agentic workflow**:

![alt text](./images-lab/agentic-workflow.png)

### Etapa 1: Crie um fluxo de trabalho baseado em agentes e configure as entradas e saídas

Primeiro, crie o nome do fluxo você usar esse **Match candidatos** vamos editar a descrição do fluxo, as entradas e as saídas. Clique no ícone de lápis ao lado do nome do fluxo no canto superior esquerdo:

![alt text](./images-lab/parametros.png)
Altere o nome para **Combinar candidatos** e a descrição para:

``` 
Extrai habilidades dos currículos dos candidatos, extrai habilidades da descrição da vaga e gera uma tabela resumo mostrando quais candidatos possuem quais habilidades exigidas e desejáveis ​​para a vaga.

```
e clique no botão  **Add output** para especificar a saída do fluxo: 

![alt text](./images-lab/add-output.png)

Aqui configuraremos a variável que armazenará a saída de todo o fluxo, retornada ao agente após a conclusão da execução do fluxo. Selecione **String** para o tipo de variável:

![alt text](./hands-on-lab-assets/select_string_output.png)

Dê o nome **match_summary** e clique em **Add**: 

![alt text](./hands-on-lab-assets/match_summary_var.png)

Após clicar em **Save**, seu fluxo de trabalho ficará semelhante a este:

![alt text](./images-lab/workflows.png)

Por enquanto, o fluxo possui apenas dois nós: o nó inicial, com 0 entradas e 0 variáveis ​​configuradas, e o nó final, com 1 variável configurada. Você pode verificar se a variável de saída foi adicionada com sucesso clicando no nó final.

![alt text](./images-lab/output-var.png)


Em seguida, configuraremos algumas variáveis ​​de fluxo que poderemos usar ao longo do nosso fluxo. Precisaremos de duas:

- *num_candidatos* - uma lista que representa um intervalo de números inteiros de *0* a *n*, onde *n* é o número de candidatos. Para carregar e processar vários currículos de candidatos, usaremos um nó **For each**. Para isso, podemos iterar sobre *num_candidatos*.
- *candidatos* - esta é uma variável de string que armazenará os nomes dos candidatos extraídos e suas respectivas habilidades. Precisaremos dela para usá-la em um nó de prompt generativo.

Clique no nó inicial e selecione **Add**.
Selecione **Integer**

![alt text](./images-lab/flow-variables.png)

Insira o nome da variável, *num_candidatos*, e uma descrição, por exemplo:

```
Quantidade de candidatos
```
Habilite a opção **List of Integer**  já que teremos uma lista, clique em **Add** para adicionar a variável.

Adicione outra variável:

![alt text](./images-lab/input-integer-list.png)

Desta vez, crie uma string. Dê o nome *candidatos* e uma descrição simples, por exemplo:

![alt text](./images-lab/flow-variables.png)

```
Nomes e habilidades dos candidatos
```

Especifique o valor padrão (starting): "" e clique em **Add**:

![alt text](./images-lab/input-string-nomes.png)

Seu fluxo de trabalho agora está assim:

![alt text](./images-lab/fluxo-no-momento.png)

### Etapa 2: Atividade do usuário para coletar o número de candidatos

Agora vamos adicionar nossa primeira atividade de usuário. A primeira atividade que vamos criar será perguntar ao usuário quantos candidatos ele gostaria de avaliar para a vaga. Passe o cursor sobre a seta que conecta o nó inicial ao nó final e clique no sinal de **+**:

![alt text](./images-lab/nova-atividade.png)

Clique em **User activity**:

![alt text](./images-lab/fluxo-2-seleciona-number.png)

A seguir será necessário adicionar a pergunta referente a quantidade de candidatos:

``` 
Quantos candidatos você gostaria de avaliar?
```

![alt text](./images-lab/fluxo-2-pergunta.png)

Seu fluxo agora deve estar assim:

![alt text](./images-lab/fluxo-2.png)

### Etapa 3: Bloco de código para armazenar o número de candidatos

Agora vamos definir um nó para atualizar a variável *num_candidatos*:

Arraste da lista **Flow nodes** o **Logic block** e adiciona entre **User activity** e **output**.
Clique no novo nó de bloco de código e abra o editor de código:

![alt text](./images-lab/fluxo-3-logic-block.png)

Enter the folowing code into the editor: 

``` 
numc = flow["User activity 1"]["Quantos candidatos você gostaria de avaliar?"].output.value
flow.private.num_candidatos = list(range(0, numc))
```

E clique no **X** para fechar o editor:

![alt text](./images-lab/fluxo-3-code.png)

Clique novamente no bloco de código e renomeie-o usando o botão Editar (lápis):

![alt text](./images-lab/fluxo-3-edit-name-flow.png)

Dê o nome **armazenar lista de candidatos** e clique **V** para salvar.  Seu fluxo agora deve estar semelhante ao seguinte:

![alt text](./images-lab/fluxo-3-momento.png)

### Etapa 4: Para cada iteração faça o upload dos currículos dos candidatos.

Nós vamos criar um **for-each loop** Para fazer o upload de cada currículo, extrair o nome do candidato e suas habilidades e armazenar todas essas informações na variável *candidatos*.

No Flow Controls arraste o **For each*** para ficar entre **Armazenar lista de candidatos** e **output**:

![alt text](./images-lab/fluxo-4-foreach.png)

### Etapa 5: Exibir mensagem para enviar um currículo

Dentro do nó **For each**, crie uma **User activity** arrastando para dentro do nó **For each** e clicando no sinal de **Add +**. Em seguida, passe o cursor sobre o interior da **User activity**, clique em **+**, selecione **isplay to user** e, em seguida, **Message**.

![alt text](./images-lab/fluxo-5-user-activity.png)

Em seguida, clique em **Message** e edite a **Output message**:

```
Faça o envio do currículo dos candidatos
```

Esta é a mensagem que será exibida ao usuário para solicitar o envio de um currículo.

Ao mesmo tempo, altere o nome do nó para:

```
Solicitar ao usuário que envie o currículo
```

![alt text](./images-lab/fluxo-5-message.png)


### Etapa 6: Envio de arquivo

Adicione outra **User Activity**:
Desta vez será uma atividade de **File Upload**:

![alt text](./images-lab/fluxo-6-atividade.png)

Clique no novo nó *File upload** e renomeie para **Upload de currículo**: 

![alt text](./images-lab/fluxo-6-change-name.png)

### Etapa 7: Extrator de documentos para currículos

Em seguida, criaremos um nó de extração de documentos para extrair o nome e as habilidades do candidato do seu currículo.

Ainda dentro do loop **For Each**, arraste **Document extractor** para criar o nó:

![alt text](./images-lab/fluxo-7-document-extrator.png)

Agora, vamos carregar um dos currículos como exemplo para treinar o extrator de documentos. Arraste e solte o arquivo **Currículo do Candidato 2** (Arquivo "Candidato 2.pdf". Talentos de RH" gerada após descompactar o LABS.zip)  que você baixou anteriormente no laboratório:

Assim que o documento for carregado, você verá a seguinte tela. Clique em **Add field** para começar a adicionar os campos que queremos extrair e usar para treinar o extrator de documentos:

![alt text](./images-lab/fluxo-7-selecionar-campos.png)

Entre **Nome** para o nome do campo e pressione Enter. O extrator de documentos tentará extrair o nome do currículo e o exibirá assim que estiver pronto:

![alt text](./images-lab/fluxo-7-entidade-nome.png)

Em seguida, precisamos adicionar outro campo: **Habilidades**. Adicione mais um campo e nomeie-o como **Habilidades**. Depois de pressionar Enter, o extrator de documentos preencherá o campo com os dados do documento.

![alt text](./images-lab/fluxo-7-entidade-habilidade.png)

Renomeie o nó do extrator de documentos para **Extrator de currículo** clicando nele e editando o nome.

Seu loop **For each** deverá agora ter este aspeto:

![alt text](./images-lab/fluxo-7-end.png)

### Etapa 8: Armazene o nome e as habilidades do candidato para uso posterior

A última atividade que precisamos criar no loop **For each** é outro bloco de código que armazena o nome e as habilidades do candidato após cada iteração:

![alt text](./images-lab/fluxo-8-code.png)

Clique no bloco de código e abra o editor de código. Digite o seguinte no editor de código:

```
flow.private.candidatos += "Nome: " + str(flow["For each 1"]["Extrator de currículo"].output.nome) + "\n\nHabilidades: " + str(flow["For each 1"]["Extrator de currículo"].output.habilidades) + "\n\n"
```
Renomeie o bloco para **Atualizar Candidatos**. O **For each** deverá agora ter este aspeto:

![alt text](./images-lab/fluxo-8-end.png)

### Etapa 9: Exibir uma mensagem para enviar a descrição da vaga

Em seguida, pediremos ao usuário que carregue uma descrição da vaga. Primeiro, exibiremos uma mensagem para o usuário e, depois, adicionaremos uma atividade de upload de arquivo.

**Abaixo** do loop **For each**, arraste a **User activity**:

Clique dentro da atividade do usuário e selecione **Display to user** e, em seguida, **Message**:

![alt text](./images-lab/fluxo-9-atividades.png)

Atualize a **Output message** para: 

```
Por favor, faça o upload da descrição da vaga.
```

E altere a **Display message** (nome do nó no fluxo) para: 

```
Solicitar ao usuário que carregue a descrição do cargo
```

![alt text](./images-lab/fluxo-9-upload-file.png)

### Etapa 10: Faça o upload da descrição da vaga

Adicione outra **User activity** logo antes do nó final. Desta vez, faça-o do tipo **File upload**: 

![alt text](./images-lab//fluxo-10-user-activity.png)

Clique no nó de upload de arquivos recém-criado e altere o nome dele para:

```
Carregar descrição da vaga
```

![alt text](./images-lab/fluxo-10-rename.png)

### Etapa 11: Extrator de documentos para habilidades da vaga

Em seguida, criaremos outro nó extrator de documentos para extrair as habilidades necessárias e desejáveis ​​da descrição da vaga.

Adicione um nó **Document extractor** antes do final do fluxo e renomeie-o como **Extrair habilidades da vaga**:

![alt text](./images-lab/fluxo-11-extractor.png)

Após o processamento do documento, você verá a seguinte tela:

![alt text](./images-lab/fluxo-11-documents.png)

Adicione dois campos, semelhantes aos que você adicionou ao extrator de currículos. Desta vez, porém, adicione os campos **necessárias** e **desejáveis** para extrair as habilidades obrigatórias e desejáveis:

Feche o nó do extrator quando terminar.

### Etapa 12: Solicitação generativa - relacionar as habilidades dos candidatos às habilidades da vaga

Estamos quase no fim do fluxo. Ainda precisamos implementar um prompt generativo. Este prompt receberá como entrada o valor da variável *candidatos*, que é uma string contendo, até o momento, os nomes de todos os candidatos e suas habilidades. Também receberá como entrada as habilidades necessárias e desejáveis, extraídas da descrição da vaga. O prompt comparará as habilidades de cada candidato com as habilidades exigidas pela vaga e gerará uma tabela que resume o quão bem as habilidades dos candidatos se encaixam na descrição da vaga.

Adicione um nó **Generate prompt** node no final do fluxo (antes do nó final).
Arraste o nó para que ele fique no final do fluxo.

![alt text](./images-lab/fluxo-12-init.png)

Renomeio o nó para **Adequar as competências do candidato às competências da vaga.** e edite o **Prompt settings**.

Para o prompt do sistema, digite o seguinte:

``` 
Você é um assistente prestativo que pode encontrar candidatos com as habilidades certas para as vagas.
```

Para o prompt do usuário, digite:

```
Crie uma tabela onde cada linha representa um candidato e cada coluna representa uma habilidade descrita na vaga. Não invente candidatos. Inclua um emoji de visto se o candidato possuir a habilidade correspondente. Marque as colunas com um asterisco (*) indicando as habilidades necessárias para a vaga. Inclua o nome do candidato em cada linha.

Nomes e habilidades dos candidatos:
Habilidades necessárias para a vaga:
Habilidades desejáveis ​​para a vaga:
```

Para funcionar, nosso prompt generativo precisará receber **como entrada** uma string contendo os nomes e habilidades dos candidatos, extraídos anteriormente no fluxo. Também precisará de duas strings para as habilidades (obrigatórias e desejáveis) da própria descrição da vaga. Portanto, precisamos criar três variáveis ​​de entrada do tipo _String_ que armazenarão esses valores e que poderemos referenciar no prompt do usuário como variáveis.

Também podemos fornecer um valor de teste de exemplo para cada variável, para que possamos executar o prompt diretamente no editor de prompts generativos e verificar se a saída está correta, sem precisar encerrar e executar todo o fluxo.

Adicione as seguintes variáveis ​​de entrada do tipo _String_: *candidatos*, *job_necessarias* e *job_desejaveis* e atribua alguns valores de teste, por exemplo:

Insira o nome da variável e adicione uma breve descrição:

Edite a variável para adicionar um valor de teste:

![alt text](./images-lab/fluxo-12-var.png)

Cole o seguinte texto para adicionar o valor:

```
Nome: Jane Smith
Habilidades: Java, Javascript

Nome: John Doe
Habilidades: Java, Python, Javascript, Aprendizado de Máquina
```

A sua variável _candidatos_ agora está assim

Siga os passos acima para adicionar mais duas variáveis ​​do tipo _String_, _job_necessarias_ e _job_desejaveis_:

![alt text](./images-lab/fluxo-12.png)

Por fim, faça referência a essas variáveis ​​no seu prompt clicando no sinal **X** na área de prompts do usuário:

Seu prompt agora deve estar assim:

![alt text](./images-lab/fluxo-12-config-prompt.png)

Clique em **Generate response** Para executar o comando com os valores de teste fornecidos e observar os resultados retornados:

Como você pode ver, o resultado é uma tabela que compara as habilidades de cada candidato com os requisitos da vaga. Isso é exatamente o que estávamos procurando, então validamos que nosso prompt generativo funciona e podemos prosseguir para a próxima etapa.

Feche a definição do prompt agora, clique no nó "Prompt generativo" que você acabou de criar e **Edite o mapeamento de dados**:

![alt text](./images-lab/fluxo-12-edit-mapping.png)

 Agora precisamos mapear os dados coletados anteriormente no fluxo para as entradas do prompt generativo.

Clique no ícone da **variável** na linha *candidatos*:

![alt text](./images-lab/prompt_edit_candidates_input.png)

No editor, selecione **Flow variables -> candidatos**: 

![alt text](./images-lab/select_candidates_fv.png)

Para *job_desejaveis*, também selecione **ícone de variável** e escolha **Extrair habilidades da vaga -> desejaveis**

![alt text](./images-lab/select_job_preferred.png)

Da mesma forma, para *job_necessarias*, selecione o ícone da variável e escolha **Extrair habilidades da vaga -> necessarias**

![alt text](./images-lab/select_job_required.png)

### Etapa 13: Exibir resumo da partida - saída do prompt generativo

Por fim, crie um último nó **User activity** para exibir a saída do prompt generativo.

Altere o nome do nó para **Mostrar resumo** e clique em **Select variable** para selecionar a mensagem de saída:

No editor, selecione o nome do nó de prompt generativo e, em seguida, selecione o valor da variável de saída correspondente:

![alt text](./images-lab/fluxo-13-end.png)

Finalmente terminamos de definir o fluxo. Clique em **Done** para fechar o fluxo.

### Atualizar o comportamento do agente


Antes de testar o agente, vamos concluir a seção **Behavior**. Siga as instruções abaixo:

``` Você especialista em análise para seleção de candidatos para vagas. Sua missão é analisar curriculos de acordo com a descriação da vaga, mas que você consiga realizar tua tarefa tem que usar a seguinte ferramenta.

Para atuar na analise é obrigatório acionar a tool `Match candidatos` que eu não tenha muitas informações sobre candidato ou descrição da vaga. Pois estas mesmas informações será solicitadas ao longo do processo.

## Retrições
- Você é obrigado a usar a tool
- No incio da interação você é obirgado a utilizar a tool
- Não pode solicitar informações sem que tenha acessado a tool
- Não pode solicitar informações do candidato ou da vaga sem que tenha acessado a tool
- Não pode sair do fluxo da tool, tem que realizar cada etapa
```

![alt text](./images-lab/behavior.png)

### Teste o agente

Teste seu agente fornecendo dois currículos de candidatos. Digite a seguinte consulta no chat:

```
recomendar um candidato para uma vaga
```

O agente perguntará quantos candidatos você gostaria de avaliar. Resposta: 2

Em seguida, você será solicitado a enviar o currículo de um candidato. Você pode enviar o currículo de qualquer candidato, por exemplo **Currículo do Candidato 3**. Observe que você poderá ser solicitado a revisar os resultados da extração. Se a confiança do extrator for inferior a 95%, será necessária a validação humana. Esse comportamento pode ser facilmente configurado no nó do extrator de documentos. O mesmo se aplica a quaisquer outros documentos carregados.

Em seguida, você será solicitado a enviar o segundo currículo. Você pode enviar o currículo de outro candidato, por exemplo **Currículo do Candidato 1**.

Por fim, você será solicitado a enviar uma descrição da vaga. Você pode usar o **Descrição da vaga**.

Os resultados devem ser semelhantes aos seguintes:

![alt text](./hands-on-lab-assets/table_output.png)

Como você pode ver, as colunas marcadas com * são habilidades exigidas para o cargo. Outras habilidades são desejáveis.
Cada linha de candidato mostra quais habilidades o candidato possui.

O agente resume, informando-nos quem é o candidato recomendado:

![alt text](./hands-on-lab-assets/recommended_candidate.png)

## Reunindo tudo

Nesta parte do laboratório, automatizamos o processo de extração de habilidades de currículos e da descrição da vaga, resumindo o quão bem as habilidades dos candidatos correspondem às habilidades exigidas e desejáveis ​​para o cargo. Usamos nós de **document processing** para definir os campos a serem extraídos dos documentos e para treinar o processador de documentos. Em seguida, alimentamos a saída dos nós de processamento de documentos como entrada para o nó de **generative prompt**, que compôs o prompt correto para o LLM resumir o quão bem as habilidades do candidato correspondem aos requisitos da vaga.

Poderíamos facilmente expandir esse fluxo de trabalho com nós e ramificações adicionais, por exemplo, para enviar um e-mail aos candidatos mais bem classificados, solicitando que escolham um horário para entrevista e confirmando o recebimento da resposta. Executar essas tarefas como um fluxo de trabalho permite uma maneira mais determinística de lidar com tarefas repetitivas, para que o agente possa conduzir o processo e envolver o gerente de RH sempre que sua contribuição for necessária.

Como você observou ao testar o fluxo, dependendo de como os limites de confiança são configurados nos nós de processamento de documentos, a verificação humana pode ser solicitada para garantir que os dados do campo sejam extraídos corretamente.

A combinação de fluxos de trabalho com agentes, ferramentas convencionais e tarefas individuais em um agente proporciona a maior flexibilidade. O usuário pode conversar com o agente e invocar tarefas individuais conforme necessário. Para processos mais complexos e com várias etapas, os fluxos de trabalho com agentes são uma ferramenta poderosa que pode gerenciar todo o processo do início ao fim.

