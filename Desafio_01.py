real = ['r$', 'real', 'reais']
euro = ['€', 'euro', 'euros']
dolar = ['us$', 'dolar', 'dolares']
iene = ['¥', 'iene', 'ienes']
rublo = ['₽', 'rublo', 'rubulos']
peso = ['$', 'peso', 'pesos']
libra = ['£', 'libra', 'libras']

moedas_validas = [euro, real, dolar, iene, rublo, peso, libra]

def trata_string(resposta):
    string = resposta.replace(' ', '')
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7' ,'8' ,'9']
    nstring = len(string)
    valor = ''
    moeda = ''
    for i in range(nstring):
        if string[i] in numeros :
            valor += string[i]
        else:
            moeda += string[i]
    return int(valor), moeda

print('Comversor de moedas')
print('Ex: euro, real, dolar, iene, rublo, peso, libra')
resposta = input('Insira o valor (Ex: 25 reais): ')
valor, moeda = trata_string(resposta.lower())

while not any(moeda in moeda_lista for moeda_lista in moedas_validas):
    print('------------------------------------------------------')
    print('Moeda invalida')
    print('Ex: euro, real, dolar, iene, rublo, peso, libra')
    resposta = input('Insira o valor (Ex: 25 reais): ')
    valor, moeda = trata_string(resposta.lower())


print('------------------------------------------------------')
print('Para')
print('Ex: euro, real, dolar, iene, rublo, peso, libra')
moeda2 = input('Insira a moeda: ')

while not any(moeda2 in moeda_lista for moeda_lista in moedas_validas):
    print('------------------------------------------------------')
    print('Moeda invalida')
    print('Ex: euro, real, dolar, iene, rublo, peso, libra')
    moeda2 = input('Insira a moeda: ')

def campio(v,m):
    if m in real :
        return v
    elif m in euro:
        comverção = v*0.18
        return comverção
    elif m in dolar:
        comverção = v*0.20
        return comverção
    elif m in iene:
        comverção = v*29.25
        return comverção   
    elif m in rublo:
        comverção = v*18.23
        return comverção    
    elif m in peso:
        comverção = v*169.32
        return comverção   
    elif m in libra:
        comverção = v*0.16
        return comverção   
def cifrão(m):
    if m in real :
        return real[0]
    elif m in euro:
        return euro[0]
    elif m in dolar:
        return dolar[0]
    elif m in iene:
        return iene[0]
    elif m in rublo:
        return rublo[0]
    elif m in peso:
        return 'ARG'+peso[0]
    elif m in libra:
        return libra[0]


valor_real = campio(valor, moeda)
valor_final = campio(valor_real, moeda2)
cifrao = cifrão(moeda2)

print(f'{valor_final:.2f} {cifrao}')