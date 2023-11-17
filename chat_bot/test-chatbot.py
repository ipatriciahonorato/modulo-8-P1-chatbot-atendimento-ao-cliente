#!/usr/bin/env python3
import re

# Definindo padrões para identificar diferentes intenções do usuário
intent_patterns = {
    r"\b(atualizar|alterar|mudar)\b.*\b(pagamento|cartão|forma de pagamento)\b": "atualizar_pagamento",
    r"\b(acompanhar|rastrear|status|onde está)\b.*\b(pedido|entrega)\b": "acompanhar_pedido"
}

# Respostas pré-definidas para cada intenção
acoes = {
    "atualizar_pagamento": lambda _: "Para atualizar suas informações de pagamento, acesse a seção de configurações de pagamento em sua conta.",
    "acompanhar_pedido": lambda _: "Para acompanhar o status do seu pedido, acesse a seção 'Meus Pedidos' no nosso site ou use o link de rastreamento enviado ao seu e-mail."
}

def main():
    # Executando o loop para receber e processar comandos
    while True:
        comando = input("Informe seu comando (digite 'sair' para finalizar): ")
        if comando.lower() == 'sair':
            break

        encontrado = False
        for expressao, intencao in intent_patterns.items():
            busca = re.compile(expressao, re.IGNORECASE)
            if busca.search(comando):
                print(acoes[intencao]())
                encontrado = True
                break

        if not encontrado:
            print("Desculpe, não consegui entender o comando.")

if __name__ == '_main_':
    main()


