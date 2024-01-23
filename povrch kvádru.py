a = input("Zadejte proměnnou a: ")
b = input("Zadejte proměnnou b: ")
c = input("Zadejte proměnnou c: ")
d = input("Zadejte proměnnou d: ")

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if a>0 and b>0 and c>0 and d>0:
    vysledek = 2*(a*b+a*c+b*c)

print("Výsledek je: ", vysledek)