from questao1 import fibonacci


def executar_questao1():
    print("\n===== Questão 1: Verificar Fibonacci =====")
    try:
        numero = int(input("Informe um número para verificar na sequência de Fibonacci: "))
        if fibonacci(numero):
            print(f"O número {numero} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

def main():
    executar_questao1()

if __name__ == "__main__":
    main()