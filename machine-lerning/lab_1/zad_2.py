#####################
#     Zadatak 2     #
#####################

"""
    Napišite program koji od korisnika zahtijeva upis jednog broja koji predstavlja nekakvu ocjenu i nalazi
    se između 0.0 i 1.0. Ispišite kojoj kategoriji pripada ocjena na temelju sljedećih uvjeta:
        >= 0.9 A
        >= 0.8 B
        >= 0.7 C
        >= 0.6 D
        <  0.6 F
    Ako korisnik nije utipkao broj, ispišite na ekran poruku o grešci (koristite try i except naredbe).
    Također, ako je broj izvan intervala [0.0 i 1.0] potrebno je ispisati odgovarajuću poruku.
"""

while True:
    value = input("Input number value (0-1): ")
    try:
        grade = float(value)
    except ValueError:
        print("'%s' is not a valid floating point number!" % value)
        continue

    # check that the grade is in a valid margin
    if 0 < grade > 1:
        print("'%d' needs to be in a range from '0' to '1'" % grade)
        continue

    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")

    # break out of the while loop
    break