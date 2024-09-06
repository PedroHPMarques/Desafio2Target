from questao1 import fibonacci
from questao2 import verificar_letra_a

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

def executar_questao2():
    print("\n===== Questão 2: Verificar Letra 'a' =====")
    string = input("Informe uma string para verificar a ocorrência da letra 'a': ")
    _, mensagem = verificar_letra_a(string)
    print(mensagem)

def main():
    executar_questao1()
    executar_questao2()

if __name__ == "__main__":
    main()
