wiek = input("Podaj wiek")
# wiek = int(wiek)

if wiek.isdigit() == False:
    exit("Wiek musi byc liczba")
wiek = int(wiek)
if wiek > 18 and wiek <= 65:
    print("Jetseś dorosły")
elif wiek > 65:
    print("Jestes za stary na alkoool")
else:
    exit("Jestes za mldy")
