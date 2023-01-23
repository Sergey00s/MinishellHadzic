import discord
from commands import Command
from dbmanage import Users

intents = discord.Intents()
intents = intents.all()
client = discord.Client(intents=intents)
users = Users("classes.db")

TOKEN="token"


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!nth'):
        cmd = Command(message.content)
        msg = cmd.run(message, users)
        if msg is not None:
            await message.channel.send(msg)

client.run(TOKEN)