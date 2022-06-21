from discord.ext import commands
import utilities.dreamily as drm
import discord

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix='.', intents=intents)


class TextGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def generate(self, ctx, *, text):
        res = await drm.default_dream(text)
        await ctx.send(text + res)


def setup(cl):
    cl.add_cog(TextGen(cl))
