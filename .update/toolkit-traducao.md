# Toolkit de Tradução - Guia Prático

Este documento fornece um guia prático passo a passo para traduzir e adicionar novos use cases ao repositório bootcamp.

---

## 📋 CHECKLIST PRÉ-TRADUÇÃO

Antes de começar a traduzir um novo use case:

- [ ] Ler completamente o use case em inglês
- [ ] Identificar todos os arquivos necessários (README, labs, imagens, etc.)
- [ ] Verificar se há vídeos ou demos
- [ ] Listar termos técnicos específicos do caso
- [ ] Verificar dependências de outros use cases
- [ ] Ler o `.update/.bobrules` para relembrar padrões

---

## 🎯 PROCESSO DE TRADUÇÃO PASSO A PASSO

### PASSO 1: Preparação da Estrutura

```bash
# 1. Criar pasta do novo use case
mkdir -p usecases/nome-do-caso

# 2. Criar subpastas necessárias
cd usecases/nome-do-caso
mkdir -p assets labs images

# 3. Copiar arquivos de imagem/assets do repositório fonte
cp -r ../../../agentic-ai-client-bootcamp/usecases/nome-original/images/* ./images/
cp -r ../../../agentic-ai-client-bootcamp/usecases/nome-original/assets/* ./assets/
```

---

### PASSO 2: Traduzir README.md Principal

#### 2.1 Criar Estrutura Base

```markdown
# Sumário
- [Sumário](#sumário)
- [🎯 Título Principal](#-título-principal)
- [🤔 O Problema](#-o-problema)
- [🎯 Objetivo](#-objetivo)
- [📈 Valor de Negócio](#-valor-de-negócio)
- [🏛️ Arquitetura](#-arquitetura)
- [🎥 Demonstração](#-demonstração)
- [📝 Laboratório prático passo a passo](#-laboratório-prático-passo-a-passo)

# 🎯 [Título do Use Case]

![Banner](./images/banner.png)

## 🤔 O Problema

[Traduzir descrição do problema...]

## 🎯 Objetivo

[Traduzir objetivos...]

## 📈 Valor de Negócio

[Traduzir valor de negócio...]

## 🏛️ Arquitetura

![Arquitetura](./images/architecture.png)

[Descrição da arquitetura...]

## 🎥 Demonstração

[Link para vídeo demo]

## 📝 Laboratório prático passo a passo

👉👉👉 [Clique aqui](./labs/hands-on-lab.md) para acessar as instruções detalhadas.
```

#### 2.2 Dicas de Tradução

**Nomes de Empresas:**
```markdown
❌ ERRADO: A TechCorp Incorporada
✅ CORRETO: A TechCorp Inc.
```

**Termos Técnicos:**
```markdown
❌ ERRADO: Geração Aumentada de Recuperação
✅ CORRETO: Retrieval-Augmented Generation (RAG)

❌ ERRADO: Orquestração de múltiplos agentes
✅ CORRETO: Multi-agent orchestration
```

**Métricas:**
```markdown
✅ CORRETO: Redução de 30% nos custos
✅ CORRETO: Melhoria de até 95% na precisão
✅ CORRETO: Aumento de 1-3% na receita
```

---

### PASSO 3: Traduzir Hands-on Lab

#### 3.1 Estrutura do Lab

```markdown
# [Título do Lab] - Laboratório Prático

## Pré-requisitos

- Acesso ao watsonx Orchestrate
- [Outros pré-requisitos...]

## Parte 1: [Nome da Parte]

### Passo 1: [Descrição do Passo]

[Instruções detalhadas...]

**Importante:** [Avisos importantes]

![Screenshot](../images/step1.png)

### Passo 2: [Próximo Passo]

[Continuar...]

## Parte 2: [Próxima Parte]

[Continuar estrutura...]

## Conclusão

[Resumo do que foi aprendido]
```

#### 3.2 Traduzindo Instruções Técnicas

**Comandos e Código:**
```markdown
Execute o seguinte comando:
```bash
npm install
```

❌ NÃO traduzir comandos
✅ Traduzir apenas a explicação
```

**Campos de Interface:**
```markdown
❌ ERRADO: No campo "Nome", digite...
✅ CORRETO: No campo "Name", digite...

Razão: Manter nomes de campos como aparecem na interface
```

**Blocos de Configuração:**
```markdown
Cole o seguinte JSON:
```json
{
  "name": "example",
  "description": "This is an example"
}
```

❌ NÃO traduzir chaves JSON
✅ Pode traduzir valores se forem exemplos
```

---

### PASSO 4: Ajustar Links e Referências

#### 4.1 Links Internos

