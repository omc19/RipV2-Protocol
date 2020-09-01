#!/bin/sh

python3 daemon.py conf1.txt&
gnome-terminal -e "python3 daemon.py conf2.txt"

