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
# FEEDBACK_CHANNEL = 728019657671311370
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

    channel = client.get_channel(FEEDBACK_CHANNEL)
    user = client.get_user(ADMIN_ID)
    if "Direct Message" in str(message.channel):
        if len(message.attachments) == 0:
            return
        global MSG_CNT
        embed=discord.Embed(title="Anonymous", description="#"+str(MSG_CNT)+"\n"+message.content, color='0xFFFF00')
        MSG_CNT += 1
        await user.send(str(message.author))
        await channel.send(embed=embed.set_image(url=message.attachments[0].url))


client.run(TOKEN)
