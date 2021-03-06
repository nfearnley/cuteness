from discord import Embed, Permissions
from discord.ext.commands import command, Cog

from cuteness.lib import cutepics


def get_category_name(p, message_text):
    names = cutepics.get_categories_and_aliases()
    commands = [f'{p}{n}' for n in names]
    if message_text not in commands:
        return None
    name = message_text[len(p):]
    return name


class CutenessCog(Cog, name="Cuteness"):
    def __init__(self, bot):
        self.bot = bot

    @command()
    async def cute(self, ctx):
        picfile = await cutepics.fetch()
        await ctx.channel.send(file=picfile)

    @command(aliases=["cuteness"])
    async def help(self, ctx, option=None):
        p = ctx.prefix
        if option == "aliases":
            category_names = sorted(cutepics.get_categories_and_aliases())
        else:
            category_names = sorted(cutepics.get_categories())
        category_commands = ', '.join(f'`{p}{c}`' for c in category_names)
        await ctx.channel.send(
            f"Type `{p}cute` to fetch a random cute picture!\n"
            + "Or use one of these categories:\n"
            + category_commands
        )

    @command()
    async def invite(self, ctx):
        invite_url = self.bot.oauth_url(permissions=Permissions(read_messages=True, send_messages=True, attach_files=True))
        await ctx.channel.send(embed=Embed(description=f"[Invite]({invite_url}) Cuteness to your server!"))

    @Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        p = await self.bot.get_prefix(message)
        name = get_category_name(p, message.content)
        if name is None:
            return
        picfile = await cutepics.fetch(name)
        await message.channel.send(file=picfile)


def setup(bot):
    bot.add_cog(CutenessCog(bot))
