import time

from discord.ext import commands
import utilities.dreamily as drm
import discord

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix='.', intents=intents)


class TextGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def generate(self, ctx, *, text):
        interaction = await ctx.respond("generating..")
        res = await drm.default_dream(text)
        await interaction.edit_original_message(content=text + res)

    @commands.slash_command()
    async def dev_generate(self, ctx, *, text):
        now = time.time()
        interaction = await ctx.respond("generating..")
        res = await drm.default_dream(text)
        await interaction.edit_original_message(content=text + res + f"\ntook: {round(time.time() - now, 4)}s")


def setup(cl):
    cl.add_cog(TextGen(cl))
