print("\n***************** Willkommen beim BMI-Rechner *****************\n")
Gewicht = int(input("Bitte geben Sie Ihr Gewicht an:\n"))
Größe = int(input("Bitte geben Sie Ihre Größe(cm) ein:\n"))

bmi = round(Gewicht/((Größe/100) ** 2),2)
print("Ihr BMI-Wert:" + str(bmi))