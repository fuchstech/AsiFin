# Asi Fin
Presentation Link
https://www.canva.com/design/DAFz5rdwMOM/wkGZtfczpahsOyC08yGRew/edit?utm_content=DAFz5rdwMOM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
## Installation

https://www.freqtrade.io/en/stable/installation/#script-installation

Do the script installation section

```bash
git clone https://github.com/freqtrade/freqtrade.git

cd freqtrade

git checkout stable

```
## Scripts Installation

```bash
./setup.sh -i  #answer y to install dependencies

```

## Change the bashrc file to run the code properly

```bash
sudo nano ~/.bashrc 
```
add this lines at the bottom of the .bashrc file

```
cd #global_path_of_your_freqtrade_folder
source ./.venv/bin/activate
```
### Install other dependencies for PyQt5
```
pip install PyQt5
sudo apt-get install '^libxcb.*-dev' libx11-xcb-dev libglu1-mesa-dev libxrender-dev libxi-dev libxkbcommon-dev libxkbcommon-x11-dev
```

## Check The file paths before running because you have to change the paths

