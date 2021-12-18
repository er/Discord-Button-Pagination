import sys
import logging
import logging.handlers
import os
import discord
from datetime import datetime
from discord.ext import commands
import config

from utils import slash_util

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(asctime)s | %(name)s | %(message)s",
    handlers=[
        logging.StreamHandler(stream=sys.stdout),
    ],
)

start_time = datetime.now().strftime("%d/%m/%Y | %H:%M")


class TemplateBot(slash_util.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            case_insensitive=True,
            intents=discord.Intents.default(),
        )
        self.ready = False

    async def on_ready(self):
        if not self.ready:
            self.remove_command('help')
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    self.load_extension(f"cogs.{filename[:-3]}")
                    logging.info(f"Loading {filename[:-3]} success...")
            await self.sync_commands()
            self.ready = True

    async def on_command_error(self, ctx, error):
        ignored = (
            commands.CommandNotFound,
            commands.DisabledCommand,
            commands.NoPrivateMessage,
            commands.CheckFailure,
        )

        if isinstance(error, ignored):
            return

        if hasattr(ctx.command, "on_error"):
            return

        error = getattr(error, "original", error)

        raise error


if __name__ == "__main__":
    TemplateBot().run(config.TOKEN)