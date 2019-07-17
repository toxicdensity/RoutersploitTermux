I make the script to install routersploit on termux.
I get the resolve of many problem installing termux in 
https://github.com/threat9/routersploit/issues/531

I just simplified and fix the command so it will take less storage

# About Issue #3

Well this issue I still dont know how to fix this because the issue is not too specific but it tells abut bash error.
So if you read the issue and have a same problem with it use this command that hope its work.
( Follow this command if you have a problem running run.sh in my script )

```
apt update && apt upgrade
cd $HOME
curl -LO https://raw.githubusercontent.com/41Team/RoutersploitTermux/master/run.sh
chmod +x run.sh
./run.sh or sh run.sh or bash run.sh
```

So if that command seems not work you can run this script with python3 with command...

# Installation

```
apt update && apt upgrade
apt install git figlet
git clone https://github.com/41Team/RoutersploitTermux
cd RoutersploitTermux
bash run.sh
```

It will take time about 30min+

# Before Installation

1. Reset termux first
2. Dont interfere the installation
3. Keep screen on
4. Have a good internet
5. Enough of space 1GB-700mb
6. Patience
7. Look all the progress for tracking error problems

# How to run routersploit

```
1. cd $HOME
2. rm -rf RoutersploitTermux ( optional )
3. cd routersploit
4. python rsf.py
```

Thank you to use my script (If occured a error or fail just send a issue) :)
