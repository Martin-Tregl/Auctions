from strategies.R_2 import R_2 

class R_5_3(R_2):
    def name(self):
        return "R_5_3";

    def get_N(self):
        return 5/3;

def strategy_ascending(num_strategies):
    return R_5_3(num_strategies)

def strategy_descending(num_strategies):
    return R_5_3(num_strategies)