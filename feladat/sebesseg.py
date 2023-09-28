sebesseg=input("Menyivel mentél? ")
sebesseg=int(sebesseg)
if 0< sebesseg <= 50:
    print("Nem mesz gyorsan")
elif 50<sebesseg <= 65:
    print("gyorsan mentel megbüntetek 15000ft-vel")
elif 65<sebesseg <=80:
    print("Megbüntettek 30e forintal")
elif 80<sebesseg <=100:
    print("Megbüntettek 90e forintal")
elif 100<sebesseg <=140:
    print("elvették a jogositványt")
elif sebesseg == 0:
    print("egyhejben állsz")
