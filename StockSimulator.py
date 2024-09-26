import random
import time

# Bitcoin Range(0,70000)
# Apple Range(0,250)
# Nvidia Range(0,1000)
# Randomizes the Stocks Price

def set_values():
        Bitcoin = random.randint(1,70001)
        Bitcoin = round(Bitcoin)
         
        Nvidia = random.randint(1,251)
        Nvidia = round(Nvidia)
    
        Apple = random.randint(1, 1001)
        Apple = round(Apple)

        print(f"Apple: {Apple} \nNvidia: {Nvidia}\nBitcoin: {Bitcoin}\n")
        return Bitcoin, Nvidia, Apple

# Check if player has enough money to buy stock and if so purchase shares of the stock ... Returns money and purchase amount to be added to share variables
def buy_shares(stock_price,money):
        if money >= stock_price and money // stock_price != 0:
                share_amount = money//stock_price
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
                                
def random_event():
        pass

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
        
        Bitcoin, Nvidia, Apple = set_values()

        while True:
                
                menu_input = int(input("What would you like to do next?\n1: Buy Stock\n2: Sell Stock\n3: Hold Stock\n"))
                match menu_input:
                        #BUY OPTION
                        case 1:
                                
                                while True:
                                        stock_input =  int(input("What stock would you like to buy?\n1:Bitcoin\n2:Nvidia\n3:Apple\n"))
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

                
                                money, purchase_amount = buy_shares(stock_input, money)
                                
                                if stock_input == Bitcoin:
                                        Bitcoin_shares +=purchase_amount
                                        
                                elif stock_input == Nvidia:
                                        Nvidia_shares += purchase_amount
                                        
                                elif stock_input == Apple:
                                        Apple_shares += purchase_amount
                                        
                                else:
                                        print("Something Went Wrong Contact Gizmo")
                                print("Bitcoin Shares", Bitcoin_shares,"\n")
                                print("Nvidia Shares", Nvidia_shares,"\n")
                                print("Apple Shares", Apple_shares,"\n")
                                Bitcoin, Nvidia, Apple = set_values()
                                
                        # SELL OPTION
                        case 2:
                                if Bitcoin_shares > 0 or Nvidia_shares > 0 or Apple_shares > 0:
                                        while True:
                                                stock_input = int(input("What stock would you like to sell?\n1: Bitcoin\n2: Nvidia\n3: Apple\n"))
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
                                                amount_to_sell = int(input("How much would you like to sell?\n"))
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

                
                        case 3:
                                
                                hold_stock()
                                
                        case _:
                                print("Invalid Input\n")
main()