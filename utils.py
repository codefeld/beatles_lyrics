import re
import json
import os
import sys
import csv

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

def count_unique_words(lyrics):
	unique_words = []
	cleaned_lyrics = cleanse_lyrics(lyrics)
	words = cleaned_lyrics.split()
	for word in words:
		word = word.strip('().,?!').lower()
		if word not in unique_words:
			unique_words.append(word)
	return unique_words

def words_per_sec(title, lyrics):
	cleaned_lyrics = cleanse_lyrics(lyrics)
	words = cleaned_lyrics.split()
	duration = get_seconds(title)
	if duration == 0:
		return 0
	return len(words) / duration

def get_seconds(title):
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			if row[0] == title:
				if row[3] != "":
					return int(row[3])
				else:
					return 0
