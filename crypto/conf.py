# yatırım miktarı 
# tek seferde açık olması istenen tradeler
# işlem yapılacak pair
#
# 

import json
def read_config(path):
    global data
# JSON dosyasının içeriğini bir değişkene yükle
    with open(path) as f:
        data = json.load(f)

    # İstenilen verileri seç
    max_open_trades = data.get('max_open_trades')
    stake_currency = data.get('stake_currency')
    dry_run_wallet = data.get('dry_run_wallet')
    pair_whitelist = data['exchange']['pair_whitelist']
    # Sonuçları yazdır
    print(f"max_open_trades: {max_open_trades}")
    print(f"stake_currency: {stake_currency}")
    print(f"dry_run_wallet: {dry_run_wallet}")
    print(f"pair_whitelist: {pair_whitelist}")

def write_config(path,max_trades,stake_currency,dry_run_wallet,pair):
    read_config(path)
    data['max_open_trades'] = max_trades
    data['stake_currency'] = stake_currency
    data['dry_run_wallet'] = dry_run_wallet
    data['exchange']['pair_whitelist'] = list(pair)


    # Güncellenmiş verileri aynı dosyaya geri kaydet
    with open('crypto\data\config1.json', 'w') as f:
        json.dump(data, f, indent=4)  # indent=4, güzel bir görüntüleme için girinti ekler

