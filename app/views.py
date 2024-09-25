"""Views, embeds, modals etc."""

import discord

from app.db import InMemoryBooksDatabase, Book


class AddBookModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Book name"))
        self.add_item(discord.ui.InputText(label="Description", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):

        book = Book()
        book.name = self.children[0].value
        book.description = self.children[1].value
        book.owner_name = interaction.user.name

        InMemoryBooksDatabase.add_book(book.name, book)

        await interaction.response.send_message("Book added")


class MyBooks(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # timeout of the view must be set to None

    @discord.ui.button(label="Show my books", style=discord.ButtonStyle.primary) # the button has a custom_id set
    async def button_callback(self, button, interaction: discord.Interaction):

        response = "Your books:\n\n"

        for book in InMemoryBooksDatabase.my_books(interaction.user.name):
            response += f"{book.name} - {book.description[0:50]}\n"

        await interaction.response.send_message(response)
