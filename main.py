import discord
from dotenv import load_dotenv
import requests
import os
import random
import time

load_dotenv()

def get_meme():
    response = requests.get('https://meme-api.com/gimme/programmingmemes')
    data = response.json()
    return data['title'], data['url'], data['postLink']

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_used = 0  # cooldown timestamp

    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Trigger only when bot is mentioned
        if self.user in message.mentions:

            # Cooldown check (10 seconds)
            current_time = time.time()
            if current_time - self.last_used < 10:
                return  # still in cooldown

            # Random chance I am setting To 90%
            chance = 0.9
            if random.random() > chance:
                return

            # Fetch meme
            title, image_url, post_link = get_meme()

            # Build embed
            embed = discord.Embed(
                title=title,
                url=post_link,
                description="Throwing Meme Bro!"
            )
            embed.set_image(url=image_url)
            embed.set_footer(text="Powered by Tabarak's Bot 🤖")

            # Send meme
            await message.channel.send(embed=embed)

            # Update cooldown
            self.last_used = current_time


Token = os.getenv("API_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(Token)
