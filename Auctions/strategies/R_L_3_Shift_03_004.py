from strategies.R_L_5_Shift_05_01 import R_L_5_Shift_05_01

class R_L_3_Shift_03_004(R_L_5_Shift_05_01):
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
        return 0.04;


    def name(self):
        return "R_L_3_Shift_03_004";

def strategy_ascending(num_strategies):
    return R_L_3_Shift_03_004(num_strategies)

def strategy_descending(num_strategies):
    return R_L_3_Shift_03_004(num_strategies)





