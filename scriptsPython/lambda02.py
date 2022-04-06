#soma = lambda a,b: a + b
#print(soma(5,10))

calculadora = {
    'soma': lambda a,b: a + b,
    'sub': lambda a,b: a - b,
    'multi': lambda a,b: a * b,
    'divi': lambda a,b: a / b,
}
soma = calculadora['soma']
print(f'A soma é {soma(10,2)}')
