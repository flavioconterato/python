cinquenta = 0
vinte = 0
dez = 0
um = 0 
def saque(valor,cinquentareais,vintereais,dezreais,umreal):
    if valor >= 50:
        cinquentareais = valor // 50
        resto = valor % 50
        #return saque(resto,cinquentareais,vintereais,dezreais,umreal)
    else:
        if valor >= 20:
            vintereais = valor // 20
            resto = valor % 20
            #return saque(resto,cinquentareais,vintereais,dezreais,umreal)
        else:
            if valor >=10:
                dezreais = valor // 10
                resto = valor % 10
                #return saque(resto,cinquentareais,vintereais,dezreais,umreal)
            else:
                umreal = valor
                return cinquentareais,vintereais,dezreais,umreal
    return saque(resto,cinquentareais,vintereais,dezreais,umreal)
        

print('Sistema de Banco')
print('Digite valores abaixo de 0 para sair')
while True:
    valor=int(input('Qual valor deseja sacar?'))
    if valor <= 0:
        break
    cinquenta,vinte,dez,um= saque(valor,cinquenta, vinte, dez, um)
    print('Você vai receber:\n{} notas de 50 \n{} notas de 20 \n{} notas de 10\n{} moedas de 1'.format(cinquenta,vinte,dez,um))
