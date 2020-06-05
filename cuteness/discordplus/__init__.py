from cuteness.discordplus import bot, command, embed, member, client


def patch():
    embed.patch()
    command.patch()
    member.patch()
    bot.patch()
    client.patch()
