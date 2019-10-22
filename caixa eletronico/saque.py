def q_100(valor):
	c = valor // 100
	return c	

def q_50(valor):
	d = valor // 50
	return d

def q_20(valor):
	n = valor // 20
	return n

def q_10(valor):
	i = valor // 10
	return i

# solicita o valor a ser sacado:
# testa se valor < 10, invalido, pede para digitar novamente
while True:
	valor = int(input('Digite o valor que deseja sacar: \n**minímo R$10 - somente notas de R$10, R$20, R$50 e R$100**\n'))
	if valor >= 10:
		break
	print('****Valor invalido!\n****Saque mínimo: R$10\n')
	print()

# testa de valor termina em 0
while valor % 10 != 0:
	print('****Valor invalido!\n****Somente notas de R$100, R$50, R$20, R$10\n')
	valor = int(input('Digite o valor que deseja sacar: \n**minímo R$10 - somente notas de R$10, R$20, R$50 e R$100**\n'))
	print()

print('SAQUE AUTORIZADO, SENDO:')
if q_100(valor) != 0:
	print('>> ', q_100(valor), 'notas de R$100.00')
	valor -= q_100(valor) * 100
if q_50(valor) != 0:
	print('>> ', q_50(valor), 'notas de R$50.00')
	valor -= q_50(valor) * 50
if q_20(valor) != 0:
	print('>> ', q_20(valor), 'notas de R$20.00')
	valor -= q_20(valor) * 20
if q_10(valor) != 0:
	print('>> ', q_10(valor), 'notas de R$10.00')
	valor -= q_10(valor) * 10



# testes 
assert q_100(10) == 0
assert q_100(20) == 0
assert q_100(50) == 0
assert q_100(100) == 1

assert q_50(10) == 0
assert q_50(20) == 0
assert q_50(50) == 1
assert q_50(100) == 2

assert q_20(10) == 0
assert q_20(20) == 1
assert q_20(50) == 2
assert q_20(100) == 5

assert q_10(10) == 1
assert q_10(20) == 2
assert q_10(50) == 5
assert q_10(100) == 10