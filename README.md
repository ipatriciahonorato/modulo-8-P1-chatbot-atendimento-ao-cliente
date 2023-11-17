# Sistema de atendimento ao cliente automatizado em Python

## Visão Geral

Esse projeto utiliza processamento de linguagem natural e expressões regulares para identificar a intenção dos usuários e fornecer respostas automáticas às suas perguntas. Sua execução acontece via terminal com script python.

## Intenções do sistema
intent_patterns = {
    r"\b(como|quero|preciso|necessito)\b.\b(atualizar|mudar|alterar)\b.\b(informações de pagamento|cartão de crédito|forma de pagamento)\b": "atualizar_pagamento",
    r"\b(onde|como|status|acompanhar|rastrear)\b.*\b(meu pedido|pedido|entrega)\b": "acompanhar_pedido"
}

Atende a requisições como:

Como atualizar informações de pagamento do cartão de cŕedito ou
Onde acompanhar meu pedido

## Instalação e Execução

##  Instalação e Execução

1. Clone o Repositório:

   ```
   cd seu_workspace
   https://github.com/ipatriciahonorato/modulo-8-P1-chatbot-atendimento-ao-cliente
    cd seu_workspace//modulo-8-P1-chatbot-atendimento-ao-cliente/chat_bot
   ```

2. **Execute o script do chatbot via terminal:**

``sseu_workspace//modulo-8-P1-chatbot-atendimento-ao-cliente/chat_bot/./test-chatbot.py``

Após isso o usuário terá acesso ao chatbot para enviar comandos para o robô. 



