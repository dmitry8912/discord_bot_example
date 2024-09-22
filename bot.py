"""Entrypoint for bot."""

import logging
from app.main import run

discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.ERROR)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
discord_logger.addHandler(handler)

general_logger = logging.getLogger()
general_logger.setLevel(logging.DEBUG)
general_handler = logging.StreamHandler()
general_handler.setFormatter(logging.Formatter('%(asctime)s | %(levelname)s | %(message)s'))
general_logger.addHandler(handler)

if __name__ == "__main__":
    run()
    