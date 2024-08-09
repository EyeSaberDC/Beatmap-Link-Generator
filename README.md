# osu! Beatmap Link Generator

This project consists of a Python script that generates a list of download links for ranked osu! standard beatmaps.

## Prerequisites

- Python 3.7 or higher
- `requests` and `ossapi` library (install with `pip install requests ossapi`)

## Setup

1. Clone this repository or download the script.
2. Create an osu! API application:
   - Go to https://osu.ppy.sh/home/account/edit#oauth
   - Click on "New OAuth Application"
   - Name your application and set the callback URL to `http://localhost:8080` (it won't be used)
   - Note down the Client ID and Client Secret

3. Open `generate_links.py` in a text editor.
4. Replace `"your_client_id_here"` and `"your_client_secret_here"` with your actual Client ID and Client Secret.

## Usage

1. Open `generate_links.py` and set the `NUMBER_OF_BEATMAPS` variable to the number of beatmap links you want to generate.
2. Run the script:
3. This will create a file named `beatmap_links.txt` containing the download links for ranked osu! standard beatmaps.

## Notes

- The script uses the osu! API v2, which has rate limits. If you encounter errors, try adding delays between requests.
- This script is for personal use only. Please respect osu!'s terms of service.
- The generated links are direct download links for the beatmaps. You'll need to be logged into your osu! account to use these links.

## Troubleshooting

If you encounter any issues:
1. Check the console output for error messages.
2. Ensure your Client ID and Client Secret are correct.
3. Verify that you have an active internet connection.
4. If you're getting rate limit errors, try adding longer delays between requests.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## Disclaimer

This tool is not officially affiliated with osu! Use it responsibly and at your own risk.

## Legal Notice

This project is provided "as is" without any warranty. The author is not responsible for any misuse or any consequences arising from the use of this software. Users are solely responsible for ensuring their use of this tool complies with osu!'s terms of service and any applicable laws or regulations.

No license is granted for this project. All rights are reserved by the author. If you wish to use, modify, or distribute this code, please contact the author for permission.
