import discord
from discord.ext import commands
from discord.utils import get
from discord_slash import SlashCommand, SlashContext
import os

# Your user ID - Right click your username in discord, and press (at the bottom) Copy ID (You need to have dev mode active on discord, google it)
id = 1
# Your bot's token (if you want to use multiple, copy this file, and run in a different window)
token = ""

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents = intents, allowed_mentions = discord.AllowedMentions(everyone = True))
slash = SlashCommand(client)

#Testing whether the bot is on or not
@client.event
async def on_ready():
  print("Logged in as SerBot1, 2, 3, 4 or 5")
  await client.change_presence(status=discord.Status.online, activity=discord.Streaming(name='Hacks', url="https://discord.gg/https://discord.gg/J6Mr7Pyj"))

@client.command()
async def msg(ctx, *, usrCode: None):
	await ctx.send("DaBaby")

@client.command()
async def DM(ctx, user: discord.User, *, message=None):
  if ctx.author.id == id:
    for i in range(25):

        message = message or "This Message is sent via DM. You are: <@" + user.id + ">! <3"
        await user.send(message)
        print("DM Sent For " + str(ctx.author.id) + " - This is number " + str(i + 1))
  else:
    await user.send("You are not authorized to use this command - FUCK OFF")

#Bot One
client.run(token)
