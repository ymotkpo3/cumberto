import discord, re
import os
from dotenv import load_dotenv
client = discord.Client(intents=discord.Intents.all())

load_dotenv()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    mensaje1 = message.content.lower()
    mensajeD = re.findall('cum', mensaje1)
    mensajeH = re.findall('pija', mensaje1)
    mensajeI = re.findall('creo que', mensaje1)
    mensajej = re.findall('caca', mensaje1)

    if mensajeI:
        embed = discord.Embed(title="Corea del norte be like", )
        embed.set_image(url='https://c.tenor.com/HUd6Vl_d47cAAAAd/fbi.gif')
        await message.reply(embed=embed)
    if mensajeD:
        await message.reply("lo que te encanta:sweat_drops:")
    if mensajeH:
        await message.reply("lo que te encanta:eggplant:")
    if mensaje:
        await message.reply("lo que a Fede le encanta:poop:")

client.run(os.getenv('TOKEN'))
