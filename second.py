from random import *
from colorama import Fore, Back, Style
from os import startfile, system, name
import subprocess
from mcstatus import MinecraftServer 
from pyfiglet import *
import sys
import time

with open("ip_temp.txt") as f:
    ip = f.readlines()[0]

def serverchecker():
    portngrok = randrange(10000,20000)
    ipduserveur = ip + ':' + str(portngrok)
    server = MinecraftServer.lookup(ipduserveur) 
    try:
        status = server.status() 
    except:
        print(Fore.RED + 'Le serveur ' + ipduserveur + ' ne fonctionne pas')
        pass
    try:
        print(Fore.GREEN + ipduserveur + ' Joueurs connectés : {0}. Ping : {1}.'.format(status.players.online, status.latency))
        os.system('mcstatus ' + ipduserveur + ' status > server_temp.txt')
        with open("server_temp.txt") as f:
            servertempfiles = f.readlines()[0]
        with open('server-list.txt', 'a') as f:
            f.write(ipduserveur + ' Joueurs connectés : {0}. Ping : {1}. '.format(status.players.online, status.latency) + servertempfiles + "\n")
        
    except:
        pass

while True:
    serverchecker()
