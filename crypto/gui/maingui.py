import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QDateTimeEdit, QMessageBox
import json
from datetime import datetime

def backtest(strategy, start_time, end_time):
    # Buraya backtest fonksiyonunu çağırmak için ek işlemler ekleyebilirsin
    print(f'Backtesting started for strategy: {strategy}')
    print(f'Start Time: {start_time}')
    print(f'End Time: {end_time}')

def read_config(path):
    global data
    with open(path) as f:
        data = json.load(f)

def write_config(read_path, write_path, max_trades, stake_currency, dry_run_wallet, pair_list):
    read_config(read_path)
    data['max_open_trades'] = max_trades
    data['stake_currency'] = stake_currency
    data['dry_run_wallet'] = dry_run_wallet
    data['exchange']['pair_whitelist'] = pair_list

    with open(write_path, 'w') as f:
        json.dump(data, f, indent=4)

class JsonConfigurator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matiricie Trade")
        self.setGeometry(100, 100, 400, 400)

        self.config_frame = self.create_frame("Config")
        self.strategy_frame = self.create_frame("Strategy")

        layout = QVBoxLayout(self)
        layout.addWidget(self.config_frame)
        layout.addWidget(self.strategy_frame)

        self.create_button("Save Config", self.save_config)
        self.create_button("Start Backtesting", self.start_backtesting)
        self.create_button("Hyperopt", self.run_hyperopt)
        self.create_button("Analysis Backtest", self.analysis_backtest)

    def create_frame(self, title):
        frame = QWidget()
        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(QLabel(title))

        if title == "Config":
            self.max_trades_entry = self.create_entry("Max Trades:")
            frame_layout.addWidget(self.max_trades_entry)

            self.stake_currency_combobox = self.create_combobox("Stake Currency:", ["USDT", "USDC"])
            frame_layout.addWidget(self.stake_currency_combobox)

            self.dry_run_wallet_entry = self.create_entry("Dry Run Wallet:")
            frame_layout.addWidget(self.dry_run_wallet_entry)

            self.pair_list_combobox = self.create_combobox("Pair List:", ["ETH/USDT", "BTC/USDT"])
            frame_layout.addWidget(self.pair_list_combobox)

            # İki tarih girişi
            self.start_time_edit = self.create_datetimeedit("Start Time:")
            frame_layout.addWidget(self.start_time_edit)

            self.end_time_edit = self.create_datetimeedit("End Time:")
            frame_layout.addWidget(self.end_time_edit)

        elif title == "Strategy":
            self.strategy_name_combobox = self.create_combobox("Strategy Name:", ["Diamond", "Heracles", "HourBasedStrategy", "UniversalMACD"])
            frame_layout.addWidget(self.strategy_name_combobox)

            self.interval_combobox = self.create_combobox("Interval:", ["5m", "15m", "1h", "4h", "1d"])
            frame_layout.addWidget(self.interval_combobox)

        return frame

    def create_entry(self, label_text):
        entry = QLineEdit()
        entry.setPlaceholderText(label_text)
        return entry

    def create_combobox(self, label_text, items):
        combobox = QComboBox()
        combobox.addItems(items)
        combobox.setPlaceholderText(label_text)
        return combobox

    def create_datetimeedit(self, label_text):
        datetime_edit = QDateTimeEdit(self)
        datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        datetime_edit.setDateTime(datetime.now())
        return datetime_edit

    def create_button(self, text, callback):
        button = QPushButton(text)
        button.clicked.connect(callback)
        self.layout().addWidget(button)

    def save_config(self):
        config_data = {
            "config": {
                "max_trades": self.max_trades_entry.text(),
                "stake_currency": self.stake_currency_combobox.currentText(),
                "dry_run_wallet": self.dry_run_wallet_entry.text(),
                "pair_list": self.pair_list_combobox.currentText(),
            },
            "strategy": {
                "strategy_name": self.strategy_name_combobox.currentText(),
                "interval": self.interval_combobox.currentText(),
            }
        }

        pair_list = []
        pair_list.append(self.pair_list_combobox.currentText())
        read_config("config.json")
        write_config("config.json", "matris_trade.json", int(self.max_trades_entry.text()), self.stake_currency_combobox.currentText(),
                     int(self.dry_run_wallet_entry.text()), pair_list)
        QMessageBox.information(self, "Config Saved", "Config saved to matris_trade.json")

    def start_backtesting(self):
        # Buraya backtesting işlemlerini ekleyin
        QMessageBox.information(self, "Backtesting", "Backtesting started")
        backtest_strategy = self.strategy_name_combobox.currentText()
        start_time = self.start_time_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        end_time = self.end_time_edit.dateTime().toString("yyyy-MM-dd HH:mm:ss")
        backtest(backtest_strategy, start_time, end_time)

    def run_hyperopt(self):
        # Buraya Hyperopt işlemlerini ekleyin
        QMessageBox.information(self, "Hyperopt", "Hyperopt started")

    def analysis_backtest(self):
        # Buraya analiz backtest işlemlerini ekleyin
        QMessageBox.information(self, "Analysis Backtest", "Analysis Backtest started")
        with open("user_data/backtest_results/.last_result.json") as last_result:
            last = json.load(last_result)
            print(last["latest_backtest"])
            with open("user_data/backtest_results/"+last["latest_backtest"]) as back:
                backtest_result = json.load(back)
                print(backtest_result)
        print("Analysis Backtest")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonConfigurator()
    window.show()
    sys.exit(app.exec_())
