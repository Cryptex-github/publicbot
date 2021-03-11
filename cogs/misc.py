import discord

from discord.ext import commands

# Image Manipulation
import cv2 as cv
from urllib.request import Request, urlopen
import numpy as np


class Misc(commands.Cog):
    """Some miscellaneous commands"""
    def __init__(self, bot):
        self.bot = bot

    def url_to_image(self,url, readFlag=cv.IMREAD_COLOR):
        # download the image, convert it to a NumPy array, and read the numpy array
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        resp = urlopen(req).read()
        image = np.asarray(bytearray(resp), dtype="uint8")
        image = cv.imdecode(image, readFlag)

        # return the image
        return image        
        
    @commands.command()
    @commands.guild_only() # Can't be used in DMs
    async def memberinfo(self, ctx, member: discord.Member = None):
        """Get info about a member"""
        async with ctx.typing():
            member = member or ctx.author()
            
            show_roles = ', '.join(
                [f"<@&{x.id}>" for x in sorted(user.roles, key = lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
            ) if len(user.roles) > 1 else 'None'
            
            embed = discord.Embed(colour = member.top_role.colour.value)
            embed.set_author(name = str(member))
            embed.add_field(name = "Nickname", value = member.nick if hasattr(member, "nick") else "None", inline = True)
            embed.add_field(name = "Account created", value = member.created_at.strftime("**%d/%m/%Y** at **%H:%M**"), inline = True)
            embed.add_field(name = "Joined this server", value = member.joined_at.strftime("**%d/%m/%Y** at **%H:%M**"), inline = True)
            embed.add_field(name = "Roles", value = show_roles, inline = False)
            embed.set_thumbnail(url = member.avatar_url)
            embed.set_footer(text = f"ID: {member.id}")
            
            await ctx.send(embed = embed)
            
    @command.command()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        """Shows info about the server"""
        guild = ctx.guild
        guild_created_on = guild.created_at.strftime("%d/%m/%Y")
        embed = discord.Embed(title = guild.name, description = f"Created on {guild_created_on}", colour = discord.Colour.random())
        embed.add_field(name = "Members", value = len(guild.members), inline = True)
        embed.add_field(name = "Roles", value = str(len(guild.roles)), inline = True)
        embed.add_field(name = "Channels", value = (f"Text channels: {len(guild.text_channels)}\nVoice channels: {len(guild.voice_channels)}"), inline = True)
        await ctx.send(embed=embed)
            
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, member: discord.Member = None):
        """Get a member's avatar"""
        member = member or ctx.author
        
        embed = discord.Embed(title = f"Avatar for {member.name}", description = f"[Link]({member.avatar_url})", colour = member.top_role.colour.value)
        embed.set_image(url = member.avatar_url)
        
        await ctx.send(embed = embed)
        
    @commands.command()
    @commands.guild_only()
    async def dm(self, ctx, member: discord.Member, *, message: str):
        """Make the bot send a message to the specified member"""
        try:
            await member.send(message)
        except discord.Forbidden:
            await ctx.send("This user might be having their DMs closed, or it's a bot.")
            await ctx.message.add_reaction("\U0000274c")

    @commands.command()
    async def canny(self,ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        else:
            member = member
        img = self.url_to_image(member.avatar_url)    
        canny = cv.Canny(img, 125, 175)
        cv.imwrite("new_image.jpg", canny)
        file=discord.File('new_image.jpg')
        await ctx.send(file=file)                

def setup(bot):
    bot.add_cog(Misc(bot))
