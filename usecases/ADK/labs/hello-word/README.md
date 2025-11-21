# 🤖✨ Watson Orchestrate — Tutorial "Hello World"



> 🔵 **Link oficial do tutorial (referência):**  
> https://developer.watson-orchestrate.ibm.com/tutorials/tutorial_1_hello_world

---

## 📚 Índice

- [📘 Visão Geral](#-visão-geral)
- [🎯 Objetivos](#-objetivos)
- [🧰 Pré-requisitos](#-pré-requisitos)
- [🚀 Passo 1 — Criar a Skill Hello World](#-passo-1--criar-a-skill-hello-world)
- [🔧 Passo 2 — Implementar a Lógica da Skill](#-passo-2--implementar-a-lógica-da-skill)
- [▶️ Passo 3 — Testar a Skill](#️-passo-3--testar-a-skill)
- [🤖 Passo 4 — Integrar com o Agente](#-passo-4--integrar-com-o-agente)
- [🧪 Exemplos de Uso](#-exemplos-de-uso)
- [🚀 Próximos Passos](#-próximos-passos)
- [📝 Créditos](#-créditos)

## 📘 Visão Geral
Os passos a seguir orientam você a disponibilizar seu agente no Criador de Agentes.

## 🧰 Pré-requisitos

Antes de começar:

- Conta ativa no **Watson Orchestrate Developer**
- Navegador moderno
- Acesso ao painel de Skills
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
<br>
```python
print("Hello World")
```

<br>
6. Cole o código no editor de texto e salve o arquivo na greetings.pypasta * hello-world* .
7. Abra o terminal que você usa normalmente.
8. Navegue até a pasta. Por exemplo, cd ~/Desktop/hello-world.
9. Execute o comando **orchestrate tools import -k python -f tools/greetings.py**
10. Execute o comando **orchestrate agents import -f greeter.yaml**
11. Execute o comando **orchestrate chat start**



## 🧪 Exemplos de Uso

Experimente os seguintes comandos no agente:

```
Execute a skill Hello World agora.
```

```
Qual é a mensagem da minha skill Hello World?
```

```
Rode minha automação Hello World.
```

---

## 🚀 Próximos Passos

Agora que você já domina o básico, continue sua jornada:

👉 Crie skills com parâmetros  
👉 Integre com APIs REST externas  
👉 Crie fluxos inteligentes  
👉 Automatize tarefas reais  
👉 Siga para o tutorial avançado de Workflows  

---

## 📝 Créditos

Este README segue a estrutura e conceitos do tutorial oficial:  
https://developer.watson-orchestrate.ibm.com/tutorials/tutorial_1_hello_world  

Conteúdo reescrito em formato educacional para uso em treinamentos e GitHub.
