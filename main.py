from film import Film
import feldolgozas



feldolgozas.fajlbeolvasas()

print(f'1. feladat:')
print(f'\tA filmek száma: {feldolgozas.adatszam()}')
print(f'2. feladat:')
print(f'\tA legrövidebb film: {feldolgozas.legrovidebb_film()}')
print(f'3. feladat:')
print(f'\tA 110 percnél hosszabb filmek száma: {feldolgozas.szaztiz()}')

feldolgozas.kiiratas()
