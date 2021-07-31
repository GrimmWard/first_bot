import discord
from discord import mentions

from discord.ext import commands
import logging
from discord.ext.commands.context import Context
import random

class New_Member(commands.Cog):
    def __init__(self, bot:commands.Bot):
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            r = random.randint(0,225)
            g = random.randint(0,225)
            b = random.randint(0,225)
            emb = discord.Embed(
                title = 'Hi',
                description = f'Welcome to our server {member.guild.name}',
                color = discord.Color.from_rgb(r, g, b),
                timestamp = member.joined_at
            )

            emb.set_thumbnail(
                url = member.avatar_url
                )
            emb.set_footer(
                text = f'{member.id} | Have a nice relax',
                icon_url= 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4qZwnNlqrXtvDaJf_o80wHQllGCe0aWD5LQ&usqp=CAU'
            )

            await self.bot.get_channel(792836943003779112).send(member.mention, embed = emb)

        except Exception as e:
            logging.exception(e)

def setup(bot:commands.Bot):
    bot.add_cog(New_Member(bot))        