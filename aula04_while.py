a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))
media = (a + b + c + d) / 4
print('Média: {}'.format(media))

"""
nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entre com a nota correta: '))
print(nota)
"""

"""
a = 0
while a <= 10:
    print(a)
    a += 1
"""