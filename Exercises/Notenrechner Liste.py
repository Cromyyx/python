liste = []
gewicht = []
while True:
    grade = float(input("Note eingeben! (falls fertig 999 eingeben)"))
    if grade == 999:
        break
    else:
        gewicht_numb = int(input("Gewichtung in%"))
        liste.append(grade * gewicht_numb)
        gewicht.append(gewicht_numb)
        print(liste)
print(liste)

schnit = sum(liste) / sum(gewicht)
print("Der Notenschnit ist:", f"{schnit:4.2f}"" mit einer Gewichtung von", sum(gewicht), "%")
