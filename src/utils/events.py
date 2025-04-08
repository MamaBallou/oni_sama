import discord
import math
from src.data.constants import PREVIOUS_PAGE, NEXT_PAGE, COMMANDS_DESCRIPTION
from src.utils.embed_utils import create_help_embed


def setup_events(bot):
    @bot.event
    async def on_ready():
        print(f'Bot connecté en tant que {bot.user.name}')
        try:
            synced = await bot.tree.sync()
            print(f"Commandes synchronisées: {len(synced)}")
        except Exception as e:
            print(f"Erreur lors de la synchronisation des commandes: {e}")

        # Initialiser le dictionnaire pour stocker les messages d'aide
        bot.help_messages = {}

    @bot.event
    async def on_reaction_add(reaction, user):
        if user.bot:
            return

        message = reaction.message
        if message.id not in bot.help_messages or user.id != bot.help_messages[message.id]["user_id"]:
            return

        help_data = bot.help_messages[message.id]
        current_page = help_data["page"]
        total_pages = math.ceil(len(COMMANDS_DESCRIPTION) / 10)

        if str(reaction.emoji) == NEXT_PAGE and current_page < total_pages:
            help_data["page"] += 1
            new_embed = await create_help_embed(help_data["page"])
            await message.edit(embed=new_embed)
        elif str(reaction.emoji) == PREVIOUS_PAGE and current_page > 1:
            help_data["page"] -= 1
            new_embed = await create_help_embed(help_data["page"])
            await message.edit(embed=new_embed)

        await reaction.remove(user)
