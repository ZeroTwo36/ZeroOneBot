import requests
import discord
from discord.ext import commands

class Images(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(usage="zt!cat",aliases=["meow"])
  async def cat(self,ctx):
    meow = requests.get("http://aws.random.cat/meow").json()["file"]
    embed = discord.Embed(title="Meow",color=discord.Color.random())
    embed.set_image(url=meow)
    await ctx.send(embed=embed)
    
  @commands.command(usage="zt!cat",aliases=["meow"])
  async def cat(self,ctx):
    meow = requests.get("http://aws.random.cat/meow").json()["file"]
    embed = discord.Embed(title="Meow",color=discord.Color.random())
    embed.set_image(url=meow)
    await ctx.send(embed=embed)
    
  @commands.command(usage="zt!dog",aliases=["woof"])
  async def dog(self,ctx):
    meow = requests.get("https://random.dog/woof.json").json()["url"]
    embed = discord.Embed(title="Woof",color=discord.Color.random())
    embed.set_image(url=meow)
    await ctx.send(embed=embed)
    
    
  @commands.command(usage="zt!fox",aliases=["floof"])
  async def fox(self,ctx):
    meow = requests.get("https://randomfox.ca/floof").json()["image"]
    embed = discord.Embed(title="Floof",color=discord.Color.random())
    embed.set_image(url=meow)
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Images(bot))