# Film Library
1. Program creates the film library from 2 csv files - films.csv and shows.csv. Film is main class and Show is its subclass.
2. Method Classid.play(library[index]) raise number of display by 1
3. Method Show.number_of_episodes(library, 'title') - shows number of all episodes from your library
FUNCTIONS
4. get_series() - gives list of all episodes from Show class
5. get_movies() - gives list of all films from the library
6. search('title') - checks if the given title is in the library.
7. generate_views() - gives a random value of display to a random element in the library
8. gen_views_10() - calls generate_views() function 10 times
9. top_titles(x = 3, content_type = 'A') - shows list of the most popular (by the display value) films in the library,
   default values are given but as a content_type user can use 'A' (all films), 'M'(just movies) or 'S' (just shows)
10. add_show_season() - adds to the library full seasons of the show with given data (name, year, genre, number of season and number of episodes)
    it also chcecks if given title and number of a season already exists in the library