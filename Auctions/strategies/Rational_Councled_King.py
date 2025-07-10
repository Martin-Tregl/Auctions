from random import random

class R_3_2:

    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0
        self.num_auctions = 0
        self.N = self.get_N();

    def get_N(self):
        return 3/2;

    # number of auctions that will be simulated - called before the first auction
    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions

    # amount of money available for all auctions - called before the first aution
    def set_money(self, money):
        self.remaining_money = money;

    # called after winning an aution with the price that was paid for the object
    def won(self, price):
        self.remaining_money -= price

    # value of the object for this agent - called before every auction
    def set_value(self, value): 
        self.value = value

    # shows interest in the object for the current price, called in each iteration of each aution
    def interested(self, price, active_strats):
        return price * self.N <= self.value and price <= self.remaining_money;

class R_8_5(R_3_2):
    def get_N(self):
        return 1.6;

class R_L_5_Shift_05_01(R_3_2):
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

    def interested(self, price, active_strats):
        self.last_price = price;
        return price * self.N <= self.value and price <= self.remaining_money;
    
    def set_money(self, money):
        self.remaining_money = money;
        self.auction_counter = 0;

class R_L_3_Shift_03_003(R_L_5_Shift_05_01):
    def __init__(self, num_strategies):
        super().__init__(num_strategies)
        self.plus_shift = self.GetPlusShift();
        self.minus_shift= self.GetMinusShift();
        self.minimum_N;
    def get_N(self):
        return 3;
    def GetPlusShift(self):
        return 0.3;
    def GetMinusShift(self):
        return 0.03;

class R_L_3_Shift_03_003_Gmin2335(R_L_5_Shift_05_01):
    def __init__(self, num_strategies):
        self.all_remaining_money = num_strategies * 1000;
        super().__init__(num_strategies)    
    def get_N(self):
        return 3;
    def GetPlusShift(self):
        return 0.3;
    def GetMinusShift(self):
        return 0.03;
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 2/3) * 3/5;
    def set_money(self, money):
        super().set_money(money);
        self.all_remaining_money = self.num_strategies * money;
        self.minimum_N = self.GetMinimum_N();
        return;
    def exp_remaining_val(self):
        return (self.num_auctions - self.auction_counter) * 150

class R_L_4_Shift_03_004_Gmin2312(R_L_3_Shift_03_003_Gmin2335):
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 2/3) * 1/2;
    def Get_N(self):
        return 4;
    def GetMinusShift(self):
        return 0.04;

class R_L_4_Shift_03_004_Gmin1335(R_L_3_Shift_03_003_Gmin2335):
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/3) * 3/5;
    def Get_N(self):
        return 4;
    def GetMinusShift(self):
        return 0.04;

class R_L_3_Shift_03_Lrat_Gmin4545(R_L_3_Shift_03_003_Gmin2335):
    def set_value(self, value): 
        if self.auction_counter > 0:
            self.noted_data.append( ( self.value , self.last_price ) );
            self.all_remaining_money -= self.last_price;
            self.minusShift = self.GetMinusShift();
        self.minimum_N = self.GetMinimum_N();
        self.N = max( self.N - self.minus_shift , self.minimum_N);
        self.value = value
        self.auction_counter += 1;

    def GetMinusShift(self):
        exp_buys = 1+ (self.remaining_money / 150); 
        inv_ratio = 0.1 +((self.num_auctions - self.auction_counter) / exp_buys);
        return self.GetPlusShift() / inv_ratio;
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 4/5) * 4/5;
    def Get_N(self):
        return 3;

class R_L_4_Shift_03_Lrat_Gmin1245(R_L_3_Shift_03_Lrat_Gmin4545):
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/2) * 4/5;
    def Get_N(self):
        return 4;

class R_L_4_Shift_03_Lrat_Gmin2312(R_L_3_Shift_03_Lrat_Gmin4545):
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 2/3) * 1/2;
    def Get_N(self):
        return 4;
    def GetMinusShift(self):
        return 0.04;

class R_L_3_Shift_03_003_Amin2335(R_L_5_Shift_05_01):
    def __init__(self, num_strategies):
        self.all_remaining_money = num_strategies * 1000;
        super().__init__(num_strategies)
    def get_N(self):
        return 3;
    def GetPlusShift(self):
        return 0.3;
    def GetMinusShift(self):
        return 0.03;
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 2/3) * 3/5;
    def set_money(self, money):
        super().set_money(money);
        self.all_remaining_money = self.num_strategies * money;
        self.minimum_N = self.GetMinimum_N();
        return;
    def exp_remaining_val(self):
        return (self.num_auctions - self.auction_counter) * 150

    def set_value(self, value): 
        if self.auction_counter > 0:
            self.noted_data.append( ( self.value , self.last_price ) );
            self.all_remaining_money -= self.last_price;
        self.minimum_N = self.GetMinimum_N();
        self.N = max( self.N - self.minus_shift , self.minimum_N);
        self.value = value
        self.auction_counter += 1;

class R_L_3_Shift_03_003_Amin1323(R_L_3_Shift_03_003_Amin2335):
    def name(self):
        return "R_L_3_Shift_03_003_Amin1323";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/3) * 2/3

