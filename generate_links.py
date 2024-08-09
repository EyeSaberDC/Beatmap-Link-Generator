import os
import time
import logging
import requests
from ossapi import Ossapi
from ossapi.enums import BeatmapsetSearchCategory

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CLIENT_ID = "your_client_id_here"
CLIENT_SECRET = "your_client_secret_here"
OUTPUT_FILE = "beatmap_links.txt"
NUMBER_OF_BEATMAPS = 50000

def get_access_token():
    token_url = "https://osu.ppy.sh/oauth/token"
    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials",
        "scope": "public"
    }
    response = requests.post(token_url, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to get access token. Status code: {response.status_code}, Response: {response.text}")

def get_beatmap_links():
    try:
        access_token = get_access_token()
        headers = {"Authorization": f"Bearer {access_token}"}
        total_collected = 0
        cursor_string = None

        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            while total_collected < NUMBER_OF_BEATMAPS:
                logging.info(f"Fetching next batch of beatmaps...")
                
                url = "https://osu.ppy.sh/api/v2/beatmapsets/search"
                params = {
                    "m": "0",
                    "s": "ranked",
                    "sort": "ranked_desc",
                    "cursor_string": cursor_string
                }
                response = requests.get(url, headers=headers, params=params)
                
                if response.status_code != 200:
                    logging.error(f"Failed to fetch beatmaps. Status code: {response.status_code}")
                    break

                data = response.json()
                beatmapsets = data.get('beatmapsets', [])
                
                if not beatmapsets:
                    logging.info("No more beatmaps available.")
                    break

                for beatmap in beatmapsets:
                    if total_collected >= NUMBER_OF_BEATMAPS:
                        break
                    if any(bm['mode'] == 'osu' for bm in beatmap['beatmaps']):
                        download_url = f"https://osu.ppy.sh/beatmapsets/{beatmap['id']}/download"
                        f.write(f"{download_url}\n")
                        f.flush()
                        total_collected += 1
                        logging.info(f"Added link for beatmap {beatmap['id']}. Progress: {total_collected}/{NUMBER_OF_BEATMAPS}")
                
                cursor_string = data.get('cursor_string')
                if not cursor_string:
                    logging.info("No more pages available.")
                    break
                
                time.sleep(1)

        logging.info(f"Finished collecting {total_collected} beatmap links. Saved to {OUTPUT_FILE}")
        
        with open(OUTPUT_FILE, 'r', encoding='utf-8') as f:
            line_count = sum(1 for line in f)
        logging.info(f"Verification: {line_count} lines written to {OUTPUT_FILE}")
        
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}", exc_info=True)

if __name__ == "__main__":
    get_beatmap_links()
