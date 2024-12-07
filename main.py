import tkinter as tk
from tkinter import *
from tkinter import messagebox
from stocks import *
from player import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygame
import time







class StockTradingGUI:
    global click
    global door_knocking_angry
    global shotgun_bang
    global shotgun_reload
    global walking_away
    global walking_towards
    global door_opening
    



    pygame.mixer.init()
    pygame.init()
    # Audio Sounds
    door_knocking_angry = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Door Banging.MP3")
    stomping_away = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Walking Away).MP3")
    stomping_towards = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Walking Towards.MP3")
    # loud_knocking = pygame.mixer.Sound(r"C:\Users\isori\Downloads\loud-knocking-banging-interior-room-door-30549.mp3")
    light_noise = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Light Noise.MP3")
    start_up_light = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Start Up Light.MP3")
    door_handle = pygame.mixer.Sound(r"C:\Users\isori\Downloads\door-handle2-86523.mp3")
    basement_door_slam = pygame.mixer.Sound(r"C:\Users\isori\Downloads\basement-door-slam-257729.mp3")
    mouse_squeak = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Mouse Squeak.MP3")
    click = pygame.mixer.Sound(r"C:\Users\isori\Downloads\clickmouse-266516.mp3")
    shotgun_bang = pygame.mixer.Sound(r"C:\Users\isori\Downloads\ShotgunBang.MP3") 
    shotgun_reload = pygame.mixer.Sound(r"C:\Users\isori\Downloads\ShotgunReload.MP3")
    walking_towards =  pygame.mixer.Sound(r"C:\Users\isori\Downloads\WalkingTowards.MP3")
    walking_away =  pygame.mixer.Sound(r"C:\Users\isori\Downloads\WalkingAway.MP3")
    door_opening =  pygame.mixer.Sound(r"C:\Users\isori\Downloads\OpeningDoor.MP3")

    
    def __init__(self, root):
        self.root = root

         # Set the window size to the screen size
        self.root.attributes("-fullscreen", True)  # Set fullscreen mode
        self.root.bind("<Escape>", self.toggle_fullscreen)  # Bind Escape key to toggle fullscreen mode
           
        self.black_background = tk.Frame(self.root, bg="black")
        self.black_background.place(relwidth=1, relheight=1)  # Cover the entire screen
        self.root.update()  # Force the GUI to render the black background

        time.sleep(2)

        

       
        pygame.mixer.init()
        pygame.init()

        self.root.title("Stock Trading Game")
        self.player = Player()
        self.difficulty = 100
        self.rent = 0
        self.turn = 0
        self.previous_stock_prices = {stock.name: stock.price for stock in get_stocks()}

        # Audio Sounds
        door_knocking_angry = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Door Banging.MP3")
        stomping_away = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Walking Away).MP3")
        stomping_towards = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Walking Towards.MP3")
        # loud_knocking = pygame.mixer.Sound(r"C:\Users\isori\Downloads\loud-knocking-banging-interior-room-door-30549.mp3")
        light_noise = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Light Noise.MP3")
        start_up_light = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Start Up Light.MP3")
        door_handle = pygame.mixer.Sound(r"C:\Users\isori\Downloads\door-handle2-86523.mp3")
        basement_door_slam = pygame.mixer.Sound(r"C:\Users\isori\Downloads\basement-door-slam-257729.mp3")
        mouse_squeak = pygame.mixer.Sound(r"C:\Users\isori\Downloads\Mouse Squeak.MP3")
        click = pygame.mixer.Sound(r"C:\Users\isori\Downloads\clickmouse-266516.mp3")
        background_noise = pygame.mixer.Sound(r"C:\Users\isori\Downloads\scary-ambience-59002.mp3")
        dripping_sound = pygame.mixer.Sound(r"C:\Users\isori\Downloads\drops-in-a-underground-parking-24705.mp3")
        
        



        # Path to the background image
        image_path = r"C:\Users\isori\Downloads\DALL·E 2024-11-19 11.56.37 - A highly detailed illustration of a secret underground lair with a dimly lit atmosphere. The perspective is at the level of the back of a hooded figur.png"

        try:
            # Load and resize the image
            bg_image_raw = Image.open(image_path)
            bg_image_resized = bg_image_raw.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(bg_image_resized)

            # Create a Label widget to hold the image (make it a class attribute)
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)  # Ensure the image fills the entire window
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None 
            self.bg_label = None

        
        basement_door_slam.play()
        stomping_away.play()
        start_up_light.play()
        light_noise.play()
        mouse_squeak.play()
        background_noise.play(loops=-1)
        dripping_sound.play(loops=-1)

        
        self.main_menu()


    def main_menu(self):
        #self.clear_window()
       
        # Display balance information with commas
        balance_label = tk.Label(
        self.root, 
        text=f"Balance: ${self.player.balance:,.2f}",  # Format balance with commas
        width=31, 
        bg='black', 
        fg='green', 
        relief=SUNKEN, 
        borderwidth=10, 
        font=("Arial", 14)
        )
        balance_label.place(relx=.425, rely=.13)

        
        # Display rent information (initialize self.rent_label)
        self.rent_label = tk.Label(self.root, text=f"Current Rent: ${self.rent}",bg='black', fg='red',relief=GROOVE, borderwidth=3, font=("Arial", 14))
        self.rent_label.place(relx=.45, rely=.175)

        # Menu options
        tk.Button(self.root, text="Check Transaction History", command=self.check_transaction_history, width=22, bg="black", fg="grey", font=("System", 12),   borderwidth=3).place(relx= .33, rely=.444)
        tk.Button(self.root, text="Buy Stock", command=self.display_stocks_for_buying, width=18, bg="green", fg="black", font=("System", 12),  borderwidth=3).place(relx=.34, rely=.15)
        tk.Button(self.root, text="Sell Stock", command=self.display_stocks_for_selling, width=18,bg="red", fg="black", font=("System", 12), borderwidth=3).place(relx= .68, rely= .15)
        tk.Button(self.root, text="Next Turn", command=self.next_turn, width=20, bg="black", fg="grey", font=("System", 12),  borderwidth=3).place(relx=.7, rely=.85)
        tk.Button(self.root, text="Check Shares Owned", command=self.get_stock_shares, width=18, bg="black", fg="grey", font=("System", 12),  borderwidth=3).place(relx=.60, rely=.44)
        tk.Button(self.root, text="File For Bankruptcy", command=self.quit, width=30, bg="black", fg="red", font=("System", 12),  borderwidth=3).place(relx=.12, rely=.6)
    
    def quit(self):
        # Ask for confirmation before quitting
        door_knocking_angry.play()

        result = messagebox.askyesno("Exit Game", "Are you sure you sure about this?")
        if result:  # If user clicks 'Yes'
            self.black_background = tk.Frame(self.root, bg="black")
            self.black_background.place(relwidth=1, relheight=1)  # Cover the entire screen
            self.root.update()  # Force the GUI to render the black background
            door_opening.play()
            time.sleep(3)
            walking_towards.play()
            time.sleep(3)
            shotgun_reload.play()
            time.sleep(3)
            shotgun_bang.play()
            time.sleep(.5)
            tk.Label(self.root, text = "You died").pack()
            time.sleep(3)
            root.quit()

            self.root.quit()  # Close the window
        else:
            return  # If user clicks 'No', do nothing

    
    
    def toggle_fullscreen(self, event=None):
        current_state = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not current_state)
        return "break"  # Prevents the default event handler


    def check_transaction_history(self):
        if self.player.transaction_history:
            history = "\n".join([f"{transaction['action']} {transaction['shares']} shares of {transaction['stock']} at ${transaction['price']} per share" for transaction in self.player.transaction_history])
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions made yet.")
    
    def display_stocks_for_buying(self):
        print("Displaying stocks for buying...")
        self.clear_window()
        tk.Label(self.root, text="Click on a stock to buy shares", width=25, bg='white', borderwidth=5, font=("System", 18)).pack(pady=10)
        stocks = get_stocks()

        for stock in stocks:
            # Calculate the percentage change
            mean_price = stock.mean  # Use the mean here
            price_difference = stock.price - mean_price
            percentage_change = (price_difference / mean_price) * 100
            
            # Determine text color based on percentage change
            if percentage_change > 0:
                change_text = (
                    f"{stock.name}: ${stock.price:.2f} "
                    f"[{'+' if percentage_change > 0 else ''}{percentage_change:.2f}%]"
                )
                color = 'green'  # Positive percentage = green text
            else:
                change_text = (
                    f"{stock.name}: ${stock.price:.2f} "
                    f"[{'+' if percentage_change > 0 else ''}{percentage_change:.2f}%]"
                )
                color = 'red'  # Negative percentage = red text

            # Display stock button with the determined color
            stock_button = tk.Button(self.root, text=change_text, command=lambda s=stock: self.buy_stock(s), fg=color, width=25, bg='black', borderwidth=5, font=("System", 18))
            stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", width=25, bg='black', borderwidth=5, fg='red', font=("System", 18), command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=20)

    def buy_stock(self, stock):
        self.clear_window()
        median_price = stock.mean
        price_difference = stock.price - median_price
        percentage_change = (price_difference / median_price) * 100

        tk.Label(
            self.root,
            text=f"Buying {stock.name} - ${stock.price:.2f} "
                f"{'+' if percentage_change > 0 else ''}( {percentage_change:.2f}% )",
             width=25, bg='black', borderwidth=5, font=("System", 18), fg='white'
        ).pack(pady=20)

        max_shares = int(self.player.balance // stock.price)
        tk.Label(self.root, text="Select number of shares to buy:",width=25, bg='black', borderwidth=5, fg='white', font=("System", 18)).pack()

        shares_slider = tk.Scale(self.root, from_=1, to=max_shares, orient=tk.HORIZONTAL, width=25, bg='black', borderwidth=10, fg='white', font=("System", 18))
        shares_slider.pack(pady=10)

        # Show dynamic cost as slider value changes
        cost_label = tk.Label(self.root, width=25, bg='black', borderwidth=5, fg='white', font=("System", 18), text=f"Total Cost: ${shares_slider.get() * stock.price:.2f}")
        cost_label.pack(pady=10)

        def update_cost_label(event):
            cost_label.config(text=f"Total Cost: ${shares_slider.get() * stock.price:.2f}")

        shares_slider.bind("<Motion>", update_cost_label)

        # Only one "Confirm Purchase" and "Back to Menu" button
        tk.Button(self.root, text="Confirm Purchase", width=25, bg='black', borderwidth=5, fg='green', font=("System", 18), command=lambda: [self.process_purchase(stock, shares_slider.get()), self.clear_window(), self.main_menu()]).pack(pady=10)
        tk.Button(self.root, text="Back to Menu", width=25, bg='black', borderwidth=5, fg='red', font=("System", 18),  command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

    def process_purchase(self, stock, shares):
        try:
            shares = int(shares)
            total_cost = shares * stock.price

            if self.player.balance >= total_cost:
                stock_name = stock.name.lower()  # Ensure the name is stored in lowercase
                self.player.owned_stocks[stock_name] = self.player.owned_stocks.get(stock_name, 0) + shares
                self.player.balance -= total_cost
                self.player.record_transaction(stock_name, shares, stock.price, "Buy")
                
                

            else:
                messagebox.showerror("Error", "Insufficient funds.")

            self.main_menu()
        except ValueError:
            messagebox.showerror("Error", "Please select a valid number of shares.")
    
    



    def display_stocks_for_selling(self):
        self.clear_window()

        # Get a list of stocks that the player owns
        owned_stocks = [
            stock for stock in get_stocks()  # Assuming get_stocks() returns a list of all available stocks
            if self.player.owned_stocks.get(stock.name.lower(), 0) > 0  # Ensure lowercase name lookup for owned stocks
        ]

        if not owned_stocks:
            messagebox.showinfo("No Stocks Owned", "You don't own any stocks to sell.")
            self.main_menu()
            return

        tk.Label(self.root, width=25, bg='black', borderwidth=5, fg='white', font=("System", 18), text="Select a stock to sell:").pack(pady=10)

        # Create buttons for each owned stock
        for stock in owned_stocks:
            stock_name = stock.name.lower()
            quantity_owned = self.player.owned_stocks.get(stock_name, 0)

            # Calculate the average buy price from transaction history
            transactions = [
                t for t in self.player.transaction_history 
                if t['stock'] == stock_name and t['action'] == 'Buy'
            ]
            if transactions:
                total_cost = sum(t['shares'] * t['price'] for t in transactions)
                total_shares = sum(t['shares'] for t in transactions)
                avg_purchase_price = total_cost / total_shares

                # Calculate percentage change
                price_difference = stock.price - avg_purchase_price
                percentage_change = (price_difference / avg_purchase_price) * 100

                # Determine text color based on percentage change
                if percentage_change > 0:
                    color = 'green'  # Positive percentage = green text
                else:
                    color = 'red'  # Negative percentage = red text

                # Display stock info with percentage change and color
                stock_button = tk.Button(
                    self.root,
                    text=(
                        f"{stock.name}: {quantity_owned} shares "
                        f"@ ${stock.price:.2f} (Avg Buy: ${avg_purchase_price:.2f}) "
                        f"[{'+' if percentage_change > 0 else ''}{percentage_change:.2f}%]"
                    ),
                    width=55, bg='black', borderwidth=5, fg='white', font=("System", 18), 
                    command=lambda s=stock: self.sell_stock(s)
                )
                stock_button.config(fg=color)  # Set the color of the percentage change text
                stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", width=25, bg='black', borderwidth=5, fg='white', font=("System", 18), command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=20)





    def sell_stock(self, stock):
        self.clear_window()

        stock_name = stock.name.lower()
        
        # Check if the player owns this stock
        if stock_name in self.player.owned_stocks:
            owned_shares = self.player.owned_stocks[stock_name]

            # Ensure the slider is set with the correct maximum number of shares
            if owned_shares > 0:
                tk.Label(self.root, text=f"Sell {stock.name} - Current Price: ${stock.price:.2f}").pack(pady=10)
                tk.Label(self.root, text=f"You own {owned_shares} shares").pack()

                # Create a slider with the max value as the owned shares
                shares_slider = tk.Scale(self.root, from_=0, to=owned_shares, orient=tk.HORIZONTAL)
                shares_slider.pack(pady=20)

                # Display dynamic revenue as slider moves
                revenue_label = tk.Label(self.root, text=f"Total revenue: $0.00")
                revenue_label.pack(pady=10)

                def update_revenue(event):
                    selected_shares = shares_slider.get()
                    total_revenue = selected_shares * stock.price
                    revenue_label.config(text=f"Total revenue: ${total_revenue:.2f}")

                shares_slider.bind("<Motion>", update_revenue)

                # Add confirm sale button
                tk.Button(self.root, text="Confirm Sale", command=lambda: [self.process_sell(stock, shares_slider.get(), shares_slider), self.clear_window(), self.main_menu()]).pack(pady=10)

                # Add back to menu button
                tk.Button(self.root, text="Back to Menu", command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

            else:
                messagebox.showinfo("No Shares", "You don't have any shares of this stock to sell.")
                self.main_menu()
        else:
            tk.Label(self.root, text="You don't own this stock.").pack(pady=20)
            tk.Button(self.root, text="Back to Menu", command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)



    
    def sell_stock_shares(self, stock):
        self.clear_window()

        # Get the number of shares the player owns
        owned_shares = self.player.owned_stocks.get(stock.name, 0)
        if owned_shares == 0:
            messagebox.showerror("Error", "You don't own any shares of this stock.")
            self.main_menu()
            return

        # Show stock and revenue details
        tk.Label(self.root, text=f"Selling {stock.name} - ${stock.price:.2f} per share", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"You own {owned_shares} shares.").pack()

        # Dynamic revenue label
        revenue_label = tk.Label(self.root, text=f"Total revenue: ${stock.price:.2f}")
        revenue_label.pack(pady=10)

        # Slider for selecting shares to sell (set maximum value to owned_shares)
        shares_slider = tk.Scale(self.root, from_=0, to=owned_shares, orient=tk.HORIZONTAL)
        
        # Update the revenue label dynamically as the slider changes
        def update_revenue(event):
            selected_shares = shares_slider.get()
            total_revenue = selected_shares * stock.price
            revenue_label.config(text=f"Total revenue: ${total_revenue:.2f}")

        shares_slider.bind("<Motion>", update_revenue)
        shares_slider.pack(pady=10)

        # Button to confirm the sale, passing the slider value as the number of shares to sell
        tk.Button(self.root, text="Confirm Sale",
                command=lambda: self.process_sell(stock, shares_slider.get(), shares_slider)).pack(pady=10)

        # Back to main menu button
        tk.Button(self.root, text="Back to Menu", command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

    def process_sell(self, stock, shares_to_sell, shares_slider):
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

                # Update the share slider maximum and reset it to 0 (since you sold shares)
                new_max = self.player.owned_stocks.get(stock.name, 0)
                shares_slider.config(to=new_max)
                shares_slider.set(0)  # Reset the slider to 0 after sale
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
        
        
        # Update rent label
        self.rent_label.config(text=f"Current Rent: ${self.rent}")
        # Update stock prices for the new turn
        stocks = get_stocks()
        for stock in stocks:
            stock.value_changer()

        # Update previous prices to track changes
        self.previous_stock_prices = {stock.name: stock.price for stock in stocks}

        # Check if balance is negative
        if self.player.balance < 0:
            answer = messagebox.askokcancel("Warning", "Your rent is higher than your balance! Continue?")
            if answer:  # If user clicks 'Yes'
                messagebox.showerror("Game Over", "You ran out of funds.")
                self.root.quit()  # Close the window
        else:
            self.main_menu()
            self.rent += self.difficulty  # Increment rent for the new turn


    def clear_window(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
        self.root.update_idletasks()  # Refresh GUI



# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = StockTradingGUI(root)
    root.mainloop()
