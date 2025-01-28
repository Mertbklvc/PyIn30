class QuizBrain:
    def __init__(self, fragen_list):
        self.frage_nummer = 0
        self.fragen_list = fragen_list
        self.punkte = 0
        
        
    def noch_frage(self):
        return self.frage_nummer < len(self.fragen_list)
        
    def next_frage(self):
        aktuelle_frage  = self.fragen_list[self.frage_nummer]
        self.frage_nummer += 1
        user_antwort = input(f"\nF.{self.frage_nummer}: {aktuelle_frage.frage} (Ja/Nein): ")
        self.prüfe_antwort(user_antwort,aktuelle_frage.antwort)
    def prüfe_antwort(self,user_antwort,correct_antwort):
        if user_antwort.lower() == correct_antwort.lower():
            print("\nRichtig!")
            self.punkte += 1
        else:
            print("\nFalsch!")
            
        print(f"Ihren Punktestand jetzt: {self.punkte}/{self.frage_nummer}")