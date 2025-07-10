from strategies.R_L_3_Shift_03_003_Amin2335 import R_L_3_Shift_03_003_Amin2335

class R_L_3_Shift_03_003_Amin4545(R_L_3_Shift_03_003_Amin2335):
    def name(self):
        return "R_L_4_Shift_03_003_Amin4545";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 4/5) * 4/5;
    def Get_N(self):
        return 3;

class R_L_4_Shift_03_003_Amin1245(R_L_3_Shift_03_003_Amin2335):
    def name(self):
        return "R_L_4_Shift_03_003_Gmin1245";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/2) * 4/5;
    def Get_N(self):
        return 4;

def strategy_ascending(num_strategies):
    return R_L_3_Shift_03_003_Amin4545(num_strategies)

def strategy_descending(num_strategies):
    return R_L_4_Shift_03_003_Amin1245(num_strategies)