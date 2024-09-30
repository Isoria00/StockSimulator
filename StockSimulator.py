import random
import time
import math
import os

# Bitcoin Range(16000,70000)
# Nvidia Range(50,250)
# Apple Range(400, 1500)

# Randomizes the Stocks Price

def clear_terminal():
    os.system('cls')
   


def set_values():
        clear_terminal()
        Bitcoin = random.randint(16000,70000)
        Bitcoin = round(Bitcoin)
         
        Nvidia = random.randint(50,250)
        Nvidia = round(Nvidia)
    
        Apple = random.randint(400, 1500)
        Apple = round(Apple)


        
        print(f"Bitcoin: {Bitcoin}\nNvidia: {Nvidia}\nApple: {Apple}\n_______________________________________________________\n")
        return Bitcoin, Nvidia, Apple

# Check if player has enough money to buy stock and if so purchase shares of the stock ... Returns money and purchase amount to be added to share variables
def buy_shares(stock_price,money):
        if money >= stock_price and money // stock_price != 0:
                share_amount = money//stock_price
                clear_terminal()
                
                while True:
                        purchase_amount = int(input(f"How much would you like to buy?\nYou can buy up to {share_amount} shares\nMoney: {money}\nStock Price: {stock_price}\n"))
                        if purchase_amount > 0 and purchase_amount <= share_amount:
                                money -= (purchase_amount * stock_price)
                                print("Remaing Balance: ",money)
                                return money, purchase_amount
                        else:
                                print("Not valid amount")

        else:
                print("Not enough Money for this Stock!")
                return None             
                         

def random_event(Bitcoin_shares, Apple_shares, Nvidia_shares):
        randomizer = random.randint(1,10)
        if randomizer > 8:
                # Good Event
                Bitcoin_shares = math.floor(Bitcoin_shares * 1.75)
                Apple_shares = math.floor(Apple_shares * 1.75)
                Nvidia_shares = math.floor(Nvidia_shares * 1.75)
        
        elif randomizer > 5 and randomizer <= 8:
                # Good Event
                Bitcoin_shares = math.floor(Bitcoin_shares * 1.25)
                Apple_shares = math.floor(Apple_shares * 1.25)
                Nvidia_shares = math.floor(Nvidia_shares * 1.25)
        
        elif randomizer > 2 and randomizer <=5:
                # Good Event
                Bitcoin_shares = math.floor(Bitcoin_shares * .75)
                Apple_shares = math.floor(Apple_shares * .75)
                Nvidia_shares = math.floor(Nvidia_shares * .75)
        
        elif randomizer >=1  and randomizer <=2:
                # Good Event
                Bitcoin_shares = math.floor(Bitcoin_shares * .50)
                Apple_shares = math.floor(Apple_shares * .50)
                Nvidia_shares = math.floor(Nvidia_shares * .50)
        
        
        else:
                # Bad Event
                Bitcoin_shares = math.floor(Bitcoin_shares * .10)
                Apple_shares = math.floor(Apple_shares * .10)
                Nvidia_shares = math.floor(Nvidia_shares * .10)
        
        return Bitcoin_shares, Apple_shares, Nvidia_shares

def sell_shares(stock_input, money, amount_of_shares, total_amount_of_shares):
        money += (amount_of_shares * stock_input)
        total_amount_of_shares -= amount_of_shares
        return money, total_amount_of_shares

def hold_stock():
        Bitcoin, Nvidia, Apple = set_values()

