

def roasting():
  if message.author.id == 728504055047127051:
    #await message.delete()
    await message.channel.send("I don't like you")
    print(f"{message.content} (message deleted)")
  if message.content == "test":
    await message.channel.send("I am dead inside")
  elif message.content == "what":
    await message.channel.send("die")
  elif message.content == "no":
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
    await message.channel.send("Haha a wild loser")
  if wow in message.content:
   await message.channel.send("Ur stoopid")
  if yes in message.content:
    await message.channel.send("r u sure ")
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
    hellorand = random.randint(1, 4)
    if hellorand == 1:
      await message.channel.send("howdy")
    elif hellorand == 2:
      await message.channel.send("lemme in ur house")
    elif hellorand == 3:
      await message.channel.send("go die")
    else:
      await message.channel.send("nOOO")