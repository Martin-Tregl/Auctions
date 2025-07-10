from strategies.R_L_3_Shift_03_003_Amin2335 import R_L_3_Shift_03_003_Amin2335

class R_L_4_Shift_03_004_Amin2312(R_L_3_Shift_03_003_Amin2335):
    def name(self):
        return "R_L_4_Shift_03_004_Amin2312";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 2/3) * 1/2;
    def Get_N(self):
        return 4;
    def GetMinusShift(self):
        return 0.04;

class R_L_4_Shift_03_004_Amin1335(R_L_3_Shift_03_003_Amin2335):
    def name(self):
        return "R_L_4_Shift_03_004_Amin1335";
    def GetMinimum_N(self):
        return 1 + (( self.exp_remaining_val() / (1 + self.all_remaining_money) ) - 1/3) * 3/5;
    def Get_N(self):
        return 4;
    def GetMinusShift(self):
        return 0.04;

def strategy_ascending(num_strategies):
    return R_L_4_Shift_03_004_Amin2312(num_strategies)

def strategy_descending(num_strategies):
    return R_L_4_Shift_03_004_Amin1335(num_strategies)