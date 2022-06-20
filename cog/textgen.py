from discord.ext import commands
import discord

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix='.', intents=intents)


class TextGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def generate(self, ctx, *, text):
        pass


def setup(cl):
    cl.add_cog(TextGen(cl))
