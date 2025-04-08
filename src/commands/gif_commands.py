import discord
from discord import app_commands
from src.utils.embed_utils import send_gif


def setup_gif_commands(bot):
    @bot.tree.command(name="hug", description="Envoie un GIF de câlin (optionnellement à une personne)")
    async def hug(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait un câlin à {user.mention}"
            await send_gif(interaction, 'hug', message)
        else:
            await send_gif(interaction, 'hug')

    @bot.tree.command(name="kiss", description="Envoie un GIF de baiser à une personne")
    async def kiss(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait un bisou à {user.mention}"
            await send_gif(interaction, 'kiss', message)
        else:
            await send_gif(interaction, 'kiss')

    @bot.tree.command(name="bonk", description="Envoie un GIF de bonk à une personne")
    async def bonk(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} donne un bonk à {user.mention}"
            await send_gif(interaction, 'bonk', message)
        else:
            await send_gif(interaction, 'bonk')

    @bot.tree.command(name="bang", description="Envoie un GIF de bang à une personne")
    async def bang(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} tire sur {user.mention}"
            await send_gif(interaction, 'bang', message)
        else:
            await send_gif(interaction, 'bang')

    @bot.tree.command(name="facepalm", description="Envoie un GIF de facepalm à une personne")
    async def facepalm(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait un facepalm devant {user.mention}"
            await send_gif(interaction, 'facepalm', message)
        else:
            await send_gif(interaction, 'facepalm')

    @bot.tree.command(name="poke", description="Envoie un GIF de poke à une personne")
    async def poke(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} poke {user.mention}"
            await send_gif(interaction, 'poke', message)
        else:
            await send_gif(interaction, 'poke')

    @bot.tree.command(name="patpat", description="Envoie un GIF de patpat à une personne")
    async def patpat(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait des patpat à {user.mention}"
            await send_gif(interaction, 'patpat', message)
        else:
            await send_gif(interaction, 'patpat')

    @bot.tree.command(name="hide", description="Envoie un GIF de hide à une personne")
    async def hide(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} se cache de {user.mention}"
            await send_gif(interaction, 'hide', message)
        else:
            await send_gif(interaction, 'hide')

    @bot.tree.command(name="jumpscare", description="Envoie un GIF de jumpscare à une personne")
    async def jumpscare(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait peur à {user.mention}"
            await send_gif(interaction, 'jumpscare', message)
        else:
            await send_gif(interaction, 'jumpscare')

    @bot.tree.command(name="wave", description="Envoie un GIF de wave à une personne")
    async def wave(interaction: discord.Interaction, user: discord.Member | discord.Role = None):
        if user:
            message = f"{interaction.user.mention} fait coucou à {user.mention}"
            await send_gif(interaction, 'wave', message)
        else:
            await send_gif(interaction, 'wave')
