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
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemx1dWNzMnEzMHo1NTQ5eXFuY281c3kxYXJzYWFyNjAxZTg5NHlwYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PHZ7v9tfQu0o0/giphy.gif',
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemx1dWNzMnEzMHo1NTQ5eXFuY281c3kxYXJzYWFyNjAxZTg5NHlwYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/143v0Z4767T15e/giphy.gif',
        'https://media.giphy.com/media/49mdjsMrH7oze/giphy.gif',
        'https://media.giphy.com/media/GMFUrC8E8aWoo/giphy.gif',
        'https://media.giphy.com/media/kvKFM3UWg2P04/giphy.gif',
        'https://media.giphy.com/media/u9BxQbM5bxvwY/giphy.gif',
        'https://media.giphy.com/media/LIqFOpO9Qh0uA/giphy.gif'
        'https://media.giphy.com/media/VXP04aclCaUfe/giphy.gif',
        'https://media.giphy.com/media/IRUb7GTCaPU8E/giphy.gif',
    ],
    'kiss': [
        'https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif',
        'https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif',
        'https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif',
        'https://media.giphy.com/media/nyGFcsP0kAobm/giphy.gif',

    ],
    'bonk': [
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjdwNmN1b2pqMHp3ZmRqbzhmd21mNnJicWZ4cDQ2ajZnbG1tcGZhZCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BUP61wrSYtrI59TbEe/giphy.gif',
    ],
    'bang': [
        'https://media.giphy.com/media/Mokwv5L0w38ju/giphy.gif',
    ],
    'facepalm': [
        'https://media.giphy.com/media/USpSzYSiH3N1C/giphy.gif',
    ],
    'poke': [
        'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmlyemtxMmV1ZDVwazFmMXpvc2FycW0wOWk0bzR4eWN0bnRmZ3JkOSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/FdinyvXRa8zekBkcdK/giphy.gif',
    ],
    'patpat': [
        'https://media.giphy.com/media/Z7x24IHBcmV7W/giphy.gif',
        'https://media.giphy.com/media/eVpKZ8lvaciU3ySYhZ/giphy.gif',
        'https://media.giphy.com/media/vaucvLYaM7UrNJHsgy/giphy.gif',
        'https://media.giphy.com/media/aZSMD7CpgU4Za/giphy.gif',
        'https://media.giphy.com/media/BNJ9NQWXrifPXb2jkW/giphy.gif',
        'https://media.giphy.com/media/ZJknJqiPBmj3cRZKE7/giphy.gif',
    ],
    'hide': [
        'https://media1.giphy.com/media/l1J9qeX2tGgPzdqKc/giphy.gif',
    ],
    'jumpscare': [
        'https://media.giphy.com/media/6wTqrr9L2ZKlGyfFYZ/giphy.gif',
    ],
    'wave': [
        'https://media.giphy.com/media/3oz8xTAJIQD6JWfTUc/giphy.gif',
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


@bot.tree.command(name="hug", description="Envoie un GIF de câlin (optionnellement à une personne)")
async def hug(interaction: discord.Interaction, user: discord.Member = None):
    if user:
        message = f"{interaction.user.mention} fait un câlin à {user.mention}"
        await send_gif(interaction, 'hug', message)
    else:
        await send_gif(interaction, 'hug')


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
