# Install r2 and Build crack-file

### install r2 tool
```
chmod 777 install.sh | ./install.sh
```

### install python3 and r2pipe library
```
sudo apt-get install python3
pip3 install r2pipe
```
### build crack-file
```
chmod 777 make.sh | ./make.sh
```


# Crack

### crack the file itself
```
crack.bin archive/cp 
crack.bin archive/tp
crack.bin archive/game
```

### copy and save file to destination and crack this copy
```
crack.bin archive/cp -d output/cp1
crack.bin archive/tp -d output/tp1
crack.bin archive/game -d output/game1
```

### if the binary file is changed, the check for the amount will not pass and you must explicitly set the application flag
```
crack.bin -cp output/cp1
crack.bin -tp output/tp1
crack.bin -game output/game1
```
