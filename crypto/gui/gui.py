import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QComboBox, QMessageBox
import json

class JsonConfigurator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Matiricie Trade")
        self.setGeometry(100, 100, 400, 350)

        self.config_frame = self.create_frame("Config")
        self.strategy_frame = self.create_frame("Strategy")

        layout = QVBoxLayout(self)
        layout.addWidget(self.config_frame)
        layout.addWidget(self.strategy_frame)

        self.create_button("Save Config", self.save_config)
        self.create_button("Start Backtesting", self.start_backtesting)
        self.create_button("Hyperopt", self.run_hyperopt)

    def create_frame(self, title):
        frame = QWidget()
        frame_layout = QVBoxLayout(frame)
        frame_layout.addWidget(QLabel(title))

        if title == "Config":
            self.max_trades_entry = self.create_entry("Max Trades:")
            frame_layout.addWidget(self.max_trades_entry)

            self.stake_currency_combobox = self.create_combobox("Stake Currency:", ["USD", "EUR"])
            frame_layout.addWidget(self.stake_currency_combobox)

            self.dry_run_wallet_entry = self.create_entry("Dry Run Wallet:")
            frame_layout.addWidget(self.dry_run_wallet_entry)

            self.pair_list_combobox = self.create_combobox("Pair List:", ["ETH/USDT", "BTC/USDT"])
            frame_layout.addWidget(self.pair_list_combobox)

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

        with open("matris_trade.json", "w") as json_file:
            json_file.write(json.dumps(config_data, indent=4))

        QMessageBox.information(self, "Config Saved", "Config saved to matris_trade.json")

    def start_backtesting(self):
        # Buraya backtesting işlemlerini ekleyin
        QMessageBox.information(self, "Backtesting", "Backtesting started")

    def run_hyperopt(self):
        # Buraya Hyperopt işlemlerini ekleyin
        QMessageBox.information(self, "Hyperopt", "Hyperopt started")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JsonConfigurator()
    window.show()
    sys.exit(app.exec_())
