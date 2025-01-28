import random

class Tier:
    pass



tier_1 = Tier()


# Wir verwenden PascalCase, um unsere Klasse zu benennen.
# PascalCase: Jedes Wort im Namen beginnt mit einem Großbuchstaben, ohne Unterstriche.


class Auto:
    
    def __init__(self):
        print("Ein neues Auto wurde erstellt.")
        
        
# __init__ ist der Konstruktor einer Klasse in Python, der beim Erstellen einer Instanz automatisch aufgerufen wird, um Attribute zu initialisieren.

mert_araba = Auto()
sinem_araba = Auto()


class User:
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
        
    def follow(self,other_user):
        other_user.followers += 1
        self.following += 1
        
    
        
user_1 = User(1907,"Mert")
print(dir(user_1))
print(user_1.__dict__)
user_2 = User(2025,"Sinem")

user_1.follow(user_2)
print(user_1.__dict__)
print(user_2.__dict__)