```markdown
❌ ERRADO: [Clique aqui](/usecases/ask-hr/README.md)
✅ CORRETO: [Clique aqui](./README.md)

❌ ERRADO: [Lab](hands-on-lab.md)
✅ CORRETO: [Lab](./labs/hands-on-lab.md)
```

#### 4.2 Links para Imagens

```markdown
❌ ERRADO: ![](images/screenshot.png)
✅ CORRETO: ![Screenshot do Passo 1](./images/screenshot.png)

Sempre incluir texto alternativo descritivo
```

#### 4.3 Links Externos

```markdown
✅ CORRETO: [Documentação oficial](https://ibm.com/docs)
✅ CORRETO: [Documentação oficial](https://ibm.com/docs) (em inglês)

Adicionar "(em inglês)" quando apropriado
```

---

### PASSO 5: Revisar e Validar

#### 5.1 Checklist de Revisão

```markdown
## Checklist de Qualidade

### Conteúdo
- [ ] Todos os termos técnicos seguem .bobrules
- [ ] Nomes de empresas não foram traduzidos
- [ ] Tom profissional mantido
- [ ] Sem erros de português
- [ ] Métricas e números corretos

### Estrutura
- [ ] Sumário com links funcionando
- [ ] Emojis corretos nos títulos
- [ ] Seções na ordem padrão
- [ ] Formatação markdown correta

### Links e Mídia
- [ ] Todos os links internos funcionam
- [ ] Imagens carregam corretamente
- [ ] Texto alternativo em todas as imagens
- [ ] Vídeos acessíveis (se aplicável)

### Código e Exemplos
- [ ] Comandos mantidos em inglês
- [ ] Blocos de código com syntax highlighting
- [ ] Exemplos funcionais
- [ ] Explicações claras

### Arquivos
- [ ] Estrutura de pastas correta
- [ ] Todos os assets copiados
- [ ] Nomenclatura de arquivos consistente
- [ ] README.md na raiz do use case
```

#### 5.2 Testar Links

```bash
# Verificar links quebrados (exemplo com ferramenta)
# Navegar até a pasta do use case
cd usecases/nome-do-caso

# Verificar se imagens existem
ls -la images/
ls -la assets/

# Testar markdown localmente
# (usar preview do VS Code ou ferramenta similar)
```

---

## 🔧 FERRAMENTAS ÚTEIS

### Editores Recomendados
- **VS Code** com extensões:
  - Markdown All in One
  - Markdown Preview Enhanced
  - Portuguese - Code Spell Checker

### Validação de Markdown
```bash
# Instalar markdownlint (opcional)
npm install -g markdownlint-cli

# Validar arquivo
markdownlint README.md
```

### Verificação de Links
```bash
# Instalar markdown-link-check (opcional)
npm install -g markdown-link-check

# Verificar links
markdown-link-check README.md
```

---

## 📝 TEMPLATES PRONTOS

### Template: README.md Completo

```markdown
# Sumário
- [Sumário](#sumário)
- [🎯 [Título]](#-título)
- [🤔 O Problema](#-o-problema)
- [🎯 Objetivo](#-objetivo)
- [📈 Valor de Negócio](#-valor-de-negócio)
- [🏛️ Arquitetura](#-arquitetura)
- [🎥 Demonstração](#-demonstração)
- [📝 Laboratório prático passo a passo](#-laboratório-prático-passo-a-passo)

# 🎯 [Título do Use Case]

![Banner](./images/banner.png)

[Breve descrição introdutória do caso de uso]

## 🤔 O Problema

[Descrição do problema de negócio]

**[Nome da Empresa]** enfrenta desafios significativos:

- **Desafio 1**: Descrição
- **Desafio 2**: Descrição
- **Desafio 3**: Descrição

## 🎯 Objetivo

[Descrição dos objetivos da solução]

**Principais Benefícios:**

✅ Benefício 1

✅ Benefício 2

✅ Benefício 3

## 📈 Valor de Negócio

### Para [Stakeholder 1]
- Valor 1
- Valor 2
- Valor 3

### Para [Stakeholder 2]
- Valor 1
- Valor 2
- Valor 3

## 🏛️ Arquitetura

![Arquitetura](./images/architecture.png)

[Descrição da arquitetura e componentes]

### Componentes Principais

**[Componente 1]**: Descrição

**[Componente 2]**: Descrição

**[Componente 3]**: Descrição

## 🎥 Demonstração

[▶️ Assistir à demonstração](URL_DO_VIDEO)

> [!IMPORTANT]
> [Notas importantes sobre o demo ou ambiente]

## 📝 Laboratório prático passo a passo

👉👉👉 [Clique aqui](./labs/hands-on-lab.md) para acessar as instruções detalhadas e implementar este caso de uso.
```

### Template: Hands-on Lab

