import os

from dotenv import load_dotenv


class DiscordTokenProvider:
    def __init__(self):
        self.token = None

    def get_token(self):
        if self.token is None:
            load_dotenv()
            token = os.getenv('DISCORD_TOKEN')
        return token