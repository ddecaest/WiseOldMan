import discord

from DiscordTokenProvider import DiscordTokenProvider
from OnMessageHandling import find_armour_handler, OnMessageHandling

# Set up the handlers
onMessageHandling = OnMessageHandling([find_armour_handler])

# TODO make singleton
token = DiscordTokenProvider().get_token()

client = discord.Client()

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

client.run(token)