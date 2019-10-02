# -*- coding: utf-8 -*-

from discord.ext import commands
import discord

class Report(commands.Cog):
    """Cog for reporting behavior on discord"""

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Report(bot))
