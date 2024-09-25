"""Discord bot logics."""
import asyncio

import discord
import logging

from app.config import app_config
from app.db import InMemoryBooksDatabase
from app.views import AddBookModal, MyBooks

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

@bot.slash_command(name="list", description="Get available books")
async def list_books(ctx):
    """List available books."""

    embed = discord.Embed(
        title="Available books",
        description="Books that you can read.",
        color=discord.Colour.blurple(),  # Pycord provides a class with default colors you can choose from
    )

    for book in InMemoryBooksDatabase.get_all_books():
        embed.add_field(name=book.name,
                        value=f"{book.description[0:50]}...")

    await ctx.respond(embed=embed)

@bot.slash_command(name="add", description="Adds new book for exchange")
async def add_book(ctx):
    """Add new books for exchange."""
    modal = AddBookModal(title="Add new book")
    await ctx.send_modal(modal)

@bot.slash_command(name="get", description="Get book to read")
async def get_book(ctx: discord.ApplicationContext, book_name: str):
    """Get book to read."""
    InMemoryBooksDatabase.read_book(book_name, ctx.interaction.user.name)
    await ctx.respond(f"Book {book_name} now is yours. Do not forget to return!", view=MyBooks())

@bot.slash_command(name="back", description="Back book to the library")
async def back_book(ctx, book_name: str):
    """Back the book to the library."""
    pass


def run():
    """Runs bot instance."""
    logging.info("Starting bot...")
    bot.run(app_config.bot_token)
