import tkinter as tk
from tkinter import *
from tkinter import messagebox
from stocks import *
from player import *
from PIL import Image, ImageTk
import pygame
import time
import os
from achievements import update_player_progress
import json


def adjust_width(original_width, reference_width, current_width):
    width_ratio = current_width / reference_width
    return int(original_width * width_ratio)

def adjust_font_size(original_font_size, reference_width, current_width):
    
    # Calculate the width ratio
    width_ratio = current_width / reference_width
    # Adjust the font size based on the ratio
    adjusted_font_size = int(original_font_size * width_ratio)
    return adjusted_font_size




def get_asset_path(*path_parts):
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory where the script is located
    return os.path.join(script_dir, "assets", *path_parts)





class StockTradingGUI:
    
    # Made Pygame sounds Global scope

    global click
    
    global door_knocking_angry
    
    global shotgun_bang
    
    global shotgun_reload
    
    global walking_away
    
    global walking_towards
    
    global door_opening
    
    global basement_door_slam
    
    global stomping_away
    
    global start_up_light
    
    global light_noise
    
    global mouse_squeak
    
    global background_noise
    
    global dripping_sound
    
    global power_outage

    global door_knocking_angry_end_game
    
    global man_screaming



    
    pygame.mixer.init()     # Initialize Pygame Mixer 
    pygame.init()           # Initialize Pygame Library
    
   # Audio Sounds
    door_knocking_angry = pygame.mixer.Sound(get_asset_path("sounds", "door-knocking-angry-88120.MP3")) 
    door_knocking_angry_end_game = pygame.mixer.Sound(get_asset_path("sounds", "Door Banging.MP3"))
    stomping_away = pygame.mixer.Sound(get_asset_path("sounds", "WalkingAway.MP3")) 
    stomping_towards = pygame.mixer.Sound(get_asset_path("sounds", "Walking Towards.MP3")) 
    light_noise = pygame.mixer.Sound(get_asset_path("sounds", "Light Noise.MP3")) 
    start_up_light = pygame.mixer.Sound(get_asset_path("sounds", "Start Up Light.MP3"))  
    basement_door_slam = pygame.mixer.Sound(get_asset_path("sounds", "basement-door-slam-257729.mp3")) 
    mouse_squeak = pygame.mixer.Sound(get_asset_path("sounds", "Mouse Squeak.MP3")) 
    click = pygame.mixer.Sound(get_asset_path("sounds", "clickmouse-266516.mp3"))  
    shotgun_bang = pygame.mixer.Sound(get_asset_path("sounds", "Shot.MP3"))  
    shotgun_reload = pygame.mixer.Sound(get_asset_path("sounds", "ShotgunReload.MP3"))   
    walking_towards = pygame.mixer.Sound(get_asset_path("sounds", "WalkingTowards.MP3"))   
    walking_away = pygame.mixer.Sound(get_asset_path("sounds", "WalkingAway.MP3")) 
    door_opening = pygame.mixer.Sound(get_asset_path("sounds", "OpeningDoor.MP3"))
    power_outage = pygame.mixer.Sound(get_asset_path("sounds", "poweroutagesfx.MP3"))
    background_noise = pygame.mixer.Sound(get_asset_path("sounds", "scary-ambience-59002.MP3"))
    dripping_sound = pygame.mixer.Sound(get_asset_path("sounds", "drops-in-a-underground-parking-24705.MP3"))
    man_screaming = pygame.mixer.Sound(get_asset_path("sounds", "man_screaming.MP3"))



    
    def __init__(self, root):                                                           # Class Constructor 
        
        self.root = root                                                                # Main window of Tkinter GUI  
        self.root.attributes("-fullscreen", True)                                       # Set Window to fullscreen mode
        self.root.bind("<Escape>", self.toggle_fullscreen)                              # Binds Escape key to toggle fullscreen mode
           
        self.black_background = tk.Frame(self.root, bg="black")                         # Create black background to cover the entire window
        self.black_background.place(relwidth=1, relheight=1)            
        
        self.root.update()                                                              # Updates root window to apply changes
        
        self.root.title("Stock Trading Game")                                           # Title of the Window
        
        self.player = Player()                                                          # Initialize player settings (found in player.py)
        self.difficulty = 500                                                           # This is the default difficulty of the game ($500 Rent increments per Turn)
        self.rent = 0                                                                   # Initialize default rent amount
        self.turn = 0                                                                   # Initialize turn 
        
        # self.previous_stock_prices = {stock.name: stock.price for stock in get_stocks()}            # Store previous stock prices
        
        self.difficulty_index = 1                                                       # Sets default difficulty index (This is for settings_menu() )
        self.difficulty_list = ['easy','medium','hard','insane','wall street warrior','crypto prodigy']                                 # Also for settings_menu()
        
            
        power_outage.play()                                                             # Plays power outage sound
        pygame.time.delay(int(power_outage.get_length() * 1000))                        # Wait for duration of sound before continuing
        dripping_sound.play(loops=-1)                                                   # Plays the dripping sound in a loop forever

        
        self.angry_upstair_debt_collector = False                                       # Flag for Angry Door knocking when rent is over or equal to 5000


        # Your reference screen width (e.g., for your monitor)
        self.reference_width = 1920

        # Get the current screen width dynamically
        self.current_width = self.root.winfo_screenwidth()

    

        


        
        self.show_pre_menu()                                                            # Calls show_pre_menu function        

    

    def settings_menu(self):
        self.clear_window_settings()                                                    # Clears all widgets and leaves black background
        
        self.settings_frame = tk.Frame(self.root, bg='black')                           # Creates settings Frame
        self.settings_frame.place(relx=.5, rely=.5, anchor='center')
        
        difficulty_text = ["Easy", "Medium", "Hard", "Insane", "Wall Street Warrior", "Crypto Prodigy"][self.difficulty_index]             # Set Difficulty level
        
    

        self.difficulty_label = tk.Label(                                               # Difficulty Label 
            self.settings_frame, 
            text=f"Difficulty: {difficulty_text}",  
            fg='white', 
            width=25,
            bg='black', 
            borderwidth=5, 
            font=("System", 22)
        ).pack(pady=10) 

        tk.Button(                                                                      # Change difficulty button    
            self.settings_frame, 
            text="Change Difficulty", 
            command=lambda: self.change_difficulty(), 
            fg='white', 
            width=adjust_width(25, self.reference_width, self.current_width),
            bg='black', 
            borderwidth=5, 
            font=("System", 22)
        ).pack(pady=10) 

        tk.Button(                                                                      # Back Button
            self.settings_frame, 
            text="Back", 
            command=self.show_pre_menu, 
            fg='white', 
            width=adjust_width(25, self.reference_width, self.current_width),
            bg='black', 
            borderwidth=5, 
            font=("System", 22)
        ).pack(pady=10) 

    def change_difficulty(self):                                                        
        self.difficulty_index +=1                                                       # Increment Difficulty Index
        
        if self.difficulty_index == 6:                                                  # Set difficulty Based on Index
            self.difficulty_index = 0
        
        if self.difficulty_index == 0:
            self.difficulty = 150
        
        if self.difficulty_index == 1:
            self.difficulty = 300
        
        if self.difficulty_index == 2:
            self.difficulty = 500
        
        if self.difficulty_index == 3:
            self.difficulty = 750

        if self.difficulty_index == 4:
            self.difficulty = 1000

        if self.difficulty_index == 5:
            self.difficulty = 1500
        
    
        
        
        
        self.clear_window_settings()
        self.settings_menu()


    def achievements(self):
        
        self.clear_window_settings()

        
        self.frame = tk.Frame(self.root, bg='black')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        
        tk.Label(
            self.frame,
            text="Achievements",
            fg='white',
            bg='black',
            font=("System", 40)
        ).pack(pady=20)

        
        with open("achievements.json", "r") as file:
            data = json.load(file)
            achievements = data.get("achievements", [])

        
        container = tk.Frame(self.frame, bg="black")
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg="black", highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="black")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        
        for achievement in achievements:
           
            name = achievement.get("name", "Unknown")
            description = achievement.get("description", "No description available")
            earned = achievement.get("earned", False)

            
            status_color = "green" if earned else "red"
            status_text = "Earned" if earned else "Not Earned"

            
            achievement_frame = tk.Frame(scrollable_frame, bg="black", pady=5)
            achievement_frame.pack(fill="x", pady=5)

           
            tk.Label(
                achievement_frame,
                text=name,
                fg="white",
                bg="black",
                font=("System", 20, "bold")
            ).pack(anchor="w")

            
            tk.Label(
                achievement_frame,
                text=description,
                fg="white",
                bg="black",
                font=("System", 16)
            ).pack(anchor="w", padx=10)

            
            tk.Label(
                achievement_frame,
                text=status_text,
                fg=status_color,
                bg="black",
                font=("System", 14, "italic")
            ).pack(anchor="w", padx=10)

        
        tk.Button(
            self.frame,
            text="Back",
            command=self.show_pre_menu,
            fg='white',
            bg='black',
            font=("System", 18),
            borderwidth=3
        ).pack(pady=20)


        

    def show_pre_menu(self):

        
                                                                   
        self.frame = tk.Frame(self.root, bg='black')                                    # Create frame to hold buttons
        self.frame.place(relx=.5, rely=.5, anchor='center')                             # Center the frame in the window


        tk.Label(self.frame,                                                            # Game Title
                 text="STOCKSIMULATOR",
                 fg='white',
                 width=adjust_width(25, self.reference_width, self.current_width),
                 bg='black',
                 font=("System", 55)).pack(pady=20)
                

        
        tk.Button(                                                                      # Start Game Button
            self.frame, 
            text="Start Game", 
            command=lambda: (self.setup_main_background(), self.main_menu(), self.start_up_sounds()), 
            fg='white', 
            width=adjust_width(25, self.reference_width, self.current_width),
            bg='black', 
            borderwidth=5, 
            font=("System", 22)
        ).pack(pady=10)  

        tk.Button(                                                                      # Settings Button                                                                          
            self.frame, 
            text="Settings", 
            fg='white', 
            width=adjust_width(25, self.reference_width, self.current_width), 
            bg='black',
            command=self.settings_menu,
            borderwidth=5, 
            font=("System", 22)
        ).pack(pady=10) 

        tk.Button(                                                                      # 
            self.frame,     
            text="Achievements", 
            fg='white', 
            width=adjust_width(25, self.reference_width, self.current_width), 
            bg='black', 
            borderwidth=5, 
            font=("System", 22),
            command=self.achievements
            ).pack(pady=10)


        tk.Button(                                                                      # 
            self.frame,     
            text="Exit", 
            fg='red', 
            width=adjust_width(25, self.reference_width, self.current_width), 
            bg='black', 
            borderwidth=5, 
            font=("System", 22),
            command=quit
            ).pack(pady=10)
        
        



    def start_up_sounds(self):

        
        basement_door_slam.play()
        stomping_away.play()
        start_up_light.play()
        light_noise.play()
        mouse_squeak.play()
        
    
    
    
    def setup_main_background(self):
        

        image_path = get_asset_path("images", "DALL·E 2024-11-19 11.56.37 - A highly detailed illustration of a secret underground lair with a dimly lit atmosphere. The perspective is at the level of the back of a hooded figur.png")


        try:
           
            bg_image_raw = Image.open(image_path)
            bg_image_resized = bg_image_raw.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(bg_image_resized)

            
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)  
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.bg_image = None 
            self.bg_label = None



    # Check to see if player won

    def win_condition(self):
        
         
        player_data = {                                                                  # for acheviements                                                  
            'difficulty': self.difficulty, 
            'win': True,  
            'win_game': True,  
              
        }

        
        from achievements import update_player_progress
        update_player_progress(player_data)
            
            
            
            
            
            
            
            
            
            
            
        
        
        
        self.clear_window()
        self.black_background = tk.Frame(self.root, bg="black")
        self.black_background.place(relwidth=1, relheight=1)  
        win_image_path = get_asset_path("images", 'DALL·E 2024-12-23 08.43.06 - A dramatic scene of someone emerging from a dark basement into freedom, with sunlight streaming in through an open door. The person is reaching toward.png')
        try:
            
            bg_image_raw = Image.open(win_image_path)
            bg_image_resized = bg_image_raw.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()))
            self.bg_image = ImageTk.PhotoImage(bg_image_resized)

            
            self.bg_label = tk.Label(self.root, image=self.bg_image)
            self.bg_label.place(relwidth=1, relheight=1)  
        except FileNotFoundError:
            print(f"Error: Image not found at {win_image_path}")
            self.bg_image = None


                                                                                                                
        self.win_message = tk.Label(                                                                    # Display the win message
        self.root, 
        fg='red', 
        text='You Survived',
        width=adjust_width(25, self.reference_width, self.current_width),
        bg='black',
        borderwidth=5, 
        font=("System", 22)
    )
        self.win_message.pack(side="top", anchor="n", pady=20) 


        tk.Button(
            self.root, 
            text="Main Menu", 
            fg='red', 
            width=adjust_width(25, self.reference_width, self.current_width),
            bg='black', 
            borderwidth=5, 
            font=("System", 22),
            command=lambda: (self.clear_window_settings(), self.show_pre_menu())
            ).pack(pady=10, anchor='s', side="bottom")
        
        self.player = Player()
        self.difficulty = 500
        self.rent = 0
        self.turn = 0
       
        
        

    def main_menu(self):
       
        if self.player.balance >=1000000:
            tk.Button(self.root, text="Pay Your Debt", command=self.win_condition, width=adjust_width(18, self.reference_width, self.current_width), bg="green", fg="black", font=("System", 12),  borderwidth=3).place(relx=.12, rely=.5)

        if self.rent >= 5000 and not self.angry_upstair_debt_collector:
            door_knocking_angry.play()
            self.angry_upstair_debt_collector = True

        

        
        balance_label = tk.Label(
        self.root, 
        text=f"Balance: ${self.player.balance:,.2f}", 
        width=adjust_width(31, self.reference_width, self.current_width), 
        bg='black', 
        fg='green', 
        relief=SUNKEN, 
        borderwidth=10, 
        font=("Arial", 14)
        )
        balance_label.place(relx=.425, rely=.13)

        

        
        
        self.rent_label = tk.Label(self.root, text=f"Current Rent: ${self.rent}",bg='black', fg='red',relief=GROOVE, borderwidth=3, font=("Arial", 14))
        self.rent_label.place(relx=.45, rely=.175)

        # Menu options
        tk.Button(self.root, text="Check Transaction History", command=self.check_transaction_history, width=22, bg="black", fg="white", font=("System", 12),   borderwidth=3).place(relx= .33, rely=.444)
        tk.Button(self.root, text="Buy Stock", command=self.display_stocks_for_buying, width=adjust_width(18, self.reference_width, self.current_width), bg="black", fg="green", font=("System", 12),  borderwidth=3).place(relx=.34, rely=.15)
        tk.Button(self.root, text="Sell Stock", command=self.display_stocks_for_selling, width=adjust_width(18, self.reference_width, self.current_width),bg="black", fg="red", font=("System", 12), borderwidth=3).place(relx= .68, rely= .15)
        tk.Button(self.root, text="Next Turn", command=self.next_turn, width=adjust_width(20, self.reference_width, self.current_width), bg="black", fg="white", font=("System", 12),  borderwidth=3).place(relx=.7, rely=.85)
        tk.Button(self.root, text="Check Shares Owned", command=self.get_stock_shares, width=18, bg="black", fg="white",wraplength=2000, font=("System", 12),  borderwidth=3).place(relx=.60, rely=.44)
        tk.Button(self.root, text="File For Bankruptcy", command=self.quit, width=adjust_width(30, self.reference_width, self.current_width), bg="black", fg="red", font=("System", 12),  borderwidth=3).place(relx=.12, rely=.6)
    '''def random_background_noises(self):
        sound =  [mouse_squeak.play(),]'''   
    
    def quit(self):
        
        door_knocking_angry_end_game.play()

        result = messagebox.askyesno("Exit Game", "Are you sure you sure about this?")
        if result:  
            self.black_background = tk.Frame(self.root, bg="black")
            self.black_background.place(relwidth=1, relheight=1)  
            self.root.update()  
            door_opening.play()
            time.sleep(3)
            walking_towards.play()
            time.sleep(3)
            shotgun_reload.play()

            time.sleep(3)
            shotgun_bang.play()
            man_screaming.play()
            time.sleep(.5)
            tk.Label(self.root, text = "You died").pack()
            time.sleep(3)
            self.player = Player()    
            self.rent = 0
            self.turn = 0
            
            self.clear_window_settings()
            self.show_pre_menu()
            stocks = get_stocks()
            for stock in stocks:
                stock.value_changer()
        else:
            return  

    
    
    def toggle_fullscreen(self, event=None):
        current_state = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not current_state)
        return "break"  


    def check_transaction_history(self):
        if self.player.transaction_history:
            
            limited_history = self.player.transaction_history[-5:]  
            
            
            history = "\n\n".join(
                [
                    f"{transaction['action']} {transaction['shares']} shares of {transaction['stock']} at ${transaction['price']} per share"
                    for transaction in limited_history
                ]
            )
            
            messagebox.showinfo("Transaction History", history)
        else:
            messagebox.showinfo("Transaction History", "No transactions made yet.")

    
    def display_stocks_for_buying(self):
        self.clear_window() 
        
                                                                                                                                        

        tk.Label(
        self.root,                                                                                                             # Click on a stock to buy label
        text="Click on a stock to buy", 
        width=adjust_width(25, self.reference_width, self.current_width), 
        bg='black', 
        fg='white', 
        borderwidth=5, 
        font=("System",adjust_font_size(18, self.reference_width, self.current_width))).pack(pady=10)
        
        tk.Label(
        self.root, 
        text=f"Balance: ${self.player.balance:,.2f}", 
        width=adjust_width(35, self.reference_width, self.current_width), 
        bg='black', 
        fg='green', 
        relief=SUNKEN, 
        borderwidth=10, 
        font=("System", adjust_font_size(35, self.reference_width, self.current_width))
        ).pack(pady=20)
        
        stocks = get_stocks()                                                                                                           # returns stock 

        for stock in stocks:
            
            mean_price = stock.mean  
            price_difference = stock.price - mean_price
            percentage_change = (price_difference / mean_price) * 100
            
            
            if percentage_change > 0:
                change_text = (
                    f"{stock.name}: ${stock.price:,.2f} "
                    f"[{'+' if percentage_change > 0 else ''}{percentage_change:,.2f}%]"
                )
                color = 'green'  
            else:
                change_text = (
                    f"{stock.name}: ${stock.price:,.2f} "
                    f"[{'+' if percentage_change > 0 else ''}{percentage_change:,.2f}%]"
                )
                color = 'red'  

           
            stock_button = tk.Button(self.root, text=change_text, command=lambda s=stock: self.buy_stock(s), fg=color, width=25, bg='black', borderwidth=5, font=("System", adjust_font_size(18, self.reference_width, self.current_width)))
            stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", width=adjust_width(25, self.reference_width, self.current_width), bg='black', borderwidth=5, fg='red', font=("System",adjust_font_size(18, self.reference_width, self.current_width)), command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=20)

    def buy_stock(self, stock):
        self.clear_window()
        median_price = stock.mean
        price_difference = stock.price - median_price
        percentage_change = (price_difference / median_price) * 100

        tk.Label(
            self.root,
            text=f"Buying {stock.name} - ${stock.price:,.2f} "
                f"{'+' if percentage_change > 0 else ''}( {percentage_change:,.2f}% )",
             width=35, bg='black', borderwidth=5, font=("System", adjust_font_size(18, self.reference_width, self.current_width)), fg='white'
        ).pack(pady=20)

        max_shares = int(self.player.balance // stock.price)
        tk.Label(self.root, text="Select number of shares to buy:",width=25, bg='black', borderwidth=5, fg='white', font=("System",adjust_font_size(18, self.reference_width, self.current_width))).pack()

        shares_slider = tk.Scale(self.root, 
                                 from_=1, 
                                 to=max_shares, 
                                 orient=tk.HORIZONTAL, 
                                 width=adjust_width(25, self.reference_width, self.current_width), 
                                 bg='black', 
                                 borderwidth=10, 
                                 fg='white', 
                                 length=1000,
                                 font=("System",adjust_font_size(18, self.reference_width, self.current_width)))
        shares_slider.pack(pady=10)

        
        cost_label = tk.Label(self.root, 
                              width=30,
                              bg='black', 
                              borderwidth=5, 
                              fg='white', 
                              font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                              text=f"Total Cost: ${shares_slider.get() * stock.price:,.2f}")
        cost_label.pack(pady=10)

        balance_label = tk.Label(self.root, 
                                width=30, 
                                bg='black', 
                                borderwidth=5, 
                                fg='green', 
                                font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                                text=f"Remaining Balance: ${self.player.balance:,.2f}"
                                )
        balance_label.pack(pady=10)


        rent_label = tk.Label(self.root, 
                                width=adjust_width(30, self.reference_width, self.current_width), 
                                bg='black', 
                                borderwidth=5, 
                                fg='red', 
                                font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                                text=f"Current Rent: ${self.rent}"
                                )
        rent_label.pack(pady=10)




        

        def update_labels(event=None):
            total_cost = shares_slider.get() * stock.price
            remaing_balance = self.player.balance - total_cost
            
            cost_label.config(text=f"Total Cost: ${total_cost:,.2f}")
            balance_label.config(text=f'Remaing Balance: ${remaing_balance:,.2f}')
        update_labels()    


        shares_slider.bind("<Motion>", update_labels)
        shares_slider.bind("<B1-Motion>", update_labels)  
        shares_slider.bind("<ButtonRelease-1>", update_labels)  

        
        tk.Button(self.root, 
                  text="Confirm Purchase", 
                  width=adjust_width(30, self.reference_width, self.current_width), 
                  bg='black', 
                  borderwidth=5, 
                  fg='green', 
                  font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                  command=lambda: [self.process_purchase(stock, shares_slider.get()), self.clear_window(), self.main_menu()]).pack(pady=10)
        tk.Button(self.root, 
                  text="Back to Menu", 
                  width=adjust_width(30, self.reference_width, self.current_width), 
                  bg='black', 
                  borderwidth=5, 
                  fg='red', 
                  font=("System",adjust_font_size(18, self.reference_width, self.current_width)),  
                  command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

    def process_purchase(self, stock, shares):
        try:
            shares = int(shares)
            total_cost = shares * stock.price

            if self.player.balance >= total_cost:
                stock_name = stock.name.lower()  
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

        
        owned_stocks = [
            stock for stock in get_stocks()  
            if self.player.owned_stocks.get(stock.name.lower(), 0) > 0  
        ]

        if not owned_stocks:
            messagebox.showinfo("No Stocks Owned", "You don't own any stocks to sell.")
            self.main_menu()
            return

        tk.Label(self.root, width=adjust_width(25, self.reference_width, self.current_width), bg='black', borderwidth=5, fg='white', font=("System",adjust_font_size(18, self.reference_width, self.current_width)), text="Select a stock to sell:").pack(pady=10)

        
        for stock in owned_stocks:
            stock_name = stock.name.lower()
            quantity_owned = self.player.owned_stocks.get(stock_name, 0)

           
            transactions = [
                t for t in self.player.transaction_history 
                if t['stock'] == stock_name and t['action'] == 'Buy'
            ]
            if transactions:
                total_cost = sum(t['shares'] * t['price'] for t in transactions)
                total_shares = sum(t['shares'] for t in transactions)
                avg_purchase_price = total_cost / total_shares

                
                price_difference = stock.price - avg_purchase_price
                percentage_change = (price_difference / avg_purchase_price) * 100

                
                if percentage_change > 0:
                    color = 'green'  
                else:
                    color = 'red'  

                
                stock_button = tk.Button(
                    self.root,
                    text=(
                        f"{stock.name}: {quantity_owned} shares "
                        f"@ ${stock.price:,.2f} (Avg Buy: ${avg_purchase_price:,.2f}) "
                        f"[{'+' if percentage_change > 0 else ''}{percentage_change:,.2f}%]"
                    ),
                    width= 80, bg='black', borderwidth=5, wraplength=8000, fg='white', font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                    command=lambda s=stock: self.sell_stock(s)
                )
                stock_button.config(fg=color)  
                stock_button.pack(pady=5)

        tk.Button(self.root, text="Back to Menu", width=adjust_width(25, self.reference_width, self.current_width), bg='black', borderwidth=5, fg='white', font=("System",adjust_font_size(18, self.reference_width, self.current_width)), command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=20)





    def sell_stock(self, stock):
        self.clear_window()

        stock_name = stock.name.lower()
        
       
        if stock_name in self.player.owned_stocks:
            owned_shares = self.player.owned_stocks[stock_name]

            
            if owned_shares > 0:
                tk.Label(
                    self.root,
                    width=35, 
                    bg='black', 
                    borderwidth=5, 
                    font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                    fg='white', 
                    text=f"Sell {stock.name} - Current Price: ${stock.price:,.2f}").pack(pady=10)
                
                tk.Label(self.root,width=adjust_width(25, self.reference_width, self.current_width), 
                         bg='black', 
                         borderwidth=5, 
                         font=("System",18), 
                         fg='white', 
                         text=f"You own {owned_shares} shares").pack()

               
                shares_slider = tk.Scale(self.root, 
                                         from_=0, 
                                         to=owned_shares, 
                                         orient=tk.HORIZONTAL,
                                         width=adjust_width(25, self.reference_width, self.current_width), 
                                         bg='black', 
                                         borderwidth=10, 
                                         fg='white', 
                                         length=1000,
                                         font=("System",adjust_font_size(18, self.reference_width, self.current_width)))
                shares_slider.pack(pady=20)

                
                revenue_label = tk.Label(self.root, 
                                         width=25, 
                                         bg='black', 
                                         borderwidth=5, 
                                         fg='white', 
                                         font=("System",18), 
                                         text=f"Total revenue: $0.00")
                revenue_label.pack(pady=10)

                balance_label = tk.Label(self.root,
                         text=f"Balance: ${self.player.balance:,.2f}",
                         width=25, 
                         bg='black', 
                         borderwidth=5, 
                         fg='green', 
                         font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                         )
                balance_label.pack(pady=10)

                rent_label = tk.Label(self.root, 
                                width=adjust_width(25, self.reference_width, self.current_width), 
                                bg='black', 
                                borderwidth=5, 
                                fg='red', 
                                font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                                text=f"Current Rent: ${self.rent}"
                                )
                rent_label.pack(pady=10)

                


                def update_revenue(event):
                    selected_shares = shares_slider.get()
                    total_revenue = selected_shares * stock.price
                    player_balance = self.player.balance + total_revenue
            
            
            
            
                    revenue_label.config(text=f"Total revenue: ${total_revenue:,.2f}")
                    balance_label.config(text=f"New Balance: {player_balance:,.2f}")

                
                

                shares_slider.bind("<Motion>", update_revenue)
                shares_slider.bind("<Button-1>", update_revenue)
                shares_slider.bind("<ButtonRelease-1>", update_revenue)

                
                
                tk.Button(self.root, 
                          text="Confirm Sale",
                          width=adjust_width(25, self.reference_width, self.current_width), 
                          bg='black', 
                          borderwidth=5, 
                          fg='green', 
                          font=("System",adjust_font_size(18, self.reference_width, self.current_width)), 
                          command=lambda: [self.process_sell(stock, shares_slider.get(), shares_slider), self.clear_window(), self.main_menu()]).pack(pady=10)

                
                tk.Button(self.root, 
                          text="Back to Menu",
                          width=adjust_width(25, self.reference_width, self.current_width), 
                          bg='black', 
                          borderwidth=5, 
                          fg='red', 
                          font=("System",adjust_font_size(18, self.reference_width, self.current_width)),  
                          command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

            else:
                messagebox.showinfo("No Shares", "You don't have any shares of this stock to sell.")
                self.main_menu()
        else:
            tk.Label(self.root, text="You don't own this stock.").pack(pady=20)
            tk.Button(self.root, text="Back to Menu", command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)



    
    def sell_stock_shares(self, stock):
        self.clear_window()

        
        owned_shares = self.player.owned_stocks.get(stock.name, 0)
        if owned_shares == 0:
            messagebox.showerror("Error", "You don't own any shares of this stock.")
            self.main_menu()
            return

        
        tk.Label(self.root, text=f"Selling {stock.name} - ${stock.price:,.2f} per share", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.root, text=f"You own {owned_shares} shares.").pack()

       
        revenue_label = tk.Label(self.root, text=f"Total revenue: ${stock.price:,.2f}")
        revenue_label.pack(pady=10)

       
        shares_slider = tk.Scale(self.root, from_=0, to=owned_shares, orient=tk.HORIZONTAL)
        
        
        def update_revenue(event):
            selected_shares = shares_slider.get()
            total_revenue = selected_shares * stock.price
            revenue_label.config(text=f"Total revenue: ${total_revenue:,.2f}")

        shares_slider.bind("<Motion>", update_revenue)
        shares_slider.pack(pady=10)

        
        tk.Button(self.root, text="Confirm Sale",
                command=lambda: self.process_sell(stock, shares_slider.get(), shares_slider)).pack(pady=10)

        
        tk.Button(self.root, text="Back to Menu", command=lambda: [self.clear_window(), self.main_menu()]).pack(pady=10)

    def process_sell(self, stock, shares_to_sell, shares_slider):
        try:
            
            shares_to_sell = int(shares_to_sell)

            
            stock_name = stock.name.lower()
            owned_shares = self.player.owned_stocks.get(stock_name, 0)

            if owned_shares >= shares_to_sell and shares_to_sell > 0:
                
                self.player.owned_stocks[stock_name] -= shares_to_sell

                
                if self.player.owned_stocks[stock_name] == 0:
                    del self.player.owned_stocks[stock_name]

                
                total_revenue = shares_to_sell * stock.price

                
                self.player.balance += total_revenue

                
                self.player.record_transaction(stock.name, -shares_to_sell, stock.price, "Sell")

                #
                messagebox.showinfo("Sale Success", f"Sold {shares_to_sell} shares of {stock.name}.")

                
                new_max = self.player.owned_stocks.get(stock.name, 0)
                shares_slider.config(to=new_max)
                shares_slider.set(0)  
            else:
                
                messagebox.showerror("Error", f"You do not own {shares_to_sell} shares of {stock.name}.")
        
        except ValueError:
            messagebox.showerror("Error", "Please select a valid number of shares to sell.")
        
        
        self.main_menu()




    def get_stock_shares(self):
        if self.player.owned_stocks:
            
            shares = "\n\n".join(
                [f"{stock}: {shares} shares" for stock, shares in self.player.owned_stocks.items() if shares > 0]
            )
            if shares:  
                messagebox.showinfo("Owned Stocks", shares)
            else:
                messagebox.showinfo("Owned Stocks", "You don't own any stocks.")
        else:
            messagebox.showinfo("Owned Stocks", "You don't own any stocks.")


    def next_turn(self):
        
        check = self.player.balance - self.rent

        if check < 0 or self.player.balance < 0:
            answer = messagebox.askokcancel("Warning", "Your rent is higher than your balance! Continue?")
            if not answer:  
                return  

           
            self.quit()
            
        else:
            self.player.balance -= self.rent

            if self.rent >= 5000:
                self.rent *= 2
            else:
                self.rent += self.difficulty

            self.rent_label.config(text=f"Current Rent: ${self.rent}")
            self.turn += 1

            stocks = get_stocks()
            for stock in stocks:
                stock.value_changer()

            self.main_menu()

       


    def clear_window(self):
        for widget in self.root.winfo_children():
            if widget != self.bg_label:
                widget.destroy()
        self.root.update_idletasks() 
    
    def clear_window_settings(self):
        for widget in self.root.winfo_children():
            if widget != self.black_background:
                widget.destroy()
        self.root.update_idletasks()  
        




if __name__ == "__main__":
    root = tk.Tk()
    app = StockTradingGUI(root)
    root.mainloop()