class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, exhale.")
        
        

class Fish(Animal):
    
    def __init__(self):
        super().__init__()
        
    def breathe(self):
        super().breathe()
        print("doing this in water...")
    def swim(self):
        print("moving in water.")
        
        
        
        
nemo = Fish()
nemo.swim()
nemo.breathe()

# In Python bedeutet Vererbung (Inheritance), dass eine Klasse (Kindklasse) Eigenschaften und Methoden von einer anderen Klasse (Elternklasse) erbt. 
# Dadurch wird Code-Wiederholung reduziert und eine bessere Struktur in der objektorientierten Programmierung geschaffen.

print(nemo.num_eyes)