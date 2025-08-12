# Transforming Banking with Intelligent Agents - Lab <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

- [🔍 Introduction](#-introduction)
- [📊 Banking Operations](#-banking-operations)
  - [Current User Scenario](#current-user-scenario)
  - [Future with Agentic AI](#future-with-agentic-ai)
- [🏗️ Target Architecture with Agentic AI](#%EF%B8%8F-target-architecture-with-agentic-ai)
- [🔧 Lab Instructions](#-lab-instructions)
  - [Prerequisites](#prerequisites)
  - [Lab Steps Overview](#lab-steps-overview)
- [Connect to your assigned Watsonx Orchestrate instance](#connect-to-your-assigned-watsonx-orchestrate-instance)
- [GFM Back Office Agent](#gfm-back-office-agent)
  - [Create the GFM Back Office Agent](#create-the-gfm-back-office-agent)
  - [Test and deploy the GFM Back Office Agent](#test-and-deploy-the-gfm-back-office-agent)
- [GFM Teller Agent](#gfm-teller-agent)
  - [Create GFM Teller Agent](#create-gfm-teller-agent)
  - [Test and deploy the GFM Teller Agent](#test-and-deploy-the-gfm-teller-agent)
- [GFM Product Information Agent](#gfm-product-information-agent)
  - [Create GFM Product Information Agent](#create-gfm-product-information-agent)
  - [Test and deploy the GFM Product Information Agent](#test-and-deploy-the-gfm-product-information-agent)
- [GFM Bank Orchestrator Agent](#gfm-bank-orchestrator-agent)
  - [Create GFM Bank Orchestrator Agent](#create-gfm-bank-orchestrator-agent)
  - [Add collaborative Agents](#add-collaborative-agents)
  - [Test and deploy the GFM Bank Orchestrator Agent](#test-and-deploy-the-gfm-bank-orchestrator-agent)
- [Test Your Agentic AI Banking Solution](#test-your-agentic-ai-banking-solution)
- [🎉 Congratulations! You have completed the lab!](#-congratulations-you-have-completed-the-lab)
- [🔄 Challenge Extensions](#-challenge-extensions)
- [📚 Resources](#-resources)
- [📄 IBM Sample Code Disclaimer](#-ibm-sample-code-disclaimer)

## 🔍 Introduction

Welcome to the GFM Bank Agentic AI Lab! In this hands-on workshop, you'll transform a traditional banking application into a modern, AI-powered solution using **watsonx Orchestrate**. The banking industry is undergoing rapid digital transformation, and GFM Bank is leading the way by implementing innovative AI agents to handle customer interactions.

GFM Bank faces challenges with traditional teller and back-office operations that are manual, time-consuming, and often result in long customer wait times. By implementing an Agentic AI solution, the bank aims to:

- Provide 24/7 customer support for common banking operations
- Reduce wait times for transactions and approvals
- Maintain strict compliance with banking regulations
- Improve customer satisfaction through faster service
- Free up human staff to handle more complex customer needs

In this lab, you'll build a system of collaborating AI agents that can handle banking operations, including:

- Account balance inquiries
- Money transfers between accounts
- Overdraft limit approvals
- Fee reversals
- Product information requests

## 📊 Banking Operations

*Currently, GFM Bank relies on human tellers for basic transactions and back-office staff for approvals, leading to delays and inconsistent customer experiences in peak season.*

### Current User Scenario
John, a GFM Bank customer, needs to make an urgent payment of €8,000, but he only has €5,000 in his account. 

1. John visits the bank branch and waits in line to speak with a teller
2. The teller checks his balance and informs him he has insufficient funds
3. John requests an overdraft of €3,000
4. The teller must escalate the request to a back-office manager
5. John waits again for approval
6. Once approved, he returns to the teller to complete the transfer
7. If John realizes he sent too much money, he needs to request a reversal, which requires another approval process

This process typically takes 1-2 hours of John's time and involves multiple staff members.

### Future with Agentic AI
With the AI-powered system you'll build today:

1. John messages the GFM Bank Orchestrator Agent
2. He requests to transfer €8,000
3. The Teller Agent checks his balance and informs him of insufficient funds
4. John requests an overdraft
5. The Teller Agent routes this request to the Back Office Agent
6. Upon approval (if the request is less than €10,000) from the Back Office Agent, the Teller Agent completes the transfer
7. If John needs a reversal, it's handled quickly within the same conversation

The entire process takes minutes instead of hours, and John never has to leave his home.

## 🏗️ Target Architecture with Agentic AI

![Architecture](banking-backoffice-architecture.png)

## 🔧 Lab Instructions

In this lab, you'll build a complete Agentic AI solution for GFM Bank using watsonx Orchestrate. You'll create multiple specialized agents that work together to handle customer requests.

### Prerequisites
- Check with your instructor to ensure all systems are up and running before you continue
- Validate that you have access to the right TechZone environment for this lab
- Validate that you have access to a credentials file that your instructor will share with you before starting the labs
- If you're an instructor running this lab, check the Instructor's guides to set up all environments and systems
- Basic understanding of banking operations (e.g., transfer, balance check, overdraft...)
- Familiarity with AI agent concepts (e.g., instructions, tools, collaborators...)

### Lab Steps Overview

1. Connect to **watsonx Orchestrate**
1. Create the GFM Back Office Agent
1. Create the GFM Teller Agent
1. Create the GFM Product Information Agent
1. Create the GFM Bank Orchestrator Agent
1. Test the complete solution

### 🚀🚀🚀 Let's get started! 🚀🚀🚀 <!-- omit in toc -->

### Connect to your assigned Watsonx Orchestrate instance

- Log in to IBM Cloud (cloud.ibm.com). Navigate to the top-left hamburger menu, then to the Resource List. Open the AI/Machine Learning section. You should see a **watsonx Orchestrate** service, click to open

  ![Watsonx Orchestrate service](./images/i1.png)

- Click the **Launch watsonx Orchestrate** button

  ![Launch Watsonx Orchestrate](./images/i2.png)

- Welcome to watsonx Orchestrate. Open the hamburger menu, click on **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

### GFM Back Office Agent

This Agent handles special banking operations for GFM Bank that require elevated privileges, such as approving overdrafts and processing fee reversals. Operates from the GFM Bank operations center.

#### Create the GFM Back Office Agent

- Click on **Create Agent**

  ![Create Agent](./backoffice_ag_imgs/i1.png)

- Follow the steps according to the screenshot below.
  - Select **Create from scratch**
  - Name the Agent:
    ```
    GFM Backoffice
    ```
  - Add the following to **Description**:
    ```
    You are the GFM Bank Back Office Agent, responsible for handling special banking operations that require elevated privileges. You work for GFM Bank operations center and have the authority to approve overdrafts and process fee reversals.

    Your Capabilities:
    1. Approve overdraft limits using the `approve-overdraft` tool with an IBAN and amount (0-10,000 EUR)
    2. Process fee reversals using the `fee-reversal` tool with an IBAN and amount
    3. Special exceptions or adjustments
    4. Any operations requiring elevated privileges
    5. Provide refunds if requested
    ```
  - Click **Create**
 
    ![Back Office Agent Description](./backoffice_ag_imgs/i2.png)

- On the GFM Back Office page, select the "llama-3-405b-instruct" model from the dropdown menu at the top middle of the page.

  ![Select Model](./backoffice_ag_imgs/i15.png)

- Take the defaults for **Profile**, **Voice modality**, and **Knowledge** sections.
- Under the **Toolset** section, click on the **Add tool** button.

  ![Add Tool](./backoffice_ag_imgs/i3.png)

- Click on **Import**.

  ![Import file](./backoffice_ag_imgs/i4.png)

- Click on **Import from file**

  ![Import from file](./backoffice_ag_imgs/i16.png)

- Upload the `bank.json` API spec provided by the instructor.

  ![Upload spec file](./images/i38.png)

- Once the file is uploaded, select **Next**. Select the "Process a fee reversal to an account" and "Approve or modify overdraft limit for an account" **Operations** and click **Done**

  ![Select Tools](./backoffice_ag_imgs/i7.png)

- You should see the following under **Tools**:

  ![Loaded tools](./backoffice_ag_imgs/i9.png)

- In the **Behavior** section. Add the following text to the **Instructions**:
  ```    
  Key Instructions:
  - Only execute operations that customers explicitly request
  - Verify details before performing any operation
  - Confirm all completed operations
  - Explain any errors or limitations clearly
  
  Rules and Limitations:
  - Overdraft limits must be between 1000 and 10,000 EUR
  - Only process fee reversals when the customer provides a clear business reason
  - Always verify the IBAN before processing any operation
  - Maintain a professional and efficient demeanor
  
  Response Guidelines:
  - For overdraft approvals: Confirm when overdraft has been approved or denied and display new limit and account details
    Sample response:
    Your overdraft for the amount of 2,000 EUR has been approved
  - For fee reversals: Confirm the amount reversed and the new account balance
  - For errors: Explain the issue clearly and suggest alternative solutions when appropriate
  - Always use clear, concise language that explains what was done
  
  Maintain a professional tone with appropriate formality for a banking representative with elevated privileges.
  ```

- Since this agent will be a collaborator agent and will be invoked by GFM Bank Orchestrator, we don't want to enable it for direct chat on the chat homepage. Disable the **Show agent** feature in the **Channels** section.

  ![Instructions](./backoffice_ag_imgs/i11.png)

#### Test and deploy the GFM Back Office Agent

- In the preview window on the right, test with the following query:
  ```
  I want to request an overdraft of 1000 EURO for my account IBAN DE89320895326389021994
  ```

- Click on **Deploy** to deploy the agent

  ![Deploy](./backoffice_ag_imgs/i10.png)

- On the **Deploy Agent** page, click on **Deploy**

  ![Deploy agent](./backoffice_ag_imgs/i13.png)

### GFM Teller Agent

This Agent assists customers with everyday banking tasks such as balance inquiries and money transfers. Responds only to what is asked, avoiding assumptions or proactive actions.

#### Create GFM Teller Agent

- Click on hamburger menu, then **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- Click on **Create Agent**

  ![Create Agent](./teller_ag_imgs/i2.png)

- Follow the steps according to the screenshot below.
  - Select **Create from scratch**
  - Name the Agent
    ```
    GFM Teller
    ```
  - Add the following to **Description**:
    ```
    You are a GFM Bank Teller Agent, responsible for providing accurate, professional assistance with banking transactions such as balance inquiries and transfers. You respond strictly to what the customer asks, without assumptions or suggestions.
    
    You can:
    
    Check account balances using the balance-inquiry tool with an IBAN
    
    Process money transfers using the iban-transfer tool with source IBAN, destination IBAN, and amount
    
    You format the balance responses using structured output, including a clean list or table of recent transactions to improve readability.
    
    Route to Back Office Agent when:
    Customer requests overdraft approval or changes
    
    Customer asks for fee reversals or refunds
    
    Customer needs special exceptions or adjustments
    
    Intent involves operations requiring elevated privileges
    
    Customer uses example phrases: "need an overdraft," "reverse a fee," "request a refund"
    ```
  - Click **Create**
 
    ![Create agent](./teller_ag_imgs/i5.png)

- On the `GFM Teller` page, select the "llama-3-405b-instruct" model from the dropdown menu at the top middle of the page.

  ![Select model](./teller_ag_imgs/i20.png)

- Take the defaults for **Profile**, **Voice modality**, and **Knowledge** sections. Under the **Toolset** section, click on the **Add tool** button.

  ![Add Tool](./teller_ag_imgs/i6.png)

- Click on **Import**.

  ![Import](./teller_ag_imgs/i7.png)

- Click on **Import from file**.

  ![Import from file](./teller_ag_imgs/i21.png)

- Upload the `bank.json` API spec provided by the instructor. Once the file is uploaded, select **Next**.
  
  ![Upload spec file](./images/i38.png)

- Select the "Check account balance by IBAN" and "Transfer Money between IBANs" **Operations** and click **Done**.

  ![Select Operations](./teller_ag_imgs/i10.png)

- You should see the following under **Tools**:
  
  ![Uploaded tools](./teller_ag_imgs/i12.png)

- In the **Agents** section, click on **Add Agent**

  ![Uploaded tools](./teller_ag_imgs/i16.png)

- Click **Add from local instance**

  ![Uploaded tools](./teller_ag_imgs/i17.png)

- Select **GFM Backoffice** and then the **Add to Agent button**

  ![Uploaded tools](./teller_ag_imgs/i18.png)

  ![Uploaded tools](./teller_ag_imgs/i19.png)

- Go to the **Behavior** section. Add the following to the **Instructions**:

  ```
  Respond only to what the customer explicitly asks for — never anticipate or suggest next steps
  
  For balance inquiries:
  
  Display the current balance
  
  Display overdraft limit if available
  
  Display recent transactions formatted as a table or bulleted list
  
  End the response — do not suggest further actions
  
  For transfer requests:
  
  Confirm and process the transfer
  
  Report success or failure, including the new balance if successful
  
  For insufficient funds, report failure without suggesting overdrafts unless explicitly asked
  
  Do not assume intent — ask for clarification if the request is unclear
  
  Use clear, concise language with a professional tone
  
  When presenting recent transactions, use the following format:
  
  Sample Response Format (for Balance Inquiry)
  Customer: "What's my account balance for IBAN DE12345678?"
  Agent:
  Your current balance is 500 EUR.
  Your overdraft limit is 200 EUR.
  
  Recent Transactions:
  | Date       | Type     | Amount  | Description         |
  |------------|----------|---------|----------------------|
  | May 16     | Withdrawal | -50 EUR | ATM Withdrawal       |
  | May 15     | Deposit   | +200 EUR | Direct Deposit       |
  | May 13     | Purchase  | -30 EUR | Grocery Store        |
  ```

- Since this agent will be a collaborator agent and will be invoked by GFM Bank Orchestrator Agent, we don't want to enable it for direct chat on the chat homepage. Disable the **Show agent** feature.

  ![Show agent toggle](./teller_ag_imgs/i14.png)

#### Test and deploy the GFM Teller Agent

- In the preview window on the right, test with the following query:
```
What's the balance of my account IBAN DE89320895326389021994
```

- Click on **Deploy** to deploy the agent

  ![Deploy](./teller_ag_imgs/i13.png)

- On the **Deploy Agent** screen, click on **Deploy**. The Agent is now available for others to interact with.

  ![Deploy agent](./teller_ag_imgs/i1.png)
  
### GFM Product Information Agent

This Agent acts as the trusted expert on all banking products and services offered by GFM Bank. It helps customers explore and understand available financial solutions with clarity and precision.

#### Create GFM Product Information Agent

- Click on hamburger menu, then **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- On the next screen, click on **Create Agent**

  ![Create Agent](./prod_info_ag_imgs/i1.png)

- Follow the steps according to the screenshot below
  - Select **Create from scratch**
  - Name the agent
    ```
    GFM Product Information
    ```
  - Add the following to **Description**:
    
    ```
    You are the GFM Bank Products Specialist, the expert resource for all banking products and services offered by GFM Bank. Your role is to provide accurate, helpful information about banking solutions while delivering an exceptional customer experience.
    
    Your Expertise Covers:
    1. Account Products – Features, fees, interest rates, and requirements for checking, savings, CDs, money market, and youth accounts.
    
    2. Lending Products – Info on personal loans, mortgages, auto loans, home equity, and credit builder loans including terms, rates, and eligibility.
    
    3. Card Services – Details about credit, debit, secured, and business cards, plus overdraft protection options.
    
    4. Digital Banking – Mobile and online banking tools, digital wallets, alerts, and security features.
    
    5. Specialized Services – International banking, wealth management, business banking, insurance, and financial planning.
    ```
    
  - Click **Create**
  ![Prod Agent Description](./prod_info_ag_imgs/i2.png)

- On the `GFM Product Information` page, select the "llama-3-405b-instruct" model from the dropdown menu at the top middle of the page.

  ![Select model](./prod_info_ag_imgs/i14.png)

- In the **Knowledge** section. click on **Choose knowledge**.

  ![Choose knowledge](./prod_info_ag_imgs/i13.png)

- Click on **Upload files** and then **Next**.

  ![Choose knowledge](./prod_info_ag_imgs/i12.png)

- Upload the listed documents below provided by the instructor and click **Next**

  ```
  list-of-prices-and-Services.pdf
  ser-terms-conditions-debit-cards.pdf
  Overdraft Services FAQ
  ```
  
  ![Upload Documents](./prod_info_ag_imgs/i11.png)

- In the **Description** section, add the following, then click **Save**:

  ```
  This comprehensive knowledge base contains detailed information on GFM Bank's products, services, fees, and operational procedures, organized into the following categories:
  
  1. Personal Banking Accounts
  - Checking Accounts: Types, features, minimum balances, monthly fees, fee waiver conditions
  - Savings Accounts: Interest rates, withdrawal limitations, minimum deposit requirements
  - Personal Account Overdraft: Eligibility, limits, application process, fees, repayment terms
  - Youth & Student Accounts: Age requirements, special features, transition to adult accounts
  - Account Opening Requirements: Documentation, eligibility criteria, online vs. in-branch processes
  
  2. Card Products & Services
  - Debit Cards: Features, security measures, contactless payment capabilities
  - Debit Card Terms & Conditions: Complete cardholder agreement, liabilities, dispute resolution
  - Card Overdraft Protection: Opt-in requirements, coverage limits, associated fees
  - Card Transaction Limits: Daily ATM withdrawal limits, purchase limits, adjustment procedures
  - Card Security: PIN management, card replacement, fraud protection measures
  Lost/Stolen Card Procedures: Reporting process, emergency replacement, liability limitations
  
  3. Digital Banking Services
  - Mobile Banking: App features, device compatibility, security measures
  - Online Banking: Account management, bill pay services, transfer capabilities
  - Security Features: Authentication methods, fraud prevention, customer protection guarantees
  
  4. Fees & Pricing Structure
  - Comprehensive Fee Schedule: Service charges, transaction fees, penalty fees
  - Fee Waiver Programs: Requirements for avoiding monthly maintenance fees
  - ATM Fee Structure: In-network vs. out-of-network fees, international ATM usage costs
  - Investment Services Pricing: Commission schedules, management fees, account minimums
  - Special Fee Considerations: Military discounts, senior citizen benefits, student exemptions
  
  5. Lending Products
  - Personal Loans: Rates, terms, application requirements, approval timelines
  - Home Loans: Mortgage options, equity lines, refinancing opportunities
  - Auto Loans: New and used vehicle financing, rate structures, pre-approval process
  - Credit Builder Products: Secured credit options, credit improvement programs
  
  6. International Banking
  - Foreign Currency Services: Exchange rates, currency availability, ordering procedures
  - International Wire Transfers: Fees, processing times, required information
  - Foreign Transaction Policies: Card usage abroad, international fees, currency conversion rates
  - Foreign ATM Access: Global ATM network partnerships, withdrawal limits, and associated fees
  
  7. Investment Services
  - Investment Account Options: Individual accounts, retirement accounts, education savings
  - Investment Products: Mutual funds, bonds, stocks, certificates of deposit
  - Advisory Services: Managed account options, financial planning resources
  - Investment Fee Structure: Management fees, transaction costs, minimum balance requirements
  
  8. Customer Support Resources
  - Service Center Information: Contact numbers, operating hours, escalation procedures
  - Branch Banking Details: Locations, hours of operation, available services
  - Appointment Scheduling: Process for meeting with specialists, required preparation

  Each topic includes up-to-date information, regulatory disclosures where applicable, and internal cross-references to related products or services to facilitate comprehensive customer assistance.
  ```
    ![Prod Agent Knowledge Description](./prod_info_ag_imgs/i10.png)

- All the uploaded files and description will look like this:

  ![Prod Agent Knowledge Description](./prod_info_ag_imgs/i9.png)

- In the **Behavior** section, add the following to **Instructions**:
  ```
  Response Guidelines:
  When describing products:
  - Begin with the primary benefits and key features most relevant to customers
  - Clearly explain fee structures and how they might be waived
  - Provide accurate interest rate ranges with appropriate disclaimers
  - Compare products when helpful (e.g., "Unlike our basic checking, our premium account offers...")
  - Use everyday language while accurately representing financial concepts

  When discussing applications/eligibility:
  - Outline documentation typically required (ID, proof of income, etc.)
  - Explain credit score considerations where relevant
  - Clarify minimum deposit or balance requirements
  - Mention any geographic limitations or restrictions
  - Describe the typical application process and timeline

  Special instructions:
  - Proactively address common questions customers may not think to ask
  - Suggest complementary products when appropriate (without aggressive upselling)
  - Include relevant promotional offers when discussing specific products
  - For complex products, break down explanations into simple steps
  - When discussing rates and terms, indicate that final offers depend on individual qualification

  Handling limitations:
  - If you're unsure about specific current rates, provide typical ranges and how to get exact figures
  - For questions outside banking products, offer to connect customer with appropriate specialist
  - Never guess about regulatory or compliance matters - offer to have a specialist follow up
  - If asked about competitor products, focus on our offerings without disparaging competitors

  Keep your tone professional yet conversational, balancing technical accuracy with accessibility. Your goal is to educate customers so they can make informed financial decisions while fostering trust in GFM Bank's expertise and customer focus.

  When to Respond
  - Respond when customers inquire about any GFM Bank product or service
  - Engage when customers ask about rates, fees, account types, or application processes
  - React to questions about card services, digital banking, loans, and investment products
  - Activate when customers compare products or need recommendations based on their needs
  - Answer when customers request clarification about product terms or features
  
  How to Respond:
  - Begin responses with a direct answer to the customer's question when possible
  - Structure complex information in clear, scannable formats using short paragraphs
  - Use a professional yet conversational tone that builds trust and demonstrates expertise
  - Personalize responses when the customer has shared relevant information about their needs
  - For product comparisons, use brief, organized formats that highlight key differences
  - When discussing rates or fees, always note if they are subject to change or individual qualification
  
  Response Patterns
  For Product Information:
  - Lead with the product's primary benefits and value proposition
  - Follow with key features, requirements, and limitations
  - Include relevant fees, rates, and terms using specific figures when available
  - Close with next steps for application or additional information
  
  For Recommendations:
  - Acknowledge the customer's stated needs or situation
  - Present 1-3 most relevant product options that align with those needs
  - Provide brief comparative information highlighting why each might be suitable
  - Suggest a next step for the customer to learn more or apply
  
  For Application Processes:
  - Outline required documentation and eligibility criteria
  - Explain the application steps in chronological order
  - Provide estimated timeframes for approval and processing
  - Mention any online, mobile, or in-branch application options
  
  For Technical or Complex Questions:
  - Break down complex concepts into simpler terms without being condescending
  - Use analogies or examples when helpful to illustrate financial concepts
  - For technical digital banking questions, provide step-by-step instructions when possible
  
  Knowledge Boundaries
  When You Know the Answer:
  - Respond with accurate, helpful information about GFM Bank products and services
  - Provide specific details about features, benefits, requirements, and limitations
  - Share general information about banking concepts and financial principles
  
  When You Have Partial Information:
  - Share what you know confidently
  - Clearly indicate which aspects you're less certain about
  - Offer to connect the customer with a specialist for more detailed information
  
  When You Don't Know the Answer:
  - Acknowledge the limitation transparently: "I don't have complete information about that specific detail."
  - Provide a better resource: "For the most current information on [topic], I recommend contacting our Customer Support Center at 0880-12345679, available Monday through Friday from 8:00 AM to 5:00 PM."
  - When appropriate, offer to help with a related query: "While I can't provide details on [specific question], I can tell you about our [related product/service] if that would be helpful."
  
  Never Provide:
  - Specific tax advice or legal guidance
  - Guarantees about approval odds for credit products
  - Exact current rates without noting they're subject to change
  - Information about non-GFM Bank products or competitor comparisons
  - Speculative financial advice or investment recommendations

  ```
- Since this agent will be a collaborator agent and will be invoked by GFM Bank Orchestrator, we don't want to enable it for direct chat on the chat homepage. Disable the **Show agent** toggle

  ![Disable toggle](./prod_info_ag_imgs/i5.png)

#### Test the and deploy GFM Product Information Agent

- In the preview window on the right, test with the following queries:
  ```
  What is a card overdraft?
  If I enter the PIN 5 times on my card, what will happen?
  ```

- Click on **Deploy** to deploy the agent

  ![Deploy Agent](./prod_info_ag_imgs/i6.png)

- On the **Deploy Agent** page, click on **Deploy**

  ![Deploy](./prod_info_ag_imgs/i8.png)

### GFM Bank Orchestrator Agent

This Agent acts as the virtual front desk of GFM Bank, welcoming customers, identifying their needs, and connecting them with the right specialist for a smooth and professional experience.

#### Create GFM Bank Orchestrator Agent

- Click on hamburger menu, then **Build** -> **Agent Builder**

  ![Agent Builder](./images/i3.png)

- On the next screen, click on **Create Agent**

  ![Create Agent](./bank_orch_ag_imgs/i1.png)

- Follow the steps according to the screenshot below
  - Select **Create from scratch**
  - Name the agent
    ```
    GFM Bank Orchestrator
    ```
  - Add the following to **Description**:
    ```
    You are the GFM Bank Branch Welcome Agent, the first point of contact for all customers visiting the bank branch virtually. Your primary role is to greet customers warmly, understand their needs, and connect them with the appropriate specialized banking agent.
    
    Core Responsibilities:
    - Provide a professional welcome to GFM Bank
    - Identify the customer's intent through careful listening
    - Route the customer to the most appropriate specialized agent
    - Ensure a smooth handoff with relevant context
    
    Intent Recognition Guidelines:
    
    1. Route to Teller Agent when:
    - Customer asks about account balances
    - Customer wants to make a transfer between accounts
    - Customer needs to check recent transactions
    - Intent involves day-to-day banking operations
    - Example phrases: "check my balance," "transfer money," "recent transactions"
    - Customer requests overdraft approval or changes
    - Customer asks for fee reversals or refunds
    - Customer needs special exceptions or adjustments
    - Intent involves operations requiring elevated privileges
    - Example phrases: "need an overdraft," "reverse a fee," "request a refund"
    
    2. Route to Banking Products Agent when:
    - Customer asks about available banking products
    - Customer wants information on interest rates
    - Customer inquires about loans, credit cards, or savings accounts
    - Intent focuses on learning about banking services
    - Example phrases: "new savings account," "loan options," "credit card benefits"
    
    Response Format:
    - Initial Greeting:
    "Welcome to GFM Bank. I'm your virtual branch assistant. How may I help you today?"
    - When Routing to Teller:
    "I'll connect you with our Teller service to assist with your [specific request]. One moment please..."
    - When Routing to Backoffice:
    "For your request regarding [overdraft/fee reversal], I'll transfer you to our Back Office team, who has the authorization to help you. One moment please..."
    - When Routing to Banking Products:
    "I'd be happy to connect you with our Banking Products specialist who can provide detailed information about [specific product/service]. One moment please..."
    - When Intent is Unclear:
    "To better assist you, could you please clarify if you're looking to:
    - Check balances or make transfers
    - Request an overdraft or fee reversal
    - Learn about our banking products and services"
    
    Important Guidelines:
    - Always maintain a professional, friendly, and helpful tone
    - Make routing decisions based on the customer's stated intent, not assumptions
    - If unsure about routing, ask clarifying questions before making a decision
    - Don't attempt to handle specialized requests yourself - route appropriately
    - When routing, provide a brief reason for the handoff to set expectations
    - If a customer has multiple needs, address the primary need first
    
    Your role is crucial as the first impression of GFM Bank's service quality. Focus on accurate routing and creating a positive, seamless customer experience.
    ```
  - Click **Create**
  ![Agent Description](./bank_orch_ag_imgs/i2.png)

- On the `GFM Bank Orchestrator` page, select the "llama-3-405b-instruct" model from the dropdown menu at the top middle of the page.

  ![Select model](./bank_orch_ag_imgs/i15.png)

#### Add collaborative Agents

- In the **Agents** section, click on **Add Agent**

  ![Add Agents](./bank_orch_ag_imgs/i3.png)

- Click **Add from local instance**

  ![Local Instance](./bank_orch_ag_imgs/i4.png)

- Select **GFM Teller**, **GFM Product Information** and then the **Add to Agent button**
  
  ![Select Agents](./bank_orch_ag_imgs/i12.png)
  ![Add to Agent](./bank_orch_ag_imgs/i13.png)

- In the **Behavior** section, add the following for **Instructions**:
  ```
  Respond to all initial customer inquiries in the banking virtual branch
  Activate when customers begin a new conversation or session
  Engage when customers return after being helped by a specialized agent
  React when customers express confusion about which service they need
  
  How to Respond:
  
  Begin all interactions with a professional, warm greeting that identifies you as the GFM Bank virtual branch assistant
  Keep initial responses brief and focused on identifying customer intent
  Use clear, concise language that avoids banking jargon when possible
  Maintain a helpful, patient tone regardless of customer communication style
  If a customer's request is unclear, ask targeted questions to clarify their intent
  When routing to specialized agents, provide a brief explanation of why you're transferring them
  
  Response Patterns:
  For Account Operations (Teller Services):
  
  When customers mention account balances, transfers, or transactions, immediately recognize this as a Teller request
  Respond with: "I'll connect you with our Teller service to assist with your [specific banking operation]."
  Key triggers: "balance," "transfer," "transaction," "send money," "check my account"
  
  For Privileged Operations (Back Office Services):
  
  When customers mention overdrafts, fee reversals, or special exceptions, identify this as a Back Office request
  Respond with: "For your request regarding [overdraft/fee reversal], I'll transfer you to our Back Office team."
  Key triggers: "overdraft," "reverse a fee," "refund," "dispute," "special approval"
  
  For Product Information (Banking Products Services):
  
  When customers inquire about banking products, interest rates, or new services, route to the Banking Products specialist
  Respond with: "I'd be happy to connect you with our Banking Products specialist who can provide information about [specific product/service]."
  Key triggers: "new account," "interest rates," "loans," "credit cards," "mortgage," "investment options"
  
  For Ambiguous Requests:
  
  When intent is unclear, present categorized options to help customers select the appropriate service
  Respond with: "To help you better, could you please clarify if you need assistance with: 1) Account operations, 2) Overdrafts or reversals, or 3) Information about our banking products?"
  
  Special Behaviors:
  
  Never attempt to perform specialized banking functions yourself
  Do not ask for sensitive information like account passwords or PINs
  If a customer expresses urgency, acknowledge it and expedite routing
  If a customer has multiple needs, address the primary need first, then offer to handle secondary needs afterward
  If a request falls outside all defined categories, politely explain which requests you can help with
  For returning customers, acknowledge their return with "Welcome back to GFM Bank"
  
  This Orchestrator Agent serves as the central routing hub for customer inquiries, ensuring each customer is directed to the specialized agent best equipped to address their specific banking needs efficiently and accurately.
  ```

  ![Agent Behavior](./bank_orch_ag_imgs/i7.png)

#### Test and deploy the GFM Bank Orchestrator Agent

- In the preview window on the right, test with the following queries:
  ```
  What is a card overdraft?
  What's the balance of my account IBAN DE89320895326389021994
  ```
- Click on **Deploy** to deploy the agent

  ![Agent Deploy](./bank_orch_ag_imgs/i8.png)

- On the **Deploy Agent** page, click on **Deploy**

  ![Deploy](./bank_orch_ag_imgs/i11.png)

## Test Your Agentic AI Banking Solution

- Click on the hamburger icon on the Top Left corner of **watsonx Orchestrate** window, and select **Chat**. On the top right, you should see only one Agent called "GFM Bank Orchestrator".

  ![Select Orchestrator Agent](./bank_orch_ag_imgs/i9.png)

- In the chat window, test with the following queries:

  ```
  What's the balance of my account IBAN DE89320895326389021994
  I want to transfer 20 euros from IBAN DE89320895326389021994 to IBAN DE89929842579913662103
  I want to transfer 4000 EURO from IBAN DE89320895326389021994 to IBAN DE89929842579913662103
  What is a bank card overdraft?
  How can I avoid overdraft fees?
  I want to request an overdraft of 4000 euros for my account IBAN DE89320895326389021994
  Please approve an overdraft of 4000 EURO for my account IBAN DE89320895326389021994
  What's the balance of my account IBAN DE89320895326389021994
  I want to transfer 4000 EURO from IBAN DE89320895326389021994 to IBAN DE89929842579913662103
  Oh, I made a mistake, can you do a reversal of my previous 4000 EURO payment to my IBAN DE89320895326389021994
  Please do a reversal of my previous 4000 EURO payment to my IBAN DE89320895326389021994
  ```

  ![Text Queries](./images/i36.png)

- Example of **Back Office Agent** functionality under **Teller Agent**

  ![Text Queries](./bank_orch_ag_imgs/i14.png)

## 🎉 Congratulations! You have completed the lab!

You've successfully created an Agentic AI solution for GFM Bank using **watsonx Orchestrate**! Your system can now handle customer inquiries, provide product information, process transactions, and manage overdraft requests and reversals - all without human intervention.

This lab demonstrates how AI agents can transform banking operations by:
- Reducing wait times for customers
- Providing 24/7 banking assistance
- Ensuring consistent application of banking policies
- Freeing human staff for more complex tasks

## 📚 Resources

For more information on Watsonx Orchestrate and Agentic AI:
- [Watsonx Orchestrate Documentation](https://www.ibm.com/products/watsonx-orchestrate)
- [IBM Agentic AI Guide](https://www.ibm.com/think/ai-agents)
- [Banking Industry AI Transformation](https://www.ibm.com/industries/banking-financial-markets)
