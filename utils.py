import re

def remove_brackets(lyrics):
    return re.sub(r'\[.*?\]', '', lyrics)

def cleanse_lyrics(lyrics):
    clean_lyrics = remove_brackets(lyrics)
    return clean_lyrics.replace('\n', ' ').strip()