import discord
from discord import app_commands
from discord.ext import commands
import random
import os
from dotenv import load_dotenv
import aiohttp

# Charger les variables d'environnement
load_dotenv()

# Configuration du bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionnaire des GIFs pour chaque commande
gifs = {
    'hug': [
        #'https://tenor.com/bR7J9.gif',
        'https://media1.tenor.com/m/2HxamDEy7XAAAAAd/yukon-child-form-embracing-ulquiorra.gif', #'https://tenor.com/sKvMcSpWTv2.gif',
        #'https://tenor.com/xjRBLymEjT.gif',
        #'https://tenor.com/trQEPQGHNHU.gif',
        #'https://tenor.com/fEt4cKFd6tJ.gif',
        #'https://tenor.com/czDJQhtoLFC.gif',
        #'https://tenor.com/dw0XbsEOm7J.gif',
        #'https://tenor.com/eLXnOcu8qzv.gif'
        #'https://tenor.com/jzC8jw7DJ07.gif'
    ],
    'kiss': [
        'https://tenor.com/view/kiss-anime-kissing-gif-1234567890',
        'https://tenor.com/view/kiss-anime-kissing-gif-1234567891',
    ],
    'bonk': [
        'https://tenor.com/view/bonk-anime-hit-gif-1234567890',
        'https://tenor.com/view/bonk-anime-hit-gif-1234567891',
    ],
    'bang': [
        'https://tenor.com/view/bang-anime-shoot-gif-1234567890',
        'https://tenor.com/view/bang-anime-shoot-gif-1234567891',
    ],
    'facepalm': [
        'https://tenor.com/view/facepalm-anime-gif-1234567890',
        'https://tenor.com/view/facepalm-anime-gif-1234567891',
    ],
    'poke': [
        'https://tenor.com/view/poke-anime-poking-gif-1234567890',
        'https://tenor.com/view/poke-anime-poking-gif-1234567891',
    ],
    'patpat': [
        'https://tenor.com/view/pat-pat-anime-head-pat-gif-1234567890',
        'https://tenor.com/view/pat-pat-anime-head-pat-gif-1234567891',
    ],
    'hide': [
        'https://tenor.com/view/hide-anime-hiding-gif-1234567890',
        'https://tenor.com/view/hide-anime-hiding-gif-1234567891',
    ],
    'jumpscare': [
        'https://tenor.com/view/jumpscare-anime-scary-gif-1234567890',
        'https://tenor.com/view/jumpscare-anime-scary-gif-1234567891',
    ],
    'wave': [
        'https://tenor.com/view/wave-anime-waving-gif-1234567890',
        'https://tenor.com/view/wave-anime-waving-gif-1234567891',
    ]
}


@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user.name}')
    try:
        synced = await bot.tree.sync()
        print(f"Commandes synchronisées: {len(synced)}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes: {e}")


async def send_gif(interaction: discord.Interaction, command: str, message: str = None):
    gif_url = random.choice(gifs[command])
    embed = discord.Embed(color=discord.Color.random())

    if message:
        embed.description = message

    embed.set_image(url=gif_url)
    embed.set_footer(text=f"Commande /{command}")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="hug", description="Envoie un GIF de câlin à une personne")
async def hug(interaction: discord.Interaction, user: discord.Member):
    message = f"{interaction.user.mention} fait un câlin à {user.mention}"
    await send_gif(interaction, 'hug', message)


@bot.tree.command(name="kiss", description="Envoie un GIF de baiser aléatoire")
async def kiss(interaction: discord.Interaction):
    await send_gif(interaction, 'kiss')


@bot.tree.command(name="bonk", description="Envoie un GIF de bonk aléatoire")
async def bonk(interaction: discord.Interaction):
    await send_gif(interaction, 'bonk')


@bot.tree.command(name="bang", description="Envoie un GIF de bang aléatoire")
async def bang(interaction: discord.Interaction):
    await send_gif(interaction, 'bang')


@bot.tree.command(name="facepalm", description="Envoie un GIF de facepalm aléatoire")
async def facepalm(interaction: discord.Interaction):
    await send_gif(interaction, 'facepalm')


@bot.tree.command(name="poke", description="Envoie un GIF de poke aléatoire")
async def poke(interaction: discord.Interaction):
    await send_gif(interaction, 'poke')


@bot.tree.command(name="patpat", description="Envoie un GIF de patpat aléatoire")
async def patpat(interaction: discord.Interaction):
    await send_gif(interaction, 'patpat')


@bot.tree.command(name="hide", description="Envoie un GIF de hide aléatoire")
async def hide(interaction: discord.Interaction):
    await send_gif(interaction, 'hide')


@bot.tree.command(name="jumpscare", description="Envoie un GIF de jumpscare aléatoire")
async def jumpscare(interaction: discord.Interaction):
    await send_gif(interaction, 'jumpscare')


@bot.tree.command(name="wave", description="Envoie un GIF de wave aléatoire")
async def wave(interaction: discord.Interaction):
    await send_gif(interaction, 'wave')

# Lancer le bot
bot.run(os.getenv('DISCORD_TOKEN'))
