import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
# Replace with your bot's token

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Predefined structure
server_structure = {
    "Welcome & Rules": ["welcome", "rules", "announcements"],
    "General": ["general-chat", "off-topic", "introductions"],
    "Python Discussions": ["beginner-questions", "intermediate-help", "advanced-discussions", "libraries-and-tools"],
    "Projects": ["project-showcase", "collaborations", "ideas-and-feedback"],
    "Learning Resources": ["tutorials", "coding-challenges", "study-groups"],
    "Debugging & Support": ["debugging-help", "code-reviews"],
    "Events": ["hackathons", "ama-and-workshops", "event-discussion"],
    "Career & Networking": ["career-advice", "job-opportunities", "networking"],
    "Bot & Fun": ["bot-commands", "fun-and-games"],
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    guild = discord.utils.get(bot.guilds)  # Automatically picks the first server the bot is in
    for category_name, channels in server_structure.items():
        # Create category
        category = await guild.create_category(category_name)
        for channel_name in channels:
            # Create channels under the category
            await guild.create_text_channel(channel_name, category=category)
    print("Server setup complete!")

bot.run(TOKEN)
