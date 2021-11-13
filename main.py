from bot import ZeroOne
from dotenv import load_dotenv
import os
from keep_alive import keep_alive
import discord
from discord.ext.commands import CommandOnCooldown
import json

load_dotenv()

def get_prefix(bot,message):

  with open("prefixes.json") as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

token = os.getenv("TOKEN")

client = ZeroOne(command_prefix=get_prefix,case_insensitive=True)
client.remove_command("help")

@client.command()
async def help(ctx):
  embed = discord.Embed(title=f"ZeroOne | Help | `{get_prefix(client,ctx)}`")
  for command in client.commands:
    if not "money" in command.name:
      embed.add_field(name=command.name,value=f"Aliases: {' '.join(command.aliases)}\nUsage:`{command.usage}`".replace("zt!",get_prefix(client,ctx)))
  await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f'Woah there! Slow it down Bro. This Command is on cooldown. Try again in {round(round(error.retry_after, 2)/60)} Minutes')

@client.event
async def on_guild_join(guild):
  
  with open("prefixes.json") as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = "zt!"

  with open("prefixes.json","w+") as f:
    json.dump(prefixes,f)



@client.event
async def on_ready():
    client.setup()
    for guild in client.guilds:
      print(guild.id)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"over {len(client.guilds)} Servers | zt!help"))

keep_alive()
client.run(token)