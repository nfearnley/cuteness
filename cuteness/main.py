import pkgutil
import os
import argparse
from pathlib import Path

import discord.errors
from discord.ext.commands import Bot
from cuteness import discordplus

from cuteness.lib.conf import conf, ConfigError
from cuteness.lib import paths

parser = argparse.ArgumentParser(description="Cute pictures discord bot", add_help=True)
parser.add_argument("--config", dest="confpath", action="store", type=Path, help="path to configuration file")
parser.add_argument("--init", dest="initconf", action="store_true", help="initialize the configuration file")

discordplus.patch()


def initConf():
    print("Initializing configuration file")
    try:
        conf.init()
        print(f"Configuration file initialized: {paths.confpath}")
    except FileExistsError as e:
        print(e)
        pass
    os.startfile(paths.confpath.parent)


def main():
    args = parser.parse_args()
    if args.confpath:
        paths.confpath = args.confpath

    if args.initconf:
        initConf()
        return

    try:
        conf.load()
    except ConfigError as e:
        print(e)
        return

    bot = Bot(command_prefix=conf.prefix)

    extension_dirs = ["cogs", "sources"]
    for d in extension_dirs:
        extensions = (m.name for m in pkgutil.iter_modules([f"cuteness/{d}"]))
        for e in extensions:
            bot.load_extension(f"cuteness.{d}.{e}")

    @bot.event
    async def on_first_ready():
        print(f"Logged in as: {bot.user} ({bot.user.id})")
        print(f"Prefix: {conf.prefix}")

    if not conf.authtoken:
        print("Authentication token not found!")
        return

    try:
        bot.run(conf.authtoken)
    except discord.errors.LoginFailure as e:
        print(e)
        return


if __name__ == "__main__":
    main()
