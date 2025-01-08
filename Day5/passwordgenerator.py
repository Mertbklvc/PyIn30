import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("\nWillkommen bei PyPassword Generator\n")

letter_zahl = int(input("\nWie viele Buchstaben möchten Sie in Ihrem Passwort haben?\n"))
number_zahl = int(input("\nWie viele Nummern möchten Sie?\n"))
symbol_zahl = int(input("\nWie viele Symbole möchten Sie?\n"))

password_list = []     
password = ""

for i in range(0,letter_zahl):
    password_list.append(random.choice(letters))
    
    
for i in range(0,number_zahl):
    password_list.append(random.choice(numbers))
    
for i in range(0,symbol_zahl):
    password_list.append(random.choice(symbols))
    
random.shuffle(password_list)

for i in password_list:
    password += i
    

print(f"\nIhr Passwort lautet: {password}")
