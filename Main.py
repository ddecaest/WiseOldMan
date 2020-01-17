import os
import discord
from dotenv import load_dotenv

from OnMessageHandling import find_armour_handler, OnMessageHandling
from RunescapeWikiScraper import get_armour

# Set up the discord client
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

# Set up the handlers
onMessageHandling = OnMessageHandling([find_armour_handler])

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    responses = onMessageHandling.handle_message(message)
    for response in responses:
        if response != '':
            await message.channel.send(response)
    return

# Make it go!
client.run(token)