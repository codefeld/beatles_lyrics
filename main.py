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

def avg_unique_by_year():
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
						years_and_words[year] = {
							"words": [],
							"songs": 0,
							"avg": 0
						}
					all_unique_words = years_and_words[year]["words"]
					for word in unique_words:
						if word not in all_unique_words:
							all_unique_words.append(word)
					years_and_words[year]["words"] = all_unique_words
					years_and_words[year]["songs"] += 1
				for year in years_and_words:
					years_and_words[year]["avg"] = len(years_and_words[year]["words"]) / years_and_words[year]["songs"]
	sorted_years = sorted(years_and_words.keys())
	y_list = []
	for year in sorted_years:
		print(f"In {year}, the Beatles used an average of {years_and_words[year]['avg']} different words per song (given the song has lyrics). There were {years_and_words[year]['songs']} songs that year.")
		y_list.append(years_and_words[year]['avg'])
	xpoints = np.array(sorted_years)
	ypoints = np.array(y_list)
	plt.plot(xpoints, ypoints)
	plt.title("Average Unique Words in Beatles Lyrics Over Time")
	plt.show()

def avg_unique_by_song_by_year():
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
						years_and_words[year] = {
							"words": 0,
							"songs": 0
						}
					years_and_words[year]["words"] += len(unique_words)
					years_and_words[year]["songs"] += 1
	sorted_years = sorted(years_and_words.keys())
	y_list = []
	for year in sorted_years:
		avg = years_and_words[year]['words'] / years_and_words[year]['songs']
		print(f"In {year}, the Beatles used an average of {avg} different words per song (given the song has lyrics).")
		y_list.append(avg)
	xpoints = np.array(sorted_years)
	ypoints = np.array(y_list)
	plt.plot(xpoints, ypoints)
	plt.title("Average Unique Words in Beatles Lyrics by Song Over Time")
	plt.show()

def songs_1963():
	all_lyrics = utils.get_all_lyrics()
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			title = row[0]
			song_lyrics = all_lyrics[title]
			if "lyrics" in song_lyrics:
				if row[1] == "1963":
					unique_words = count_unique_words(song_lyrics["lyrics"])
					print(f"{title} - {len(unique_words)} unique words")

def unique_words_by_album():
	all_lyrics = utils.get_all_lyrics()
	albums = {
		"Please Please Me": {},
		"With the Beatles": {},
		"A Hard Day's Night": {},
		"Beatles for Sale": {},
		"Help!": {},
		"Rubber Soul": {},
		"Revolver": {},
		"Sgt. Pepper's Lonely Hearts Club Band": {},
		"Magical Mystery Tour": {},
		"The Beatles": {},
		"Yellow Submarine": {},
		"Abbey Road": {},
		"Let It Be": {}
	}
	for album in albums:
		albums[album] = {
			"words": 0,
			"songs": 0
		}
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			for album in albums:
				if "UK:" in row[2]:
					if f"UK: {album}" in row[2]:
						song_lyrics = all_lyrics[row[0]]
						if "lyrics" in song_lyrics:
							unique_words = count_unique_words(song_lyrics["lyrics"])
							albums[album]["words"] += len(unique_words)
						albums[album]["songs"] += 1
				elif album == row[2]:
					song_lyrics = all_lyrics[row[0]]
					if "lyrics" in song_lyrics:
						unique_words = count_unique_words(song_lyrics["lyrics"])
						albums[album]["words"] += len(unique_words)
					albums[album]["songs"] += 1
	x_list = []
	y_list = []
	for album in albums:
		avg = albums[album]["words"] / albums[album]["songs"]
		print(f"The Beatles album {album} has an average of {avg} unique words.")
		x_list.append(album)
		y_list.append(avg)
	xpoints = np.array(x_list)
	ypoints = np.array(y_list)
	plt.bar(xpoints, ypoints)
	plt.title("Average Unique Words in Beatles Lyrics by Song by Album")
	plt.show()

# def unique_by_album():
# 	all_lyrics = utils.get_all_lyrics()
# 	albums = {
# 		"Please Please Me": {},
# 		"With the Beatles": {},
# 		"A Hard Day's Night": {},
# 		"Beatles for Sale": {},
# 		"Help!": {},
# 		"Rubber Soul": {},
# 		"Revolver": {},
# 		"Sgt. Pepper's Lonely Hearts Club Band": {},
# 		"Magical Mystery Tour": {},
# 		"The Beatles": {},
# 		"Yellow Submarine": {},
# 		"Abbey Road": {},
# 		"Let It Be": {}
# 	}
# 	with open('beatles2.csv', 'r') as csvfile:
# 		csvreader = csv.reader(csvfile)
# 		next(csvreader)
# 		for row in csvreader:
# 			if "Lennon" in row[9] or "McCartney" in row[9] or "Harrison" in row[9] or "Starkey" in row[9]:
# 				title = row[0]
# 				album = row[2]
# 				song_lyrics = all_lyrics[title]
# 				if "lyrics" in song_lyrics:
# 					unique_words = count_unique_words(song_lyrics["lyrics"])
# 					if year not in albums:
# 						albums[year] = []
# 					all_unique_words = albums[year]
# 					for word in unique_words:
# 						if word not in all_unique_words:
# 							all_unique_words.append(word)
# 					albums[year] = all_unique_words
# 	sorted_years = sorted(albums.keys())
# 	y_list = []
# 	for year in sorted_years:
# 		print(f"In {year}, the Beatles used {len(albums[year])} different words.")
# 		y_list.append(len(albums[year]))
# 	xpoints = np.array(sorted_years)
# 	ypoints = np.array(y_list)
	# plt.plot(xpoints, ypoints)
	# plt.title("Number of Unique Words in Beatles Lyrics Over Time")
	# plt.show()	

