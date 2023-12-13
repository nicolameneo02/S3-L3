#Programma S3-L3

import math

while True:
    print("Scegli la figura geometrica:")
    print("1. Quadrato")
    print("2. Cerchio")
    print("3. Rettangolo")
    print("4. Esci")

    scelta = input("Inserisci il numero corrispondente alla figura desiderata: ")

    if scelta == '1':
        lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
        perimetro = lato * 4
        print("Il perimetro del quadrato è:", perimetro)

    elif scelta == '2':
        raggio = float(input("Inserisci il raggio del cerchio: "))
        circonferenza = 2 * math.pi * raggio
        print("La circonferenza del cerchio è:", circonferenza)

    elif scelta == '3':
        base = float(input("Inserisci la lunghezza della base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = 2 * base + 2 * altezza
        print("Il perimetro del rettangolo è:", perimetro)

    elif scelta == '4':
        print("Arrivederci!")
        break

    else:
        print("Scelta non valida. Riprova.")