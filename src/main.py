import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

from src.commands.gif_commands import setup_gif_commands
from src.commands.help_command import setup_help_command
from src.utils.events import setup_events


def run_bot():
    # Charger les variables d'environnement
    load_dotenv('.env', override= True)

    # Configuration du bot
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Configuration des commandes et événements
    setup_gif_commands(bot)
    setup_help_command(bot)
    setup_events(bot)

    # Lancer le bot
    bot.run(os.getenv('DISCORD_TOKEN'))


if __name__ == "__main__":
    run_bot()
