a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
print(type(b))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = ('Soma: {soma}\n'
            'Subtração: {subtracao}\n'
            'Multiplicação: {multiplicacao}\n'
            'Divisão: {divisao}\n'
            'Resto: {resto}' .format(soma=soma,
                                    subtracao=subtracao,
                                    multiplicacao=multiplicacao,
                                    divisao=divisao,
                                    resto=resto))

print(resultado)