class Rational_Councled_King:
    def __init__(self, num_strategies):
        self.num_strategies = num_strategies
        self.remaining_money = 0;
        self.num_auctions = 0;
        self.half_advisors = self.GetHalfAdvisors();
        self.one_advisors = self.GetOneAdvisors();
        self.two_advisors = self.GetTwoAdvisors();

    def GetHalfAdvisors(self):
        return [];
    def GetOneAdvisors(self):
        return [];
    def GetTwoAdvisors(self):
        return [];

    # name of the strategy - make sure it is unique
    def name(self):
        return "Rational_Councled_King"

    # name of the author of the strategy
    def author(self):
        return "Martin Tregl"

    # number of auctions that will be simulated - called before the first auction
    def set_num_auctions(self, num_auctions):
        self.num_auctions = num_auctions
        for adv in self.half_advisors:
            adv.set_num_auctions(num_auctions);
        for adv in self.one_advisors:
            adv.set_num_auctions(num_auctions);
        for adv in self.two_advisors:
            adv.set_num_auctions(num_auctions);

    # amount of money available for all auctions - called before the first aution
    def set_money(self, money):
        self.remaining_money = money;
        for adv in self.half_advisors:
            adv.set_money(money);
        for adv in self.one_advisors:
            adv.set_money(money);
        for adv in self.two_advisors:
            adv.set_money(money);
        self.value_money_rat = 150 * self.num_auctions / ( money * self.num_strategies )
        self.distribute_influence();

    def distribute_influence(self):
        self.half_influence = 1;
        self.one_influence = 0;
        self.two_influence = 0;
        if 0.5 < self.value_money_rat and self.value_money_rat <= 1:
            self.half_influence = 2 - 2*self.value_money_rat;
            self.one_influence = 2*self.value_money_rat - 1;
            self.two_influence = 0;
        elif 1 < self.value_money_rat and self.value_money_rat < 2 :
            self.half_influence = 0
            self.one_influence = 2 - self.value_money_rat;
            self.two_influence = self.value_money_rat - 1;
        elif self.value_money_rat >= 2:
            self.half_influence = 0
            self.one_influence = 0
            self.two_influence = 1;
        
        

    # called after winning an aution with the price that was paid for the object
    def won(self, price):
        self.remaining_money -= price
        for adv in self.half_advisors:
            adv.won(price);
        for adv in self.one_advisors:
            adv.won(price);
        for adv in self.two_advisors:
            adv.won(price);

    # value of the object for this agent - called before every auction
    def set_value(self, value): 
        self.value = value
        for adv in self.half_advisors:
            adv.set_value(value);
        for adv in self.one_advisors:
            adv.set_value(value);
        for adv in self.two_advisors:
            adv.set_value(value);

    # shows interest in the object for the current price, called in each iteration of each aution
    def interested(self, price, active_strats):
        if price > self.remaining_money or price >= self.value:
            return False;
        max_intrest = self.half_influence * len( self.half_advisors) + self.one_influence * len( self.one_advisors ) + self.two_influence * len( self.two_advisors);
        interest = 0;
        for i in range( len(self.half_advisors)):
            if self.half_advisors[i].interested(price,active_strats):
               interest += self.half_influence;
        for i in range( len (self.one_advisors)):
            if self.one_advisors[i].interested(price,active_strats):
                interest += self.one_influence;
        for i in range(len(self.two_advisors)):
            if self.two_advisors[i].interested(price,active_strats):
                interest += self.two_influence;
        return self.decide( interest , max_intrest ) ;

    def decide(self , intr , max_intr ):
        return random() * max_intr <= intr;

class Counciled_King_Richard(Rational_Councled_King):
    def name(self):
        return "Counciled_King_Richard";
    def GetHalfAdvisors(self):
        return [ R_L_4_Shift_03_004_Gmin2312(self.num_strategies) , R_L_3_Shift_03_003_Gmin2335(self.num_strategies) ];
    def GetOneAdvisors(self):
        return [ R_3_2(self.num_strategies) , R_L_3_Shift_03_003( self.num_strategies) ];
    def GetTwoAdvisors(self):
        return [ R_L_3_Shift_03_Lrat_Gmin4545( self.num_strategies), R_L_4_Shift_03_Lrat_Gmin2312(self.num_strategies) ];

class Counciled_Prince_William(Rational_Councled_King):
    def name(self):
        return "Counciled_Prince_William";
    def GetHalfAdvisors(self):
        return [ R_L_4_Shift_03_004_Gmin1335(self.num_strategies) , R_L_5_Shift_05_01(self.num_strategies) ];
    def GetOneAdvisors(self):
        return [ R_8_5(self.num_strategies) , R_3_2( self.num_strategies) ];
    def GetTwoAdvisors(self):
        return [ R_L_3_Shift_03_003_Amin1323( self.num_strategies) , R_L_4_Shift_03_Lrat_Gmin1245(self.num_strategies) ];

def strategy_ascending(num_strategies):
    return Counciled_King_Richard(num_strategies)

def strategy_descending(num_strategies):
    return Counciled_Prince_William(num_strategies)





