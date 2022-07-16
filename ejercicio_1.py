from datetime import date


file = open('archivo.txt', 'w+')
file.write('Hola mi nombre es Luciano\n')
file.write(f'Hoy es: {date.today()}' )
file.close()


file = open('archivo.txt', 'r')

for line in file.readlines():
    print(line)

file.close()
