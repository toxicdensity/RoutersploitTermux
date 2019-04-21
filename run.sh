echo ==Installing Routersploit==
cd $HOME
sleep 2
apt update && apt upgrade
sleep 1
pkg upgrade && pkg install autoconf automake bison bzip2 clang cmake \ coreutils diffutils flex gawk git grep gzip libtool make patch perl \ sed silversearcher-ag tar wget pkg-config -y
sleep 1
pkg install python-dev clang libcrypt-dev libffi-dev git openssl-dev -y
sleep 1
git clone https://github.com/threat9/routersploit
sleep 1
cd routersploit 
sleep 1
pip install --upgrade pip
sleep 1
pip install requests
sleep 1
python3 -m pip install -r requirements.txt
sleep 2
python3 -m pip install -r requirements-dev.txt
sleep 2
cd $HOME
sleep 1
figlet Done
sleep 1
clear
echo Run routersploit with command
echo cd routersploit and python rsf.py 

