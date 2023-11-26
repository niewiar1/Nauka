from random import randint
from math import sqrt
szerokosc = 5
wysokosc = 5

klucz_x = randint(0, szerokosc)
klucz_y = randint(0, wysokosc)

gracz_x = 0
gracz_y = 0

kroki = 0
odleglosc_przed_ruchem = sqrt((klucz_x - gracz_x)**2 + (klucz_y - gracz_y)**2) #-> sqrt pierwiastek kwadratowy z x
                            # wzor na dlugosc odcina

gracz_znalazl_klucz = False

#print(f"Pozycja kluczX: {klucz_x} Pozycja kluczaY: {klucz_y} ")

while not gracz_znalazl_klucz:
    kroki += 1
    print()
    print("Mozesz udac sie w kierunkach W/S/A/D")

    poruszanie = input("Dokad idziesz? ")
    match poruszanie.lower():
        case "w":
            gracz_y += 1
            if gracz_y > wysokosc:
                print("SCIANA nie mozesz isc go gory")
                gracz_y = wysokosc
        case "s":
            gracz_y -= 1
            if gracz_y < 0:
                print("SCIANA nie mozesz isc do dolu")
                gracz_y = 0
        case "a":
            gracz_x -= 1
            if gracz_x < 0:
                print("SCIANA nie mozesz isc w lewo ")
                gracz_x = 0
        case "d":
            gracz_x += 1
            if gracz_x > szerokosc:
                print("SCIANA nie mozesz isc w prawo ")
                gracz_x = szerokosc
        case "q":
            print("Koniec gry!")
            quit()
        case _:
            print("Nie wiem dokad idziesz..")
            continue

    if gracz_x == klucz_x and gracz_y == klucz_y:
        print(f"HURA ODNALAZLES KLUCZ!!! Zrobiles to w {kroki} ruchach")
        if input("Czy chcesz kontynuowac Y/N : ") == "y":
            klucz_x = randint(0, szerokosc)
            klucz_y = randint(0, wysokosc)
            gracz_x = 0
            gracz_y = 0
            print()
            print(f"Nowa gra jestes na pozycji X = {gracz_x} Y = {gracz_y}")
        else:
            quit()

    odleglosc_po_ruchu = sqrt((klucz_x - gracz_x) ** 2 + (klucz_y - gracz_y) ** 2)

    # print("pred ruchem", odleglosc_przed_ruchem)
    # print("po ruchu", odleglosc_po_ruchu)

    if odleglosc_po_ruchu < odleglosc_przed_ruchem:
        print()
        print("Cieplo")
        print()
    else:
        print()
        print("Zimno")
        print()

    odleglosc_przed_ruchem = odleglosc_po_ruchu
    print(f"X = {gracz_x} Y = {gracz_y}")
    #print("Aby zakonczyc wcisnij q ")




