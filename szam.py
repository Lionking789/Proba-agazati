"""1. feladat:  összesen 7p szerezhető, a modul neve: szam.py
minta
(a stílus kialakítása nem feladat, de a feladat sorszámának és betűjelének a kiíratása igen):
I/A:
A generált szám: 45

I/B:
A szám öttel és hárommal is osztható!

A.Generálj egy véletlen egész  számot az [1, 50] zárt intervallumban! (2p)

B.A program írja ki a következők egyikét: (a mintának megfelelően – 1p):
Amennyiben a szám 5-tel osztható:
“A szám öttel osztható!”,
Amennyiben a szám 3-mal osztható:
“A szám hárommal  osztható!”,
Amennyiben a szám 5-tel és 3 – mal is osztható:
“A szám öttel és hárommal is osztható!”,"""
"""A három kiírás közül csak az egyik jelenjen meg a képernyőn!. (4p + 1p)"""


import random

def vel_szam():
    i = 0
    vel = 1
    while ((i < 1) and (vel >= 0)):
        vel = int(random.randrange(vel) * 40 ) -1
        print(str(vel))
        i +=1

    print(f"I/A: \n \t A generált szám:{vel} ")










