user_data = "/home/fuchsvm/freqtrade/user_data" #user_data path
strategy_list = ["Diamond", "Heracles", "HourBasedStrategy", "UniversalMACD"]

strategy = "UniversalMACD" #input strateji
interval = "1h" #input time intervat

# Dosyayı açma ve stratejileri yazma
dosya = []
with open(f"{user_data}/strategies/{strategy}.py","r+") as strat:
    dosya = strat.readlines()
    row = 0
    for time in dosya:
        if "timeframe =" in time:
            print(time,row)
            break
        row += 1
    if row != 0:
        dosya[row] = "    timeframe = "+f"'{interval}'"

with open(f"crypto/strat/strategies/{strategy}.py","w") as strat:
    strat.writelines(dosya)