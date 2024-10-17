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
    while i<=10:
        a=random.choice([0,1])
        lista.append(a)
        i+=1
    return(lista)

def kockadobas():
    i:int=0
    a:int=0
    lista = []
    while i<=10:
        a=random.choice([1,2,3,4,5,6])
        lista.append(a)
        i+=1
    return(lista)


 
