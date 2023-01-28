from film import Film

def fajlbeolvasas():
    f = open("film.txt","r",encoding='utf-8')
    fejlec = f.readline()
    fajltartalom = f.readlines()
    f.close()
    f_feldolgozas(fajltartalom)

filmek = []

def f_feldolgozas(fajltartalom):
    i = 0
    while (i < len(fajltartalom)):
        sor = fajltartalom[i].strip().split(';')
        film = Film(sor)
        filmek.append(Film(sor))

        i += 1


def adatszam():
    i = 0
    while (i <len(filmek)):
        i += 1
    return i

def legrovidebb_film():
    i = 0
    film_index = 0
    legrovidebb = filmek[film_index].perc

    while (i < len(filmek)):
        if legrovidebb > filmek[i].perc:
            legrovidebb= filmek[i].perc
            film_index = i

        i += 1
    return filmek[film_index].cim

def szaztiz():
    i = 0
    db = 0
    while (i < len(filmek)):
        if filmek[i].perc >= 110:
            db += 1

        i += 1
    return db

def szinesz():
    szereplo = input('Adj meg egy színészt: ')

def kiiratas():
    f = open("feladat6.txt","w", encoding='utf-8')
    f.write(str(szaztiz()))
    f.close()
