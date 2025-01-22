import random
import ascii


def kart_geben():
    """gibt eine zufällige Karte vom Schreibtisch zurück
    """
    
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def berechnen_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def vergleich_score(u_score,c_score):
    if u_score == c_score:
        return "\nUnentschieden!"
    elif c_score == 0:
        return "\nSie haben verloren! Computer hat Blackjack"
    elif u_score == 0:
        return "\nSie haben gewinnen! Sie haben Blackjack"
    elif u_score > 21:
        return "\nDie Summe von ihrer Karten übersteigt 21! Sie haben verloren!"
    elif c_score > 21:
        return "\nDie Summe der Karten, die der Computer hat, übersteigt 21! Sie haben gewinnen!"
    elif u_score > c_score:
        return "\nSie haben gewinnen!"
    else:
        return "\nSie haben verloren!"
 
def play_game():   
    print(ascii.casino)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    ist_game_over = False

    for i in range(2):
        user_cards.append(kart_geben())
        computer_cards.append(kart_geben())

    while not ist_game_over:
        user_score = berechnen_score(user_cards)
        computer_score = berechnen_score(computer_cards)

        print(f"Ihre Karten: {user_cards}, Aktuelle Punkte: {user_score}")
        print(f"\nErste Karte von Computer: {computer_cards[0]}")
            
            
            
        if user_score == 0 or computer_score == 0 or user_score >21:
            ist_game_over = True
        else:
            user_neue_karte = input("\nEine neue Karte ziehen: 'n', passen: 'p' eingeben: ").lower()
            if user_neue_karte == 'n':
                user_cards.append(kart_geben())
            else:
                ist_game_over = True
                
                
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(kart_geben())
        computer_score = berechnen_score(computer_cards)



    print(f"\nFinal Hand {user_cards}, final score: {user_score}")
    print(f"\nComputer Final Hand: {computer_cards}, final score: {computer_score}")
    print(vergleich_score(user_score, computer_score))


while input("\nMöchtest du eine Partie Blackjack spielen? Wenn 'ja' bitte geben Sie 'ja' ein: ") == "ja":
    print("\n" * 50)
    play_game()