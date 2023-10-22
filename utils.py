import re
import json
import os
import sys

def clear():
	if sys.platform.startswith("linux"):
		os.system("clear")
	elif sys.platform.startswith("win32"):
		os.system("cls")
	elif sys.platform.startswith("darwin"):
		os.system("clear")

def get_all_lyrics():
    with open("lyrics.json", 'r') as json_file:
        data = json.load(json_file)
        return data

def remove_brackets(lyrics):
    return re.sub(r'\[.*?\]', '', lyrics)

def cleanse_lyrics(lyrics):
    clean_lyrics = remove_brackets(lyrics)
    clean_lyrics = re.sub(r'\s+', " ", clean_lyrics.replace('\n', ' ').strip())
    clean_lyrics = clean_lyrics.lower()
    return re.sub(r'\s+', " ", clean_lyrics.replace('-', ' ').strip())

def count_words(lyrics):
    words = lyrics.split()
    return len(words)

