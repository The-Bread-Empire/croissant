import os
import random
import time
from time import sleep
from discord.ext import commands
import discord.utils
from discord.utils import get
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import asyncio
from discord.ext import commands


def botsection():
  print("1")
  bot = Bot(command_prefix='')

  @bot.command(name="dm")
  async def id_(ctx, user: discord.User):
    await ctx.send(f"its marks fault, {user.name}")
    spame = user
    spam = 1
    while spam == 1:
      await spame.send("marks fault sorry")
      sleep(1)
      spamr = random.randint(1, 25)
      print(spamr)
      if spamr == 25:
        spam = 3

  token = os.environ.get("DISCORD_BOT_SECRET")
  bot.run(token)
