import discord
import json
from discord.ext import commands
import random

TEAM = [
  899722893603274793,
  883004373519716372,
  685180177419993102
]

crime_success = [
  "You stole <en> ZeroBux from a small Café",
  "You commited Tax Fraud and earned <en> ZeroBux",
  "You robbed a bank and got <en> ZeroBux!"
]
crime_fail = [
  "You were caught whilst trying to steal some Gum and got fined with <en> ZeroBux",
  "I caught you trying to steal from me and sued you for <en> ZeroBux",
  "While trying to rob me, *you* got robbed and lost <en> ZeroBux"
]

class Economy(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  async def update_bank(self,user,change=0,mode="wallet"):
    users = await self.get_bank_data()
    
    users[str(user.id)][mode] += change
    
    with open("mainbank.json","w+") as f:
      json.dump(users,f)

    balance = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]

    return balance

  async def open_account(self,user):
    with open("mainbank.json") as f:
      users = json.load(f)

    if(str(user.id) in users):
      return False

    users[str(user.id)] = {}
    users[str(user.id)]["wallet"] = 0
    users[str(user.id)]["bank"] = 0
    with open("mainbank.json","w+") as f:
      json.dump(users,f)

    return True

  async def get_bank_data(self):
    with open("mainbank.json") as f:
      users = json.load(f)
    return users 

  @commands.command()
  async def changemoney(self,ctx,member:discord.Member,amount=1):
    if not ctx.author.id in TEAM:
      return await ctx.send("U dont have adminstrator perms!")

    await self.open_account(member)
    await self.update_bank(member,amount,"bank")
    em = discord.Embed(color=0xFFC300)
    em.description = f":white_check_mark: Changed {member.name}'s Balance by {amount} ZeroBux !"
    await ctx.send(embed=em)



  @commands.command(aliases=["with"],usage="zt!withdraw <amount>")
  async def withdraw(self,ctx,amount:int=None):
    await self.open_account(ctx.author)
    if not amount:
      return await ctx.send("Please enter an amount to withdraw")

    balance = await self.update_bank(ctx.author)
    if amount > balance[1]:
      return await ctx.send("You don't have that much ZeroBux in your Wallet")

    if amount<0:
      return await ctx.send("Amount has to be positive!")

    await self.update_bank(ctx.author,amount)
    await self.update_bank(ctx.author,amount*-1,"bank")
    em = discord.Embed(color=0xFFC300)
    em.description = f":white_check_mark: You withdrew {amount} ZeroBux from your Bank!"
    await ctx.send(embed=em)

    
  @commands.command(aliases=["dep","dump"],usage="zt!deposit <amount>")
  async def deposit(self,ctx,amount:int=None):
    await self.open_account(ctx.author)
    if not amount:
      return await ctx.send("Please enter an amount to deposit")

    balance = await self.update_bank(ctx.author)
    if amount > balance[0]:
      return await ctx.send("You don't have that much ZeroBux in your Bank")

    if amount<0:
      return await ctx.send("Amount has to be positive!")

    await self.update_bank(ctx.author,amount*-1)
    await self.update_bank(ctx.author,amount,"bank")
    em = discord.Embed(color=0xFFC300)
    em.description = f":white_check_mark: You deposited {amount} ZeroBux onto your Bank!"
    await ctx.send(embed=em)
    
  @commands.command(aliases=["gift","give"],usage="zt!send [@member] [amount]")
  async def send(self,ctx,member:discord.Member=None,amount:int=None):
    await self.open_account(ctx.author)
    await self.open_account(member)
    if not amount:
      return await ctx.send("Please enter an amount to gift!")
    if not member:
      return await ctx.send("Please mention a Member!")
    balance = await self.update_bank(ctx.author)
    if amount > balance[1]:
      return await ctx.send("You don't have that much ZeroBux in your Bank")

    if amount<0:
      return await ctx.send("Amount has to be positive!")

    await self.update_bank(ctx.author,amount*-1,"bank")
    await self.update_bank(member,amount,"bank")
    em = discord.Embed(color=0xFFC300)
    em.description = f":white_check_mark: You gifted {amount} ZeroBux to {member.name}!"
    await ctx.send(embed=em)

  


  @commands.command(aliases=["bal"],usage="zt!balance")
  async def balance(self,ctx):
    await self.open_account(ctx.author)
    users = await self.get_bank_data()

    wallet = users[str(ctx.author.id)]["wallet"]
    bank = users[str(ctx.author.id)]["bank"]
    networth = wallet+bank

    em = discord.Embed(title=f"{ctx.author.name}'s Balance",color=ctx.author.color)
    em.add_field(name = "Wallet",value=f'{wallet} ZeroBux')
    em.add_field(name = "Bank",value=f'{bank} ZeroBux')
    em.add_field(name = "Net Worth",value=f'{networth} ZeroBux')
    await ctx.send(embed=em)

  @commands.command(usage="zt!beg")
  @commands.cooldown(1,1800,commands.BucketType.user)
  async def beg(self,ctx):
    
    await self.open_account(ctx.author)
    users = await self.get_bank_data()
    earnings = random.randrange(0,101)
    embed = discord.Embed(description=f"Someone gave you {earnings} ZeroBux!",color=0xFFC300)
    await ctx.send(embed=embed)
    users[str(ctx.author.id)]["wallet"] += earnings
    with open("mainbank.json","w+") as f:
      json.dump(users,f)

      
  @commands.command(usage="zt!crime")
  @commands.cooldown(1,1800,commands.BucketType.user)
  async def crime(self,ctx):
    print("crime")
    
    await self.open_account(ctx.author)
    users = await self.get_bank_data()
    earnings = random.randint(-101,101)
    print(earnings)
    if earnings <= 0:
      
      embed = discord.Embed(description=random.choice(crime_fail).replace("<en>",str(earnings)),color=0xFF0000)
      if users[str(ctx.author.id)]["wallet"] <= 0:
        users[str(ctx.author.id)]["bank"] += earnings
        
      else:      
        users[str(ctx.author.id)]["wallet"] += earnings
    else:
      embed = discord.Embed(description=random.choice(crime_success).replace("<en>",str(earnings)),color=discord.Color.green())

    await ctx.send(embed=embed)
    
    with open("mainbank.json","w+") as f:
      json.dump(users,f)

def setup(bot):
  bot.add_cog(Economy(bot))