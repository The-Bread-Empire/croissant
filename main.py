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
  
client = discord.Client()

@client.event
async def on_ready():
  clear()
  sleep(1)
  print("I'm online")
  sleep(1)
  print(f"username: {client.user}")


@client.event
async def on_message(message):
  print("test complete")



#below is just certain commands connecting the bot to the interent and connecting it to discord
make_website()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)