from discord.ext.commands import command, Cog

from cuteness.lib.cutepics import cutepics


class HelpCog(Cog, name="Cuteness"):
    @command(help="Get a random cute picture", aliases=["cuteness"])
    async def help(self, ctx):
        p = ctx.prefix
        commands = (f'`{p}{c}`' for c in cutepics.categories)
        await ctx.channel.send(
            f"Type `{p}cute` to fetch a random cute picture!\n"
            "Or use one of these categories:\n"
            f"{', '.join(commands)}"
        )


def setup(bot):
    bot.add_cog(HelpCog(bot))
