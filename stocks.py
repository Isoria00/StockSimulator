import random


class Stocks():
    def __init__(self, name , low, high, price, mean = None, stddev = None):
        self.name = name
        self.low = low
        self.high = high
        self.price = price

        self.mean = mean if mean is not None else (low + high) / 2
        self.stddev = stddev if stddev is not None else (high - low) / 4



    def __str__(self):
        return f"{self.name}: Low = {self.low} - - - High = {self.high} - - - Current Price  - - - {self.price}"





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

cocacola = Stocks("Coca-Cola", 10, 100, 50, mean=50.00, stddev=10.00) 

disney = Stocks("Disney", 30, 300, 81.34, mean=110.00, stddev=15.00)    

meta = Stocks("Meta", 1500, 10000, 5000, mean=5000, stddev=2000)     

tesla = Stocks("Tesla", 500, 5000, 2700, mean=2500.00, stddev=700)    

costco = Stocks("Costco", 100, 1000, 500, mean=500.00, stddev=100.00)

intel = Stocks("Intel", 1, 20, 10, mean=10.00, stddev=2.5)          

apple = Stocks("Apple", 300, 3000, 1700, mean=1700, stddev=500)      

nvidia = Stocks("Nvidia", 5000, 50000, 25000, mean=24000, stddev=15000)     

bitcoin = Stocks("Bitcoin", 10000, 100000, 50000, mean=50000, stddev=25000)   


stock_list = [bitcoin, nvidia, meta, tesla, apple, costco,  disney, cocacola, intel, jazmy]

def get_stocks():
    return stock_list

