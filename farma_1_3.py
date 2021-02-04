#   Farma wersja 1.2
gra_wersja = '1.3.0'
#   - Rozbicie na 3 pliki - gra+poziomy_gry+teksty
#   - Dodanie wyjścia z gry przez 'x' lub 'X'

####################################

import poziomy_gry
import teksty_gry
import random as r

poziomy=poziomy_gry.get_poziomy()
s=teksty_gry.get_slownik()
#   START

poziom = 0      #   Czytaj +1
koniec = False

while poziom <=9:
    print(s['nag_end'],s['poziom'],poziomy[poziom]['nazwa'], sep='')
    if poziomy[poziom]['krowy_max'] < 5:
        print("W oborze są : ",poziomy[poziom]['krowy_max'],' krowy.', sep='')
    else:
        print("W oborze jest : ",poziomy[poziom]['krowy_max'],' krów.', sep='')
    print("Każda krowa daje max: ",poziomy[poziom]['mleko_max'],' Litrów mleka', sep='')
    if poziomy[poziom]['koty'] == 1:
        print("W okolicy mieszka: ",poziomy[poziom]['koty'],' kot', sep='')
    else:
        if poziomy[poziom]['koty'] < 5:
            print("W okolicy mieszkają: ",poziomy[poziom]['koty'],' koty', sep='')
        if poziomy[poziom]['koty'] >= 5:
            print("W okolicy mieszka: ",poziomy[poziom]['koty'],' kotów', sep='')
    print('\n- - - - -')
    podejscie = 1
    while podejscie <=5:
        print("Dojenie: ",podejscie)
        krowy = r.randrange(poziomy[poziom]['krowy_min'],poziomy[poziom]['krowy_max']+1)
        licznik = []
        suma_all = 0
        suma_opis = ''
        for i in range(1,krowy+1):
            mleko_tmp = r.randrange(poziomy[poziom]['mleko_min'],poziomy[poziom]['mleko_max']+1)
            licznik.append(mleko_tmp)
            if suma_all != 0:
                suma_opis+= "+"
            suma_opis+=str(mleko_tmp)
            suma_all+= mleko_tmp
            print("Krowa nr. ",i,' dała: ',mleko_tmp,' L', sep='') 
        koty = poziomy[poziom]['koty']
        if poziomy[poziom]['koty'] > 0:
            for i in range(1,koty+1):
                mleko_tmp = r.randrange(poziomy[poziom]['koty_min'],poziomy[poziom]['koty_max']+1)
                licznik.append(-mleko_tmp)
                suma_opis+=str(-mleko_tmp)
                suma_all-=mleko_tmp
                print("Kot nr. ",i," wypił: ",mleko_tmp," L mleka", sep='')
            pytanie_end="Ile zostało mleka? : "
        else:
            pytanie_end="Ile dały razem? : "
        wynik_tmp=input(pytanie_end)
        while True:
            if wynik_tmp.isdigit():
                suma = int(wynik_tmp)
                if suma != suma_all:
                    print(":( zly wynik")
                    wynik_tmp=input(pytanie_end)
                else:
                    break
            else:
                if wynik_tmp == 'x' or wynik_tmp == 'X':
                    koniec = True
                    break
                else:
                    print("Zła wartość")
                    wynik_tmp=input(pytanie_end)
        if koniec:
            break
        podejscie+=1
        print("OK - wynik poprawny\n",suma_opis,"=",suma_all,'\n', sep='')
    if koniec:
        break
    poziom+=1

print("\n\n# # # # # # # # # # #\n\n   K O N I E C \n\n# # # # # # # # # # #")
koniec=input("")