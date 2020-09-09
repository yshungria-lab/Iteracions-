number = int(input('Ingresa el primer número '))
max_number = int(input('Ingresa el número máximo '))
max_mult = int(input('Ingresa el máximo multiplicador '))

print(f'{number} x {max_number}')

print(f'Las tablas del {number} - {max_number}')

while number <= max_number:
    print(f'La tabla del {number}')
    #Aquí se pondrá la lógica
    mult = 1
    while mult <= max_mult:
        resul = number * mult
        print(f'{number} x {mult} = {resul}')
        mult += 1
    number += 1
