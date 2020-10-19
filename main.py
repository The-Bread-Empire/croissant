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
from botty import botsection
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
#this is just certain dependencies that we may use later very standered
gamesc = 0
gamesr = random.randint(3, 6)


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
    
    status = random.randint(1, 6)
    if status == 1:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you eat"))
    elif status == 2:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))
    elif status == 3:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you eat cheese at 3am in the morning"))
    elif status == 4:
      await client.change_presence(activity=discord.Game(name="roasting you"))
    elif status == 5:
     await client.change_presence(activity=discord.Game(name="Ur mom"))
    else:
      await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))
    if message.guild.id == 691024705905229945:
      nospam1 = 1
      nospam2 = 4
    else:
      nospam1 = 1
      nospam2 = 2
    randomspeak = random.randint(nospam1, nospam2)
    if randomspeak == 1:
      if not message.author.id == 764150242438283335:

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
        await message.channel.send("you're a dissapointment")
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
            gamesr = random.randint(3, 6)

    if message.content == "Croissant eat the chat":
      while True:
        
        await message.channel.send("** ** \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ** **")
    
    if message.author.id == 424413952559153178:
      if message.author.guild.id == 691024705905229945:
        print("suppression disabled")
      else:
        #message.delete()
        #await message.channel.send("Your mean")
        print(f"{message.author} said: {message.content} (message suppresed in {message.channel.name} channel in the {message.guild.name} server)")
    if message.author.id == 764656938947969035:
      await message.channel.send(f"Shut up {message.author.name} or I will yeet a snake at you")
        
    if message.author.id == 515704039686668310:
        #message.delete()
        #await message.channel.send("Your mean")
        print(f"{message.author} said: {message.content} (message suppresed in {message.channel.name} channel in the {message.guild.name} server)")
    if message.author.id == 515704039686668310:
      randannoy = random.randint(1, 9)
      print(randannoy)
      if randannoy == 1:
        await message.channel.send(f"{message.author.name} thinks im a good bot :smirk:")
      elif randannoy == 2:
        await message.channel.send("I am a good bot :smirk:")
      
    
    answers = {
    "rock" : "skizzors",
    "skizzors" : "paper",
    "paper" : "rock"}
    if message.content in answers:
      if message.author.id == 764150242438283335:
        print("i challenged myself and lost")
      else:
        rps = random.randint(1, 4)
        if rps == 1:
          turn = "rock"
        elif rps == 2:
          turn = "paper"
        elif rps == 3:
          turn = "skizzors"
        else:
          turn = "gun"
        await message.channel.send(turn)
        if message.content == turn:
          await message.channel.send("Tie")
        elif answers[message.content] == turn:
          await message.channel.send("I lost")
        else:
          await message.channel.send("I won")
    if message.content == "roll":
      diceroll = random.randint(1, 6)
      await message.channel.send(f"You rolled a {diceroll}")
    if message.content == "join a server":
      await message.channel.send("Join code for croissant bot: https://discord.com/api/oauth2/authorize?client_id=764150242438283335&permissions=8&scope=bot")
    if (message.guild.id == 691024705905229945) or (message.guild.id == 761323034782597140):
      gunrand = random.randint(1, 100)
      bodyrand = random.randint(1, 4)
      if bodyrand == 1:
        bodypart = "foot"
      elif bodyrand == 2:
        bodypart = "leg"
      elif bodyrand == 3:
        bodypart = "eye"
      elif bodyrand == 4:
        bodypart = "hair"
      if gunrand == 1:
        await message.channel.send(f"I told you guns are dangerous. You shot yourself in the {bodypart}")
    if message.content == "destroy":
      channel_name = "art"
      existing_channel = discord.utils.get(message.guild.channels, name=channel_name)
      await existing_channel.delete()
    
    if message.content == "Kill me":
      discord.Member = message.author
      print(message.author)          
      await discord.Member.kick(reason = None)
    if message.author.id == 459905208160616459:
      await message.delete()
      print(f"now thats a bad mark you cant say: ||{message.content}||")

  
#below is just certain commands connecting the bot to the interent and connecting it to discord
make_website()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)


