import discord
import os
import random
import time
from time import sleep
from make_website import make_website
from commands import clear
from discord.ext import commands
import discord.utils
from datetime import datetime
from os import system, name 
#this is just certain dependencies that we may use later very standered
gamesc = 0
gamesr = random.randint(4, 5)
client = discord.Client()

@client.event
async def on_ready():
  clear()
  sleep(1)
  print("I'm online")
  sleep(1)
  print(f"username: {client.user}")

lonley = "lonley"
lol = "lol"
wow = "wow"
yes = "yes"
nice = 'nice'
wtf = "wtf"
lmao = "lmao"
bae = "bae"
fish = "fish"
no = "no "
I_am_b = "i am b"

@client.event
async def on_message(message):
  randomspeak = random.randint(1, 3)
  if randomspeak == 1:
    if message.author.id == 459905208160616459:
      await message.delete()
    #await message.channel.send("Your mean")
      print(f"{message.author} said: {message.content} (message suppresed)")
    if message.content == "test":
      await message.channel.send("I am dead inside")
    elif message.content == "what":
      await message.channel.send("learn or I will chew ur eye balls")
    if no in message.content:
      await message.channel.send("BUT WHY")
    elif message.content == "bruh":
      await message.channel.send("bruh bruh")
    if wtf in message.content:
      await message.channel.send("lmao this asshole")
    if bae in message.content:
      await message.channel.send("wassup my shawty Bae")
    elif message.content == "stfu":
      await message.channel.send("why dipshit")
    elif lol in message.content:
      await message.channel.send("Haha a laughing loser")
    if wow in message.content:
      await message.channel.send("Ur stoopid")
    if yes in message.content:
      await message.channel.send("r u sure ")
    if I_am_b in message.content:
      await message.channel.send ("let me go grab the spatchula")
    if nice in message.content:
      await message.channel.send("NOICE")
    if lmao in message.content: 
      await message.channel.send("wow what a dipstick")
    
    if fish in message.content:
      if message.content == "fishy sticks":
        print("spam prevented")
      else:
        await message.channel.send("fishy sticks")
    elif message.content == "I hate you":
      await message.channel.send("Ungrateful loser")
  
    if lonley in message.content:
      await message.channel.send("hey, die alone")
    
    if (message.content == "hello") or (message.content == "hi"):
      hellorand = random.randint(1, 5)
      if hellorand == 1:
        await message.channel.send("howdy")
      elif hellorand == 2:
        await message.channel.send("lemme in ur house")
      elif hellorand == 3:
        await message.channel.send("go die")
      elif hellorand == 4:
        await message.channel.send("nOOO")
      else:
        await message.channel.send("im out, NOPE")
    randomspeak = random.randint(1, 2)
  if message.content == "!rank":
    await message.channel.send ("your a dissapointment")
  if (message.content == "games") and (message.channel.id == 761325921029586974):
    global gamesc
    global gamesr
    gamesc = gamesc + 1
    print(gamesc)
    
    print(f"{gamesr} till next games")
    if gamesc >= gamesr:
      gamesc = 0
      await message.channel.send("games")
      gamesr = random.randint(3, 9)


#below is just certain commands connecting the bot to the interent and connecting it to discord
make_website()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)