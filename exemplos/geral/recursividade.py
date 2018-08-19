#Exemplo de recursividade utilizando função

def recursivo(valor):
    if valor == 0 :
		pass
    else:
        print(valor)
        recursivo(valor-1)


print('-'*15,'Calculador de Fatorial','-'*15)
n = int(input('Digite o número que você deseja calcular o fatorial:'))
recursivo(n)
