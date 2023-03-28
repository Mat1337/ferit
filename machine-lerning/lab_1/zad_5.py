#####################
#     Zadatak 5     #
#####################

"""
    Napišite Python skriptu koja će učitati tekstualnu datoteku naziva song.txt. Potrebno je napraviti rječnik koji kao
    ključeve koristi sve različite riječi koje se pojavljuju u datoteci, dok su vrijednosti jednake broju puta koliko se svaka
    riječ (ključ) pojavljuje u datoteci. Koliko je riječi koje se pojavljuju samo jednom u datoteci? Ispišite ih.
"""

word_count = {}

with open("../assets/%s" % input("File: ")) as file:
    for line in file:
        line = line.replace('\n', "")
        words = line.split(" ")
        for word in words:
            if (word in word_count):
                word_count[word] += words.count(word)
            else:
                word_count[word] = 1

print(word_count)