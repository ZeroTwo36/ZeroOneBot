from discord.ext import commands


class ZeroOne(commands.AutoShardedBot):
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)

    def setup(self):
        cogs = [
            "cogs.anime",
            "cogs.events",
            "cogs.admin",
            "cogs.economy",
            "cogs.memes",
            "cogs.images",
            "cogs.moderation"
        ]
        for cog in cogs:
            self.load_extension(cog)
