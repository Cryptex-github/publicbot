import discord

from discord.ext import commands

class Misc(commands.Cog):
    """Some miscellaneous commands"""
    def __init__(self, bot):
        self.bot = bot
        
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

def setup(bot):
    bot.add_cog(Misc(bot))
