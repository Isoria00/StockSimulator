import random
# Only Stock Manipulation Allowed Here!

class Stocks():
    def __init__(self, name , low, high, price, mean = None, stddev = None):
        self.name = name
        self.low = low
        self.high = high
        self.price = price

        self.mean = mean if mean is not None else (low + high) / 2
        self.stddev = stddev if stddev is not None else (high - low) / 4



    def __str__(self):
        return f"{self.name}: Low = {self.low}, High = {self.high}, Current Price = {self.price}"





    def value_changer(self):
        if self == jazmy:
            new_price = round(random.normalvariate(self.mean, self.stddev),4)
        else:
            new_price = round(random.normalvariate(self.mean, self.stddev),2)
        
        if new_price < self.low:
            new_price = self.low
        elif new_price > self.high:
            new_price= self.high
        
        self.price = new_price





jazmy = Stocks("Jazmy", 0.001, 5.00, 0.50, mean=0.0190, stddev=0.005)  
cocacola = Stocks("Coca-Cola", 0.25, 67.20, 54.39, mean=40.00, stddev=5.00) 
disney = Stocks("Disney", 1.19, 202.68, 81.34, mean=90.00, stddev=15.00)    
meta = Stocks("Meta", 17.55, 384.33, 303.87, mean=250.00, stddev=50.00)     
tesla = Stocks("Tesla", 3.10, 414.50, 245.34, mean=300.00, stddev=70.00)    
costco = Stocks("Costco", 1.67, 571.49, 565.89, mean=500.00, stddev=100.00)  
intel = Stocks("Intel", 25, 75.81, 34.88, mean=50.00, stddev=10.00)          
apple = Stocks("Apple", 100, 198.23, 172.47, mean=150.00, stddev=20.00)      
nvidia = Stocks("Nvidia", 50, 140.76, 122.61, mean=110.00, stddev=30.00)     
bitcoin = Stocks("Bitcoin", 9000, 70000, 50000, mean=40000, stddev=20000)   


stock_list = [bitcoin, nvidia, apple, intel, jazmy, costco, tesla, meta, disney, cocacola]

def get_stocks():
    return stock_list
