import time
import sys

def loading_animation():
    animation = ["|", "/", "-", "\\"]
    for i in range(20):  # Döngü sayısını artırabilirsiniz
        time.sleep(0.1)  # Her adım arasında bekleme süresi
        sys.stdout.write(f"\rProzess wird ausgeführt... {animation[i % len(animation)]}")
        sys.stdout.flush()
    sys.stdout.write("\rProzess abgeschlossen! \n")

print("\n------------- Willkommen am Bamberg Bank Geldautomaten -------------")
programm_status = 1
geld = 0

while programm_status:
    print("\n1- Kontostand abfragen!")
    print("\n2- Geld einzahlen!")
    print("\n3- Geld abheben!")
    print("\n4- Programm beenden!")
    status =int(input("\nBitte wählen Sie die gewünschte Transaktion aus: "))
    
    if status == 1:
        print(f"\nIhr Kontostand: {geld}€")
        time.sleep(1)
        print("-------------------------------------------------------------------")
    elif status == 2:
        einzahlwert = int(input("\nBitte geben Sie den gewünschten Einzahlungsbetrag ein:\n"))
        loading_animation()
        geld += einzahlwert
        time.sleep(1)
        print("-------------------------------------------------------------------")
    elif status == 3:
        auszahlWert = int(input("\nBitte geben Sie den Betrag ein, den Sie abheben möchten: "))
        
        loading_animation()
        if auszahlWert > geld:
            print("\nIhr Kontostand ist nicht ausreichend, um den gewünschten Betrag abzuheben!")
        else:
            geld -= auszahlWert
        time.sleep(1)
        print("-------------------------------------------------------------------")
    elif status == 4:
        break
    else:
        print("\nBitte geben Sie eine der angegebenen Zahlen für die Transaktion ein!")
        time.sleep()
        print("-------------------------------------------------------------------")