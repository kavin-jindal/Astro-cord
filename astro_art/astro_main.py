#!/usr/bin/env python


import os
import pyfiglet
import platform
import discord
import as_cogs
from colorama import *

import astro_cord

if platform.system() == "Linux":
    os.system("clear")
elif platform.system() == "Windows":
    os.system('cls')
else:
    pass

init()
print(Fore.CYAN + """

░█████╗░░██████╗████████╗░█████╗░  ░█████╗░░█████╗░██████╗░██████╗░
██╔══██╗██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗
███████║╚█████╗░░░░██║░░░██║░░██║  ██║░░╚═╝██║░░██║██████╔╝██║░░██║
██╔══██║░╚═══██╗░░░██║░░░██║░░██║  ██║░░██╗██║░░██║██╔══██╗██║░░██║
██║░░██║██████╔╝░░░██║░░░╚█████╔╝  ╚█████╔╝╚█████╔╝██║░░██║██████╔╝
╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░╚════╝░  ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
""")

print(Fore.CYAN + "[SYS]" + Fore.GREEN + " Welcome to Astro Cord!" + Fore.GREEN)

print(Fore.CYAN + "\n\t\t [+]" + Fore.GREEN + "Developed by: Kavin Jindal")
print(Fore.CYAN + "\n\t\t [+]" + Fore.GREEN + "Github: @kavin-jindal\n")


while True:
    menu_input = input(" [=] Write 1 if you want to generate a bot with cogs, \n or write 2 if you want to generate a bot without cogs >> ")
    if menu_input == "1":
        as_cogs.cogs_file()
        break
    elif menu_input == "2":
        astro_cord.astro_normal()
        break
    else:
        print(Fore.RED + "[!] Invalid Input, try again")
        

print(' ')
    