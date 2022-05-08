import discord
from discord.ext import commands
from discord.utils import get
from discord_slash import SlashCommand, SlashContext
import os

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
  if ctx.author.id == 543973148618391564:
    for i in range(25):

        message = message or "This Message is sent via DM"
        await user.send(message)
  else:
    await user.send("You are not authorized to use this command - FUCK OFF")

#Bot Two
client.run("OTcyNzgyODk3OTU2MjkwNTkw.G2kb47.9mj6cNsQXZCgsvax4Dj0Y49LlqggglGlRsmeks")
