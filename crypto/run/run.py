
import os

def run(command):
    os.system("cd ..")
    print(os.popen('ls').read())
    os.system("source ./.venv/bin/activate")
    print(os.popen('freqtrade backtesting -c /home/fuchsvm/Desktop/matris_trade/crypto/conf/data/config.json --strategy Diamond').read())
run("aa")