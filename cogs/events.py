import discord
from discord.ext import commands
import json


def get_prefix(bot,message):

  with open("prefixes.json") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
      if message.mentions[0] == self.bot.user:
        await message.channel.send(f'My Prefix here is `{get_prefix(self.bot,message)}`')
    

def setup(bot):
    bot.add_cog(Events(bot))
