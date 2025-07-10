from strategies.R_2 import R_2 

class R_3_2(R_2):
    def name(self):
        return "R_3_2";

    def get_N(self):
        return 1.5;

def strategy_ascending(num_strategies):
    return R_3_2(num_strategies)

def strategy_descending(num_strategies):
    return R_3_2(num_strategies)