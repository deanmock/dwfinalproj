#   imdb_helper.py
#   A helper class for the IMDB API
#   https://imdbpy.sourceforge.io/     (pip install imdbpy)
import imdb
import main.py

class IMDb_Movie():

    def __init__(self, movie_name, existing_movie = None):
        dbobj = imdb.IMDb()
        extra_info = ['full credits', 'keywords', 'main', 'release dates']
        
        if (existing_movie == None):
            search_result = dbobj.search_movie(movie_name)
            if (len(search_result) > 0):
                self.movie = search_result[0]
                dbobj.update(self.movie, info = extra_info)
            else:
                self.movie = None
        else:
            self.movie = existing_movie
            dbobj.update(self.movie, info = extra_info)


    def get_director_names(self):
        if (self.movie != None):
            return sorted([direc['name'] for direc in self.movie['directors']])
        else:
            return []

    def get_full_title(self):
        if (self.movie != None):
            if ('title' in self.movie.keys()):
                return self.movie['title']
            else:
                return "No title found"
        else:
            return "No movie found"

    def get_long_title(self):
        if (self.movie != None):
            if ('title' in self.movie.keys()):
                return self.movie['long imdb title']
            else:
                return "No title found"
        else:
            return "No movie found"

    def get_actor_names(self, count = 7):
        if (self.movie != None):
            count = min(count, len(self.movie['cast']))
            return sorted(
                [(actor['name'], actor.notes)
                for actor in self.movie['cast']][:count],
                key = lambda x: x[0])
        else:
            return []

    def get_release_info(self):
        if (self.movie != None):
            return self.movie['original air date']
        else:
            return 0

    def get_ratings(self):
        if (self.movie != None):
            return self.movie['rating']
        else:
            return None

def get_movie_list(movie_name, count = 5):
    out = []

    dbobj = imdb.IMDb()
    search_result = dbobj.search_movie(movie_name)

    for i in range(min(count, len(search_result))):
        tup = (search_result[i]['long imdb title'], search_result[i])
        out.append(tup)
    return out