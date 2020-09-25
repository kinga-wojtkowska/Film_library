# Film Library
1. Program creates the film library from 2 csv files - films.csv and shows.csv. Film is main class and Show is its subclass.
2. play('title', library) raise number of display by 1 (if it's a series, it will ask for the season and episode number)
3. number_of_episodes('title', library) - shows number of all episodes from your library
4. get_series(library) - gives list of all episodes from Show class
5. get_movies(library) - gives list of all films from the library
6. search('title', library) - checks if the given title is in the library.
7. generate_views(library) - gives a random value of display to a random element in the library
8. gen_views_10(library) - calls generate_views() function 10 times
9. top_titles(library, x = 3, content_type = 'A') - shows list of the most popular (by the display value) films in the library,
   default values are given but as a content_type user can use 'A' (all films), 'M'(just movies) or 'S' (just shows)
10. add_show_season(library) - adds to the library full seasons of the show with given data (name, year, genre, number of season and number of episodes)
    it also chcecks if given title and number of a season already exists in the library