import discord
from discord import app_commands
import asyncio
from src.utils.embed_utils import create_help_embed
from src.data.constants import PREVIOUS_PAGE, NEXT_PAGE


def setup_help_command(bot):
    @bot.tree.command(name="help", description="Affiche la liste des commandes disponibles")
    async def help(interaction: discord.Interaction):
        embed = await create_help_embed()
        await interaction.response.send_message(embed=embed)

        # Attendre un court instant pour s'assurer que le message est bien envoyé
        await asyncio.sleep(1)

        try:
            # Récupérer le message original pour ajouter les réactions
            original_message = await interaction.original_response()
            await original_message.add_reaction(PREVIOUS_PAGE)
            await original_message.add_reaction(NEXT_PAGE)

            # Stocker les informations nécessaires pour la pagination
            bot.help_messages[original_message.id] = {
                "page": 1,
                "user_id": interaction.user.id,
                "message": original_message
            }
        except discord.NotFound:
            # Si le message n'est pas trouvé, on ignore simplement l'erreur
            pass
