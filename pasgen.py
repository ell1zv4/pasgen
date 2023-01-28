#!/usr/bin/python3

import sys
import secrets
import string
from colorama import Fore, Back, Style
import os
from pathlib import Path

def save():

    try:
        if len(sys.argv) <= 3:
                print(Fore.BLUE + ' \n Save usage pasgen.py s (pwd to save) (name archive)')

        passw = sys.argv[2]

        name_file = sys.argv[3]

        if os.path.isdir('/root/.pwds') == True:
            os.system("echo '{}' > /root/.pwds/{}".format(passw, name_file))
            print(Fore.BLUE + ' \n Password saved in /root/.pwds')

        else:
            os.system("mkdir /root/.pwds && echo '{}' > /root/.pwds/{}".format(passw, name_file))

    except:
        pass


def create():
    try:
        if sys.argv[1] == "c":
            if len(sys.argv) <= 2:
                print(Fore.BLUE + ' \n Create usage: pagsen.py c {numr characters}')
                exit(0)

            try:
                characters = int(sys.argv[2])
        
            except:
                pass

            letters = string.ascii_letters
            digits = string.digits
    
            alphabet = letters + digits 

            pwd_length = characters

            pwd = ''

            for i in range(pwd_length):
                pwd += ''.join(secrets.choice(alphabet))

            print(Fore.RED +  "\n Password: {}".format(pwd))

    except:
        pass


if os.getuid() == 0:

    if len(sys.argv) <= 1:
        print(Fore.BLUE + '\n Usage: pasgen.py c(Create pwds)/s(Save pwds)')
    else:
        if sys.argv[1] == "c":
            create()
        if sys.argv[1] == "s":
            save()

else:
    print(Fore.RED + ' \n You are not root!!!')