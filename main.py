from colorama import Fore
from os import system

# Clear


def clear():
    system('cls')


# ASCII
figlet = Fore.LIGHTYELLOW_EX + """
  _________ __                                             __   
 /   _____//  |________   ____   ____  __ ______________ _/  |_ 
 *_____  **   __*_  __ *_/ __ *_/ ___*|  |  *_  __ *__  **   __*
 /        *|  |  |  | */*  ___/*  *___|  |  /|  | *// __ *|  |  
/_______  /|__|  |__|    *___  >*___  >____/ |__|  (____  /__|  
        */                   */     */                  */      
"""
print(figlet.replace("*", chr(92)))

print(Fore.WHITE + "1.EU" + Fore.BLUE + " Search" + Fore.WHITE +
      "   2.US" + Fore.LIGHTRED_EX + " Search \n" + Fore.WHITE)

while True:
    try:
        reponse = int(input())
        if reponse == 1:
            ip = "3.124.142.205"
            break

        elif reponse == 2:
            ip = "3.134.125.175"
            break
        else:
            print(Fore.RED + "You need to do a choice between 1 and 2 !" + Fore.WHITE)
    except:
        print(Fore.RED + "This is not a number !" + Fore.WHITE)

with open('ip_temp.txt', 'w') as f:
    f.write(ip)

clear()

print(Fore.YELLOW + "How many server search windows do you want to open ? (more windows = faster)" + Fore.WHITE)

while True:
    try:
        fenetres = int(input())
        break
    except:
        print(Fore.RED + "This is not a number !" + Fore.WHITE)

for i in range(fenetres):
    system('start loop.bat')
