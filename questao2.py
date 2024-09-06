def verificar_letra_a(string):
    string = string.lower()
    contagem = string.count('a')
    if contagem > 0:
        mensagem = f"A letra 'a' aparece {contagem} vez(es) na string."
    else:
        mensagem = "A letra 'a' não aparece na string."

    return contagem, mensagem
