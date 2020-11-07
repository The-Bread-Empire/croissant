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


client = discord.Client()

@client.event
async def on_message(message):
  ch = message.content
  re = message.channel.send
  if "lonley" in ch: re("hey die alone")

eventcommands = {
  "lonley":"hey, die alone",
  "I hate you":"Ungrateful loser",
  "test":"I am dead inside",
  "sus":"nah u vented no cap",
  "what":"Learn or I will chew your eyeballs out",
  "no":"BUT WHY",
  "wtf":"lmao this asshole",
  "bruh":"bruh bruh",
  "bae":"wassup my shawty Bae",
  "stfu":"why dipstick",
  "ahaha":"alive, ahaha why q-q",
  "lol":"haha a laughing loser",
  "wow":"ur stoopid",
  "yes":"r u sure",
  "i am b":"let me go grab the spatchula",
  "nice":"NOICE",
  "lmao":"wow what a dipstick",
  "Marmu":"eww a worm",
  "yes, my life":"oh, OH SHIZ",
  "yes, inside":"Same q-q",
  "Demon Cheese": "Only the best cheese possible",
  "what are you doing?":"Illigal doings don't call the police",
  "Markoth":"Alexa play Mothman",
  "The collector":"H A N D S",
  "Pure Vessel":"oh that mothertrucker",
  "Groz Mother":"He do be sleeping doe",
  "No eyes":"lel imaginge not being able to see",
  "Broken Vessel":"He do be looking like a lava lamp",
  "Xero":"Mr tentacle man",
  "Paintmaster Sheo":"r u gonna paint me like ur french girls?",
  "Massive Moss Charger (aka: the bush)":"B U S H M A N",
  "Gorb":"Micro worm butt",
  "Soul Master":"ur a wizzard harry",
  "Galien":"CRAB MEAT",
  "Dung Defender":"He yeets poopoo",
  "Nightmare King Grim":"Stoopid vampire man",
  "Winged Nosk":"My pet, miNEEE",
  "Crystal Guardian":"roCk",
  "Uumuu":"UWU   i want to die now",
  "Hive knight":"Swarm of death bees rain from above!",
  "cheese":"unholy",
  "gun":"guns are dangerous",
  "croissant":"haha a bored loser",
  "nou":"get fwhucked brandon",
  "heck": "Error 420: No applicable 'bad word' can satisfy. Please try again",
  "shoot": "Error 420: No applicable 'bad word' can satisfy. Please try again",
  "Angel":"He is my best fwriend, we get icecream together!! :D"
}
