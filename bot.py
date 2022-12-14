import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import music

load_dotenv()
DISCORD_KEY= os.getenv("DISCORD_KEY")

bot = commands.Bot(command_prefix ="$", description = "On découvre python c nice",intents=discord.Intents.all())

@bot.event
async def setup_hook():
    cogs=[music]
    for i in cogs:
        await i.setup(bot)

@bot.event
async def on_ready():
    print("--- Ready ---")
    channel = bot.get_channel(1028731610251665462)
    await channel.send("Ready",delete_after=10)

bot.run(DISCORD_KEY)
