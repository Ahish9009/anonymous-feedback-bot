import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

FEEDBACK_CHANNEL = 727987265560903780
TEST_FEEDBACK_CHANNEL = 728019657671311370
ADMIN_ID = 540235460790976512
MSG_CNT = 0

pic = open("img/anon_dp.png", 'rb')
pfp = pic.read()

pic_count = 0

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

    if "TEST9009" in message.content:
        channel = client.get_channel(TEST_FEEDBACK_CHANNEL)
    else:
        channel = client.get_channel(FEEDBACK_CHANNEL)
    user = client.get_user(ADMIN_ID)
    if "Direct Message" in str(message.channel):
        if len(message.attachments) == 0:
            return
        global MSG_CNT
        embed=discord.Embed(title="Anonymous", description="#"+str(MSG_CNT)+"\n"+message.content, color=random.choice(colors))
        MSG_CNT += 1
        await user.send("Sent by: "+str(message.author))
        await channel.send("#"+str(MSG_CNT), embed=embed.set_image(url=message.attachments[0].url))


client.run(TOKEN)
