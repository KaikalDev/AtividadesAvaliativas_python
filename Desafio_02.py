import random

frutas = ['maçã', 'banana', 'laranja', 'uva', 'abacaxi', 'morango', 'melancia', 'limão', 'pera', 'kiwi', 'mamão', 'amora', 'pêssego', 'goiaba', 'cereja']
profissoes = ['engenheiro', 'advogado', 'dentista', 'médico', 'professor', 'programador', 'enfermeiro', 'contador', 'arquiteto', 'cozinheiro', 'designer', 'piloto', 'veterinário', 'jornalista', 'psicólogo']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Salvador', 'Brasília', 'Curitiba', 'Fortaleza', 'Recife', 'Porto Alegre', 'Manaus', 'Belém', 'Goiânia', 'Campinas', 'São Luís', 'Natal']
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja', 'branco', 'preto', 'rosa', 'cinza', 'marrom', 'violeta', 'turquesa', 'bege', 'ouro']

tipo = 6
r = random.randint(1, 15)
while tipo > 4:
    tipo = int(input('Categoria da palavra: \n 1 - Frutas \n 2 - Profissão \n 3 - Cidade \n 4 - Cor \n Opção: '))
    if tipo == 1:
        texto = frutas[r].lower()
        opcao = frutas[r]
    elif tipo == 2:
        texto = profissoes[r].lower()
        opcao = profissoes[r]
    elif tipo == 3:
        texto = cidades[r].lower()
        opcao = cidades[r]
    elif tipo == 4:
        texto = cores[r].lower()
        opcao = cores[r]
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")
        continue
    texto = texto.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('â', 'a').replace('ã', 'a').replace('ê', 'e').replace('õ', 'o').replace('ô', 'o').replace('ç', 'c').replace('í', 'i').replace('à', 'a').replace('è', 'e').replace('ì', 'i').replace('ò', 'o').replace('ù', 'u')

print('  +---+ \n  |   | \n  O   | \n /|\  | \n / \  | \n      | \n=========')
barra = ['_' for _ in texto]
print(' '.join(barra))
letras = ['letras usadas']
erros = 1

while '_' in barra:
    letra = input('Letra: ')
    if letra in letras:
        print('Ja foi usada')
    elif letra in texto:
        for i in range(len(texto)):
            if texto[i] == letra:
                barra[i] = letra
        print(' '.join(barra))
        letras.append(letra)
        print(letras)
    elif erros == 1:
        print('erro 1')
        erros += 1
        letras.append(letra)
        print(letras)
        print('  +---+ \n  |   | \n  O   | \n /|\  | \n /    | \n      | \n=========')
        print(' '.join(barra))

    elif erros == 2:
        print('erro 2')
        erros += 1
        letras.append(letra)
        print(letras)
        print('  +---+ \n  |   | \n  O   | \n /|\  | \n      | \n      | \n=========')
        print(' '.join(barra))

    elif erros == 3:
        print('erro 3')
        erros += 1
        letras.append(letra)
        print(letras)
        print('  +---+ \n  |   | \n  O   | \n /|   | \n      | \n      | \n=========')
        print(' '.join(barra))

    elif erros == 4:
        print('erro 4')
        erros += 1
        letras.append(letra)
        print(letras)
        print('  +---+ \n  |   | \n  O   | \n  |   | \n      | \n      | \n=========')
        print(' '.join(barra))

    elif erros == 5:
        print('erro 5')
        erros += 1
        letras.append(letra)
        print(letras)
        print('  +---+ \n  |   | \n  O   | \n      | \n      | \n      | \n=========')
        print(' '.join(barra))

    elif erros == 6:
        print('erro 6')
        erros += 1
        letras.append(letra)
        print(letras)
        break
if erros <= 6:
    print('Parabén você Conseguiu')
else:
    print(opcao)
    print('Perdeu')