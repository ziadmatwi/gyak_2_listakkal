import random

def poz_szamok_szama(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if (lista[i]>0):
            db+=1
        i+=1
    return db

def negativ_szamok_osszege(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if (lista[i]<0):
            db+=1
        i+=1
    return db

def ottel_oszthato(lista):
    i:int=0
    db:int=0
    a:int=0
    while (i<len(lista)):
        if lista[i] % 5 == 0:
            a+=lista[i]
            db+=1
        i+=1
    return a/db


def ermedobas():
    i:int=0
    a:int=0
    lista = []
    while i<10:
        a=int(random.random()*2+1)
        lista.append(a)
        i+=1
    return(lista)

def fejszamlalo(lista):
    i:int=0
    db:int=0
    while i < len(lista):
        if lista[i] == 1:
            db+=1
        i+=1
    return db

def kockadobas():
    i:int=0
    a:int=0
    lista = []
    while i<200:
        a=int(random.random()*6+1)
        lista.append(a)
        i+=1
    return(lista)

def kockaszamlalas(lista):
    i:int=0
    egy:int=0
    ket:int=0
    harom:int=0
    negy:int=0
    ot:int=0
    hat:int=0
    while i < len(lista):
        if lista[i] == 1:
            egy+=1
        if lista[i] == 2:
            ket+=1
        if lista[i] == 3:
            harom+=1
        if lista[i] == 4:
            negy+=1
        if lista[i] == 5:
            ot+=1
        if lista[i] == 6:
            hat+=1
        i+=1
    return egy, ket, harom, negy, ot, hat

def kockacinkelt():
    i:int=0
    a:int=0
    lista = []
    while i<200:
        a=int(random.random()*7+1)
        lista.append(a)
        i+=1
    return(lista)

def kockaszamlalascinkelt(lista):
    i:int=0
    egy:int=0
    ket:int=0
    harom:int=0
    negy:int=0
    ot:int=0
    hat:int=0
    while i < len(lista):
        if lista[i] == 1:
            egy+=1
        if lista[i] == 2:
            ket+=1
        if lista[i] == 3:
            harom+=1
        if lista[i] == 4:
            negy+=1
        if lista[i] == 5:
            ot+=1
        if lista[i] == 6:
            hat+=1
        if lista[i] == 7:
            hat+=1
        i+=1
    return egy, ket, harom, negy, ot, hat

def kockaszamlalasuj(lista,szam):
    i:int=0
    db:int=0
    while i < len(lista):
        if szam == lista[i]:
            db+=1
        i+=1
    return db

def kockacinkeltuj():
    i:int=0
    a:int=0
    lista = []
    while i<200:
        a=int(random.random()*7+1)
        if a >= 6:
            lista.append(6)
        else:
            lista.append(a)
        i+=1
    return(lista)

 
def kockaszamlalasx(lista):
    i:int=0
    lista2 = [0,0,0,0,0,0]
    while i < len(lista):
        lista2[lista[i] -1 ]+=1
        i+=1
    return lista2