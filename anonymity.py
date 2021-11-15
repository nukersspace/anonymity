import discord
from discord.ext import commands
import aiohttp
import os
from colorama import Fore
#LOL
token = 'tonken here gamor'
password = 'password here gamor'
prefix = '.'
command_prefix=prefix,
intents=discord.Intents.all(),
help_command=None

do_stuff = 0
amount = 5000000
client = commands.Bot(command_prefix = '.')

clear = os.system('cls;clear')
for x in range(amount):
  done = (((x + 1) / amount))
  do_stuff += 1 
  if done == 0.1:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■{Fore.WHITE}■■■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.2:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■{Fore.WHITE}■■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.3:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■{Fore.WHITE}■■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.4:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■{Fore.WHITE}■■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.5:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■{Fore.WHITE}■■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.6:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■■{Fore.WHITE}■■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.7:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■■■{Fore.WHITE}■■■ ' + str(int(done * 100)) + '%')
  elif done == 0.8:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■■■■{Fore.WHITE}■■ ' + str(int(done * 100)) + '%')
  elif done == 0.9:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■■■■■{Fore.WHITE}■ ' + str(int(done * 100)) + '%')
  elif done == 1.0:
    os.system('cls ; clear')
    print(f'{Fore.LIGHTGREEN_EX}■■■■■■■■■■ ' + str(int(done * 100)) + '%')
os.system('cls ; clear')

@client.event
async def on_ready():
    print('''

                                                       
  ##   #    #  ####  #    # #   # #    # # ##### #   # 
 #  #  ##   # #    # ##   #  # #  ##  ## #   #    # #  
#    # # #  # #    # # #  #   #   # ## # #   #     #   
###### #  # # #    # #  # #   #   #    # #   #     #   
#    # #   ## #    # #   ##   #   #    # #   #     #   
#    # #    #  ####  #    #   #   #    # #   #     #


[1] ^ghost | changes pfp to blank, and changes name to blank.
[2] ^leavegroup | leaves all group chats.
[3] ^leaveserver | leaves all servers.
[4] ^delfriends | removes all friends.
[5] ^anonymity | makes you completely anonymous (does all of the listed commands at once)

''')

@client.command()
async def ghost(ctx):
    await ctx.message.delete()
    with open('Avatars/spoof.png', 'rb') as f:
            try:
                await ctx.user.edit(password=password, username="᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼",avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
				
@client.command(name='group-leaver',
                aliase=['leaveallgroups', 'leavegroup', 'leavegroups', "groupleave", "groupleaver"])
async def _group_leaver(ctx):
    await ctx.message.delete()
    for channel in ctx.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
        
@client.command()
async def leaveserver(ctx):
    for guild in client.guilds:
        try:
                server = client.get_guild(guild.id)
                await server.leave()
        except:
          pass
@client.command()
async def delfriends(ctx):
    await ctx.message.delete()
    for relationship in ctx.user.relationships:
        if relationship is discord.RelationshipType.friend:
            await relationship.delete()




@client.event
async def anonymity(ctx):
 await ctx.message.delete()
 with open('Avatars/spoof.png', 'rb') as f:
            try:
                await ctx.user.edit(password=password, username="", avatar=f.read())
            except discord.HTTPException as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)

 for channel in ctx.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()
            
        for guild in client.guilds:
         try:
                server = client.get_guild(guild.id)
                await server.leave()
         except:
                pass
                
        for relationship in ctx.user.relationships:
          if relationship is discord.RelationshipType.friend:
            await relationship.delete()

            
            print(f"{Fore.MAGENTA} [SUCCESS]: {Fore.GREEN} Successfully became anonymous." + Fore.RESET)
            

client.run(token, bot=False)
