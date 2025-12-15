# 🧑‍💼 AskHR: Automatize tarefas de RH com a IA da Agentic

## Sumário

- [🧑‍💼 AskHR: Automatize tarefas de RH com a IA da Agentic](#-askhr-automatize-tarefas-de-rh-com-a-ia-da-agentic)
  - [Sumário](#sumário)
  - [Descrição do caso de uso](#descrição-do-caso-de-uso)
  - [Arquitetura](#arquitetura)
  - [Pré requisitos](#pré-requisitos)
  - [Instruções:](#instruções)
    - [Abrir Agent Builder](#abrir-agent-builder)
    - [Criando um Agente de RH](#criando-um-agente-de-rh)
    - [Teste o Agente de RH em Preview](#teste-o-agente-de-rh-em-preview)
      - [Testar o Agente de RH no Chat](#testar-o-agente-de-rh-no-chat)
    
## Descrição do caso de uso

Este caso de uso tem como objetivo desenvolver e implementar um agente AskHR utilizando o <b>IBM watsonx Orchestrate</b>, conforme ilustrado no diagrama de arquitetura abaixo. Esse agente vai permitir que os colaboradores interajam com os sistemas de RH e acessem informações de forma simples e eficiente, usando IA conversacional.

No laboratório, vamos construir um agente de RH no <b>watsonx Orchestrate</b>, aproveitando ferramentas e conhecimento externo para se conectar a um sistema de Gestão de Capital Humano simulado. Esse agente será capaz de recuperar informações relevantes de documentos para responder às perguntas dos usuários e também permitir que eles visualizem e gerenciem seus próprios perfis.

## Arquitetura

<img width="1000" alt="image" src="arch_diagm.png">

## Pré requisitos

- Verifique com seu instrutor se **todos as aplicações** estão funcionando antes de continuar.
- Confirme se você tem acesso ao ambiente techzone correto para este laboratório.
- Confirme que você fez o dowload do arquivo LABS.zip 


## Instruções:

### Abrir Agent Builder

Faça login na IBM Cloud (cloud.ibm.com). Navegue até o menu hambúrguer no canto superior esquerdo, depois até Lista de Recursos. Abra a seção de `IA/Machine Learning`. Você deve ver um serviço **watsonx Orchestrate**, clique nele para abrir.

<img width="1000" alt="image" src="../../../environment-setup/assets/cloud-resource-list.png">

Clique no botão azul "Launch watsonx Orchestrate" como ilustrado na imagem abaixo:

<img width="1000" alt="image" src="../../../environment-setup/assets/cloud-wxo.png">

Bem vindo ao <b>watsonx Orchestrate</b> 💙 

Abra o menu hambúrguer do lado esquerdo da interface, clique `Agent Builder`

<img width="1000" alt="image" src="hands-on-lab-assets/step_1_v2.png">

### Criando um Agente de RH

1. Clique em **Create agent +**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_2_v2.png">

2. Selecione **Create from scratch**, de o nome ao seu agente, por exemplo, `Agente de RH`, e preencha o campo **Description** conforme mostrado abaixo:﻿

```
Você é um agente que lida com as dúvidas dos funcionários sobre RH. Você fornece respostas curtas e diretas, com no máximo 200 palavras ou menos. Você pode ajudar os usuários a verificar os seus dados do perfil, recuperar o saldo de folgas mais recente, atualizar cargo ou endereço e solicitar folgas. Você também pode responder a perguntas gerais sobre os benefícios da empresa.
```  
Clique em **Create**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_3_v2.png">

Na próxima página:

Em `Model`, mantenha o modelo padrão, não é necessário alterar 

3. Selecione **Default** na seção **Agent style**.

<img width="1000" alt="image" src="hands-on-lab-assets/step_5_v3.png">

Ainda durante a etapa de definição do tipo de agente, você também pode configurar uma mensagem de boas vindas que será exibida na interface para o usuário, como mostrado na imagem abaixo.

<b>Essa mensagem é opcional. Você pode escrever algo como:</b> 

`Olá! Sou o Agente de RH da empresa X`

Ou simplesmente deixar em branco para manter as mensagens padrão.

<img width="1000" alt="image" src="hands-on-lab-assets/step_6-1_v4.png">

A seguir, podemos definir mensagens de atalho. Essas mensagens serão exibidas para o usuário como botões na interface, funcionando como atalhos para ações.

Por exemplo:

`marcação de férias`

`consultar saldo de férias`

`atualização de endereço`

Você pode criar esses botões clicando em `Add prompt +` e removê-los clicando no ícone de lixeira.

Esse passo também é opcional.
Para que essas opções apareçam na telinha de preview do lado direito da tela, use o ícone de restart para atualizar a interface. <b> Não é necessário sair da página. </b>

<img width="1000" alt="image" src="hands-on-lab-assets/step_6-2_v4.png">

4. Role a tela para baixo até a seção **Knowledge**. Clique em **Choose knowledge**.

<img width="1000" alt="image" src="hands-on-lab-assets/step_6_v3.png">

5. Clique em  **Upload files** e depois **Next**

<img width="1000" alt="image" src="hands-on-lab-assets/step_7_v3.png">

6. Clique e arraste o arquivo de Benefícios para funcionários (Arquivo `Employee-Benefits_ptbr.pdf` dentro da pasta "1. AskRH" gerada após descompactar o LABS.zip) e clique em **Next**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_8_v3.png">  

7. Copie a seguinte descrição na seção **Description** e clique em **Save**:

```
Esta base de conhecimento aborda os benefícios dos funcionários da empresa, incluindo licenças-maternidade, política de animais de estimação, acordos de trabalho flexíveis e pagamento de empréstimos estudantis.
``` 

8. Role para baixo até a seção **Toolset**. Clique em **Add tool +**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_9_v4.png">

9. Na janela _pop up_,  Selecione **Open API**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_10_v5.png">

10.  Arraste e solte ou clique para carregar o arquivo **hr.yaml** (Arquivo `hr.yaml` dentro da pasta "1. AskRH" gerada após descompactar o LABS.zip) , então clique em **Next**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_12_v3.png">  

12. Selecione todas as operações e clique em **Done**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_13_v3.png">

13. Role para baixo até a seção **Behavior**. Insira as instruções abaixo no campo **Instructions**:

```
Use sua base de conhecimento para responder a perguntas gerais sobre benefícios para funcionários.

Use as ferramentas para obter ou atualizar informações específicas do usuário.

Quando o usuário solicitar a exibição de dados de perfil, a verificação do saldo de folgas, a atualização do cargo/endereço ou a solicitação de folga pela primeira vez, primeiro pergunte o nome do usuário, depois invoque a ferramenta e use o mesmo nome em toda a sessão, sem solicitá-lo novamente.

Quando o usuário solicitar folga, converta as datas para o formato AAAA-MM-DD. Por exemplo, 22/05/2025 deve ser convertido para 2025-05-22 antes de passar a data para a ferramenta post_request_time_off.
 ```

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step12.png">

14. Ative o botão de alternância para **Chat with documents**. Selecione **None** em **Citations show in webchat**. Ative o botão de **Show agent**. Clique em **Deploy** no canto superior direito para implantar seu agente:

<img width="1000" alt="image" src="hands-on-lab-assets/step_14_v3.png">

### Teste o Agente de RH em Preview

Teste seu agente no chat de pré visualização à direita, fazendo as seguintes perguntas e validando as respostas. Elas devem ser semelhantes às mostradas nas capturas de tela abaixo:

<b> IMPORTANTE: </b> Quando o agente perguntar seu nome você deve perguntar ao Agente de Suporte lá na página do git.

```
Qual é a política para animais de estimação? 
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13.png">

```
Mostrar os dados do meu perfil.
Gostaria de atualizar meu título. 
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_2.png">

```
Atualize meu endereço.
Qual é o meu saldo de folgas?
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_3.png">

```
Solicitar folgas.
Mostrar os dados do meu perfil.
```
<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_4.png">

#### Testar o Agente de RH no Chat

- Clique no menu de hambúrguer no canto superior esquerdo e depois clique em **Chat**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step15.png">

> Certifique-se que o **HR Agent** está selecionado. 

Agora você pode testar seu agente (Pode repetir as mesmas perguntas do teste anterior)

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step16.png">
