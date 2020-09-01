#!/bin/sh

python3 daemon.py config1.txt&
gnome-terminal -e "python3 daemon.py config2.txt" 
gnome-terminal -e "python3 daemon.py config3.txt" 
gnome-terminal -e "python3 daemon.py config4.txt" 
gnome-terminal -e "python3 daemon.py config5.txt" 
