import media
import fresh_tomatoes

#Movies can be added by creating an instance of class Movie and supply it with the movies name as argument.
#Remember to add it to the "movies" array at the bottom of the file.

casino = media.Movie("casino")
trainspotting = media.Movie("trainspotting")
inception = media.Movie("inception")
starship_troopers = media.Movie("starship troopers")
fear_and_loathing = media.Movie("fear and loathing")
pulp_fiction = media.Movie("pulp fiction")

#Add movie in this array.
movies = [casino, trainspotting, inception, starship_troopers, fear_and_loathing,pulp_fiction]

fresh_tomatoes.open_movies_page(movies)


