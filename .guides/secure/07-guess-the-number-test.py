#!/usr/bin/env python3

import subprocess
import re
import os

def main():

    if not os.path.exists('adivina.cpp'):
        print('</br><hr/><h3 style="color:red">No se encuentra el archivo fuente</h3>')
        print('El archivo fuente debe llamarse <code>adivina.cpp</code>.')
        exit(-1)

    compilation_result = os.system('g++ adivina.cpp -o adivina')
    if compilation_result != 0:
        print('</br><hr/><h3 style="color:red">Tu programa tiene errores de compilación.</h3>')
        print('Intenta corregir los errores mencionados arriba.')
        exit(-1)

    proc = subprocess.Popen(['./adivina'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    maxguess = 100;
    minguess = 0;
    answer = 'mayor'
    mayor = re.compile('.*mayor.*')
    menor = re.compile('.*menor.*')
    tries = 0
    history = []
    while (mayor.match(answer) or menor.match(answer)) and tries < 9:
        tries = tries + 1
        guess = (maxguess + minguess) // 2
        strguess = f'{guess}\n'
        proc.stdin.write(bytes(strguess, 'utf8'))
        proc.stdin.flush()
        answer = proc.stdout.readline().decode()
        if mayor.match(answer):
            minguess = guess
            history.append((guess, 'mayor', minguess, maxguess))
        elif menor.match(answer):
            maxguess = guess
            history.append((guess, 'menor', minguess, maxguess))
        else:
            history.append((guess, 'correcto', minguess, maxguess))
    proc.stdin.close()
    proc.terminate()
    proc.wait(timeout=0.2)
    print('Se muestra a continuación la historia de intentos realizados y respuestas obtenidas:')
    for item in history:
        print('Intento: ', item[0], ' Respuesta: ', item[1])
    if tries > 7:
        print('</br><hr/><h3 style="color:red">Algo falla...</h3>')
        print('Han sido necesarios demasiados intentos. Las respuestas del programa no han sido correctas.')
        exit(-1)
    else:
        tries_re = re.compile(r'.*(\d+).*intentos.*')
        tries_match = tries_re.match(answer)
        tries_reported = tries_match.group(1)
        if int(tries_reported) != tries:
            print('</br><hr/><h3 style="color:red">Algo falla...</h3>')
            print(f'El número de intentos indicado por el programa es incorrecto.')
            print(f'El programa indica que hubo {tries_reported} intentos, pero hubo {tries} intentos.')
            exit(1)
        else:
            print('<h3 style="color:green">Tu programa no tiene errores y funciona como se esperaba.</h3>')
            print('Buen trabajo.')
            exit(0)


if __name__ == '__main__':
    main()
