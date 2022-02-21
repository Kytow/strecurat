from random import randint
from colorama import Fore
from mcstatus import MinecraftServer

with open("ip_temp.txt") as f:
    ip = f.readlines()[0]


def serverchecker():
    portngrok = randint(10000, 20000)
    ipduserveur = ip + ':' + str(portngrok)
    server = MinecraftServer.lookup(ipduserveur)
    try:
        status = server.status()
    except:
        print(Fore.RED + 'The server ' + ipduserveur + " does not work")
        pass
    try:
        print(f"{Fore.GREEN}{ipduserveur} | Joueurs connectés : {status.players.online}. Ping : {status.latency}. Version : {status.version.name}")
        with open('server-list.txt', 'a') as f:
            f.write(
                f"{ipduserveur} | Joueurs connectés : {status.players.online}. Ping : {status.latency}. Version : {status.version.name} \n")
    except:
        pass


while True:
    serverchecker()
