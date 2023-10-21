import utils

def avg_wc():
    all_lyrics = utils.get_all_lyrics()
    all_words = 0
    count = 0
    for title, song_lyrics in all_lyrics.items():
        if "lyrics" in song_lyrics:
            cleaned_lyrics = utils.cleanse_lyrics(song_lyrics["lyrics"])
            all_words += utils.count_words(cleaned_lyrics)
            count += 1
    avg = float(all_words) / float(count)
    print("The average word count of a Beatles song is " + str(avg) + " words.")


if __name__ == '__main__':
    avg_wc()
        