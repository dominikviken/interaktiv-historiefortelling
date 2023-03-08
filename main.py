from os import system

# importerer de to python filene
import animertVersion
import uanimertVersion

input('Spillet er best spilt på en Windows PC, siden spillet bruker command prompt sin color funksjon.\nTrykk på enter for å starte..')
input('Her kan du velge 2 versioner av spillet å spille. Den ene har animert tekst, og den andre har ikke det.')
#bruker read funksjonen fra animertVersion.py
animertVersion.read('[1] Den med kul tekst')
x = input('[2] Den med ukul tekst\n -  ')

if x == '1':
    input('Lykke til!')
    system('cls')
    animertVersion.start()
    
elif x == '2':
    input('Lykke til!')
    system('cls')
    uanimertVersion.start()
    
else:
    # printer at du skrev noe som ikke var et av alternativene
    print(f'du skrev {x} og ikke noen av alternativene.')
    input('prøv igjen')