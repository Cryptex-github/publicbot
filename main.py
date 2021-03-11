# Hi, here you can modify this repo with your code!
# How? Just request to be a collaborator for this code, in our discord server (#opensrc-req), sending your github profile link, and wait for a mod reply!
# Discord Server = https://discord.gg/ZcErEwmVYu

import discord
from discord import Client
from discord.ext import commands, tasks
import aiosqlite
import os

token = "we have a proper bot, don't edit here."

# Connection to a sqlite database will be where most the work happens
async def _check_prefix(bot,message):
    async with aiosqlite.connect("prefix.db") as db:
        prefix  = ["mb! ", "Mb! "]
        cur = await db.cursor()
        await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
        await cur.execute("SELECT * FROM Streams WHERE guild_id = ?", (message.guild.id,))
        result_prefix = await cur.fetchone()
        if result_prefix:
            return result_prefix
        else:
            return prefix

bot = commands.Bot(command_prefix=_check_prefix)

# Loading cog files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print('we are ready to go. logged in as {0.user}'.format(bot))

# If bot is mentioned, it shows the prefix for that guild    
@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            #cur.execute('CREATE TABLE Transactions(Date TEXT, Number TEXT, Type TEXT, From TEXT, To TEXT, Amount REAL)')
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await cur.execute("SELECT prefix FROM Streams WHERE guild_id = ?", (message.guild.id,))
            result_prefix = await cur.fetchone()
            if result_prefix is None:
                result_prefix = 'mb!'
            else:
                result_prefix = result_prefix[0]    
        await message.channel.send(f"My Prefix for this guild is {result_prefix}")
    else:                 
        await bot.process_commands(message)       

# Change prefix command could be improved         
@bot.command()
@commands.has_permissions(administrator= True)
async def prefix(ctx,*,prefix=None):
    if prefix is None:
        await ctx.send("WTF ARE YOU DOING LMAO")
    else:
        prefix = prefix + " "
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await db.commit()
            await cur.execute("update Streams SET prefix = ? where guild_id=?", (prefix, ctx.message.guild.id))
            await db.commit()
        await ctx.send(f"I Have changed the prefix of this guild to {prefix} ")
        async with aiosqlite.connect("prefix.db") as db:
            cur = await db.cursor()
            await cur.execute('create table if not exists Streams(guild_id TEXT,prefix TEXT)')
            await db.commit()
            await cur.execute("SELECT * FROM Streams WHERE guild_id = ?", (ctx.message.guild.id,))
            await db.commit()
            result_prefix = await cur.fetchone()
            if result_prefix is None:
                await cur.execute('INSERT into Streams(guild_id, prefix) values(?,?)',(ctx.message.guild.id,prefix))
                await db.commit()        
    
client.run(token)
