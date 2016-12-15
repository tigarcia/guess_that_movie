import movies


##
#
# movie_data is a python dict.  If you're
# unfamiliar with the data structure, you
# can learn more here:
#
# https://www.rithmschool.com/courses/python-fundamentals-part-1/python-dictionaries-dictionary-basics
#
# The dict has the following keys:
#
# {"Actors": "A comma separate names of actors as a string",
#  "Director": "The name of the director",
#  "Plot": "A short plot summary",
#  "Title": "The title of the movie",
#  "Year": "The year the movie was made"
# }
#
##
movie_data = movies.random_movie_data()

##
#
# Project Description:
#
# Make a guessing game where the user's goal is to
# try to guess the title of a random movie.  The code
# for getting a random movie is already provided above.
#
# The game should first print all the actors in the movie.
# From there, the users has 2 options, make a guess or ask
# for a hint.  If the user guesses and is correct, they win!
# The user should be given another movie to guess.  If the
# user asks for a hint, more movie information should be shown.
# After all the hints are given, the user can give up and
# see the answer.  The user should be able to quit the game
# at any time.
#
# Here is a suggested order for hints:
# Actors
# Year
# Director
# Plot
##
