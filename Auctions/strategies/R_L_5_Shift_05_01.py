from strategies.R_2 import R_2

class R_L_5_Shift_05_01(R_2):
    def __init__(self, num_strategies):
        super().__init__(num_strategies)
        self.auction_counter = 0;
        self.plus_shift = self.GetPlusShift();
        self.minus_shift= self.GetMinusShift();
        self.minimum_N = self.GetMinimum_N();
        self.last_price = -1;
        self.noted_data = []; # ( my_value , price_sold )
        self.bougt_at = [];

    def get_N(self):
        return 5;
    def GetPlusShift(self):
        return 0.5;
    def GetMinusShift(self):
        return 0.1;
    def GetMinimum_N(self):
        return 1.2;


    def name(self):
        return "R_L_5_Shift_05_01";

    def won(self, price):
        self.remaining_money -= price;
        self.bougt_at.append( round( self.N , 2 ) );
        self.N += self.plus_shift + self.minus_shift # minus shift will me reduced back in set_value
        

    def set_value(self, value): 
        if self.last_price > -1:
            self.noted_data.append( ( self.value , self.last_price ) );
        self.value = value
        self.auction_counter += 1;
        self.N = max( self.N - self.minus_shift , self.minimum_N);
        return;
        """if self.auction_counter == self.num_auctions:
            avg = 0;
            for ba in self.bougt_at:
                avg += ba;
            print( avg / len(self.bougt_at) ) ;
"""     
    def interested(self, price, active_strats):
        self.last_price = price;
        return price * self.N <= self.value and price <= self.remaining_money;
    
    def set_money(self, money):
        self.remaining_money = money;
        self.auction_counter = 0;

def strategy_ascending(num_strategies):
    return R_L_5_Shift_05_01(num_strategies)

def strategy_descending(num_strategies):
    return R_L_5_Shift_05_01(num_strategies)

 



