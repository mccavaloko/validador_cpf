# Pedindo o cpf ao usuário
try:
    # Primeiro dígito
    cpf = input('Digite seu cpf.  ')
    cpf_lista = []
    cpf_lista_resultado = []
    cpf_lista_resultado_2 = []
    contagem_regressiva_1 = 10
    contagem_regressiva_2 = 11
    contador = 0
    contador_2 = 0

    # Colocando os números na lista
    for numeros in cpf:
        cpf_lista.append(numeros)

    # Transformando os números em int
    for i, item in enumerate(cpf_lista):
        cpf_lista[i] = int(item)

    # Fazendo a conta
    for i in range(len(cpf_lista)):
        if contador == 9:
            break
        contador += 1
        resultado = cpf_lista[i] * contagem_regressiva_1
        contagem_regressiva_1 -= 1
        cpf_lista_resultado.append(resultado)

    # Somar todos os resultados e multiplicar
    digito_cpf_1 = sum(cpf_lista_resultado) * 10
    digito_resto = digito_cpf_1 % 11
    digito_resto = digito_resto if digito_resto <= 9 else 0
    print(digito_resto)

    # Segundo dígito
    # Somar os 9 dígitos + o segundo dígito
    digito_cpf_2 = sum(cpf_lista_resultado) + cpf_lista[9]
    # Somar todos os resultados e multiplicar
    for i in range(len(cpf_lista)):
        if contador_2 == 10:
            break
        contador_2 += 1
        resultado_digito_2 = cpf_lista[i] * contagem_regressiva_2
        contagem_regressiva_2 -= 1
        cpf_lista_resultado_2.append(resultado_digito_2)
    digito_cpf_3 = sum(cpf_lista_resultado_2) * 10
    digito_resto_2 = digito_cpf_3 % 11
    digito_resto_2 = digito_resto_2 if digito_resto_2 <= 9 else 0
    print(digito_resto_2)
    if digito_resto == cpf_lista[9] and digito_resto_2 == cpf_lista[10] :
        print('Esse é um cpf válido!')
    else:
        print('Esse cpf é inválido!')                       
except ValueError:
    print("Ooops! Insira apenas números no seu CPF.")