# Hi, here you can modify this repo with your code!
# How? Just fork this repo, add your files and you've done!
# When you've finish, send in #opensrc-pull into the discord server, the link of your fork repo, and in the less time, a mod adds your code here! have fun!
# Discord Server = https://discord.gg/ZcErEwmVYu

import discord
from discord import Client
from discord.ext import commands, tasks

token = "we have a proper bot, don't edit here."

@client.event
async def on_ready():
    print(f"Ready")
    
    
client.run(token)
