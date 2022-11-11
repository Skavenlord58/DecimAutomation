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
    AZSTATUS = "OK"
    test.add_field(name=f'Is azure up?', value=AZSTATUS, inline=0)
    test.add_field(name=f'Current location of cluster:', value=CLUSTER_LOCATION)
    test.add_field(name=f'Ping of {CLUSTER_LOCATION}:', value=f'WIP/NIY: Check for yourself: https://cloudpingtest.com/azure')
    
    await ctx.send(embed=test)

@client.command()
async def isdecimup(ctx: Context):
    m = await ctx.send("Checking... (if no change, he's down)")
    decim = await client.fetch_user("DecimBOT 2.0#8467")
    await decim.send("$autostat")

    def check(m):
        return "OK" in m.content.split(";")[0]

    msg = await client.wait_for("message", check=check)
    if msg:
        await m.edit(content="DecimBot is up.")
    else:
        pass

client.run(TOKEN)
