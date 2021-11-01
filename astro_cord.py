#!/usr/bin/env python


import os
import pyfiglet
import platform
import discord

from colorama import *
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
print(Fore.CYAN + "\n\t\t [+]" + Fore.GREEN + "Github: @klevrboi\n")

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
script_non_embed = f'''
# non embed 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = f"{command_prefix}")
# Generated using Astro Cord
@client.event
async def on_ready():
    print("bot is online!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def hello(ctx):
    await ctx.send("Hey there!")

client.run(f"{token}")
'''

script = f'''
# embed script
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = f"{command_prefix}")
# Generated using Astro Cord
@client.event
async def on_ready():
    print("bot is online")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def hello(ctx):
    await ctx.send("Hey there!")

@client.command()
async def embed(ctx):
    sample_embed = discord.Embed(
        title = "This is a sample embed",
        colour = discord.Colour.red()
    )
    sample_embed.add_field(name = 'This is a sample field', value='This is a field value', inline=False)
    sample_embed.set_image(url=ctx.author.avatar_url)
    sample_embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
    sample_embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    sample_embed.set_footer(text="This is a footer")
    await ctx.send(embed = sample_embed)

client.run(f"{token}")

        '''
while True:
    embed_ask = input("[SYS] Do you want a sample discord embed in your file? [y/n] >> ")
    if embed_ask == "y":
        botfile = open(f"{final_bot_name}.py", "w")
        botfile.write(script)
        break;
    elif embed_ask == "n":
        botfile = open(f"{final_bot_name}.py", "w")
        botfile.write(
f'''
# non embed 
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = f"{command_prefix}")
# Generated using Astro Cord
@client.event
async def on_ready():
    print("bot is online!")

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def hello(ctx):
    await ctx.send("Hey there!")

client.run(f"{token}")
        
''')
        break;
    else:
        print(Fore.RED + "[ERROR!]" + Fore.YELLOW + "Please enter a valid answer: ")



print(Fore.GREEN + "[SUCCESS!]" + Fore.YELLOW + "The code is generated!")

