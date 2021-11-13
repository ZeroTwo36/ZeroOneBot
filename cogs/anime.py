import animec
import discord
from datetime import datetime
from discord.ext import commands


class Anime(commands.Cog):
    """Anime Commands for Weens"""
    def __init__(self,bot):
        self.bot=bot

    @commands.command(usage="zt!anime [query]")
    async def anime(self,ctx,*,query):
        try:
            anime = animec.Anime(query)
        except:
            return await ctx.send(embed=discord.Embed(description="No corresponding anime found for Query",color=discord.Color.red()))
    
        embed = discord.Embed(title=anime.title_english,url=anime.url,description=f'{anime.description[:200]}...',color=discord.Color.random())
        embed.add_field(name="Episodes",value=str(anime.episodes))
        embed.add_field(name="Rating",value=str(anime.rating))
        embed.add_field(name="Broadcast",value=str(anime.broadcast))
        embed.add_field(name="Status",value=str(anime.status))
        embed.add_field(name="Type",value=str(anime.type))
        embed.add_field(name="NSFW Status",value=str(anime.is_nsfw()))
        embed.set_thumbnail(url=anime.poster)
        await ctx.send(embed=embed)

    @commands.command(aliases=["char"],usage="zt!character [Query]")
    async def character(self,ctx,*,query):
        try:
            anime = animec.Charsearch(query)
        except:
            return await ctx.send(embed=discord.Embed(description="No corresponding Character found for Query",color=discord.Color.red()))
        embed = discord.Embed(title=anime.title,url=anime.url,color=discord.Color.random())
        embed.set_image(url=anime.image_url)
        embed.set_footer(text=f', '.join(list(anime.references.keys())[:2]))
        await ctx.send(embed=embed)

    @commands.command(usage="zt!waifu")
    async def waifu(self,ctx):
        _waifu = animec.Waifu.waifu()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=_waifu)
        await ctx.send(embed=embed)

        
    @commands.command(usage="zt!neko")
    async def neko(self,ctx):
        _waifu = animec.Waifu.neko()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=_waifu)
        await ctx.send(embed=embed)


    @commands.command(usage="zt!shinobu")
    async def shinobu(self,ctx):
        _waifu = animec.Waifu.shinobu()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=_waifu)
        await ctx.send(embed=embed)
    
    @commands.command(usage="zt!aninews <optional:Count>")
    async def aninews(self,ctx,amount:int=3):
        
        news = animec.Aninews(amount)
        links = news.links
        titles = news.titles
        descs = news.description

        embed = discord.Embed(title = "Latest Anime News",color=discord.Color.random(),timestamp=datetime.utcnow())
        embed.set_thumbnail(url=news.images[0])
        for i in range(amount):
            embed.add_field(name=f'{i+1}) {titles[i]}',value=f'{descs[i][:200]}...\n[Read More]({links[i]})',inline=False)
        
        await ctx.send(embed = embed)
        
        

        
def setup(bot):
    bot.add_cog(Anime(bot))