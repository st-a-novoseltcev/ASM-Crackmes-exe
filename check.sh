if ! command -v r2 > /dev/null
then
    echo "r2 not founded. Unstalling...."
    git clone https://github.com/radareorg/radare2
    radare2/sys/install.sh
fi
