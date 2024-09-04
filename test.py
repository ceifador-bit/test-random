while True:
    try:
        n1 = int(input('digite o primeiro número: '))
        n2 = int(input('digite o segundo número: '))
        n3 = int(input('digite o terceiro número: '))
        if n1 and n2 and n3 !=0:
            break
        else:
            print('digite um número diferente de zero !')

    except ValueError:
        print('Isso não é valido, tente novamente !')

d1 = n1 + n2 + n3/n1
d2 = n1 + n2 + n3/n2
d3 = n1 + n2 + n3/n3
print(f'os números que você digitou foram: {n1}, {n2}, {n3}')
print(f'As divisões entre os números é:{d1:.2f}, {d2:.2f}, {d3:.2f}')