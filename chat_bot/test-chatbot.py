#!/usr/bin/env python3
import re

# Definindo padrões para identificar diferentes intenções do usuário
intent_patterns = {
    r"\b(como|quero|preciso|necessito)\b.\b(atualizar|mudar|alterar)\b.\b(informações de pagamento|cartão de crédito|forma de pagamento)\b": "atualizar_pagamento",
    r"\b(onde|como|status|acompanhar|rastrear)\b.*\b(meu pedido|pedido|entrega)\b": "acompanhar_pedido"
}

# Respostas pré-definidas para cada intenção
acoes = {
    "atualizar_pagamento": lambda: "Para atualizar suas informações de pagamento, acesse a seção de configurações de pagamento em sua conta.",
    "acompanhar_pedido": lambda: "Para acompanhar o status do seu pedido, acesse a seção 'Meus Pedidos'."
}

def main():
    print("Bem-vindo ao Atendimento Automatizado!")
    # Executando o loop para receber e processar comandos
    while True:
        comando = input("\nInforme seu comando (digite 'sair' para finalizar): ")
        if comando.lower() == 'sair':
            print("Atendimento encerrado. Volte sempre!")
            break

        encontrado = False
        for expressao, intencao in intent_patterns.items():
            busca = re.compile(expressao, re.IGNORECASE)
            if busca.search(comando):
                print(acoes[intencao]())
                encontrado = True
                break

        if not encontrado:
            print("Desculpe, não consegui entender o comando. Tente reformular sua pergunta.")

if __name__ == '__main__':
    main()



