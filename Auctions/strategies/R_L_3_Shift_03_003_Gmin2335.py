from strategies.R_L_5_Shift_05_01 import R_L_5_Shift_05_01

class R_L_3_Shift_03_003_Gmin2335(R_L_5_Shift_05_01):
    def __init__(self, num_strategies):
        self.all_remaining_money = num_strategies * 1000;
        super().__init__(num_strategies)
    
    def name(self):
        return "R_L_3_Shift_03_003_Gmin2335";
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
    
class R_L_3_Shift_03_003_Gmin1323(R_L_3_Shift_03_003_Gmin2335):
    def name(self):
        return "R_L_3_Shift_03_003_Gmin1323";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/3) * 2/3;

def strategy_ascending(num_strategies):
    return R_L_3_Shift_03_003_Gmin2335(num_strategies)

def strategy_descending(num_strategies):
    return R_L_3_Shift_03_003_Gmin1323(num_strategies)




