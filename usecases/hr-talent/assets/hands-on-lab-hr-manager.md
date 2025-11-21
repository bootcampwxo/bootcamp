
# 🧑‍💼 Agente Gerente de RH

## Índice

- [Descrição do caso de uso](#descrição-do-caso-de-uso)
- [Agente de aquisição de talentos](#agente-de-aquisicao-de-talentos)
- [Automatize o processo de recrutamento de talentos usando fluxos de trabalho baseados em agentes](#automatize-processo-de-recrutamento)
- [Agente de revisão de casos de RH](#agente-de-revisao-de-casos-de-rh)


## Descrição do caso de uso

Esta é a história da **Luisa**. **Luisa** é a gerente de RH de uma grande corporação que está contratando 5.000 funcionários para sua nova divisão. A luta dela é dupla:

1. **Recrutando Candidatos** para suas vagas aberta
2. **Gerenciamento de denúncias** de funcionários sobre possíveis violações das Diretrizes de Conduta Empresarial.

Para recrutamento, Luisa recebe muitos PDFs com currículos de candidatos. Ela tem que:

- Verificar se os candidatos **atendem aos requisitos** de uma determinada vaga
- Preencher uma **tabela** com as habilidades/experiência de cada candidato
- Selecionar os **candidatos** para entrevistas
- Designar os **entrevistadores** da equipe
- Coordenar as **entrevistas** com os candidatos e entrevistadores por e-mail
- Agendar as **entrevistas**
- Compilar o **feedback** dos diferentes avaliadores
- **Reportar** os resultados ao gerente de contratação

Luisa gostaria de tornar seu processo de contratação mais eficiente.

## Agente de aquisição de talentos

Este primeiro agente ajudará no processo de recrutamento. Siga estes passos para criar seu Agente de IA para Aquisição de Talentos:

1. Abra o Watsonx Orchestrate. Você verá a tela abaixo. Em seguida, clique em **Create an Agent** no canto inferior esquerdo:

<img alt="Solução" src="hands-on-lab-assets/images/1welcome.png">
<br>
<br>

2. Dê um nome e uma descrição. As descrições são usadas para direcionar uma determinada consulta a este agente quando necessário. Você pode usar a descrição abaixo ou experimentar com a sua própria:
```
Este agente ajuda a determinar se um conjunto de candidatos corresponde às habilidades especificadas na descrição da vaga.
```

<img alt="Solução" src="hands-on-lab-assets/images/2create_agent.png">
<br>
<br>

3. Depois de clicar em **Create**, você será direcionado para esta tela:

<img alt="Solução" src="hands-on-lab-assets/images/3talentaquisition.png">
<br>
<br>

4. Deslize a tela para baixo e ative a opção **Chat with Documents**:

<img alt="Solução" src="hands-on-lab-assets/images/4scrool.png">
<br>
<br>

5. Agora, vamos implantar o agente clicando no botão azul **Deploy**. É assim que você pode implantar um agente no WatsonX Orchestrate com facilidade.

<img alt="Solução" src="hands-on-lab-assets/images/5deploy.png">
<br>
<br>

6. Agora, vamos simular o que o gerente de RH faria para processar currículos automaticamente. Primeiro, baixe os arquivos de currículo e descrição de vagas abaixo. Depois de tê-los em seu computador, faça o upload de todos de uma vez clicando no botão **Upload** abaixo do chat. Você também pode arrastar e soltar os arquivos no chat como alternativa.


- Currículo do Candidato 1 (Arquivo "Candidate 1_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 
- Currículo do Candidato 2 (Arquivo "Candidate 2_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 
- Currículo do Candidato 3 (Arquivo "Candidate 3_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 
- Currículo do Candidato 4 (Arquivo "Candidate 4_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 
- Currículo do Candidato 5 (Arquivo "Candidate 5_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 
- Descrição da vaga (Arquivo "Descricao_Vaga.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) 

<img alt="Solução" src="hands-on-lab-assets/images/6upload.png">
<br>
<br>


7. Você verá uma confirmação do upload dos arquivos da seguinte forma:

<img alt="Solução" src="hands-on-lab-assets/images/7preview.png">
<br>
<br>

8. Agora, vamos experimentar algumas perguntas diferentes para processar os currículos e compará-los com a descrição da vaga. Primeiro, vamos resumir as habilidades e os requisitos da descrição da vaga:

``` 
Acima, enviei 5 documentos com currículos de candidatos e um documento com a descrição da vaga. Você pode me fornecer um breve resumo da descrição da vaga em um parágrafo?

```

9. Agora, vamos verificar se os currículos foram enviados corretamente, consultando os nomes dos candidatos:

```
dê-me os nomes de todos os candidatos
```

<img alt="Solução" src="hands-on-lab-assets/images/9test.png">
<br>
<br>


10. Agora vamos gerar uma tabela que relacione as habilidades necessárias com cada candidato:

```
Crie uma tabela onde cada linha representa um candidato e cada coluna representa uma habilidade na descrição da vaga. Inclua um emoji de visto se o candidato possuir a habilidade correspondente.
```

<img alt="Solução" src="hands-on-lab-assets/images/10test.png">
<br>
<br>

Você pode ver que Emma é a pessoa com as habilidades mais adequadas ao perfil. No entanto, o gerente de RH ainda precisa analisar o perfil e o currículo de Emma antes de prosseguir. É importante manter um profissional envolvido, principalmente ao tomar decisões que afetam pessoas. O objetivo da IA ​​Agente é automatizar as tarefas tediosas, e não substituir o trabalho do gerente de RH.

<!--11. Agora, vamos pedir para redigir um e-mail para agendar uma entrevista:
```
Redija um e-mail pedindo a Emma três horários possíveis para a próxima semana para a entrevista.
```

<img width="685" alt="Screenshot 2025-09-25 at 10 26 53 AM" src="https://github.ibm.com/skol/agentic-ai-client-bootcamp/assets/12043/47a3ef11-20ce-4e15-82a2-13ca81ef4362">

-->

11. Agora vamos trabalhar no agendamento das entrevistas. Primeiro, vamos adicionar os dados dos entrevistadores. Na prática, esses dados viriam de um banco de dados ou data lake que consulta vários sistemas da organização. Para simplificar, vamos supor que temos um arquivo PDF com a disponibilidade dos entrevistadores e suas habilidades. Podemos usar o Watsonx Orchestrate para adicionar o **Knowledge** dos entrevistadores ao agente. Role para baixo até a seção **Knowledge** e clique em **Choose Knowledge**.

<img alt="Solução" src="hands-on-lab-assets/images/11knowledge.png">
<br>
<br>


12. Selecione **Upload Files** na parte inferior, clique **Next**:

<img alt="Solução" src="hands-on-lab-assets/images/12upload.png">
<br>
<br>

13. Arraste e solte ou carregue o arquivo "Disponibilidade do Entrevistador" (Arquivo "Disponibilidade do Entrevistador.docx" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) . Clique **Next**:

<img alt="Solução" src="hands-on-lab-assets/images/113drag.png">
<br>
<br>

Agora você precisa definir uma descrição. Ela será usada para determinar quando invocar o conhecimento contido no arquivo. Adicione o seguinte em **Description** e clique em **Save**:

``` 
Este documento contém a disponibilidade e as habilidades de diferentes entrevistadores.
```

<img alt="Solução" src="hands-on-lab-assets/images/13description.png">
<br>
<br>


14.Agora, vamos executar algumas consultas adicionais para as entrevistas. Primeiro, vamos verificar se os dados dos entrevistadores foram carregados corretamente:

```
mostrar a disponibilidade dos entrevistadores
```

<img alt="Solução" src="hands-on-lab-assets/images/14result.png">
<br>
<br>

15. Agora, vamos ajudar Luisa a selecionar os entrevistadores mais adequados para a descrição da vaga:

``` 
Quem é o entrevistador mais competente para a descrição da vaga? Mostre-me as habilidades que ele(a) possui.
```

16. Por fim, vamos escolher um entrevistador e redigir um e-mail para um dos candidatos, informando a disponibilidade dele:

``` 
Redija um e-mail para Emma convidando-a para uma entrevista com Aisha. Inclua a disponibilidade de Aisha no rascunho do e-mail.
```

<img alt="Solução" src="hands-on-lab-assets/images/16result.png">
<br>
<br>

## Automatize o processo de recrutamento de talentos usando fluxos de trabalho baseados em agentes

Até agora, você criou um agente utilizando o recurso **Chat with documents** do Watsonx Orchestrate para fazer o upload de currículos, descrições de vagas e agendamentos de entrevistas. Nesse caso, o LLM do agente realiza todo o trabalho pesado, enquanto a função de Luisa é fornecer a mensagem/consulta adequada.

No entanto, muitas vezes não é óbvio qual deve ser a mensagem adequada, especialmente para um gerente de RH sem experiência em engenharia de mensagens. Além disso, podem existir etapas adicionais envolvidas, como entrar em contato automaticamente com o candidato selecionado ou agendar entrevistas automaticamente. Nesse caso, poderíamos utilizar **Agentic Workflows**.

A próxima parte do laboratório é mais avançada e requer algumas habilidades de low-code e familiaridade com conceitos básicos de programação, como variáveis ​​e loops for each. Se você quiser aprender a trabalhar com **Agentic Workflows**, [siga estas etapas](./hands-on-lab-hr-manager-flows.md)

**🎉🎉 Parabéns!! Você concluiu o módulo de aquisição de talentos. Agora você está pronto para o próximo!**

## Agente de revisão de casos de RH

1. Crie outro agente como fez anteriormente. Desta vez, adicione o seguinte à descrição:
```
Este agente analisa casos de RH referentes a reclamações de funcionários sobre possíveis violações das diretrizes de conduta empresarial.
```

<img alt="Solução" src="hands-on-lab-assets/images/hr1.png">
<br>
<br>

2. Adicione conhecimento. Role para baixo até a seção **Knowledge** e clique em **Choose Knowledge**.

<img alt="Solução" src="hands-on-lab-assets/images/hr2.png">
<br>
<br>

3. Agora você fará o upload do "Documento de Diretrizes de Conduta Empresarial da IBM" (Arquivo "Candidate 1_ptBR.pdf" dentro da pasta "7. Talentos de RH" gerada após descompactar o LABS.zip) . Você também pode experimentar com as Diretrizes de Conduta Empresarial (BCG) da sua empresa, se disponíveis. Insira uma descrição. Pode ser algo como:

```
Estas são as Diretrizes de Conduta Empresarial da IBM
```

Após salvar, você verá algo como:

<img alt="Solução" src="hands-on-lab-assets/images/hr3.png">
<br>
<br>

4. Agora você está pronto para testar algumas consultas:

``` Ajude-me a entender se a seguinte reclamação de um funcionário infringe as Diretrizes de Conduta Empresarial da IBM: "Meu gerente levantou a voz, me xingou, zombou de mim e me disse coisas muito desagradáveis ​​todos os dias durante o último mês."
```

<img alt="Solução" src="hands-on-lab-assets/images/hr4.png">
<br>
<br>

```
Que tal esta: minha gerente me deu um chocolate do Havaí depois da viagem dela para Maui. Isso é uma violação da regra BCG?
```

<img alt="Solução" src="hands-on-lab-assets/images/hr4_1.png">
<br>
<br>

5. Você pode perceber que o exemplo acima pode não constituir, na prática, uma violação real das Diretrizes de Conduta Empresarial. Podemos ajustar o agente para lidar com determinadas situações de forma diferente. Para isso, podemos usar o recurso **Guidelines**. Role a página para baixo até a seção **Guidelines** e clique em **New Guideline**.

<img alt="Solução" src="hands-on-lab-assets/images/hr5.png">
<br>
<br>

6. Salve e tente a mesma consulta mais uma vez no chat. Você deverá ver algo como isto:

<img alt="Solução" src="hands-on-lab-assets/images/hr6.png">
<br>
<br>

7. O resultado após repetir a mesma consulta seria semelhante a este:

<img alt="Solução" src="hands-on-lab-assets/images/hr7.png">
<br>
<br>

## 🛠️ Vamos juntar tudo.

Vimos como você pode criar dois agentes separados para atender a diferentes necessidades de negócios, ou seja, (1) Recrutamento e Seleção e (2) Análise de Casos de RH. Mas não seria interessante ter uma única interface para lidar com ambos os tipos de consultas do usuário? Para isso, vamos criar um Agente de Gerenciamento de RH capaz de encaminhar as consultas adequadamente.

1. Crie um novo agente. Use o mesmo procedimento acima. Na descrição, forneça algumas instruções básicas de roteamento, como:

```
Este agente gerencia diferentes solicitações de RH:

1. Recrutamento e Seleção: processamento de currículos, descrições de cargos, anúncios de entrevistadores, encaminhamento para o agente de recrutamento e seleção

2. Análise de Casos de RH: processamento de reclamações ou casos de RH submetidos por funcionários como possíveis violações das Diretrizes de Conduta Empresarial
```

2. Role para baixo até a seção Agentes.

3. Selecione Adicionar da Instância Local
4. Procure os dois agentes que você acabou de criar e adicione ambos.

5. Agora, tente fazer diferentes consultas no Agente de Gerenciamento de RH


