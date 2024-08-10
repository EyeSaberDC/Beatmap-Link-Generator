import discord
from discord import app_commands
import asyncio
import aiohttp
import random
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CLIENT_ID = os.getenv('OSU_CLIENT_ID')
CLIENT_SECRET = os.getenv('OSU_CLIENT_SECRET')

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

intents = discord.Intents.default()
client = MyClient(intents=intents)

async def get_access_token():
    async with aiohttp.ClientSession() as session:
        token_url = "https://osu.ppy.sh/oauth/token"
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials",
            "scope": "public"
        }
        async with session.post(token_url, data=data) as response:
            if response.status == 200:
                json_response = await response.json()
                return json_response["access_token"]
            else:
                raise Exception(f"Failed to get access token. Status code: {response.status}")

async def get_random_beatmap(star_category):
    star_ranges = {
        1: (0, 1.99),
        2: (2, 2.99),
        3: (3, 3.99),
        4: (4, 4.99),
        5: (5, 5.99),
        6: (6, 6.99),
        7: (7, 7.99),
        8: (8, 8.99),
        9: (9, 10)
    }

    min_stars, max_stars = star_ranges[star_category]

    access_token = await get_access_token()
    headers = {"Authorization": f"Bearer {access_token}"}
    
    async with aiohttp.ClientSession() as session:
        url = "https://osu.ppy.sh/api/v2/beatmapsets/search"
        params = {
            "m": "0",  # 0 is for osu! standard mode
            "s": "ranked",
            "sort": "difficulty_rating",
            "q": f"stars>{min_stars} stars<{max_stars}"
        }
        async with session.get(url, headers=headers, params=params) as response:
            if response.status != 200:
                raise Exception(f"Failed to fetch beatmaps. Status code: {response.status}")

            data = await response.json()
            beatmapsets = data.get('beatmapsets', [])
            
            if not beatmapsets:
                return None

            beatmap = random.choice(beatmapsets)
            osu_difficulties = [bm for bm in beatmap['beatmaps'] if bm['mode'] == 'osu']
            difficulties_in_range = [bm for bm in osu_difficulties if min_stars <= bm['difficulty_rating'] <= max_stars]
            
            if difficulties_in_range:
                chosen_difficulty = random.choice(difficulties_in_range)
                preview_url = beatmap['preview_url']
                if not preview_url.startswith('http'):
                    preview_url = f"https:{preview_url}"
                return {
                    'id': beatmap['id'],
                    'title': beatmap['title'],
                    'artist': beatmap['artist'],
                    'difficulty_name': chosen_difficulty['version'],
                    'stars': chosen_difficulty['difficulty_rating'],
                    'download_url': f"https://osu.ppy.sh/beatmapsets/{beatmap['id']}/download",
                    'preview_url': preview_url
                }
            return None

@client.tree.command()
@app_commands.describe(stars="Choose a difficulty level from 1 to 9")
@app_commands.choices(stars=[
    app_commands.Choice(name="1 (0, 1.99)", value=1),
    app_commands.Choice(name="2 (2, 2.99)", value=2),
    app_commands.Choice(name="3 (3, 3.99)", value=3),
    app_commands.Choice(name="4 (4, 4.99)", value=4),
    app_commands.Choice(name="5 (5, 5.99)", value=5),
    app_commands.Choice(name="6 (6, 6.99)", value=6),
    app_commands.Choice(name="6 (6, 6.99)", value=7),
    app_commands.Choice(name="8 (8, 8.99)", value=8),
    app_commands.Choice(name="9 (9, 10)", value=9),
])
async def rndmp(interaction: discord.Interaction, stars: int):
    await interaction.response.defer()
    
    try:
        beatmap = await get_random_beatmap(stars)
        if beatmap:
            embed = discord.Embed(title=f"{beatmap['artist']} - {beatmap['title']} [{beatmap['difficulty_name']}]", 
                                  url=f"https://osu.ppy.sh/beatmapsets/{beatmap['id']}", 
                                  color=0x00ff00)
            embed.add_field(name="Star Rating", value=f"{beatmap['stars']:.2f}⭐", inline=True)
            embed.add_field(name="Download", value=f"[Click here]({beatmap['download_url']})", inline=True)
            
            preview_button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Get Preview Link", custom_id="preview_link")
            
            async def send_preview_link(interaction: discord.Interaction):
                await interaction.response.send_message(f"Preview link: {beatmap['preview_url']}", ephemeral=True)

            preview_button.callback = send_preview_link
            view = discord.ui.View()
            view.add_item(preview_button)
            
            await interaction.followup.send(embed=embed, view=view)
        else:
            await interaction.followup.send("No beatmaps found for the specified star rating.")
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {str(e)}")

client.run(TOKEN)