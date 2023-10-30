import utils
from utils import clear, count_unique_words
import csv
import matplotlib.pyplot as plt
import numpy as np

def avg_wc():
	all_lyrics = utils.get_all_lyrics()
	all_words = 0
	given_lyrics_count = 0
	count = 0
	most_words = ""
	most_words_value = 0
	least_words = ""
	least_words_value = 9999999999999999
	for title, song_lyrics in all_lyrics.items():
		if "lyrics" in song_lyrics:
			cleaned_lyrics = utils.cleanse_lyrics(song_lyrics["lyrics"])
			all_words += utils.count_words(cleaned_lyrics)
			given_lyrics_count += 1
			if utils.count_words(cleaned_lyrics) > most_words_value:
				most_words = title
				most_words_value = utils.count_words(cleaned_lyrics)
			if utils.count_words(cleaned_lyrics) < least_words_value:
				least_words = title
				least_words_value = utils.count_words(cleaned_lyrics)
		count += 1
	avg_given_lyrics = float(all_words) / float(given_lyrics_count)
	avg = float(all_words) / float(count)
	print("The average word count of a Beatles song is " + str(avg) + " words.")
	print("The average word count of a Beatles song (given it has lyrics) is " + str(avg_given_lyrics) + " words.")
	print("The Beatles song with the most lyrics is \"" + most_words + "\", which has " + str(most_words_value) + " words.")
	print("The Beatles song with the least lyrics is \"" + least_words + "\", which has " + str(least_words_value) + " words.")

def unique_words():
	all_lyrics = utils.get_all_lyrics()
	most_unique_words = 0
	unique_words_test = 0
	least_unique_words = 999999999999
	song_with_most = ""
	song_with_least = ""
	for title, song_lyrics in all_lyrics.items():
		if "lyrics" in song_lyrics:
			cleaned_lyrics = utils.cleanse_lyrics(song_lyrics["lyrics"])
			words = cleaned_lyrics.split()
			unique_words_in_song = set()
			for word in words:
				word = word.strip('().,?!').lower()
				unique_words_in_song.add(word)
			unique_words_test = len(unique_words_in_song)
			if unique_words_test > most_unique_words:
				most_unique_words = unique_words_test
				song_with_most = title
			if unique_words_test < least_unique_words:
				least_unique_words = unique_words_test
				song_with_least = title
	print("The Beatles song with the most unique lyrics is \"" + song_with_most + "\", which has " + str(most_unique_words) + " unique words.")
	print("The Beatles song with the least unique lyrics is \"" + song_with_least + "\", which has " + str(least_unique_words) + " unique words.")

def unique_songwriter():
	all_lyrics = utils.get_all_lyrics()
	lennon_unique_lyrics = []
	mccartney_unique_lyrics = []
	harrison_unique_lyrics = []
	starr_unique_lyrics = []
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			if True:
				title = row[0]
				song_lyrics = all_lyrics[title]
				if "lyrics" in song_lyrics:
					unique_words = count_unique_words(song_lyrics["lyrics"])
					if "Lennon" in row[9]:
						for word in unique_words:
							if word not in lennon_unique_lyrics:
								lennon_unique_lyrics.append(word)
					elif "McCartney" in row[9]:
						for word in unique_words:
							if word not in mccartney_unique_lyrics:
								mccartney_unique_lyrics.append(word)
					elif "Harrison" in row[9]:
						for word in unique_words:
							if word not in harrison_unique_lyrics:
								harrison_unique_lyrics.append(word)
					elif "Starkey" in row[9]:
						for word in unique_words:
							if word not in starr_unique_lyrics:
								starr_unique_lyrics.append(word)
	print("John Lennon used a total of " + str(len(lennon_unique_lyrics)) + " unique words in Beatles songs.")
	print("Paul McCartney used a total of " + str(len(mccartney_unique_lyrics)) + " unique words in Beatles songs.")
	print("George Harrison used a total of " + str(len(harrison_unique_lyrics)) + " unique words in Beatles songs.")
	print("Ringo Starr used a total of " + str(len(starr_unique_lyrics)) + " unique words in Beatles songs.")

def unique_by_year():
	all_lyrics = utils.get_all_lyrics()
	years_and_words = {}
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			if "Lennon" in row[9] or "McCartney" in row[9] or "Harrison" in row[9] or "Starkey" in row[9]:
				title = row[0]
				year = row[1]
				song_lyrics = all_lyrics[title]
				if "lyrics" in song_lyrics:
					unique_words = count_unique_words(song_lyrics["lyrics"])
					if year not in years_and_words:
						years_and_words[year] = []
					all_unique_words = years_and_words[year]
					for word in unique_words:
						if word not in all_unique_words:
							all_unique_words.append(word)
					years_and_words[year] = all_unique_words
	sorted_years = sorted(years_and_words.keys())
	y_list = []
	for year in sorted_years:
		print(f"In {year}, the Beatles used {len(years_and_words[year])} different words.")
		y_list.append(len(years_and_words[year]))
	xpoints = np.array(sorted_years)
	ypoints = np.array(y_list)
	plt.plot(xpoints, ypoints)
	plt.title("Number of Unique Words in Beatles Lyrics Over Time")
	plt.show()
				

if __name__ == '__main__':
	clear()
	avg_wc()
	print("\n")
	unique_words()
	print("\n")
	unique_songwriter()
	print("\n")
	unique_by_year()
		