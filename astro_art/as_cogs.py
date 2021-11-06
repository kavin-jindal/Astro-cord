from colorama import *
def cogs_file():

    #!/usr/bin/env python


    import os
    import pyfiglet
    import platform
    import discord
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
    print(Fore.CYAN + "\n\t\t [!]" + Fore.GREEN + "This program generates discord.py bots WITH cogs.")



    user_bot_name = input("[SYS] Enter the bot's name>> ")
    final_bot_name = user_bot_name.replace(" ", "_")

    # Strings
    while True:
        command_prefix = input("[SYS] Enter the command prefix for the bot>> ")
        if command_prefix == " ":
            print(Fore.RED + "[Error!] Enter a valid prefix!")
        elif command_prefix == "":
            print(Fore.RED + "[Error!] Enter a valid prefix!")
        else:
            break


    token = input("[SYS] Enter the bot token >> ")
    os.makedirs(f"{final_bot_name}/cogs")
    botfile = open(f"{final_bot_name}/cogs/start.py", "w")
    botfile_main = open(f"{final_bot_name}/main.py", "w")
    readstart = open("astro_cord_files/startcode.py", 'r')
    botfile.write(readstart.read())
    botfile_main.write(f"""
import discord
from discord.ext import commands
import os
from discord.utils import get
import praw
from discord.ext.commands import Bot
import platform
import asyncio
from discord import Intents


intents = Intents.all()

client = commands.Bot(command_prefix='{command_prefix}')""" + """\n
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'```Loaded {extension} extension```')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'```Unloaded `{extension}` extension```')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


""" + f"""
client.run(f'{token}')
""")
    print("generated!")