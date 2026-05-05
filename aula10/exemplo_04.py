print('*** Cálculo de Produtividade ***')

try:
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('Total de funcionários: '))
    media_por_funcionario = total_produzido / funcionarios
   

except (ValueError, TypeError):
    print('O valor precisa ser númerico.')
except ZeroDivisionError:
    print('Funcionário não pode ser zero.')
else:
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
finally:
    print('Programa encerrado.')