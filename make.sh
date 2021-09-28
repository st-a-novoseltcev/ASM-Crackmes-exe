#!/bin/sh

sudo apt-get install python3
pip3 install -U nuitka
nuitka3 --follow-imports crack/crack.py
rm -r crack.build > /dev/null

