import csv
import json
import os
from dotenv import load_dotenv
from lyrics_extractor import SongLyrics

load_dotenv()
GCS_API_KEY=os.environ['GCS_API_KEY']
GCS_ENGINE_ID=os.environ['GCS_ENGINE_ID']
extract_lyrics = SongLyrics(GCS_API_KEY, GCS_ENGINE_ID)

lyrics = {}

with open('beatles2.csv', 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    for row in csvreader:
        title = row[0].strip()
        lead_vocal = row[10].strip()
        if title == "Title":
            continue
        elif lead_vocal == "" or lead_vocal == "N/A":
            print("Skipping: " + title + ", '" + lead_vocal + "'")
            lyrics[title] = {}
            continue
        print("Downloading: " + title + ", '" + lead_vocal + "'")
        data = extract_lyrics.get_lyrics("beatles " + title)
        lyrics[title] = data
        print("  - Found: " + data["title"])
        with open('lyrics.json', 'w') as json_file:
            json.dump(lyrics, json_file)