import numpy as np
import exchange as ex
import product as pd

def main():
    state_machine = True
    coin = 0
    product = ''
    product_price = 0
    while state_machine :
        pd.select_product(product)
        ex.insert_coin(coin)
        ex.accept_coin(coin)
        ex.make_change(product_price, coin)
        
        


if __name__ == "__main__":
    main()
    
