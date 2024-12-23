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





jazmy = Stocks("JASMY", 0.001, 5.00, 0.50, mean=0.0190, stddev=0.010)  

bitcoin = Stocks("BTC", 10, 500111000, 100000, mean=100000, stddev=48000)  

nvidia = Stocks("NVDA", 5, 1001111000, 50000, mean=50000, stddev=19200)  

meta = Stocks("META", 10, 100111000, 25000, mean=25000, stddev=8400)  

tesla = Stocks("TSLA", 10, 50111000, 20000, mean=20000, stddev=5760)  

apple = Stocks("AAPL", 10, 10011100, 10000, mean=10000, stddev=3000)  

costco = Stocks("COSTCO", 50, 101111000, 5000, mean=5000, stddev=1200)  

disney = Stocks("DISNEY", 30, 1111000, 1000, mean=1000, stddev=180)  

cocacola = Stocks("COCA-COLA", 10, 5111100, 100, mean=100, stddev=12)  

intel = Stocks("INTEL", 1, 11111200, 10, mean=10, stddev=1)




stock_list = [bitcoin, nvidia, meta, tesla, apple, costco,  disney, cocacola, intel, jazmy]

def get_stocks():
    return stock_list

