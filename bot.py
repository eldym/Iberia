import discord
import asyncio
import json

from discord.ext import tasks, commands
from database import Database

INITIAL_EXTENSIONS = [
    'cogs.admin',
    'cogs.misc',
    'cogs.moderation'
]

def get_config():
    with open('config.json') as f:
        return json.load(f)
    
def get_token():
    with open('credentials.json') as f:
        return json.load(f)
    
config = get_config()
token = get_token()

class bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=config["prefixes"], description="Very good description",intents=discord.Intents.all())
        self.initial_extensions = INITIAL_EXTENSIONS
        self.token = token["token"]

    async def on_ready(self):
        # Starts up the bot!
        print('Waking up!')
        print(f"Bot is online!\nLogged in as:\nUsername: \"{self.user.name}\"\nID: {self.user.id}")

    async def setup_hook(self) -> None:
        # Sets it all up
        for extension in self.initial_extensions:
            try: await self.load_extension(extension)
            except Exception as e: print(f"ERROR: Extension {extension} did not load!\nException:", e)
            else: print(f"{extension} loaded.")
        
        # Database
        try: self.database = Database()
        except Exception as e:
            print("ERROR: Database is not initialized!\nException:", e)
        
    def run(self):
        super().run(self.token, reconnect=True)

if __name__ == '__main__':
    bot = bot()
    bot.run()