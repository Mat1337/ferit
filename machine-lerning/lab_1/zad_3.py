#####################
#     Zadatak 3     #
#####################

"""
    Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok korisnik ne upiše „Done“ (bez
    navodnika). Pri tome brojeve spremajte u listu. Nakon toga potrebno je ispisati koliko brojeva je korisnik unio, njihovu
    srednju, minimalnu i maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran.
    Dodatno: osigurajte program od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
    ispiše odgovarajuću poruku.
"""

numbers = []

while True:
    value = input("Input a number: ")
    try:
        numbers.append(float(value))
    except ValueError:
        # check for exit
        if (value == "Done"):
            break

        print("'%s' is not a valid floating point number!" % value)
        continue

print("User entered '%d'" % len(numbers))
print("Average '%d'" % (sum(numbers) / len(numbers)))
print("Min '%d'" % min(numbers))
print("Max '%d'" % max(numbers))

print(sorted(numbers))