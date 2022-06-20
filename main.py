import os
import discord
import secrets_folder.secret as sc
from discord.ext import commands

"""
secret folder contains:
api_key: dreamily api key
bot_token: discord bot token
"""

intents = discord.Intents.default()
bot = commands.Bot(command_prefix=">", intents=intents)

last_reload = ""


async def load_cog(ctx, extension):
    directory = os.listdir("cog")

    if extension + ".py" in directory:
        try:
            bot.load_extension(f"Cog.{extension}")
            await ctx.send(f"cog {extension} has been loaded")
        except discord.ext.commands.errors.ExtensionAlreadyLoaded:
            await ctx.send(f"cog {extension} has already been loaded or couldnt be loaded")
    else:
        await ctx.send(f"'{extension}' isn't a cog")


async def unload_cog(ctx, extension):
    directory = os.listdir("cog")

    if extension + ".py" in directory:
        try:
            bot.unload_extension(f"Cog.{extension}")
            await ctx.send(f"cog {extension} has been unloaded")
        except discord.ext.commands.errors.ExtensionNotLoaded:
            await ctx.send(f"cog {extension} has already been unloaded or couldnt be unloaded")
    else:
        await ctx.send(f"'{extension}' isn't a cog")


@bot.command()
@commands.has_any_role("Owner", "Senior Moderator")
async def load(ctx, extension):
    await load_cog(ctx, extension)


@bot.command()
@commands.has_any_role("Owner", "Senior Moderator")
async def unload(ctx, extension):
    await unload_cog(ctx, extension)


bot.run(sc.bot_token)
