import discord
from discord.ext import commands

from utils import slash_util
from utils.pagination import Paginator


class TestCog(slash_util.ApplicationCog):

    @slash_util.slash_command()
    async def slashpagination(self, ctx: slash_util.Context):
        embeds = [
            discord.Embed(
                description="This is page 1"
            ),
            discord.Embed(
                description="This is page 2"
            ),
            discord.Embed(
                description="This is page 3"
            ),
            discord.Embed(
                description="This is page 4"
            ),
        ]
        await ctx.send(embed=embeds[0], view=Paginator(embeds))

    @commands.command()
    async def pagination(self, ctx: discord.ext.commands.Context):
        embeds = [
            discord.Embed(
                description="This is page 1"
            ),
            discord.Embed(
                description="This is page 2"
            ),
            discord.Embed(
                description="This is page 3"
            ),
            discord.Embed(
                description="This is page 4"
            ),
        ]
        await ctx.send(embed=embeds[0], view=Paginator(embeds))


def setup(bot):
    bot.add_cog(TestCog(bot))
