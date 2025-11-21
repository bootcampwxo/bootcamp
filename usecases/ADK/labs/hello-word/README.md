# 🤖✨ Watson Orchestrate — Tutorial "Hello World"

> 🔵 **Link oficial do tutorial (referência):**  
> https://developer.watson-orchestrate.ibm.com/tutorials/tutorial_1_hello_world



## 📘 Visão Geral
Os passos a seguir orientam você a disponibilizar seu agente no Criador de Agentes.

## 🧰 Pré-requisitos

Antes de começar:

- Conta ativa no **Watson Orchestrate Developer**
- Navegador moderno
- VM com o ADK.
- Vontade de aprender 😄

---

## 🚀 Passo a Passo — Hello World

1. Em seu diretório, crie uma pasta com o nome hello-world .
2. Abra um editor de texto, como o Visual Studio Code.
3. Para criar o agente, copie o seguinte código:

```yaml
spec_version: v1
kind: native
name: greeter
description: An agent that greets you using the output from its tool
instructions: Always run the tool "Greeting" when the user types Greeting in the chat. 
llm: watsonx/meta-llama/llama-3-2-90b-vision-instruct
style: default
collaborators: []
tools:
  - greeting
```
 
4. Cole o código no editor de texto e salve o arquivo como **greeter.yaml** dentro da pasta **hello-world** .
5. Para criar a ferramenta, copie o seguinte código:
```python
#greetings.py
from ibm_watsonx_orchestrate.agent_builder.tools import tool


@tool
def greeting() -> str:
    """
    Greeting for everyone   
    """

    greeting = "Hello World"
    return greeting
```

6. Cole o código no editor de texto e salve o arquivo como **greetings.py** dentro da pasta **hello-world** .
7. Abra o terminal que você usa normalmente.
8. Navegue até a pasta. Por exemplo, cd ~/Desktop/hello-world.
9. Execute o comando **orchestrate tools import -k python -f tools/greetings.py**
10. Execute o comando **orchestrate agents import -f greeter.yaml**
11. Execute o comando **orchestrate chat start**



## 🧪 Testando seu agente

Após a configuração, você pode digitar “Saudação” na janela de bate-papo e continuar interagindo com seu agente.
