# Hi, here you can modify this repo with your code!
# How? Just fork this repo, add your files and you've done!
# When you've finish, send in #opensrc-pull into the discord server, the link of your fork repo, and in the less time, a mod adds your code here! have fun!
# Discord Server = https://discord.gg/ZcErEwmVYu

import discord
from discord import Client
from discord.ext import commands, tasks
from datetime import datetime

token = "we have a proper bot, don't edit here."
bot.launch_time = datetime.utcnow()

@client.event
async def on_ready():
    print(f"Ready")

@client.command
async def uptime(ctx):
    delta_uptime = datetime.utcnow() - bot.launch_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    await ctx.send(f"{days}d, {hours}h, {minutes}m, {seconds}s")

@client.command
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start)
    await message.edit(content='Pong! {:.2f}ms.'.format(duration))

client.run(token)
