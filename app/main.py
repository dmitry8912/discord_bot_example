"""Discord bot logics."""
import asyncio

import discord
import logging

from app.config import app_config


bot = discord.Bot()

@bot.event
async def on_ready():
    """Event handler called when the bot is ready."""
    logging.info(f"We have logged in as {bot.user}")

@bot.slash_command(name="sleep", description="Simple command that sends hello as response")
async def sleep(ctx, duration: int):
    """Sleep command, simulates long-running task."""
    await asyncio.sleep(duration)
    await ctx.respond("Sleep is over!")

@bot.slash_command(name="defer", description="Simple command that sends hello as response")
async def defer(ctx, duration: int):
    """Sleep command, simulates long-running task. Deferred."""
    await ctx.defer()
    await asyncio.sleep(duration)
    await ctx.respond("Sleep with defer is over!")

@bot.slash_command(name="hello", description="Simple command that sends hello as response")
async def hello(ctx):
    """Command that replies only hello."""
    await ctx.respond("Hello!")


def run():
    """Runs bot instance."""
    logging.info("Starting bot...")
    bot.run(app_config.bot_token)
