user_data = "/home/fuchsvm/freqtrade/user_data" #user_data path
strategy_list = ["Diamond", "Heracles", "HourBasedStrategy", "UniversalMACD"]

strategy = "Diamond" #input strateji
interval = "5m" #input time intervat

# Dosyayı açma ve stratejileri yazma
with open(f"{user_data}/strategies/{strategy}.py","r+") as strat:
    for time in strat.readlines():
        if "timeframe =" in time:
            print(time)
