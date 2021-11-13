import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    
    @commands.command(usage="zt!whois [@member]")
    async def whois(self,ctx,member:discord.Member=None):
        if not member:
            member = ctx.author

        embed = discord.Embed(color=member.color)
        embed.description=f'Displaying user Information for {member}'
        embed.add_field(name="ID",value=member.id)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="On Mobile?",value=member.is_on_mobile())
        if member.voice:
            embed.add_field(name="Voice State",value=member.voice.channel.name)
        
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Moderation(bot))
