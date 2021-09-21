# Install

install python3 and r2pipe library
```
sudo apt-get install python3
pip3 install r2pipe
```

install r2 tool
```
./install.sh
```

# Crack

crack the file itself
```
python3 crack.py archive/cp 
python3 crack.py archive/tp
python3 crack.py archive/game
```

copy and save file to destination and crack this copy
```
python3 crack.py archive/cp -o cp1
python3 crack.py archive/tp -o tp1
python3 crack.py archive/game -o game1
```

if the binary file is changed, the check for the amount will not pass and you must explicitly set the application flag
```
python3 crack.py -cp cp1
python3 crack.py -tp tp1
python3 crack.py -game game1
```
