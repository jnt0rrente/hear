#!/bin/env python3

import os

#throw error if ran as sudo
if os.geteuid() == 0:
    print('Please do not run this script as sudo.')
    exit(1)

#create a file in .config/hear/ called api_key
os.system('mkdir -p ~/.config/hear')
os.system('touch ~/.config/hear/api_key')
with open(os.path.expanduser("~/.config/hear/api_key"), "w") as f:
    f.write('sk-')


#symbolic link to main.py
os.system('ln -s {} ~/.local/bin/hear'.format(os.path.abspath(__file__.replace('setup.py', 'main.py'))))