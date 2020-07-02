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

@client.event
async def on_ready():
    # print(f'{client.user} has connected to Discord!')
    # for guild in client.guilds:
        # if guild.name == GUILD:
            # break

    # print(
        # f'{client.user} is connected to the following guild:\n'
        # f'{guild.name}(id: {guild.id})'
    # )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')
    pass

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    embed=discord.Embed(title="Anonymous", description=message.content, color=0xFFFF00)
    channel = client.get_channel(FEEDBACK_CHANNEL)
    if "Direct Message" in str(message.channel):
        # print(message.author)
        # print(message.channel)
        # await channel.send(message.content)
        await channel.send(embed=embed.set_image(url=message.attachments[0].url))


client.run(TOKEN)
