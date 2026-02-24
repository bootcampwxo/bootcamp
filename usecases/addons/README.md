# 🔧 Addons do Bootcamp

Esta pasta contém módulos que você pode adicionar a qualquer laboratório para demonstrar diferentes funcionalidades do produto de forma agnóstica ao caso de uso.

## 📦 Addons Disponíveis

### 1. 🚀 [Bob-Orchestrate](./bob-orchestrate/README.md)
**Deploy de Agentes IA em Produção usando IBM Bob**

Aprenda a usar o IBM Bob para rapidamente incorporar seus agentes IA em websites e criar protótipos funcionais em minutos.

**O que você vai aprender:**
- Criar uma nova aba funcional em um website existente
- Gerar um `server.py` completo com autenticação e integração de APIs
- Integrar agentes do watsonx Orchestrate diretamente no código
- Conectar a UI aos agentes IA

**Pré-requisitos:**
- Laboratório de Análise Competitiva concluído
- Agente de análise competitiva deployado no watsonx Orchestrate
- IBM Bob IDE instalado

**[Iniciar Lab →](./bob-orchestrate/README.md)**

---

### 2. 🛡️ [Governance](./governance/README.md)
**Governança de Agentes no watsonx Orchestrate**

Garanta que seus agentes IA entreguem respostas consistentes, seguras e de alta qualidade através de capacidades abrangentes de avaliação e monitoramento.

**O que você vai aprender:**
- Testar agentes antes do deployment usando casos de teste estruturados
- Monitorar performance de agentes em produção com analytics em tempo real
- Medir indicadores-chave de qualidade (relevância, segurança, custos)
- Rastrear uso de tokens e métricas operacionais
- Manter compliance com trilhas de auditoria completas

**Pré-requisitos:**
- Pelo menos um laboratório de caso de uso concluído
- Agente deployado ou em draft no watsonx Orchestrate
- Acesso ao watsonx Orchestrate com capacidades de avaliação e monitoramento

**Labs Incluídos:**
- **[Avaliação Pré-Deployment](./governance/evaluation.md)** - Teste seus agentes antes de colocá-los em produção
- **[Monitoramento Pós-Deployment](./governance/monitoring.md)** - Monitore performance de agentes em produção

**[Iniciar Labs →](./governance/README.md)**

---

## 🎯 Como Usar os Addons

Os addons são projetados para serem **independentes de casos de uso específicos**. Você pode aplicá-los a qualquer agente que tenha criado nos laboratórios principais.

### Fluxo Recomendado

1. **Complete um caso de uso principal** (ex: AskHR, Retail, Análise Competitiva)
2. **Escolha um addon** baseado no que deseja aprender:
   - Use **Bob-Orchestrate** se quiser aprender a deployar agentes em websites
   - Use **Governance** se quiser aprender a avaliar e monitorar agentes
3. **Siga as instruções do lab** do addon escolhido
4. **Aplique o conhecimento** a outros agentes que criar

### Ordem Sugerida

Para máximo aprendizado, recomendamos esta ordem:

1. ✅ Complete um caso de uso principal
2. 🛡️ **Governance - Evaluation** (teste antes de deployar)
3. 🚀 **Bob-Orchestrate** (deploy em produção)
4. 🛡️ **Governance - Monitoring** (monitore em produção)

---

## 💡 Benefícios dos Addons

### Bob-Orchestrate
- ⚡ **Prototipagem rápida**: De conceito a demo funcional em minutos
- 👥 **Empoderamento de usuários de negócio**: Product managers podem dirigir mudanças de UI
- 📋 **Melhores requisitos**: Protótipos realistas levam a requisitos mais claros
- ♻️ **Reuso para produção**: Código gerado pode ser endurecido para produção

### Governance
- ✅ **Qualidade garantida**: Teste antes de deployar
- 🔒 **Segurança e compliance**: Monitore HAP, PII e riscos de prompt
- 💰 **Gestão de custos**: Rastreie uso de tokens e otimize custos
- 📊 **Melhoria contínua**: Use dados de produção para refinar agentes
- 🎯 **Mitigação de riscos**: Identifique problemas antes que impactem usuários

---

## 📚 Recursos Adicionais

### Documentação Oficial
- [IBM Bob](https://www.ibm.com/products/bob)
- [watsonx Orchestrate - Evaluating Agents](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-evaluating-draft-agent)
- [watsonx Orchestrate - Monitoring Agents](https://www.ibm.com/docs/en/watsonx/watson-orchestrate/base?topic=agents-monitoring)
- [IBM watsonx.governance](https://www.ibm.com/products/watsonx-governance)

### Suporte
- Para questões sobre IBM Bob, consulte a [documentação oficial](https://www.ibm.com/products/bob)
- Para questões sobre watsonx Orchestrate, consulte a [documentação do produto](https://www.ibm.com/docs/en/watsonx/watson-orchestrate)

---

> [!TIP]
> **Dica**: Comece com o addon de Governance para garantir que seus agentes estejam prontos para produção antes de fazer o deploy com Bob-Orchestrate!

---

*Mais addons em breve...*