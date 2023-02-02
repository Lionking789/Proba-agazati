"""3. feladat:    összesen 17p szerezhető, a modul neve: gombak.py
A gombak.txt forrásállomány, gombák adatait tartalmazza, a feladatok megoldása során ezeket az adatokat használja!
A gep.txt állomány szerkezete:
·         gomba neve: pl.: piros csészegomba
·         nemzettség pl.: csészegomba
·         évszak pl.: tél, tavasz
Az állomány első sora a mezőneveket tartalmazza @  jellel elválasztva.
A megoldás mintája:
III/A, B:
            	A gombák száma: 78.
III/C:
           Az első papsapkagomba neve: homoki papsapka.
III/D:
            	A tinóru gombák száma: 14.
A.Olvassa be osztály segítségével (utóbbit hozza létre külön modulban) a gombák.txt fájlból a játékosok adatait, és tárolja el összetett adatszerkezetben, ami elősegíti a további feladatok könnyű megoldását! Ügyeljen arra, hogy az állomány első sora az adatok fejlécét tartalmazza! (7p)
B.Írassa ki a gombák számát a mintának megfelelően a konzolra! A metódus neve legyen gombak_szama! (2p)
C.Határozza meg és írassa ki a konzolra a minta szerint, hogy a melyik a papsapkagombák nemzettségben melyik az első gomba, amelyik szerepel a listában?  A metódus neve legyen papsapka! (4p)
D.Írassa ki konzolra a mintának megfelelően a tinóru nemzettséghez tartozó gombák számát! A metódus neve tinoru legyen  (4p)"""

from Gombak1 import Gombak
gombak_lista=[]

def beolvas():
    fajl = open("gombak_jav.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()
    print(sorok)





