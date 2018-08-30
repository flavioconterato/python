def saque(valor):
    global cinquentareais
    global vintereais
    global dezreais
    global umreal
    if valor >= 50:
        cinquentareais = valor // 50
        resto = valor % 50
        saque(resto)
    elif valor >= 20:
        vintereais = valor // 20
        resto = valor % 20
        saque(resto)
    elif valor >=10:
        dezreais = valor // 10
        resto = valor % 10
        saque(resto)
    elif valor >=1:
        umreal = valor

print('Sistema de Banco')
print('Digite valores abaixo de 0 para sair')
while True:
    cinquentareais = 0
    vintereais = 0
    dezreais = 0
    umreal = 0
    valor=int(input('Qual valor deseja sacar?'))
    if valor <= 0:
        break
    saque(valor)
    print('Você vai receber:\n{} notas de 50 \n{} notas de 20 \n{} notas de 10\n{} moedas de 1'.format(cinquentareais,vintereais,dezreais,umreal))