```markdown
# [Título do Use Case] - Laboratório Prático

## Visão Geral

[Breve descrição do que será construído]

## Pré-requisitos

- [ ] Acesso ao watsonx Orchestrate
- [ ] [Outros pré-requisitos]

## Tempo Estimado

⏱️ Aproximadamente [X] minutos

---

## Parte 1: [Nome da Primeira Parte]

### Passo 1: [Título do Passo]

[Instruções detalhadas]

1. Ação 1
2. Ação 2
3. Ação 3

![Screenshot](../images/step1.png)

**Dica:** [Dica útil]

### Passo 2: [Próximo Passo]

[Continuar...]

---

## Parte 2: [Segunda Parte]

[Continuar estrutura...]

---

## Testando a Solução

[Instruções para testar]

### Cenário de Teste 1

[Descrição e passos]

### Cenário de Teste 2

[Descrição e passos]

---

## Conclusão

Parabéns! 🎉 Você completou o laboratório de [Nome do Use Case].

**O que você aprendeu:**
- Item 1
- Item 2
- Item 3

**Próximos Passos:**
- Sugestão 1
- Sugestão 2

---

## Recursos Adicionais

- [Link 1](URL)
- [Link 2](URL)
```

---

## 🚨 ERROS COMUNS E COMO EVITAR

### Erro 1: Traduzir Termos Técnicos
```markdown
❌ ERRADO: "Geração Aumentada de Recuperação"
✅ CORRETO: "Retrieval-Augmented Generation (RAG)"
```

### Erro 2: Quebrar Links
```markdown
❌ ERRADO: [Lab](hands-on-lab.md)
✅ CORRETO: [Lab](./labs/hands-on-lab.md)
```

### Erro 3: Esquecer Texto Alternativo
```markdown
❌ ERRADO: ![](image.png)
✅ CORRETO: ![Diagrama de Arquitetura](./images/architecture.png)
```

### Erro 4: Traduzir Código
```markdown
❌ ERRADO:
```python
def calcular_total(itens):
    return soma(itens)
```

✅ CORRETO:
```python
def calculate_total(items):
    return sum(items)
```
```

### Erro 5: Inconsistência de Emojis
```markdown
❌ ERRADO: ## 💡 O Problema
✅ CORRETO: ## 🤔 O Problema

Seguir padrão definido em .bobrules
```

---

## 📊 MÉTRICAS DE QUALIDADE

### Critérios de Aceitação

**Tradução (Peso: 40%)**
- Precisão técnica: 10%
- Clareza: 10%
- Tom profissional: 10%
- Gramática: 10%

**Estrutura (Peso: 30%)**
- Organização: 10%
- Formatação: 10%
- Consistência: 10%

**Funcionalidade (Peso: 30%)**
- Links funcionam: 15%
- Imagens carregam: 10%
- Código executável: 5%

**Mínimo para Aprovação: 85%**

---

## 🎓 EXEMPLOS DE REFERÊNCIA

### Use Cases Bem Traduzidos (para usar como referência)
1. `usecases/ask-hr/README.md`
2. `usecases/banking-financial-research-analyst/README.md`
3. `usecases/order-to-cash/README.md`

### Comparar Antes/Depois
```markdown
# Exemplo: Seção "O Problema"

## Versão Original (EN):
"TechCorp Inc., a global IT leader with a workforce of 100,000 employees..."

## Versão Traduzida (PT):
"A TechCorp Inc., líder global em TI com uma força de trabalho de 100.000 colaboradores..."

✅ Mantém: TechCorp Inc. (nome da empresa)
✅ Traduz: "global IT leader" → "líder global em TI"
✅ Adapta: "employees" → "colaboradores" (mais comum em PT-BR corporativo)
```

---

## 🔄 FLUXO DE TRABALHO COMPLETO

```
1. Preparação
   ├── Ler use case original
   ├── Criar estrutura de pastas
   └── Copiar assets

2. Tradução
   ├── README.md principal
   ├── Hands-on lab
   └── Documentação adicional

3. Revisão
   ├── Checklist de qualidade
   ├── Testar links
   └── Validar imagens

4. Finalização
   ├── Commit no Git
   ├── Atualizar README principal
   └── Documentar mudanças
```

---

## 📞 SUPORTE

### Dúvidas Frequentes

**P: Devo traduzir nomes de produtos IBM?**
R: Não. Manter: watsonx Orchestrate, watsonx.ai, etc.

**P: E siglas como RAG, LLM?**
R: Manter em inglês. Primeira menção pode incluir tradução entre parênteses.

**P: Como lidar com termos sem tradução clara?**
R: Manter em inglês e adicionar explicação em português se necessário.

**P: Posso adaptar exemplos para contexto brasileiro?**
R: Sim, mas manter nomes de empresas fictícias originais.

---

**Última atualização:** 2026-02-24  
**Versão:** 1.0