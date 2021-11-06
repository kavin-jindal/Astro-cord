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

client = commands.Bot(command_prefix=f'')
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



client.run(f'')