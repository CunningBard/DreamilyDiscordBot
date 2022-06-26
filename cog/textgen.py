import time

from discord.ext import commands
import utilities.dreamily as drm
import main as mn
import discord

# intents = discord.Intents.all()
# client = commands.Bot(command_prefix='.', intents=intents)


class TextGen(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def generate(self, ctx, *, text=""):
        if not mn.database.has(ctx.author.id):
            mn.database.new_user(ctx.author.id)
        else:
            person = mn.database.get(ctx.author.id)
            time_since_last = time.time() - person.last_use
            if time_since_last < mn.wait_time:
                await ctx.respond(f"please wait for {round(mn.wait_time - time_since_last, 4)} more seconds")
                return
            person.last_use = time.time()
            person.command_use_times += 1

        interaction = await ctx.respond("Generating..")
        res = await drm.default_dream(text)
        await interaction.edit_original_message(content=text + res)

    @commands.slash_command()
    async def dev_generate(self, ctx, *, text=""):
        if not mn.database.has(ctx.author.id):
            mn.database.new_user(ctx.author.id)
        else:
            person = mn.database.get(ctx.author.id)
            time_since_last = time.time() - person.last_use
            if time_since_last < mn.wait_time:
                await ctx.respond(f"please wait for {round(mn.wait_time - time_since_last, 4)} more seconds")
                return
            person.last_use = time.time()
            person.command_use_times += 1

        now = time.time()

        interaction = await ctx.respond("Generating..")
        res = "lorem imps-um"
        # res = await drm.default_dream(text)
        await interaction.edit_original_message(content=text + res + f"\n\ntook: {round(time.time() - now, 2)}")

    @commands.slash_command(description="")
    @commands.has_any_role("Owner", "Senior Moderator")
    async def db(self, ctx):
        await ctx.respond(mn.database.data)


def setup(cl):
    cl.add_cog(TextGen(cl))
