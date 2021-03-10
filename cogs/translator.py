# works with only gooletrans version 3.1.0a0
from googletrans import Translator
from discord.ext import commands

class Translator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()
        
    @commands.command()
    async def translate(self,ctx,lang,*,args):
        try:
            
            a = self.translator.translate(args, dest=lang)
            #await ctx.send(a.text)
            embed = discord.Embed(title='Translator', color=0xC01FE4)
            embed.add_field(name=f"Translated: {args} to", value=f'{lang}', inline=False)
            embed.add_field(name="Content: ", value=f'{a.text}', inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send("Brain.exe stopped working")

            
    @commands.command()
    async def detect(self,ctx,*,message):
        try:
            x = self.translator.detect(message)
            print(x.confidence)
            embed = discord.Embed(title="Language Detector", color=0XC01EF4)
            embed.add_field(name='***Language:***', value=x.lang, inline=False)
            await ctx.send(embed=embed)    
        except:
            await ctx.send("Error 404 Brain not found!")
            
def setup(bot):
    bot.add_cog(Translator(bot))            
