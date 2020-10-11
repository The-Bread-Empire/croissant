import discord
import os
import random
import time
from time import sleep
from make_website import make_website
from eventcommands import eventcommands
from commands import clear
from discord.ext import commands
import discord.utils
from datetime import datetime
from os import system, name

#this is just certain dependencies that we may use later very standered
gamesc = 0
gamesr = random.randint(3, 9)


client = discord.Client()


@client.event
async def on_ready():
    clear()
    sleep(1)
    print("I'm online")
    sleep(1)
    print(f"username: {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))


fish = "fish"
rank = "!rank"
@client.event
async def on_message(message):
    

    status = random.randint(1, 5)
    if status == 1:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you eat"))
    elif status == 2:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))
    elif status == 3:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you piss"))
    elif status == 4:
      await client.change_presence(activity=discord.Game(name="roasting you"))
    else:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    randomspeak = random.randint(1, 2)
    if randomspeak == 1:
        if message.content in eventcommands:
          await message.channel.send(eventcommands[message.content])
          #about 40 of the commands come from th 2 lines of code above this comment
        
        if fish in message.content:
            if message.content == "fishy sticks":
                print("spam prevented")
            else:
                await message.channel.send("fishy sticks")


        if (message.content == "hello") or (message.content == "hi"):
            hellorand = random.randint(1, 5)
            if hellorand == 1:
                await message.channel.send("howdy")
            elif hellorand == 2:
                await message.channel.send("lemme in ur house")
            elif hellorand == 3:
                await message.channel.send("don't bother me")
            elif hellorand == 4:
                await message.channel.send("nOOO")
            else:
                await message.channel.send("im out, NOPE")
    
        randomspeak = random.randint(1, 2)
    if rank in message.content:
      print(f"{message.author} sent the message")
      if message.content == "!rank":
        await message.channel.send("your a dissapointment")
      else:
       print("Someone is trying to surpass you")
    
    if (message.content == "games") and (
            message.channel.id == 761325921029586974):
        global gamesc
        global gamesr
        gamesc = gamesc + 1
        print(gamesc)

        print(f"{gamesr} till next games")
        if gamesc >= gamesr:
            gamesc = 0
            await message.channel.send("games")
            gamesr = random.randint(3, 9)

    if message.content == "Croissant eat the chat":
      for i in range(100):
        if message.author.id == 547942699572002836: 
          await message.channel.send("** ** \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ** **")
          
    if message.author.id == 424413952559153178:
      if message.guild.id == 691024705905229945:
        print("suppression disabled")
      else:
        
      #await message.channel.send("Your mean")
        print(f"{message.author} said: {message.content} (message suppresed in {message.channel.name} channel in the {message.guild.name} server)")
    if message.author.id == 589309749141569554:
      await message.channel.send(f"Shut up {message.author.name} or I will yeet a snake at you")
    
 


#below is just certain commands connecting the bot to the interent and connecting it to discord
make_website()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
