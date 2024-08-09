# osu! Beatmap Downloader

This project consists of two Python scripts that allow you to download ranked osu! standard beatmaps in bulk.

1. `generate_links.py`: Generates a list of download links for ranked osu! standard beatmaps.
2. `download_beatmaps.py`: Downloads the beatmaps from the generated list.

## Prerequisites

- Python 3.7 or higher
- `requests` library (install with `pip install requests`)

## Setup

1. Clone this repository or download the scripts.
2. Create an osu! API application:
   - Go to https://osu.ppy.sh/home/account/edit#oauth
   - Click on "New OAuth Application"
   - Name your application and set the callback URL to `http://localhost:8080` (it won't be used)
   - Note down the Client ID and Client Secret

3. Open both `generate_links.py` and `download_beatmaps.py` in a text editor.
4. Replace `"your_client_id_here"` and `"your_client_secret_here"` with your actual Client ID and Client Secret in both scripts.

## Usage

### Step 1: Generate Beatmap Links

1. Open `generate_links.py` and set the `NUMBER_OF_BEATMAPS` variable to the number of beatmaps you want to download.
2. Run the script.
3. This will create a file named `beatmap_links.txt` containing the download links.

### Step 2: Download Beatmaps

1. Open `download_beatmaps.py` and set the `DOWNLOAD_FOLDER` variable to the path where you want to save the beatmaps (typically your osu! Songs folder).
2. Adjust `MAX_CONCURRENT_DOWNLOADS` if needed (default is 5).
3. Run the script.
4. The script will download the beatmaps from the links in `beatmap_links.txt`.

## Notes

- The scripts use the osu! API v2, which has rate limits. If you encounter errors, try reducing `MAX_CONCURRENT_DOWNLOADS` or adding delays between requests.
- Some beatmaps might fail to download due to various reasons (e.g., removed from osu!, temporary network issues). The script will log these failures.
- Ensure you have enough disk space to store all the beatmaps.
- These scripts are for personal use only. Please respect osu!'s terms of service and do not distribute downloaded beatmaps.

## Troubleshooting

If you encounter any issues:
1. Check the console output for error messages.
2. Ensure your Client ID and Client Secret are correct.
3. Verify that you have an active internet connection.
4. If you're getting rate limit errors, try reducing the number of concurrent downloads or adding longer delays between requests.

## Contributing

Feel free to fork this repository and submit pull requests with improvements or bug fixes.

## License

[Include your chosen license here]

## Disclaimer

This tool is not officially affiliated with osu!. Use it responsibly and at your own risk.
