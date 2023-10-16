x = float(input("Ievadiet x vērtību: "))
y = float(input("Ievadiet y vērtību: "))

if (x == -4 or x == 2) and (y >= -2 and y <= 3):
    print("Ievadītie dati atrodas uz robežlīnijas!")
elif (x > -4 and x < 2) and (y > -2 and y < 3):
    print("Ievadītie punkti atrodas figūrā!!")
else:
    print("Ievaditie dati neatrodas figūrā un nav uz robežlīnijas!")