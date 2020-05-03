def menu():
    sg.theme('DarkBlue')
    layout=[[sg.Text('BIENVENIDO A JUEGOS')],
            [sg.Text('ESOJE UN JUEGO')],
            [sg.Button('AHORCADO'),sg.Button('ADIVINA'),sg.Button('Salir')],
        ]
    windowMenu=sg.Window('Menu',layout)
    while True:
        event, values = windowMenu.Read()
        if event == 'Salir': #CHEQUEO SIEMPRE POR SI SE QUIERE SALIR
            break
        if event == 'AHORCADO' :
            return 1
        if event == 'ADIVINA' :
            return 2
    windowMenu.close()

def juegoAhorcado():
    temas = ['ANIMALES', 'COLORES', 'COMIDA']
    palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
    sg.theme('DarkBlue')	# Add a touch of color
    layout1=[  [sg.Text('---BIENVENIDO AL AHORCADO---')],
            [sg.Text('Ingrese su nombre: '), sg.InputText(key='nom_jugador')],
            [sg.Text('SELECCIONE UN TEMA')],
            [sg.InputCombo(temas, size=(20, 1),key='_LIST_')],
            [sg.Button('Jugar'), sg.Button('Salir')],
            ]
    layout2=[  [sg.Text('PALABRA A ADIVINAR ---> ')],
            [sg.Text('-------------------------------',key='_INPUT_')],
            [sg.Text('INGRESE UNA LETRA:'),sg.InputText(size=(3, 1),key='_CHAR_')],
            [sg.Button('VERIFICAR LETRA')],
            [sg.Button('Volver al Inicio')]
            ]
    layout=[[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')]]
    window = sg.Window('Ahorcado', layout)
    trys=3
    cantLetrasAcertadas=0

    csv_file = open("datos.csv", "w")
    fieldnames = ['Nombre_Jugador','Juego', 'Resultado']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()


    while True:
        event, values = window.Read()
        if event == 'Salir': #CHEQUEO SIEMPRE POR SI SE QUIERE SALIR
            break
        if event == 'Jugar' : #INICIO DE JUEGO
            window['-COL1-'].update(visible=False)
            window['-COL2-'].update(visible=True)
            sg.Popup('Elegiste el tema ', values['_LIST_'])
            if values['_LIST_']=='ANIMALES':tema=1
            elif values['_LIST_']=='COLORES':tema=2
            elif values['_LIST_']=='COMIDA':tema=3
            pal = palabras[tema][random.randrange(len(palabras[tema]))] #sg.Popup(pal)  #test palabra
            cantLetras=len(pal)
            pal_separada = []
            for y in pal:
                pal_separada.append('-')
            window['_INPUT_'].update(pal_separada)
        if event =='VERIFICAR LETRA' :
            #introducción de letras por parte del jugador
            letra =  values['_CHAR_'].lower()
            # Si hay al menos una aparición de la letra..
            if letra in pal:
                sg.Popup('Correcto')
                for key, value in enumerate(pal):
                    if value == letra:
                        pal_separada[key] = value.upper()
                        cantLetrasAcertadas=cantLetrasAcertadas+1
                window['_INPUT_'].update(pal_separada)
            else:
                sg.Popup('Incorrecto')
                trys=trys-1
                sg.Popup("Te quedan",trys,"intentos")
        window['_CHAR_']('')#limpia el textBox de Letra
        #CHEQUEO SI SE ACABARON LOS INTENTOS
        if trys==0:
            writer.writerow({'Nombre_Jugador': values['nom_jugador'],'AHORCADO', 'Resultado': 'Perdio'})#se carga el nombre del jugador y que perdio
            sg.Popup('Perdiste! la Palabra era: ',pal.upper())
            break
        #CHEQUEO SI GANO
        if cantLetras==cantLetrasAcertadas:
            writer.writerow({'Nombre_Jugador': values['nom_jugador'],'AHORCADO', 'Resultado': 'Gano'})#se carga el nombre del jugador y que gano
            sg.Popup('Ganaste!')
            break
        if event == 'Volver al Inicio' : #INICIO DE JUEGO
            window['-COL1-'].update(visible=True)
            window['-COL2-'].update(visible=False)

    csv_file.close()
    window.close()

import random
import PySimpleGUI as sg
import csv

#Preparo el juego

#Defino estructura del ahoracado
ahorcado = [' O ', '/|\\','/ \\']

num=menu()
print(num)
if num==1:
    juegoAhorcado()
else:
    print("ACA VA EL ADIVINA",num)
