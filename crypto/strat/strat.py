user_data = "user_data" #user_data path
strategy_list = ["Diamond", "Heracles", "HourBasedStrategy", "UniversalMACD"]



# Dosyayı açma ve stratejileri yazma
for strategy in strategy_list:
    with open(f"{user_data}/strategies/{strategy}.py") as strat:
        print(strat)
