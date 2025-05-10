import os

# Define the folder and file structure
structure = {
    "cogs": ["__init__.py", "general.py"],
    "handlers": ["__init__.py", "command_parser.py", "message_handler.py"],
    "utils": ["__init__.py", "logger.py"],
    "data": ["users.json"],
}

base_files = {
    "bot.py": """import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Load cogs from /cogs/
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv("DISCORD_TOKEN"))
""",
    ".env": "DISCORD_TOKEN=your_actual_token_here\n",
    "requirements.txt": "discord.py\npython-dotenv\n",
    ".gitignore": "venv/\n.env\n__pycache__/\n*.pyc\n*.log\n*.db\n",
}

# Create folders and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        with open(os.path.join(folder, file), "w") as f:
            if file.endswith(".py"):
                f.write("# " + file + "\n")
            else:
                f.write("")

for file, content in base_files.items():
    with open(file, "w") as f:
        f.write(content)

print("✅ Project structure created successfully.")
