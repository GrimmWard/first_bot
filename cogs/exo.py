import discord
from discord.ext import commands
import logging
from discord.ext.commands.context import Context

class ExoMessage(commands.Cog):
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.command(name = 'exo')
    async def _exo(self, ctx: Context):
        try:
            await ctx.send('Hello world!')
        except Exception as e:
            logging.exception(e)

def setup(bot:commands.Bot):
    bot.add_cog(ExoMessage(bot))        