import os 
import time
print("\n********************** Wilkommen beim geheimen Auktionsprogramm **********************\n")


def max_auktion(dict):
    winner = ""
    highest_bid = 0
    for i in dict:
        bid_amount = dict[i]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = i
            
    print(f"\nThe winner is {winner} with {bid_amount}")
        
            
            
            
            
            
            
bid_dict = {}
status = 1
while status:
    
    name = input("\nBitte geben Sie Ihren Namen ein: ")
    gebot = int(input("Bitte geben Sie Ihr Gebot ein: €"))
    bid_dict[name] = gebot
    
    programm_status = input("Wird noch jemand ein Gebot abgeben? Wenn ja, geben Sie bitte 'ja' ein. Sonst geben Sie 'nein' ein: ")
    
    time.sleep(2)  # Döngüye bir saniyelik gecikme ekler
    os.system("cls" if os.name == "nt" else "clear")
    
    if programm_status == "nein":
        max_auktion(bid_dict)
        time.sleep(2)
        status= 0
        




    

    