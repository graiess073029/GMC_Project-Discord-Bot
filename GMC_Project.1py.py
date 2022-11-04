#importing discord librarie and an extension to have the bot class
import discord
from discord.ext import commands

#creating an instance from intent class
intent = discord.Intents.default()
intent.members = True

bot = commands.Bot(command_prefix='!',intents=intent)

@bot.event
async def on_ready():
    print("Ready to work now!")

@bot.event
async def on_member_join(member):
    new_member = member.name
    welcome_chat: discord.TextChannel = bot.get_channel(id=991801755023179869)
    await welcome_chat.send('Welcome {} to GomyCode! We hope that you will have a nice experience with us!'.format(new_member))

@bot.event  
async def on_message(message):
    #auto reply system
    author = message.author.mention
    if not message.guild:
        pass

    elif message.author != bot.user and 'hello' in message.content.lower():
        await message.channel.send('Hello {} i hope you are well. :smiley:'.format(author))

    elif  message.author !=  bot.user and 'help' in message.content.lower():
        await message.channel.send("How can i help you {}! :grinning: ".format(author))

    elif  message.author !=  bot.user and 'good bye' in message.content.lower():
        await message.channel.send("See you later {}! :wave:".format(author))    

    elif  message.author != bot.user and 'play valo' in message.content.lower() or 'play lol' in message.content.lower():
        await message.channel.send("Go do your checkpoint  {}! :wave:".format(author))

@bot.command()
async def clean(ctx,number: int):
    messages = await ctx.channel.history(limit=number+1).flatten()
    x = 0
    for message in messages:
        await message.delete
        x += 1
    x -= 1
    await ctx.channel.send('{} messages deleted'.format(x))






bot.run('OTk2MDY2OTA3MDA4NTQ4OTc0.G4czim.5CYJnpuGiOKrYMbXi7vmUle9E0dmiToLy1Lmag')