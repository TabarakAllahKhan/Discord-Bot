# Discord Bot 🤖
A lightweight, interactive Discord bot designed to engage developer communities with programming humor. The bot leverages the Meme API to fetch and display relatable coding memes upon request, featuring intelligent rate-limiting and embedded formatting.

## Features 🚀
- **Mention-Based Trigger**: Responds strictly when mentioned (@BotName), keeping server channels clean.

- **Dynamic Content**: Fetches real-time programming memes from meme-api.com.

- **Rich Media Embeds**: Displays content in a polished, consistent card format.

- **Spam Protection**: Built-in cooldown timer (default: 10s) to prevent API abuse and channel flooding.

- **Randomized Interaction**: Configurable probability logic for responses to create a more organic feel.

## Demo Video
[![Watch the demo](https://img.youtube.com/vi/6-MFm3VeTsY/maxresdefault.jpg)](https://www.youtube.com/watch?v=6-MFm3VeTsY)

## 🛠️ Tech & Tools
- Python 
- Discord Api Token
- Request Library for Http Request
- Random Library to generate random response chance.
- Time Library to use for bot cool down time.
- python-dotenv to store the Discord Api token securely
- Os module to load the env variables from .env file.

## SetUp Guide
- First you have to get a Discord Api Key on the link https://discord.com/developers/applications/

## Code Setup
**1.Clone & Install**
```
git clone https://github.com/TabarakAllahKhan/Discord-Bot.git
cd Discord-Bot
pip install -r requirements.txt
```
**2. Configure Rename .env.example to .env and add your token:**
```
DISCORD_TOKEN=your_token_here
```
**3.Run**

````
python main.py
````

