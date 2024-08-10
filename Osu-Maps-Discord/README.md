# osu! Random Beatmap Discord Bot

This Discord bot allows users to get random osu! beatmaps based on specified star ratings and provides preview links for the beatmaps.

## Features

- `/rndmp [stars]` command to get a random osu! beatmap within a specified star rating range
- Displays beatmap information including title, artist, difficulty name, and star rating
- Provides a download link for the beatmap
- Offers a button to get a preview link for the beatmap audio

## Prerequisites

- Python 3.7 or higher
- Discord Bot Token
- osu! API Client ID and Client Secret

## Installation

1. Clone this repository or download the script.
2. Install the required Python libraries using `pip install -r requirements.txt`.

## Configuration

1. Create a `.env` file in the same directory as the script with the following content:
2. Replace `your_discord_bot_token`, `your_osu_client_id`, and `your_osu_client_secret` with your actual Discord bot token and osu! API credentials.

## Usage

1. Run the script to start the bot.
2. In a Discord server where the bot is invited, use the command `/rndmp [stars]`

Choose a star rating category from 1 to 9 when prompted.
3. The bot will respond with an embed containing the beatmap information and a "Get Preview Link" button.
4. Click the "Get Preview Link" button to receive a private message with the preview audio link.

## Star Rating Categories

- 1: 0-1.99 stars
- 2: 2-2.99 stars
- 3: 3-3.99 stars
- 4: 4-4.99 stars
- 5: 5-5.99 stars
- 6: 6-6.99 stars
- 7: 7-7.99 stars
- 8: 8-8.99 stars
- 9: 9-9.99 stars

## Permissions

Ensure that your Discord bot has the following permissions:

- Read Messages/View Channels
- Send Messages
- Embed Links
- Use Slash Commands

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes. However, please note that this project does not have an open-source license, and all rights are reserved by the author.

## Disclaimer

This bot is not officially affiliated with osu!. Use it responsibly and in accordance with osu!'s terms of service.

## Copyright

© 2023 SkLite(Minecraft Skript Organization). All rights reserved.

This project is provided "as is" without any express or implied warranties. The author retains all rights to the code and associated documentation. No permission is granted to use, modify, or distribute this software for any purpose without prior written consent from the author.