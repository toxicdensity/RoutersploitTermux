#!/data/data/com.termux/files/usr/bin/python

import os
import sys
from time import sleep

def runscript():
 print("[*] Initializing...")
 sleep(2)
 os.system("cd $HOME")
 os.system("termux-setup-storage")
 sleep(1)

 print("[*] Installing routersploit requirements with apt...")
 sleep(2)
 os.system("apt update && apt upgrade -y")
 os.system("pkg upgrade && pkg install autoconf automake bison bzip2 clang cmake coreutils diffutils flex gawk git grep gzip libtool make patch perl sed silversearcher-ag tar wget pkg-config -y")
 os.system("pkg install python-dev clang libcrypt-dev libffi-dev git openssl-dev -y")
 sleep(1)

 print("[*] Cloning routersploit...")
 sleep(2)
 os.system("git clone https://github.com/threat9/routersploit")
 sleep(1)

 print("[*] Installing requirements using python3-pip...")
 sleep(2)
 os.system("cd routersploit")
 os.system("pip install --upgrade pip")
 os.system("pip install requests")
 os.system("pip install future")
 os.system("pip install paramiko")
 os.system("pip install pysnmp==4.4.6")
 os.system("pip install pycryptodome")
 os.system("pip install pytest==4.4.0")
 os.system("pip install pytest-forked")
 os.system("pip install pytest-xdist")
 os.system("pip install flake8")
 os.system("pip install git+git://github.com/threat9/threat9-test-bed")
 os.system("cd $HOME")
 sleep(1)

 print("[*] All installation is done. Clearing up installation script...")
 sleep(2)
 os.system("rm -rf $HOME/RoutersploitTermux")
 os.system("rm -rf $HOME/run.sh")
 sleep(1)
 os.system("clear")

 print("[*] All done!")
 sleep(2)
 print("Run routersploit with command cd routersploit && python rsf.py")
 print("")
 print("Tools by Cose no copyright intended")
 sleep(1)