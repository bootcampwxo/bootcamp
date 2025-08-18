
# 🧑‍💼 AskHR: Automatize tarefas de RH com a IA da Agentic

## Índice

- [Descrição do caso de uso](#use-case-description)
- [Arquitetura](#Arquitetura)
- [Pre-requisitos](#pre-requisitos)
- [Instruções passo a passo para criar agentes](#Instruções-passo-a-passo-para-criar-agentes)
  - [Implantando agente de RH](#deploying-hr-agent)


    
## Descrição do caso de uso
Este caso de uso visa desenvolver e implementar um agente AskHR utilizando o IBM Watsonx Orchestrate, conforme ilustrado no diagrama de arquitetura fornecido. Este agente capacitará os funcionários a interagir com os sistemas de RH e acessar informações de forma eficiente por meio de IA conversacional.

Neste laboratório, construiremos um agente de RH no Watsonx Orchestrate, utilizando ferramentas e conhecimento externo para se conectar a um Sistema de Gestão de Capital Humano simulado. Este agente recupera informações relevantes de documentos para responder às consultas dos usuários e permite que eles visualizem e gerenciem seus perfis.

## Arquitetura

<img width="1000" alt="image" src="arch_diagm.png">




## Pre-requisitos

- Verifique com seu instrutor se **todos os sistemas** estão funcionando antes de continuar.
- Confirme se você tem acesso ao ambiente techzone correto para este laboratório.
- Confirme que você fez o dowload do arquivo LABS.zip 


## Instruções passo a passo para criar agentes:

1. Ao iniciar o watsonx Orchestrate, você será direcionado para esta página. Clique no menu de hambúrguer no canto superior esquerdo:

<img width="1000" alt="image" src="hands-on-lab-assets/step1.png">

2. Clique na seta para baixo ao lado de **Build**.  Em seguida, clique em **Agent Builder**:

<img width="1000" alt="image" src="hands-on-lab-assets/step2.png">

3. Clique em **Create agent +**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_2_v2.png">

4. Selecione "Create from scratch":

Nome: Agente de RH

Descrição:
```
Você é um agente que lida com as dúvidas dos funcionários sobre RH. Você fornece respostas curtas e concisas, com no máximo 200 palavras. Você pode ajudar os usuários a verificar os dados do perfil, recuperar o saldo de folgas mais recente, atualizar cargo ou endereço e solicitar folgas. Você também pode responder a perguntas gerais sobre os benefícios da empresa.
```  
Clique em **Create**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step4.png">


5. Selecione "Default" na seção Agent style.

<img width="1000" alt="image" src="hands-on-lab-assets/step_5_v2.png">

6. Role a tela para baixo até a seção **Knowledge**. Copie a seguinte descrição na seção **Knowledge Description**:

```
Esta base de conhecimento aborda os benefícios dos funcionários da empresa, incluindo licenças-maternidade, política de animais de estimação, acordos de trabalho flexíveis e pagamento de empréstimos estudantis.
```

Clique em  **Upload files**:

<img width="1000" alt="image" src="hands-on-lab-assets/step_7_v3.png">

7. Clique e arraste o arquivo de Benefícios para funcionários (Arquivo "Employee-Benefits_ptbr.pdf" dentro da pasta "2. AskRH" gerada após descompactar o LABS.zip) e clique em **Upload**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step6.png">  

8. Aguarde até que o arquivo seja carregado com sucesso e verifique novamente se ele agora é exibido na seção Knowledge:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step7.png">  

9. Role para baixo até a seção **Toolset**. Clique em **Add tool +**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step8.png">

10. Selecione **Import**:

<img width="1000" alt="image" src="hands-on-lab-assets/step13.png">

11. Arraste e solte ou clique para carregar o arquivo **hr.yaml** (Arquivo "hr.yaml" dentro da pasta "2. AskRH" gerada após descompactar o LABS.zip) , então clique em **Next**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step10.png">    

12. Selecione todas as operações e clique em **Done**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step11.png">

13. Role para baixo até a seção **Behavior**. Insira as instruções abaixo no campo **Instructions**:

```
Use sua base de conhecimento para responder a perguntas gerais sobre benefícios para funcionários.

Use as ferramentas para obter ou atualizar informações específicas do usuário.

Quando o usuário solicitar a exibição de dados de perfil, a verificação do saldo de folgas, a atualização do cargo/endereço ou a solicitação de folga pela primeira vez, primeiro pergunte o nome do usuário, depois invoque a ferramenta e use o mesmo nome em toda a sessão, sem solicitá-lo novamente.

Quando o usuário solicitar folga, converta as datas para o formato AAAA-MM-DD. Por exemplo, 22/05/2025 deve ser convertido para 2025-05-22 antes de passar a data para a ferramenta post_request_time_off.
 ```

 <img width="1000" alt="image" src="hands-on-lab-assets/hr_step12.png">

14. Teste seu agente no chat de pré-visualização à direita, fazendo as seguintes perguntas e validando as respostas. Elas devem ser semelhantes às mostradas nas capturas de tela abaixo:

> IMPORTANTE: Quando o agente perguntar seu nome você deve utilizar qualquer um disponível em na planilha de usuários (Arquivo "users_data.xlsx" dentro da pasta "2. AskRH" gerada após descompactar o LABS.zip) 

```
1. Qual é a política para animais de estimação?

2. Mostrar os dados do meu perfil.

3. Gostaria de atualizar meu título.

4. Atualizar meu endereço.

5. Qual é o meu saldo de folgas?

6. Solicitar folgas.


```

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13.png">

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_2.png">

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_3.png">

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step13_4.png">

15. Depois de validar as respostas, clique em **Deploy** no canto superior direito para implantar seu agente:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step14.png">

16. Clique no menu de hambúrguer no canto superior esquerdo e depois clique em **Chat**:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step15.png">

17. Certificar-se que o **HR Agent** está selecionado. Agora você pode testar seu agente:

<img width="1000" alt="image" src="hands-on-lab-assets/hr_step16.png">
