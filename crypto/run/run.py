
import os

def backtest(strategy):
    #print(os.popen('ls').read())
    #os.system("source ./.venv/bin/activate")
    print(os.popen(f'freqtrade backtesting -c matris_trade.json --strategy {strategy}').read())
backtest("Diamond")

