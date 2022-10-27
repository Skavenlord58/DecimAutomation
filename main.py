import discord
import os
from discord import Message
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext import commands
from pythonping import ping

import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')
CLUSTER_LOCATION = os.getenv('CURRENT_LOCATION')

LOCATIONS = {
    'Germany North': '51.116.56.0',
    'Germany West Central': '51.116.152.0'
}

client = commands.Bot(command_prefix=PREFIX)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def ping(ctx: Context):
    m = await ctx.send(f'Ping?')
    ping = int(str(m.created_at - ctx.message.created_at).split(".")[1]) / 1000
    await m.edit(content=f'Pong! Latency is {ping}ms. API Latency is {round(client.latency * 1000)}ms.')
    pass

@client.command()
async def azurestatus(ctx: Context):
    test = discord.Embed(
        title="Azure Status",
        description="Shows current Azure cluster status.",
        color=discord.Colour.dark_purple()
    )
    
    test.add_field(name=f'Current location of cluster:', value=CLUSTER_LOCATION)
    azping = await ping(LOCATIONS[CLUSTER_LOCATION], count=3)
    test.add_field(name=f'Ping of {CLUSTER_LOCATION}:', value=f'WIP/NIY: Check for yourself: https://cloudpingtest.com/azure')
    
    await ctx.send(embed=test)

client.run(TOKEN)
