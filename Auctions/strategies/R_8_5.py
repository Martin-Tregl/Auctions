from strategies.R_2 import R_2 

class R_8_5(R_2):
    def name(self):
        return "R_8_5";

    def get_N(self):
        return 1.6;

def strategy_ascending(num_strategies):
    return R_8_5(num_strategies)

def strategy_descending(num_strategies):
    return R_8_5(num_strategies)