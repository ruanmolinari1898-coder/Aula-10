print('*** Caixa Eletrônico ***')

try:
    saldo = 1000
    saque = float(input('Infome o valor que deseja sacar: '))

except ValueError:
    print('Valor inválido.')
except KeyboardInterrupt:
    print('Programa encerrado pelo usuário.')
else:
    if saque > saldo:
        print('Saldo insuficiente.')
    elif saque <=0:
        print('Saque precisa ser maior ou igual a R$ 2,00')
    else:
        saldo - saque
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta {saldo:.2f})

finally:
    print('Operação realizada.')

print('\n Programa encerrado.')
