liste = []
while True:
    grade = int(input("Note eingeben! (falls fertig 999 eingeben)"))
    if grade == 999:
        break
    else:
        liste.append(grade)
        print(liste)
print(liste)

schnit = sum(liste) / len(liste)
print("Der Notenschnit ist:", schnit)
