def verificar_a(string):
    string_lower = string.lower()

    quantidade_a = string_lower.count('a')

    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")


texto = input("Digite uma string: ")

verificar_a(texto)
