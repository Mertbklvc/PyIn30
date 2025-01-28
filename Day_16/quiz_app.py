from fragen_model import Frage
from data import fragen
from quiz_brain import QuizBrain
import logo
print(logo.logo)
fragen_bank = []
for i in fragen:
    frage = i["frage"]
    antwort = i["antwort"]
    neue_Frage = Frage(frage,antwort)
    fragen_bank.append(neue_Frage)
    
    
    
quiz = QuizBrain(fragen_bank)

while quiz.noch_frage():
    quiz.next_frage()
    
    
print("Sie haben das Quiz abgeschlossen!!!")
print(f"Endstand: {quiz.punkte}/quiz.frage_nummer")