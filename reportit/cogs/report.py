# -*- coding: utf-8 -*-

from discord.ext import commands
import discord

class Report(commands.Cog):
    """Cog for reporting behavior on discord"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def report_group(self, ctx):
        pass

    @report_group.command()
    async def report(self, ctx):
        pass

def setup(bot):
    bot.add_cog(Report(bot))
