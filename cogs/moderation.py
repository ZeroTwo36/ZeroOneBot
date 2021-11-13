import discord
from discord.ext import commands
import json

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def prefix(self,ctx,pre="zt!"):
      
      with open("prefixes.json") as f:
        prefixes = json.load(f)

      prefixes[str(ctx.guild.id)] = pre
      await ctx.send(f"Prefix updated to `{pre}`!")
      with open("prefixes.json","w+") as f:
        json.dump(prefixes,f)
    

def setup(bot):
    bot.add_cog(Moderation(bot))
