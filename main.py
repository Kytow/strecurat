from random import *
from colorama import Fore, Back, Style
from os import startfile, system, name, write
import subprocess
from mcstatus import MinecraftServer 
from pyfiglet import *
import sys
import time

# Clear

def clear():
    if name == 'nt':
        _ = system('cls')

clear()

print(figlet_format("Strecurat \n"))

print(Fore.WHITE + "1.Recherche" + Fore.BLUE + " EU" + Fore.WHITE + "   2.Recherche" + Fore.LIGHTRED_EX + " US \n" + Fore.WHITE)

try:
    reponse = int(input())
except:
    print(Fore.RED + "Le choix doit être un chiffre !")
    print(Fore.RED + "Le programme va quitter dans 3 secondes")
    time.sleep(3)
    quit()

if reponse == 1:
    ip = "3.124.142.205"

if reponse == 2:
    ip = "3.134.125.175"

# Réponses invalides

if reponse >= 3:
    print(Fore.RED + "Erreur ! : Le chiffre doit être 1 ou 2")
    print(Fore.RED + "Le programme va quitter dans 3 secondes")
    time.sleep(3)
    quit()

if reponse <= 0:
    print(Fore.RED + "Erreur ! : Le chiffre doit être 1 ou 2")
    print(Fore.RED + "Le programme va quitter dans 3 secondes")
    time.sleep(3)
    quit()

with open('ressources/ip_temp.txt', 'w') as f:
    f.write(ip)

clear()

print(Fore.YELLOW + "Combien de fenêtres de recherche voulez vous ouvrir ?")

fenetres = int(input())

for i in range(fenetres):
    os.system('start loop.cmd')