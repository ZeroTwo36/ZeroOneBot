import discord
import magic8ball as ball
import requests
import random
from discord.ext import commands


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.command(usage="zt!8ball <your question>",name="8ball")
    async def _8ball(self,ctx):
      await ctx.reply(random.choice(ball.list))

    @commands.command(usage="zt!meme")
    async def meme(self,ctx):
      r = requests.get("https://meme-api.herokuapp.com/gimme/dankmemes").json()
      embed = discord.Embed(title=r["title"],url=r["postLink"])
      embed.set_image(url=r["url"])
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Meme(bot))
