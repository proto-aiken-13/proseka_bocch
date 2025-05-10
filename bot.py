import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Required for prefix commands and message reading
# Please remember to go to https://discord.com/developers/applications/<application or bot name>/bot
# and ensure ALL Privieleged Gateway Intents are enabled

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot logged in as {bot.user}")

bot.run(TOKEN)
