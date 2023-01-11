import disnake
import os
from disnake import Message
from disnake.ext.commands import Context
from dotenv import load_dotenv
from disnake.ext import tasks, commands
import requests

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = os.getenv('BOT_PREFIX')

# add intents for bot and command prefix for classic command support
intents = disnake.Intents.all()
client = disnake.ext.commands.Bot(command_prefix=PREFIX, intents=intents)

# running job check
@tasks.loop(seconds = 30)
async def check_jobs_loop():
    print("Running job checker!")
    pass
    
@check_jobs_loop.before_loop
async def before_check_jobs():
    print('Waiting...')
    await client.wait_until_ready()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # print(check_cronjobs())
    if check_jobs_loop.start():
        print("DecimAutomation running...")
    else:
        print("DecimAutomation failed to run.")
    

## other DecimAutomation platform commands
@client.command()
async def ping(ctx: Context):
    m = await ctx.send(f'Ping?')
    ping = int(str(m.created_at - ctx.message.created_at).split(".")[1]) / 1000
    await m.edit(content=f'Pong! Latency is {ping}ms. API Latency is {round(client.latency * 1000)}ms.')
    pass

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


## parsing incoming messages
@client.event
async def on_message(m: Message):
    if not m.content:
        pass
    elif m.content[0] == PREFIX:
        # needed for commands to work    
        await client.process_commands(m)
    elif str(m.author) != "DecimAutomation#4633":
        # you can add your automatic reactions
        # check decimbot2 for inspiration
        pass

client.run(TOKEN)
