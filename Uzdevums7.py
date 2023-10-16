x = float(input("Ievadiet x vērtību: "))
y = float(input("Ievadiet y vērtību: "))

if (x == -1 or x == 1) and (y >= -1 and y <= 1):
    print("Ievadītie dati atrodas uz robežlīnijas!")
elif (x > -1 and x < 1) and (y > -1 and y < 1):
    print("Ievadītie punkti atrodas figūrā!!")
else:
    print("Ievaditie dati neatrodas figūrā un nav uz robežlīnijas!")

