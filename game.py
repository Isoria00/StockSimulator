from stocks import *
from player import *
import os
import time




def clear_terminal():
    os.system("cls")

def check_stock_price():
    stocks = get_stocks()
    print("Current Stock Prices\n")
    for stock in stocks:
        print(stock)

def update_stock_prices():
    stocks = get_stocks()
    for stock in stocks:
        stock.value_changer()
    print("Stock Value Change")

def get_stock_shares(player):
    print("\nOwned Stocks:")
    for stock, shares in player.owned_stocks.items():
        print(f"{stock.capitalize()}: {shares} shares")

def buy_stock(player):
    stocks = get_stocks()

    print("Available Stocks:\n")
    for i, stock in enumerate(stocks, 1):
        print(f"{i}. {stock.name} - ${stock.price}")
    
    
    while True:
        try:

            stock_choice = int(input("What stock would you like to buy?\nPress 0 to Cancel Purchase\n"))
            
            if stock_choice == 0:
                print("Cancelled stock purchase")
                return
            if stock_choice < 1 or stock_choice > len(stocks):
                print("Inavalid Stock number, please try again")
                continue
            selected_stock = stocks[stock_choice - 1]

            buy_up_to = player.balance // selected_stock.price
            buy_up_to = round(buy_up_to)
            if buy_up_to < 1:
                print("You dont have enough money for this stock!")
                break

            clear_terminal()
            shares = int(input(f"How many shares of {selected_stock.name} would you like to buy?\nYou can buy up to {buy_up_to} shares of {selected_stock.name}\n"))
            total_cost = shares * selected_stock.price
            clear_terminal()
            
            if player.balance >= total_cost:
                player.owned_stocks[selected_stock.name] = player.owned_stocks.get(selected_stock.name, 0) + shares
                player.balance -= total_cost
                player.record_transaction(selected_stock.name, shares, selected_stock.price, "Buy")
                print(f"You have sucessfully bought {shares} of {selected_stock.name} for ${total_cost:.2f}. ")
                print(f"Your new balance is: ${player.balance:.2f}")
            else:
                print("You dont have enough funds to complete this purchase")

            break

        except ValueError:
            print("Invalid input, please enter a number")

    return player


def sell_stock(player):
    while True:
        try:
            stocks = get_stocks()
            print("\n")
            for i, stock in enumerate(stocks, 1):
                print(f"{i}.{stock.name} - ${stock.price}")
            
            stock_choice = int(input("\nWhat stock would you like to sell?\n"))
            if stock_choice == 0:
                print("Cancelled stock transaction")
                return
            if stock_choice < 1 or stock_choice > len(stocks):
                print("Inavalid Stock number, please try again")
                continue
            selected_stock = stocks[stock_choice - 1]
            owned_shares = player.owned_stocks.get(selected_stock.name, 0)
            if owned_shares == 0:
                print(f"You don't own any shares of {selected_stock.name}.")
                continue
            print(f"\nYou own {owned_shares} shares of {selected_stock.name}.")
            while True:
                amount_to_sell = int(input(f"How many shares of {selected_stock.name} would you like to sell? (Press 0 to cancel)\n"))
                if amount_to_sell == 0:
                    print("Cancelled stock sale.")
                    return
                if amount_to_sell > owned_shares:
                    print(f"You cannot sell more shares than you own. You only have {owned_shares} shares.")
                else:
                    
                    total_sale_value = amount_to_sell * selected_stock.price
                    player.owned_stocks[selected_stock.name] -= amount_to_sell
                    player.balance += total_sale_value
                    player.record_transaction(selected_stock.name, amount_to_sell, selected_stock.price, "Sell")
                    
                    
                    if player.owned_stocks[selected_stock.name] == 0:
                        del player.owned_stocks[selected_stock.name]
                    
                    print(f"Successfully sold {amount_to_sell} shares of {selected_stock.name} for ${total_sale_value:.2f}.")
                    print(f"Your new balance is ${player.balance:.2f}")
                    return  

        except ValueError:
            print("Invalid input, please enter a number.")


def check_transaction_history(player):
    if player.transaction_history:
        print("Transaction History:")
        for transaction in player.transaction_history:
            print(f"{transaction['action']} {transaction['shares']} shares of {transaction['stock']} at ${transaction['price']} per share.")
    else:
        print("No transactions made yet")
def menu_option(player):
    while True:
        try:
            user_input = int(input("\n1.Check Stock Prices\n2.Check Transaction History\n3.Buy Stock\n4.Sell Stock\n5.Next Turn\n6.Check Shares Owned\n7.Exit Game\n"))
            match user_input:
                case 1:
                    clear_terminal()
                    check_stock_price()
                case 2:
                    clear_terminal()
                    check_transaction_history(player)
                case 3:
                    clear_terminal()
                    buy_stock(player)
                case 4:
                    clear_terminal()
                    sell_stock(player)
                case 5:
                    clear_terminal()
                    update_stock_prices()
                case 6:
                    get_stock_shares(player)
                case 7:
                    clear_terminal()
                    while True:
                        try:
                            user_choice = int(input("\nAre you sure you want to exit?(Press 0 to Exit)\nPress any other Number to Cancel\n"))
                            if user_choice == 0:
                                return
                            else:
                                print("Canceled...")
                                break
                        except ValueError:
                            print("Invalid Option Please Try Again")
                case _:
                    clear_terminal()
                    print("\nPlease Enter Valid Number\n")
                    time.sleep(1)
                    clear_terminal()

        except ValueError:
            print("Please Enter Valid Number")





def main():
    # Creates instance of Player class
    player = Player()
    # Runs main menu with player as parameter
    menu_option(player)
# Run Game
main()