

# Cette fonction permet de demander à l'utilisateur le nombre de pièce
def insert_coin():
    print("Insert coin")
    coin = int (input())
        

# Cette fonction n'autorise pas des pièces inférieur à 5 cts
def accept_coin(coin):

    if coin >= 5 :
        return True
    else :
        return False
# Cette fonction permet d'échanger les pièces et de retourner le bon nombre de pièce
def make_change(product_price,coin):
    coin_to_return = 0
    if coin == product_price :
        return 0
    elif coin > product_price :
        coin_to_return = coin - product_price
        return coin_to_return
    elif coin > product_price :
        coin_to_return = coin  - product_price 
        return coin_to_return

def distribute_ok(coin_to_return) :
    if coin_to_return == 0 :
        return 0
    elif coin_to_return > 0
        



    
