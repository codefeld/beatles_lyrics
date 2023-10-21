import re
import json

def get_all_lyrics():
    with open("lyrics.json", 'r') as json_file:
        data = json.load(json_file)
        return data

def remove_brackets(lyrics):
    return re.sub(r'\[.*?\]', '', lyrics)

def cleanse_lyrics(lyrics):
    clean_lyrics = remove_brackets(lyrics)
    return re.sub(r'\s+', " ", clean_lyrics.replace('\n', ' ').strip())

def count_words(lyrics):
    words = lyrics.split()
    return len(words)

