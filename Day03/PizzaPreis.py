print("\nWillkommen bei Python Pizza!\n")
size = input("\nWelche Größe der Pizza möchten Sie? S, M oder L: ")
pepperoni = input("\nMöchten Sie auch Pepperoni auf Ihrer Pizza? Y oder N: ")
kase = input("\nMöchten Sie extra Käse? Y oder N: ")

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Wrong size")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if kase == "Y":
    if size == "S":
        bill += 1
    else:
        bill += 2

print(f"Der zu zahlende Betrag: {bill}€")
print('''
                                               
                                   ,(  `-.
                                 ,': `.   `.
                               ,` *   `-.   
                             ,'  ` :+  = `.  `.
                           ,~  (o):  .,   `.  `.
                         ,'  ; :   ,(__) x;`.  ;
                       ,'  :'  itz  ;  ; ; _,-'
                     .'O ; = _' C ; ;'_,_ ;
                   ,;  _;   ` : ;'_,-'   i'
                 ,` `;(_)  0 ; ','       :
               .';6     ; ' ,-'~
             ,' Q  ,& ;',-.'
           ,( :` ; _,-'~  ;
         ,~.`c _','
       .';^_,-' ~
     ,'_;-''
    ,,~
    i'
    :
      ''')