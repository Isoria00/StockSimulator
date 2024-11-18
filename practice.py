import tkinter as tk
from tkinter import *
from tkinter import messagebox
from stocks import *
from player import *

class StockTradingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Trading Game")
        self.player = Player()
        self.rent = 0
        self.turn = 0
        self.previous_stock_prices = {stock.name: stock.price for stock in get_stocks()}
        
        self.main_menu()

    def main_menu(self):
        self.clear_window()
        
        # Display balance and rent information
        balance_label = tk.Label(self.root, text=f"Balance: ${self.player.balance:.2f}", font=("Arial", 14))
        balance_label.pack(anchor="w", padx=10)
        
        rent_label = tk.Label(self.root, text=f"Current Rent: ${self.rent}", font=("Arial", 14))
        rent_label.pack(anchor="w", padx=10, pady=(0, 20))

        # Menu options
        tk.Button(self.root, text="Check Stock Prices", command=self.check_stock_price, width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Check Transaction History", command=self.check_transaction_history,width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Buy Stock", command=self.display_stocks_for_buying,width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Sell Stock", command=self.display_stocks_for_selling, width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Next Turn", command=self.next_turn,width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Check Shares Owned", command=self.get_stock_shares,width=30, borderwidth=3).pack(pady=5)
        tk.Button(self.root, text="Exit Game", command=self.root.quit,width=30, borderwidth=3).pack(pady=5)
        
    def check_stock_price(self):
        self.clear_window()
        
        tk.Label(self.root, text="Stock Prices (Compared to Your Purchase Price)", font=("Arial", 16)).pack(pady=10)

        stocks = get_stocks()
        for stock in stocks:
            # Get the price change compared to the purchase price (if owned)
            if stock.name in self.player.owned_stocks:
                transactions = [
                    t for t in self.player.transaction_history 
                    if t['stock'] == stock.name and t['action'] == 'Buy'
                ]
                if transactions:
                    total_cost = sum(t['shares'] * t['price'] for t in transactions)
                    total_shares = sum(t['shares'] for t in transactions)
                    avg_purchase_price = total_cost / total_shares
                    price_change = stock.price - avg_purchase_price
                    change_text = f"(+${price_change:.2f})" if price_change > 0 else f"(-${abs(price_change):.2f})"
                    tk.Label(
                        self.root, 
                        text=f"{stock.name}: ${stock.price:.2f} (Avg Purchase Price: ${avg_purchase_price:.2f}) {change_text}",
                        font=("Arial", 12)
                    ).pack(anchor="w")
            else:
                # If not owned, compare to the previous turn's price
                previous_price = self.previous_stock_prices[stock.name]
                price_change = stock.price - previous_price
                change_text = f"(+${price_change:.2f})" if price_change > 0 else f"(-${abs(price_change):.2f})"
                tk.Label(self.root, text=f"{stock.name}: ${stock.price:.2f} {change_text}", font=("Arial", 12)).pack(anchor="w")
        
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=20)

    def check_transaction_history(self):
        if self.player.transaction_history:
            history = "\n".join([f"{transaction['action']} {transaction['shares']} shares of {transaction['stock']} at ${transaction['price']} per share" for transaction in self.player.transaction_history])
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions made yet.")
    
    def display_stocks_for_buying(self):
        print("Displaying stocks for buying...")
        self.clear_window()

        tk.Label(self.root, text="Click on a stock to buy shares", font=("Arial", 16)).pack(pady=10)
        stocks = get_stocks()

        for stock in stocks:
            # Calculate the percentage change
            mean_price = stock.mean  # Use the mean here
            price_difference = stock.price - mean_price
            percentage_change = (price_difference / mean_price) * 100
            change_text = (
                f"{stock.name}: ${stock.price:.2f} (Mean: ${mean_price:.2f}) "
                f"[{'+' if percentage_change > 0 else ''}{percentage_change:.2f}%]"
            )

            # Display stock button with percentage change
            stock_button = tk.Button(self.root, text=change_text, command=lambda s=stock: self.buy_stock(s))
            stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=20)

    def buy_stock(self, stock):
        self.clear_window()

        median_price = stock.mean
        price_difference = stock.price - median_price
        percentage_change = (price_difference / median_price) * 100

        tk.Label(
            self.root,
            text=f"Buying {stock.name} - ${stock.price:.2f} (Median: ${median_price:.2f}, "
                f"{'+' if percentage_change > 0 else ''}{percentage_change:.2f}%)",
            font=("Arial", 16)
        ).pack(pady=20)

        max_shares = int(self.player.balance // stock.price)
        tk.Label(self.root, text="Select number of shares to buy:").pack()

        shares_slider = tk.Scale(self.root, from_=1, to=max_shares, orient=tk.HORIZONTAL)
        shares_slider.pack(pady=10)

        # Show dynamic cost as slider value changes
        cost_label = tk.Label(self.root, text=f"Total Cost: ${shares_slider.get() * stock.price:.2f}")
        cost_label.pack(pady=10)

        def update_cost_label(event):
            cost_label.config(text=f"Total Cost: ${shares_slider.get() * stock.price:.2f}")

        shares_slider.bind("<Motion>", update_cost_label)

        # Only one "Confirm Purchase" and "Back to Menu" button
        tk.Button(self.root, text="Confirm Purchase", command=lambda: self.process_purchase(stock, shares_slider.get())).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

    def process_purchase(self, stock, shares):
        try:
            shares = int(shares)
            total_cost = shares * stock.price

            if self.player.balance >= total_cost:
                stock_name = stock.name.lower()  # Ensure the name is stored in lowercase
                self.player.owned_stocks[stock_name] = self.player.owned_stocks.get(stock_name, 0) + shares
                self.player.balance -= total_cost
                self.player.record_transaction(stock_name, shares, stock.price, "Buy")
                messagebox.showinfo("Purchase Success", f"Bought {shares} shares of {stock.name}.")
                print(f"Owned stocks after purchase: {self.player.owned_stocks}")  # Print the dictionary for debugging
            else:
                messagebox.showerror("Error", "Insufficient funds.")

            self.main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please select a valid number of shares.")


    def display_stocks_for_selling(self):
        self.clear_window()

        # Get a list of stocks that the player owns
        owned_stocks = [
            stock for stock in get_stocks()
            if self.player.owned_stocks.get(stock.name.lower(), 0) > 0  # Ensure lowercase name lookup
        ]

        if not owned_stocks:
            messagebox.showinfo("No Stocks Owned", "You don't own any stocks to sell.")
            self.main_menu()
            return

        tk.Label(self.root, text="Select a stock to sell:", font=("Arial", 16)).pack(pady=10)

        # Create buttons for each owned stock
        for stock in owned_stocks:
            stock_button = tk.Button(self.root, text=f"{stock.name}: {self.player.owned_stocks.get(stock.name.lower(), 0)} shares",  # Ensure lowercase lookup
                                    command=lambda s=stock: self.sell_stock(s))
            stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=20)


    def sell_stock(self, stock):
        self.clear_window()

        # Ensure you're comparing the stock name in lowercase
        stock_name = stock.name.lower()

        # Check if the player owns this stock
        if stock_name in self.player.owned_stocks:
            # Get the transaction history for this stock
            transactions = [
                t for t in self.player.transaction_history 
                if t['stock'] == stock_name and t['action'] == 'Buy'
            ]
            
            if transactions:
                # Calculate the total cost and number of shares bought
                total_cost = sum(t['shares'] * t['price'] for t in transactions)
                total_shares = sum(t['shares'] for t in transactions)
                
                # Calculate the average purchase price
                avg_purchase_price = total_cost / total_shares

                # Calculate the potential profit if selling at current price
                potential_profit = (stock.price - avg_purchase_price) * total_shares
                profit_text = f"Potential Profit: {'+' if potential_profit > 0 else ''}${potential_profit:.2f}"

                # Display stock information along with potential profit
                tk.Label(
                    self.root,
                    text=f"Sell {stock.name} - Current Price: ${stock.price:.2f} (Avg Purchase Price: ${avg_purchase_price:.2f})\n{profit_text}",
                    font=("Arial", 16)
                ).pack(pady=20)
                
                # Ask for the number of shares to sell
                max_shares = total_shares
                tk.Label(self.root, text="Select number of shares to sell:").pack()

                shares_slider = tk.Scale(self.root, from_=1, to=max_shares, orient=tk.HORIZONTAL)
                shares_slider.pack(pady=10)

                # Show dynamic profit as slider value changes
                profit_label = tk.Label(self.root, text=f"Potential Profit: ${shares_slider.get() * (stock.price - avg_purchase_price):.2f}")
                profit_label.pack(pady=10)

                # Update the profit label dynamically as slider value changes
                def update_profit_label(event):
                    profit_label.config(text=f"Potential Profit: ${shares_slider.get() * (stock.price - avg_purchase_price):.2f}")

                shares_slider.bind("<Motion>", update_profit_label)

                # Button to confirm the sell
                tk.Button(self.root, text="Confirm Sell", command=lambda: self.process_sell(stock, shares_slider.get())).pack(pady=10)
                tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)
            else:
                # If no transaction history for the stock, show a message
                tk.Label(self.root, text="You haven't bought this stock yet.").pack(pady=20)
                tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)
        else:
            # If the player doesn't own this stock
            tk.Label(self.root, text="You don't own this stock.").pack(pady=20)
            tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)


    
    def sell_stock_shares(self, stock):
        self.clear_window()

        owned_shares = self.player.owned_stocks.get(stock.name, 0)
        if owned_shares == 0:
            messagebox.showerror("Error", "You don't own any shares of this stock.")
            self.main_menu()
            return

        tk.Label(self.root, text=f"Selling {stock.name} - ${stock.price:.2f} per share", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"You own {owned_shares} shares.").pack()

        # Dynamic revenue label
        revenue_label = tk.Label(self.root, text=f"Total revenue: ${stock.price:.2f}")
        revenue_label.pack(pady=10)

        # Slider for selecting shares to sell
        shares_slider = tk.Scale(self.root, from_=1, to=owned_shares, orient=tk.HORIZONTAL)

        def update_revenue(event):
            total_revenue = shares_slider.get() * stock.price
            revenue_label.config(text=f"Total revenue: ${total_revenue:.2f}")

        shares_slider.bind("<Motion>", update_revenue)
        shares_slider.pack(pady=10)

        tk.Button(self.root, text="Confirm Sale",
                command=lambda: self.process_sale(stock, shares_slider.get())).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", command=self.main_menu).pack(pady=10)

    

    def process_sell(self, stock, shares_to_sell):
        try:
            # Ensure that the number of shares to sell is an integer
            shares_to_sell = int(shares_to_sell)
            
            # Check if the player owns enough shares to sell
            stock_name = stock.name.lower()
            owned_shares = self.player.owned_stocks.get(stock_name, 0)

            if owned_shares >= shares_to_sell and shares_to_sell > 0:
                # Update the owned shares: deduct the sold shares
                self.player.owned_stocks[stock_name] -= shares_to_sell

                # If the player has no more shares of this stock, remove it from the owned stocks
                if self.player.owned_stocks[stock_name] == 0:
                    del self.player.owned_stocks[stock_name]

                # Calculate revenue from the sale
                total_revenue = shares_to_sell * stock.price

                # Update the player's balance
                self.player.balance += total_revenue

                # Record the sale transaction (can be a 'Sell' type)
                self.player.record_transaction(stock.name, -shares_to_sell, stock.price, "Sell")

                # Show success message
                messagebox.showinfo("Sale Success", f"Sold {shares_to_sell} shares of {stock.name}.")
            else:
                # Handle the case where the player doesn't have enough shares to sell
                messagebox.showerror("Error", f"You do not own {shares_to_sell} shares of {stock.name}.")
        
        except ValueError:
            messagebox.showerror("Error", "Please select a valid number of shares to sell.")
        
        # Return to the main menu after processing the sale
        self.main_menu()


    def get_stock_shares(self):
        if self.player.owned_stocks:
            # Display stock names in lowercase to avoid case sensitivity issues
            shares = "\n".join([f"{stock}: {shares} shares" for stock, shares in self.player.owned_stocks.items()])
            messagebox.showinfo("Owned Stocks", shares)
        else:
            messagebox.showinfo("Owned Stocks", "You don't own any stocks.")

    def next_turn(self):
        self.turn += 1
        self.player.balance -= self.rent
        self.rent += 1
        

        # Update stock prices for the new turn
        stocks = get_stocks()
        for stock in stocks:
            stock.value_changer()

        # Update previous prices to track changes
        self.previous_stock_prices = {stock.name: stock.price for stock in stocks}

        # Check if balance is negative
        if self.player.balance < 0:
            messagebox.showerror("Game Over", "You ran out of funds.")
            self.root.quit()
        else:
            self.main_menu()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = StockTradingGUI(root)
    root.mainloop()
