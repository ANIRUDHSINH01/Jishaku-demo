import jishaku
from discord.ext import commands
from discord import *
import os

intents = Intents.all()

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  # Loading the jishaku extension
  await bot.load_extension("jishaku")
  print("Loaded jishaku")


bot.run(os.getenv("TOKEN"))
