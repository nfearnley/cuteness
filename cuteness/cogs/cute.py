from discord.ext.commands import command, Cog

from cuteness.lib.cutepics import cutepics


class RandomPicCog(Cog, name="Cuteness"):
    @command(help="Get a random cute picture")
    async def cute(self, ctx):
        picfile = await cutepics.fetch()
        await ctx.channel.send(file=picfile)


def setup(bot):
    bot.add_cog(RandomPicCog(bot))
