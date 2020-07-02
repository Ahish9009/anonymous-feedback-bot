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

pic = open("img/anon_dp.png", 'rb')
pfp = pic.read()

@client.event
async def on_ready():
    client.user.edit(avatar=pfp)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    embed=discord.Embed(title="Anonymous", description=message.content, color=0xFFFF00)
    channel = client.get_channel(FEEDBACK_CHANNEL)
    user = client.get_user(ADMIN_ID)
    if "Direct Message" in str(message.channel):
        # print(message.author)
        # print(message.channel)
        # await channel.send(message.content)
        await user.send(str(message.author))
        await channel.send(embed=embed.set_image(url=message.attachments[0].url))


client.run(TOKEN)
