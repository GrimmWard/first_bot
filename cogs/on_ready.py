import discord
from discord.ext import commands
import logging

class BotReady(commands.Cog):
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            user:discord.Member = self.bot.get_user(531116449272561666)
            await user.send(
                'This bot is ready for game\n'\
                'He is ready to talk with you'
            )
        except Exception as e:
            logging.exception(e)

def setup(bot:commands.Bot):
    bot.add_cog(BotReady(bot))        