def poz_szamok_szama(lista):
    i:int=0
    db:int=0
    while(i<len(lista)):
        if (lista[i]>0):
            db+=1
    return db
