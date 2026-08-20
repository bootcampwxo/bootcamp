# 🎓 Configuração do Instrutor para Monitoramento de Agentes 🚗


Este guia fornece aos instrutores as informações necessárias para implantar e gerenciar o ambiente do laboratório do Assistente de Compra de Carros para os alunos.

## 📋 Pré-requisitos

### Requisitos Gerais

**Recursos do IBM Cloud**:
- Conta IBM Cloud com acesso ao watsonx Orchestrate
- Acesso ao IBM Container Registry
- Acesso ao IBM Code Engine (Serverless Containers)
- Instância do serviço watsonx.ai

**Autenticação**:
- **Chave SSH**: Se você não tiver uma, crie uma [chave SSH](https://github.ibm.com/skol/agentic-ai-client-bootcamp-instructors/blob/main/environment-setup/common/sshkey.md) não criptografada (sem passphrase) e salve a chave pública nas configurações do seu usuário em `github.ibm.com`. A chave privada será usada nas etapas de implantação.
- **Chave de API do IBM Cloud**: Se você ainda não tiver uma, crie uma [chave de API do IBM Cloud](https://github.ibm.com/skol/agentic-ai-client-bootcamp/blob/main/environment-setup/api_key_setup.md) para a conta TechZone Cloud.

### Requisitos Específicos da Aplicação

**Chaves de API**:
- **Chave de API Tavily**: Crie uma chave de API Tavily em https://tavily.com/ (faça login usando sua conta Google)



## 🚀 Guia de Implantação

### Passo 1: Reservar Ambiente TechZone

Você precisa reservar um bundle TechZone, que inclui acesso a:
- **watsonx.ai**
- **watsonx Orchestrate Trial Bundle**
- **IBM Container Registry**
- **IBM Serverless Containers (Code Engine)**

📖 **Instruções**: Siga o [Guia de Configuração de Ambiente](../../../../environment-setup/readme.md) para fazer a reserva.

### Passo 2: Implantar Agentes Externos

Existem duas opções para agentes de terceiros backend: 
1. Agente LangGraph implementado usando **FastAPI** e **LangGraph**, implantado no **IBM Code Engine**. A imagem do container será carregada no **IBM Container Registry**. 

      📄 **Script Backend**: [api/app.py](https://github.ibm.com/Hannah-Benig/langgraph-gov/blob/main/api/app.py)

      Siga as instruções aqui para implantar a aplicação backend.

      📖 **Instruções de Implantação**: [DEPLOY_MANUAL.md](./DEPLOY_MANUAL.md)

2. **Agente de Busca Web LangGraph no Google Cloud (GCP)**.
   Siga as instruções aqui para implantar a aplicação backend.
   
   📄 **Instruções de Implantação**: [Deploy GCP](hyperscalers/gcp_car_agent/README.md)

**Importante**: Anote a URL de implantação após completar as etapas manuais.

## 👥 Configuração dos Alunos

### Informações para Fornecer aos Alunos

Após a conclusão da implantação, forneça aos alunos:

1. **URL do Endpoint do Agente**: A URL do agente LangGraph implantado (da saída da implantação)
   ```
   Exemplo: https://your-agent-url.codeengine.appdomain.cloud/v1/chat
   ```

2. **Chave de API**: A Chave de API do Agente que você gerou durante a configuração
   ```
   Exemplo: 1234 (ou sua chave gerada)
   ```

3. **PDF do Catálogo de Carros**: O arquivo `abcCatalog with prices.pdf` do diretório sample-data

4. **CSV de Avaliação**: O arquivo `car-buying-eval.csv` para testes (opcional)

### Guia de Laboratório para Alunos

Direcione os alunos para o guia de laboratório abrangente:

📖 **[Guia de Laboratório para Alunos](../README.md)**

