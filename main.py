#   main.py
import imdb_helper
import tweets


def print_intro():
    print("\n   Welcome to Cinescrape!")

def get_movie_from_search():
    #   Get the search from the user
    name = input("\n   Please enter search keywords for a movie: ")
    mov_list = imdb_helper.get_movie_list(name, 7)

    #   Print the list of movies
    print()
    for i in range(len(mov_list)):
        print("   ", i + 1, ": ", mov_list[i][0], sep = "")
    print("   0: Search again")

    #   Allow the user to select a movie
    inum = None
    while inum == None:
        num = input("   Please select a movie: ")
        try:
            inum = int(num)
            if inum < 0 or inum > len(mov_list):
                inum = None
        except ValueError:
            inum = None

    #   Search again or return the movie
    if inum == 0:
        return get_movie_from_search()
    else:
        return mov_list[inum - 1][1]

def print_movie_info(movie):
    expanded = imdb_helper.IMDb_Movie(movie['title'], movie)
    print("\n   Printing data for", expanded.get_long_title())
    print("   IMDb Rating: ", expanded.get_ratings())

    print("\n   Actors:")
    for actor, role in expanded.get_actor_names(5):
        print("     ", actor, " - ", role)
        
    print("\n   Directors:")
    for direct in expanded.get_director_names():
        print("     ", direct)

    print("\n   Release Info:")
    info = expanded.get_release_info()
    print("     ", info)

def get_tweet_texts(tweet_texts):
	for tweet_text in tweet_texts[0:9]:
		return tweet_text

def print_tweet_texts(tweet_text):
	print(tweet_text)



def main():
    print_intro()
    mov = get_movie_from_search()
    print_movie_info(mov)
    #####################
    #   Twitter goes here
    
    print_tweet_texts()

    #####################

if __name__ == '__main__':
    main()