def main():
        money = 5000
        Bitcoin_shares = 0
        Nvidia_shares = 0
        Apple_shares = 0
        Bitcoin = 0
        Nvidia = 0
        Apple = 0
        
        

        while True:
                Bitcoin, Nvidia, Apple = set_values() 
                print(f"Bitcoin Shares: {Bitcoin_shares}\nNvidia Shares: {Nvidia_shares}\nApple Shares: {Apple_shares}\n_______________________________________________________\n")
                print(F"MONEY: {money}\n_______________________________________________________\n")
                menu_input = int(input("What would you like to do next?\n1: Buy Stock\n2: Sell Stock\n3: Hold Stock\n"))
                match menu_input:
                        #BUY OPTION
                        case 1:
                                clear_terminal()
                                print(f"Bitcoin: {Bitcoin}\nNvidia: {Nvidia}\nApple: {Apple}\n_______________________________________________________\n")

                                
                                while True:
                                        stock_input =  int(input(f"What stock would you like to buy?\n\nAvailable Money: {money}\n\n1:Bitcoin: {Bitcoin}\n2:Nvidia: {Nvidia}\n3:Apple: {Apple}\n"))
                                        match stock_input:
                                                case 1:
                                                        stock_input = Bitcoin
                                                        break
                                                case 2:
                                                        stock_input = Nvidia
                                                        break
                                                case 3: 
                                                        stock_input =  Apple
                                                        break
                                                case _:
                                                        print("Invalid Input\n")

                
                                result = buy_shares(stock_input, money)
                                if result is not None:
                                        money, purchase_amount = result
                                        if stock_input == Bitcoin:
                                                Bitcoin_shares +=purchase_amount
                                                
                                        elif stock_input == Nvidia:
                                                Nvidia_shares += purchase_amount
                                                
                                        elif stock_input == Apple:
                                                Apple_shares += purchase_amount
                                                
                                        else:
                                                print("Something Went Wrong Contact Gizmo")
                                        print(f"Bitcoin Shares: {Bitcoin_shares}\nNvidia Shares: {Nvidia_shares}\nApple Shares: {Apple_shares}\n")

                                
                        # SELL OPTION
                        case 2:
                                if Bitcoin_shares > 0 or Nvidia_shares > 0 or Apple_shares > 0:
                                        while True:
                                                stock_input = int(input(f"What stock would you like to sell?\n1:Bitcoin: {Bitcoin}\n2:Nvidia: {Nvidia}\n3:Apple: {Apple}\n"))
                                                match stock_input:
                                                        case 1:
                                                                if Bitcoin_shares > 0:
                                                                        stock_input = Bitcoin
                                                                        total_amount_of_shares = Bitcoin_shares
                                                                        break
                                                                else:
                                                                        print("You don't have any Bitcoin shares!")
                                                                        continue
                                                        
                                                        case 2:
                                                                if Nvidia_shares > 0:
                                                                        stock_input = Nvidia
                                                                        total_amount_of_shares = Nvidia_shares
                                                                        break
                                                                else:
                                                                        print("You don't have any Nvidia shares!")
                                                                        continue
                                                                        
                                                        case 3:
                                                                if Apple_shares > 0:
                                                                        stock_input = Apple
                                                                        total_amount_of_shares = Apple_shares
                                                                        break
                                                                else:
                                                                        print("You don't have any Apple shares!")
                                                                        continue
                                                                        
                                                        case _:
                                                                print("Invalid Input\n")

                                        while True:
                                                amount_to_sell = int(input(f"How much would you like to sell?\n\n1:Bitcoin: {Bitcoin_shares}\n2:Nvidia: {Nvidia_shares}\n3:Apple: {Apple_shares}\n"))
                                                if amount_to_sell <= total_amount_of_shares:
                                                        money, total_amount_of_shares = sell_shares(stock_input, money, total_amount_of_shares, amount_to_sell)
                                                        if stock_input == Bitcoin:
                                                                 Bitcoin_shares = total_amount_of_shares
                                                                 break
                                                        elif stock_input == Nvidia:
                                                                 Nvidia_shares = total_amount_of_shares
                                                                 break
                                                        elif stock_input == Apple:
                                                                 Apple_shares = total_amount_of_shares
                                                                 break
                                                else:
                                                        print("That is more than you currently have!")
                                        print(f"Share Balance:\nBitcoin: {Bitcoin_shares}\nNvidia: {Nvidia_shares}\nApple: {Apple_shares}")
                                        print("Your Money Balance:", money)
                                        Bitcoin, Nvidia, Apple = set_values()

                                else:
                                        print("You don't have any shares!\n")

                        #HOLD OPTION
                        case 3:
                                hold_stock()
                                Bitcoin_shares, Apple_shares, Nvidia_shares = random_event(Bitcoin_shares,Apple_shares,Nvidia_shares)
                                print(Bitcoin_shares, Apple_shares, Nvidia_shares)

                                
                        case _:
                                print("Invalid Input\n")
main()