import discord
from discord.ext import commands
from discord import DMChannel
import random
from datetime import datetime
from discord import Intents

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online')
        await self.client.change_presence(status = discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='Developed by Astro Inc. || m!help'))
        
    @commands.command()
    async def test(self, ctx):
        await ctx.send('Hello there')

    

def setup(client):
    client.add_cog(Start(client))
