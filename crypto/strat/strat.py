user_data = "/home/fuchsvm/freqtrade/user_data" #user_data path
strategy_list = ["Diamond", "Heracles", "HourBasedStrategy", "UniversalMACD"]

strategy = "Diamond" #input strateji
interval = "5m" #input time intervat

# Dosyayı açma ve stratejileri yazma
with open(f"{user_data}/strategies/{strategy}.py","r+") as strat:
    dosya = strat.readlines()
    row = 0
    for time in dosya:
        row += 1
        if "timeframe =" in time:
            print(time,row)
            break
    if row is not None:
        dosya[row] = interval
        strat.writelines(dosya)
