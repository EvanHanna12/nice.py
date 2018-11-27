import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import random
from discord import Game
import asyncio

#defining client and Client

Client = discord.Client()
client = commands.Bot(command_prefix = "+")

#on message

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='+commands | Version 2.7.2'))
    print("Logged in as:")
    print("NiceBot")
    print("By Thief")


#embeds & commands   

@client.event
async def on_message(message):
    if message.content.upper().startswith('+INFO'):
        embed = discord.Embed(title="NiceBot", description="Thanks for using NiceBot! Below is info about me.", color=0x0011fa)
        embed.add_field(name="How was I made?", value="I was made in python 3.5 using discord.py", inline=False)
        embed.add_field(name="Who made me?", value="A person called Aj#1636 Made Me", inline=False)
        embed.add_field(name="Looking for the commands?" , value="Do the +commands command. Also, all my commands are not case sensetive.", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('+COMMANDS'):
        embed = discord.Embed(title="NiceBot", description="Thanks for using NiceBot! Below are my commands. None of these are case sensetive.", color=0x0011fa)
        embed.add_field(name="+Info", value="gives info about NiceBot!", inline=False)
        embed.add_field(name="+Commands", value="this shows all the commands.", inline=False)
        embed.add_field(name="+Cookie", value="gives you a cookie, not in real life though :( ", inline=False)
        embed.add_field(name="+8Ball <your question>", value="the magic 8ball will answer your question (only yes or no questions)", inline=False)
        embed.add_field(name="+Wakeup", value="Wakes the bot up (makes sure the bot works)", inline=False)
        embed.add_field(name="+Food", value="Orders you food (not actual food, it's for roleplay)", inline=False)
        embed.add_field(name="+Guessgame", value="Try to guess a number from 1-5 and the bot will reply with the number that it was thinking of.", inline=False)
        embed.add_field(name="+Support", value="Gives an invite link to the owner's server.", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('+VERSION'):
        embed = discord.Embed(title="NiceBot Version", descripton="Here is my version below.", color=0x0011fa)
        embed.add_field(name="version 2.7.2", value="added +invite command", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('+ONLINE'):
        embed=discord.Embed(title="NiceBot", color=0x00f510)
        embed.add_field(name="NiceBot At The Moment:", value="Online!", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('+OFFLINE'):
        embed=discord.Embed(title="NiceBot", color=0xf50004)
        embed.add_field(name="NiceBot Status At The Moment:", value="Offline", inline=False)
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith('+COOKIE'):
        await client.send_message(message.channel, ":cookie: <- why did you want that?")
    if message.content.upper().startswith('+8BALL'):
        randomlist = ["It is certain :8ball:", "It is decidedly so :8ball:", "Without a doubt :8ball:", "Yes, definitely :8ball:", "You may rely on it :8ball:", "As I see it, yes :8ball:", "Most likely :8ball:", "Outlook good :8ball:", "Yes :8ball:", "Signs point to yes :8ball:", "Ask again later :8ball:", "Better not tell you now :8ball:", "Cannot predict now :8ball:", "Concentrate and ask again :8ball:", "Don't count on it :8ball:", "My reply is no :8ball" "My sources say no :8ball:",  "Outlook not so good :8ball:", "Very doubtful :8ball:"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.upper().startswith('HELLO'):
        await client.send_message(message.channel, "howdy!")
    if message.content.upper().startswith('+WAKEUP'):
        await client.send_message(message.channel, ":sleeping: zzzzzzzzzz..... Huh? Oh. You woke me up, I'm getting ready to go to work on your server.")
    if message.content.upper().startswith('+ORDER'):
        await client.send_message(message.channel, "your food has been ordered. Type in chat '+food' to get your food.")
    if message.content.upper().startswith('+FOOD'):
        userID = message.author.id
        await client.send_message(message.channel, "Your food is ready! <@%s>" % (userID))
    if message.content.upper().startswith('+GUESSGAME'):
        randomlist = ["My number was 1, did you guess it right?", "My number was 2, did you guess it right?", "My number was 3, did you guess it right?", "My number was 4, did you guess it right?", "My number was 5, did you guess it right?"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.upper().startswith('+SUPPORT'):
        await client.send_message(message.channel, "To get support for me, you will need to join the owner's server. Here is the link: Soon Out")
    if message.content.upper().startswith('+INVITE'):
        await client.send_message(message.channel, "Thanks for wanting to invite me! Soon Out")

#bot token
      
client.run("NTE2NzIwNjA3ODMyOTY1MTQ2.Dt5Rrw.U-fdwZf81hAsebIzzYysB3UXJYw")
