# Install r2 and Build crack-file

### build crack-file
```bash
make crack
```


# Crack

### crack the file itself
```bash
crack.bin archive/cp 
crack.bin archive/tp
```

### copy and save file to destination and crack this copy
```bash
crack.bin archive/cp -d output/cp1
crack.bin archive/tp -d output/tp1
```

### if the binary file is changed, the check for the amount will not pass and you must explicitly set the application flag
```bash
crack.bin -cp output/cp1
crack.bin -tp output/tp1
```
