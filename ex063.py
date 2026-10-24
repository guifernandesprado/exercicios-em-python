frase = input('Digite uma frase: ')

print(frase.title())
palavras = frase.split()
total = len(palavras)
print(f'A frase tem {total} palavras. ')


if total % 2 == 1:
    meio = total // 2
    print(f'A palavra do meio é a {palavras[meio]}.')
else:
    print(f'A frase tem números pares de palavras.')