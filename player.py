
class Player:
    def __init__(self, balance = 1000):
        self.balance = balance
        self.owned_stocks = {
            "jazmy": 0, 
            "cocacola": 0,
            "disney": 0 ,
            "meta": 0,
            "tesla": 0,
            "costco": 0,
            "intel": 0,
            "apple": 0,
            "nvidia": 0,
            "bitcoin": 0
                             }
        self.transaction_history = []  #  List Transactions
    
    def record_transaction(self, stock_name, shares, price, action):
        self.transaction_history.append({
            'stock': stock_name,
            'shares': shares,
            'price': price,
            'action': action
        })
    
    
    
    
    
    def __str__(self):
        # Return a string that shows the player's stats
        stock_info = "\n".join(f"{stock.capitalize()}: {shares} shares" for stock, shares in self.owned_stocks.items())
        return f"Player Balance: ${self.balance:.2f}\nOwned Stocks:\n{stock_info}"
    
