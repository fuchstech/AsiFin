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

def write_config(path, max_trades, stake_currency, dry_run_wallet, pair_list):
    read_config(path)
    data['max_open_trades'] = max_trades
    data['stake_currency'] = stake_currency
    data['dry_run_wallet'] = dry_run_wallet
    data['exchange']['pair_whitelist'] = pair_list

    # Güncellenmiş verileri aynı dosyaya geri kaydet
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)  # indent=4, güzel bir görüntüleme için girinti ekler

if __name__ == "__main__":
    # Kullanıcıdan girdi al
    config_path = input("JSON dosyasının yolunu girin: ")

    # Config dosyasını oku ve bilgileri göster
    read_config(config_path)

    # Yeni değerleri kullanıcıdan al
    yeni_max_trades = int(input("Yeni max_trades değerini girin: "))
    yeni_stake_currency = input("Yeni stake_currency değerini girin: ")
    yeni_dry_run_wallet = float(input("Yeni dry_run_wallet değerini girin: "))

    yeni_pair_listesi = []
    pair = input("pair girin (örn. ETH/USDT): ")
    yeni_pair_listesi.append(pair)

    # Config dosyasını güncelle ve kaydet
    write_config(config_path, yeni_max_trades, yeni_stake_currency, yeni_dry_run_wallet, yeni_pair_listesi)
