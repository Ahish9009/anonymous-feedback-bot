import os
import random, discord
from discord.ext import commands

client = discord.Client()

TOKEN = os.getenv('DISCORD_TOKEN')
FEEDBACK_CHANNEL = int(os.getenv('TARGET_CHANNEL'))
TEST_FEEDBACK_CHANNEL = int(os.getenv('TEST_CHANNEL'))
ADMIN_ID = int(os.getenv('ADMIN_ID')) 
TEST_TOKEN = os.getenv('TEST_TOKEN')
MSG_CNT = 0

pic = open("img/anon_dp.png", 'rb')
pfp = pic.read()

@client.event
async def on_ready():
    await client.user.edit(avatar=pfp)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    colors = [
            0x000000,
            0x0000FF,
            0x00FF00,
            0x00FFFF,
            0xFF0000,
            0xFF00FF,
            0xFFFF00,
            0xFFFFFF,
            0x0000BB,
            0x00BB00,
            0x00BBBB,
            0xBB0000,
            0xBB00BB,
            0xBBBB00,
            0xBBBBBB
            ]

    if TEST_TOKEN in message.content:
        channel = client.get_channel(TEST_FEEDBACK_CHANNEL)
    else:
        channel = client.get_channel(FEEDBACK_CHANNEL)
    user = client.get_user(ADMIN_ID)
    if "Direct Message" in str(message.channel):
        if len(message.attachments) == 0:
            return
        global MSG_CNT
        embed = discord.Embed(title="Anonymous", description="#"+str(MSG_CNT)+"\n"+message.content, color=random.choice(colors))
        await user.send("Sent by: "+str(message.author))
        for i in range(len(message.attachments)):
            await channel.send("#"+str(MSG_CNT+i), embed=embed.set_image(url=message.attachments[i].url))

        MSG_CNT += len(message.attachments)

client.run(TOKEN)
