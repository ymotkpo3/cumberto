import discord, re, keep_alive

client = discord.Client()

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

    if mensajeI:
        embed = discord.Embed(title="Corea del norte be like", )
        embed.set_image(url='https://c.tenor.com/HUd6Vl_d47cAAAAd/fbi.gif')
        await message.reply(embed=embed)
    if mensajeD:
        await message.reply("lo que te encanta:sweat_drops:")
    if mensajeH:
        await message.reply("lo que te encanta:eggplant:")

keep_alive.keep_alive()
client.run('ODMwNTM5NjQyOTY0Mjc5MzI4.YHIKUQ.HSUd2IxRrXV5-EvwS-uqWJfmX-s')