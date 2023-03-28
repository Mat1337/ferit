#####################
#     Zadatak 4     #
#####################

"""
    Napišite program koji od korisnika zahtijeva unos imena tekstualne datoteke.
    Program nakon toga treba tražiti linije oblika:

        X-DSPAM-Confidence: <neki_broj>

    koje predstavljaju pouzdanost korištenog spam filtra. Potrebno je izračunati srednju vrijednost pouzdanosti.
    Koristite datoteke mbox.txt i mbox-short.txt
"""

# what the file needs to be searched for
search = "X-DSPAM-Confidence: "

# all the spam values will be stored here
values = []

with open('../assets/%s' % input("File: "), 'r') as file:
    for line in file:
        line = line.replace('\n', "")
        if line.startswith(search):
            line = line.replace(search, "")
            values.append(float(line))

print("Average '%.5f'" % (sum(values) / len(values)))