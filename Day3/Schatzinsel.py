import time


print('''  
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
    
''')
print("\nWillkommen auf der Schatzinsel!\n")
print("\nDeine Aufgabe ist es, den Schatz zu finden!\n")
auswahl1 = input('\nDu bist an eine Kreuzung gekommen. Schreibe "rechts", um nach rechts zu gehen, oder "links", um nach links zu gehen: ').lower()
time.sleep(2)


if auswahl1 == 'links':
    auswahl2 = input('\nDu bist an einem kleinen See angekommen. Möchtest du schwimmen oder bis zum Abend warten? Schreibe "schw" für schwimmen oder "war" für warten: ').lower()
    time.sleep(2)
    if auswahl2 == 'war':
        auswahl3 = input('\nEin alter Mann kam bei Sonnenuntergang zu deinem Standort und sagte, dass er dich mit seinem Boot hinüberbringen könnte. Schreibe "y" für Ja oder "n" für Nein, um zu antworten: ').lower()
        time.sleep(2)
        if auswahl3 == 'y':
            auswahl4 = input('\nDu bist auf die andere Seite des Sees gelangt und vor dir liegt ein Friedhof. Es gibt zwei Gräber auf dem Friedhof. Welches möchtest du ausgraben? Schreibe "rechts" für das rechte Grab oder "links" für das linke Grab: ')
            time.sleep(2)
            if auswahl4 == 'links':
                print("\nDu hast den Schatz gefunden! Herzlichen Glückwunsch! Du hast eine Belohnung von 10€ gewonnen :)")
                
            else:
                print("\nAus dem Grab kam ein Zombie heraus und hat dich getötet!")
                time.sleep(1)
                print('''
                               (()))
                               /|x x|
                              /\( - )
                      ___.-._/\/
                     /=`_'-'-'/  !!
                     |-{-_-_-}     !
                     (-{-_-_-}    !
                      \{_-_-_}   !
                       }-_-_-}
                       {-_|-_}
                       {-_|_-}
                       {_-|-_}
                       {_-|-_}  
                   
                      ''')
                
        else:
            print("\nDu wurdest in der Nacht von Wölfen getötet!")
            time.sleep(1)
            print('''
                  
      /^\      /^\
      |  \    /  |
      ||\ \../ /||
      )'        `(
     ,;`w,    ,w';,
     ;,  ) __ (  ,;
      ;  \(\/)/  ;;
     ;|  |vwwv|    ``-...
      ;  `lwwl'   ;      ```''-.
     ;| ; `""' ; ;              `.
      ;         ,   ,          , |
      '  ;      ;   l    .     | |
      ;    ,  ,    |,-,._|      \;
       ;  ; `' ;   '    \ `\     \;
       |  |    |  |     |   |    |;
       |  ;    ;  |      \   \   (;
       | |      | l       | | \  |
       | |      | |    | |  ) |
       | |      | ;       | |  | |
       ; ,      : ,      ,_.'  | |
      :__'      | |           ,_.'
               `--'
                  ''')
    else:
        print("\nDu hast einen Krampf im Bein bekommen und bist ertrunken! Spiel vorbei!")
        print('''
                               .-"""-.
                       ---------       
                      ;_.-"""-._;
   .,_       __,.---.-(=(o)-(o)=)-.---.,__       _,.
   '._'--"```          \   ^   /          ```"--'_.'
      ``"''~---~~%^%^.%.`._0_.'%,^%^%^~~---~''"``
  jgs ~^~- `^-% ^~.%~%.^~-%-~.%-^.% ~`% ~-`%^`-~^~
         ~^- ~^- `~.^- %`~.%~-'%~^- %~^- ~^
              ''')
    
else:
    print("\nDu bist in ein Loch gefallen. Spiel vorbei!")
    time.sleep(1)
    print('''
          
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣤⣴⣾⣿⣿⡿⠿⠿⠿⠟⠛⠛⠻⠿⠿⠿⢿⣿⣿⣷⣦⣤⡀⠀⠀⠀
⠀⢀⣼⣿⡿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣧⡀⠀
⠀⢸⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡇⠀
⠀⠈⢻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀
⠀⠀⠀⠈⠛⠳⢦⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⡴⠞⠛⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀

          ''')