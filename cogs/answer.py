import discord
from discord.ext import commands
import logging
from discord.ext.commands.context import Context

class ExoAnswer(commands.Cog):
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        try:
            msg = message.content
            channel = message.channel.id
            if msg == 'Привет':
                await self.bot.get_channel(channel).send(f'Привет {message.author.mention}!')
        except Exception as e:
            logging.exception(e)




def setup(bot:commands.Bot):
    bot.add_cog(ExoAnswer(bot))        