def all_unique_by_album():
	all_lyrics = utils.get_all_lyrics()
	albums = {
		"Please Please Me": {},
		"With the Beatles": {},
		"A Hard Day's Night": {},
		"Beatles for Sale": {},
		"Help!": {},
		"Rubber Soul": {},
		"Revolver": {},
		"Sgt. Pepper's Lonely Hearts Club Band": {},
		"Magical Mystery Tour": {},
		"The Beatles": {},
		"Yellow Submarine": {},
		"Abbey Road": {},
		"Let It Be": {}
	}
	for album in albums:
		albums[album] = {
			"words": []
		}
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			for album in albums:
				if "UK:" in row[2]:
					if f"UK: {album}" in row[2]:
						song_lyrics = all_lyrics[row[0]]
						if "lyrics" in song_lyrics:
							unique_words = count_unique_words(song_lyrics["lyrics"])
							for word in unique_words:
								if word not in albums[album]["words"]:
									albums[album]["words"].append(word)
				elif album == row[2]:
					song_lyrics = all_lyrics[row[0]]
					if "lyrics" in song_lyrics:
						unique_words = count_unique_words(song_lyrics["lyrics"])
						for word in unique_words:
							if word not in albums[album]["words"]:
								albums[album]["words"].append(word)
	x_list = []
	y_list = []
	for album in albums:
		print(f"The Beatles album {album} has a total of {len(albums[album]['words'])} unique words.")
		x_list.append(album)
		y_list.append(len(albums[album]['words']))
	xpoints = np.array(x_list)
	ypoints = np.array(y_list)
	plt.bar(xpoints, ypoints)
	plt.title("Total Unique Words in Beatles Lyrics by Album")
	plt.show()

def most_words_per_sec():
	all_lyrics = utils.get_all_lyrics()
	most = 0
	song_with_most = ""
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			title = row[0]
			song_lyrics = all_lyrics[title]
			if "lyrics" in song_lyrics:
				if utils.words_per_sec(title, song_lyrics["lyrics"]) > most:
					most = utils.words_per_sec(title, song_lyrics["lyrics"])
					song_with_most = title
	print(f"The Beatles song with the most words per second is \"{song_with_most}\", with {most} words per second.")

def top_ten_words_per_sec():
	all_lyrics = utils.get_all_lyrics()
	song_with_value = []
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			title = row[0]
			song_lyrics = all_lyrics[title]
			if "lyrics" in song_lyrics:
				value = utils.words_per_sec(title, song_lyrics["lyrics"])
				song_with_value.append((value, title))
	sorted_list_desc = sorted(song_with_value, key=lambda x: x[0], reverse=True)
	print("The top 10 Beatles songs with the most words per second are:")
	count = 1
	for x in sorted_list_desc[:10]:
		print(f"{count}: {x[1]}, with {x[0]} words per second")
		count += 1

def top_ten_beatles_words_per_sec():
	all_lyrics = utils.get_all_lyrics()
	song_with_value = []
	with open('beatles2.csv', 'r') as csvfile:
		csvreader = csv.reader(csvfile)
		next(csvreader)
		for row in csvreader:
			if "Lennon" in row[9] or "McCartney" in row[9] or "Harrison" in row[9] or "Starkey" in row[9]:
				title = row[0]
				song_lyrics = all_lyrics[title]
				if "lyrics" in song_lyrics:
					value = utils.words_per_sec(title, song_lyrics["lyrics"])
					song_with_value.append((value, title))
	sorted_list_desc = sorted(song_with_value, key=lambda x: x[0], reverse=True)
	print("The top 10 Beatles songs with the most words per second are:")
	count = 1
	for x in sorted_list_desc[:10]:
		print(f"{count}: {x[1]}, with {x[0]} words per second")
		count += 1

def avg_word_count_by_chart():
	all_lyrics = utils.get_all_lyrics()
	words_and_ranks = {}
	x = 1
	while x != 51:
		with open('beatles2.csv', 'r') as csvfile:
			csvreader = csv.reader(csvfile)
			next(csvreader)
			songs = 0
			all_words = 0
			for row in csvreader:
				title = row[0]
				song_lyrics = all_lyrics[title]
				if row[13] == "":
					chart_num = 0
				else:
					chart_num = int(row[13])
				if "lyrics" in song_lyrics:
					cleaned_lyrics = utils.cleanse_lyrics(song_lyrics["lyrics"])
					if chart_num == x:
						# if chart_num not in words_and_ranks:
						# 	words_and_ranks[chart_num] = 0
						songs += 1
						all_words += utils.count_words(cleaned_lyrics)
			if songs == 0:
				words_and_ranks[x] = 0
			else:
				words_and_ranks[x] = all_words / songs
		x += 1
	print(words_and_ranks)
	x_list = []
	y_list = []
	for chart in words_and_ranks:
		x_list.append(chart)
		y_list.append(words_and_ranks[chart])
	xpoints = np.array(x_list)
	ypoints = np.array(y_list)
	plt.bar(xpoints, ypoints)
	plt.title("Average Word Count by Chart")
	plt.show()


if __name__ == '__main__':
	clear()
	# avg_wc()
	# print("\n")
	# unique_words()
	# print("\n")
	# unique_songwriter()
	# print("\n")
	# unique_by_year()
	# print("\n")
	# avg_unique_by_year()
	# print("\n")
	# avg_unique_by_song_by_year()
	# print("\n")
	# unique_words_by_album()
	# print("\n")
	# all_unique_by_album()
	# print("\n")
	# most_words_per_sec()
	# top_ten_words_per_sec()
	# top_ten_beatles_words_per_sec()
	avg_word_count_by_chart()
