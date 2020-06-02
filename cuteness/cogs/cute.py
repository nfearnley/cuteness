from discord.ext import commands

from sizebot.lib.cutepics import cutepics


class CuteCog(commands.Cog):
    """Commands for cute pictures."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def cute(self, ctx, category=None):
        """Get a cute picture."""
        cat = cutepics.getCategory(category)
        picfile = await cat.get()
        await ctx.channel.send(file=picfile)


def setup(bot):
    bot.add_cog(CuteCog(bot))
