"""2. feladat:    összesen 14p szerezhető, a modul neve: korok.py
minta:
II/A, B, C:
           	20 : 34 : 78 : 83 : 90
II/D, E:
           	Első idős ember korának helye a listában: 2.
kimutatas.txt tartalma:
II/F:
 Első idős ember korának helye a listában: 2.

A.Kérj be 5 egész számot a felhasználótól, melyek az egyes személyek korát jelentik! [0,120] (4p)
B.A bekért  értékeket tárolja lista adatszerkezetben! (1p)
C.Írasd ki a képernyőre a számokat : -tal (kettősponttal) elválasztva. A : jel csak az értékek között szerepeljen (a végén, elején ne)! (2p)
D.Írj függvényt elso_idos néven, ami megkeresi az első  70 év feletti kort. A visszatérési érték legyen egy egész szám, melynek a kornak az INDEX-ét tartalmazza, a függvény bemenete a lista! (3p)
E.Az elso_idos függvény eredményét írasd ki a mintának megfelelően a konzolra, amit konzolra_ir nevű metódusban fogalmazz meg! (2p)
F.Az elso_idos függvény eredményét írasd ki a mintának megfelelően a oreg.txt nevű fájlba, amit fajl_ir nevű metódusban fogalmazzon meg! (2p)"""

import random
vel_lista=[]

def eletkor():
    #kor = int(input("Kérek 5 egész számot: "))

    i = 0
    szoveg = ""
    while i <= 5:
        vel = int(random.random() * 5) - 1
        vel_lista(vel)
        if i == 5:
            szoveg += str(vel) + ""

        else:
            szoveg += str(vel) + ":"
        i += 1

    print(f"II/ A, B, C: \n \t {szoveg}")























