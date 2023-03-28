#####################
#     Zadatak 6     #
#####################

"""
    Napišite Python skriptu koja će učitati tekstualnu datoteku naziva SMSSpamCollection.txt [1].
    Ova datoteka sadrži 425 SMS poruka pri čemu su neke označene kao spam, a neke kao ham.
    Primjer dijela datoteke:

        ham Go until jurong point, crazy.. Available only in bugis n great world la e buffet... Cine there got amore wat...
        ham Ok lar... Joking wif u oni...
        spam Did you hear about the new "Divorce Barbie"? It comes with all of Ken's stuff!
        ham Yup next stop.

    a) Izračunajte koliki je prosječan broj riječi u SMS porukama koje su tipa ham, a koliko je prosječan broj riječi u porukama koje su tipa spam.
    b) Koliko SMS poruka koje su tipa spam završava uskličnikom ?
"""

line_count = {}
spam_count = {}

spam_questions = 0

with open("../assets/%s" % input("File: ")) as file:
    for line in file:
        line = line.replace('\n', "")
        line = line.replace('\t', " ")
        words = line.split(" ")

        if (words[0] == "spam" and line.endswith('?')):
            spam_questions += 1

        if (words[0] in line_count):
            line_count[words[0]] += 1
        else:
            line_count[words[0]] = 1

        if (words[0] in spam_count):
            spam_count[words[0]] += len(words[1:])
        else:
            spam_count[words[0]] = 1

    spam_count['ham'] /= line_count['ham']
    spam_count['spam'] /= line_count['spam']

print(spam_count)
print("Spam words that end with '?' = %d" % spam_questions)