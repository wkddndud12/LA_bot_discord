import discord
import os

@client.event
async def on_ready():
    print("bot on!")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswish('!test'):
        await message.channel.send('test!')
        
        
access_token= os.environ["BOT_TOKEN"]
client.run(access_token)
