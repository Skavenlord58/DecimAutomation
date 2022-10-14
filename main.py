import discord
import os
from discord import Message
from discord.ext.commands import Context
from dotenv import load_dotenv
from discord.ext import commands

import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
TEXT_SYNTH_TOKEN = os.getenv('TEXT_SYNTH_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

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

client.run(TOKEN)
