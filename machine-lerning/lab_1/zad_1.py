#####################
#     Zadatak 1     #
#####################

"""
    Napišite program koji od korisnika zahtijeva unos radnih sati te koliko je plaćen po radnom satu. Koristite ugrađenu
    Python metodu input(). Nakon toga izračunajte koliko je korisnik zaradio i ispišite na ekran. Na kraju prepravite
    rješenje na način da ukupni iznos izračunavate u zasebnoj funkciji naziva total_euro.
"""

# Function reads a floating point number
# from the input console
def input_float(message):
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("'%s' is not a valid floating point number!" % value)
            continue

# Function calculates total salary based
# on the work_hours & payment_per_hour
# of the user
def total_euro(work_hours, payment_per_hour):
    return work_hours * payment_per_hour

work_hours = input_float("Work hours: ")
payment_per_hour = input_float("Salary: ")

print("User has earned %.2f€" % total_euro(work_hours, payment_per_hour))