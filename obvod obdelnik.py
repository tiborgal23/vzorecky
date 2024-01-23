#privitani uzivatele
print("Vítejte v aplikaci a pro výpočet obvodu obdelníku")

#Deklarace (spíše inicializace) promněnných, následně do nich ukládáme vstupy
a = input("Zadejte proměnnou a: ")
b = input("Zadejte proměnnou b: ")

#Přetypování z stringu na int
a = int(a)
b = int(b)

#Podmínka, kontrola zda v proměnných není záporné číslo
if a>0 and b>0:
    #Deklarace proměnné výsledek
    vysledek = 2*(a+b)
    #Output pro výsledek
    print("Výsledek je: ", vysledek)

