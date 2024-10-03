from stocks import *
from player import Player
def menu_option():
    while True:
        user_input = int(input("\n1.Check Stock Prices\n2.Check Transaction History\n3.Buy Stock\n4.Sell Stock\n5.Next Turn\n"))
        match user_input:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case _:
                "Invalid Option!"





def main():
    menu_option()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''   
    stocks = get_stocks()
    print("Current Stock Prices\n")
    for stock in stocks:
        print(stock)
    
    for stock in stocks:
        stock.value_changer()
    
    print("\nUpdated stock prices after the value change!")
    for stock in stocks:
        print(stock)
    

    '''
main()  