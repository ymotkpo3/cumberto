import discord
import re

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    mensaje1 = message.content.lower()
    mensajeR = re.findall(' cum ', mensaje1)

    if mensajeR:
        await message.reply("lo que te encanta:sweat_drops:")

client.run('ODMwNTM5NjQyOTY0Mjc5MzI4.YHIKUQ.1qr7Koqf4hnjGjkEEVpO526Napg')

