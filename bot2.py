import discord
from discord.ext import commands
import asyncio
bot=commands.Bot(command_prefix="!")
@bot.command(name="ping")
async def ping_command_handler(ctx):
    await ctx.send("pong!")
asyncio.get_event_loop().run_until_complete(bot.start("tokenhere", bot=True))
