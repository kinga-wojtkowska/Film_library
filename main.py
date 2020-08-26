class Film:
    def __init__(self, title, year, genre, display):
        self.title = title
        self.year = year
        self.genre = genre
        #variables
        self.display = 0

    def __str__(self):
        return ("{} ({})".format(self.title, self.year,))

    def __repr__(self):
        return "{} {}, {}, {})".format(self.title, self.year, self.genre, self.display)

    def play(self, step=1):
        self.display += step

class Show(Film):
    def __init__(self, episode, season, *args):
        super().__init__(*args)
        self.episode = episode
        self.season = season

    def __str__(self):
        return ("{} S{:02}E{:02} ".format(self.title, int(self.season), int(self.episode)))
    def __repr__(self):
        return "{} S{:02}E{:02}, {}, {}, {})".format(self.title, int(self.season), int(self.episode), self.year, self.genre, self.display)
#shows number of all episodes from your library
    def number_of_episodes(self, title):
        search_show_list = [(i.title, i.season, i.episode) for i in library if title == i.title]
        return "There are {} episodes of this series in the database".format((len(search_show_list)))

library = []
def load_films(filename):         
    import csv
    with open(filename, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        if filename == films:
            for row in reader:
                library.append(Film(row['title'], row['year'], row['genre'], row['display']))
        elif filename == shows:
            for row in reader:
                library.append(Show(row['episode'], row['season'], row['title'], row['year'], row['genre'], row['display']))
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
films = os.path.join(THIS_FOLDER, 'films.csv')
shows = os.path.join(THIS_FOLDER, 'shows.csv')

load_films(films)
load_films(shows)
#gives list of all episodes from Show class
def get_series():
    shows_only = [x for x in library if (isinstance(x, Show))]
    by_title_shows = sorted(shows_only, key=lambda show: show.title)
    for i in by_title_shows:
        print(i)
#gives list of all films from the library       
def get_movies():
    movies_only = [x for x in library if not isinstance(x, Show)]
    by_title_movies = sorted(movies_only, key=lambda movie: movie.title)
    for i in by_title_movies:
        print(i)

#checks if the given title is in the library
def search(title):
    search_title = [i.title for i in library if title == i.title]
    if len(search_title) == 0:
        txt = "The title you are looking for does not exist in the library."
        return txt    
    for i in library:
        if i.title in search_title:
            return print("The given title: '{}' exists in our database.".format(i.title))
        else:
            pass

#gives a random value of display to a random element in the library
def generate_views():
    import random
    x = random.choice(library)
    x.display = x.display + random.randint(0,101)
def gen_views_10():
    for i in range(10):
        generate_views()

def top_titles(x = 3, content_type = 'A'):
    by_display_all = sorted(library, key=lambda all: all.display, reverse = True)
    movies_only = [x for x in library if not isinstance(x, Show)]
    by_display_movies = sorted(movies_only, key=lambda movies: movies.display, reverse = True)
    shows_only = [x for x in library if (isinstance(x, Show))]
    by_display_shows = sorted(shows_only, key=lambda shows: shows.display, reverse = True)
    '''x = input("How many top titles you want to see? ")
    content_type = input("What do you want to see? all titles ('A'), only movies ('M') or just series ('S')? ")'''
    z = 0
    options = {
        'A': by_display_all,
        'M': by_display_movies,
        'S': by_display_shows
    }
    for k, v in options.items():
        if content_type == k:
            for i in options[k]:
                print(repr(i))
                z += 1
                if z == int(x):
                    break
        elif content_type not in options.keys() :
            print("You gave the wrong value")
            break
# adds to the library full seasons of the show
def add_show_season():
    title = input("Enter the title of the show: ")
    search_title = [i.title for i in library if title == i.title]
    year = input("Enter the year of production: ")
    genre = input("Enter the genre of the show: ")
    season = input("Enter the season number you want to add: ")
    episodes = input("How many episodes does this season have?: ")
    display = 0
    if len(search_title) == 0:
        for i in range(1,(int(episodes) + 1)):
            library.append(Show(i, season, title, year, genre, display))
    elif title in search_title:
        search_show_list = [(i.title, i.season) for i in library if title == i.title]
        search_show_dict = dict(search_show_list)
        if season in search_show_dict.values():
            print("The given season number already exists in our database.")
        else:
            for i in range(1,(int(episodes) + 1)):
                library.append(Show(i, season, title, year, genre, display))

print()
print("Biblioteka filmów")                
print()
gen_views_10()
gen_views_10()
gen_views_10()

from dateutil import tz
import datetime
Warsaw_tz = tz.gettz("Europe/Warsaw")
d = datetime.datetime.now(tz=Warsaw_tz)
print("Najpopularniejsze filmy i seriale dnia {:02}.{:02}.{} r.:".format(d.day, d.month, d.year))
print()
print('LISTA TOP 3 NA DZIŚ')
print()
top_titles(x = 3, content_type = 'A')