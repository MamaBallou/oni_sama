import discord
import random
from src.data.gifs import GIFS


async def send_gif(interaction: discord.Interaction, command: str, message: str = None):
    gif_url = random.choice(GIFS[command])
    embed = discord.Embed(color=discord.Color.random())

    if message:
        embed.description = message

    embed.set_image(url=gif_url)
    embed.set_footer(text=f"Commande /{command}")

    await interaction.response.send_message(embed=embed)


async def create_help_embed(page: int = 1) -> discord.Embed:
    from src.data.constants import COMMANDS_DESCRIPTION
    import math

    commands_per_page = 10
    commands = list(COMMANDS_DESCRIPTION.items())
    total_pages = math.ceil(len(commands) / commands_per_page)

    start_idx = (page - 1) * commands_per_page
    end_idx = start_idx + commands_per_page
    current_commands = commands[start_idx:end_idx]

    embed = discord.Embed(
        title="Liste des commandes disponibles",
        description="Utilisez les réactions pour naviguer entre les pages",
        color=discord.Color.blue()
    )

    for cmd, desc in current_commands:
        embed.add_field(name=f"/{cmd}", value=desc, inline=False)

    embed.set_footer(text=f"Page {page}/{total_pages}")
    return embed
