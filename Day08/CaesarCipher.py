import art
import time
import os




def schließ_animation():
    animation_frames = [
        "╔════════════════════╗",
        "║  Programm wird     ║",
        "║  geschlossen...    ║",
        "╚════════════════════╝"
    ]
    
    closing_message = [
        "╔════════════════════╗",
        "║  Programm wurde    ║",
        "║  erfolgreich       ║",
        "║  geschlossen!      ║",
        "╚════════════════════╝"
    ]
    
    for i in range(3, 0, -1):
        os.system("cls" if os.name == "nt" else "clear")
        print("\n".join(animation_frames))
        print(f"\nSchließen in {i} Sekunde{'n' if i > 1 else ''}...")
        time.sleep(1)
    
    for _ in range(3):
        os.system("cls" if os.name == "nt" else "clear")
        for line in animation_frames:
            print(line.replace("...", "." * (_ % 3 + 1)))
        time.sleep(0.5)
    
    os.system("cls" if os.name == "nt" else "clear")
    print("\n".join(closing_message))
    time.sleep(2)
    
    
def caesar(original_text, verschieben_zahl,encode_oder_decode):
    output_text = ""
   
    if encode_oder_decode == "decode":
            verschieben_zahl *= -1
    for i in original_text:
        if i not in alphabet_lowercase:
            output_text += i
        else:       
            verschobene_position = alphabet_lowercase.index(i) + verschieben_zahl
            verschobene_position %= len(alphabet_lowercase)
            output_text += alphabet_lowercase[verschobene_position]      
    print(f"Ergebnis: {output_text}")
    
alphabet_lowercase = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

print(art.logo)

programm_status = 1

while programm_status:
    if programm_status:
        auswahl = input("\nZum Verschlüsseln 'encrypt' und zum Entschlüsseln 'decode' eingeben: ").lower()
        text = input("\nBitte geben Sie den Text ein: ").lower()
        shift = int(input("\nGeben Sie ein, wie viele Buchstaben Sie verschieben möchten: "))
        caesar(text,shift,auswahl)
        status = input("\nWollen Sie den Prozess wiederholen? Zum Fortfahren 'ja', zum Beenden 'nein' eingeben: ").lower()
        if status == 'nein':
            schließ_animation()
            
            programm_status = 0

    



