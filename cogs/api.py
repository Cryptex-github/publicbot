import aiohttp

from discord.ext import commands

class Api(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    
    @commands.command()
    async def joke(self, ctx):
        """Returns a random joke"""
        api = "https://official-joke-api.appspot.com/jokes/random"
        async with aiohttp.request("GET", api) as r:
            result = await r.json()
            await ctx.send("\n".join([result["setup"], result["punchline"]]))
            
    @commands.command()
    async def dadjoke(self, ctx):
        """Returns a random dadjoke"""
        api = "https://icanhazdadjoke.com/"
        async with aiohttp.request("GET", api, headers = {"Accept": "text/plain"}) as r:
            result = await r.text()
            await ctx.send(result)
            
    @commands.command()
    async def cat(self, ctx):
        """Returns a random image of a cat"""
        api = "https://aws.random.cat/meow"
        async with aiohttp.request("GET", api) as r:
            result = await r.json()
            embed = discord.Embed(title = "Random cat image...", colour = discord.Colour.random())
            embed.set_image(url = result["file"])
            await ctx.send(embed=embed)
            
    @commands.command()
    async def dog(self, ctx):
        """Returns a random image of a dog"""
        api = "https://random.dog/woof.json"
        async with aiohttp.request("GET", api) as r:
            result = await r.json()
            embed = discord.Embed(title="Random dog image...", color = discord.Color.random())
            embed.set_image(url = result["url"])
            await ctx.send(embed=embed)
        
        
    @commands.command()
    async def fox(self, ctx):
        """Returns a random image of a fox"""
        api = "https://randomfox.ca/floof/"
        async with aiohttp.request("GET", api) as r:
            result = await r.json()
            embed = discord.Embed(title = "Random fox image...", color = discord.Color.random())
            embed.set_image(url=result["image"])
            await ctx.send(embed = embed) 
        
    @commands.command(aliases=["uf"])
    async def uselessfact(self, ctx):
        """Returns a useless fact that you're probably not gonna care about"""
        api = "https://useless-facts.sameerkumar.website/api"
        async with aiohttp.request("GET", api) as r:
            result = await r.json()
            embed = discord.Embed(title = "Here's your random useless fact...", description = result["data"], color = discord.Colour.random())
            await ctx.send(embed = embed)
        
def setup(bot):
    bot.add_cog(Api(bot))
