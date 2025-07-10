from strategies.R_L_3_Shift_03_003_Gmin2335 import R_L_3_Shift_03_003_Gmin2335

class R_L_3_Shift_03_Lrat_Gmin2335(R_L_3_Shift_03_003_Gmin2335):
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

    def name(self):
        return "R_L_3_Shift_03_Lrat_Gmin2335";

        
class R_L_3_Shift_03_Lrat_Gmin1323(R_L_3_Shift_03_Lrat_Gmin2335):
    def name(self):
        return "R_L_3_Shift_03_Lrat_Gmin1323";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/3) * 2/3;

def strategy_ascending(num_strategies):
    return R_L_3_Shift_03_Lrat_Gmin2335(num_strategies)

def strategy_descending(num_strategies):
    return R_L_3_Shift_03_Lrat_Gmin1323(num_strategies)