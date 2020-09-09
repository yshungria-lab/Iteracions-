print('Contador de Una semana en dias horas y minutos')
contador_dias = 1
contador_horas = 00
contador_minutos = 00

while contador_dias < 8:
    while contador_horas < 24:
        while contador_minutos <= 59:
            print(contador_dias, contador_horas, contador_minutos)
            contador_minutos += 1
        contador_horas +=1
        contador_minutos =0
    contador_dias += 1
    contador_horas = 0
