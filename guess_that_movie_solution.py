import movies


def game_menu(hints):
    print("Type your guess, or")
    if len(hints) == 0:
        print("g - give up, tell me the answer")
    else:
        print("h - get a hint")
    print("q - quit")
    return input()


def movie_intro(movie_data):
    print("Guess the movie!")
    print("Actors: {}".format(movie_data['Actors']))


def handle_response(hints, movie_data, resp):

    # Status codes:
    # 0 nothing interesting happened
    # 1 need a new guess
    # 2 quit the game
    status = 0

    if resp == "h":
        h = hints.pop()
        print("{}: {}".format(h, movie_data[h]))
    elif resp == "g":
        print("\nThe moive was {\n".format(movie_data['Title']))
        status = 1
    elif resp == "q":
        status = 2
    elif resp.lower() == movie_data['Title'].lower():
        print("\nYou got it! The movie is {}\n".format(movie_data['Title']))
        status = 1
    else:
        print("Sorry, try again!")

    return status


def hint_array():
    return ["Plot", "Director", "Year"]


def guessing_game():
    hints = None

    status = 1
    while status != 2:
        if status == 1:
            movie_data = movies.random_movie_data()
            hints = hint_array()
            movie_intro(movie_data)

        resp = game_menu(hints)
        status = handle_response(hints, movie_data, resp)

    print("\nThanks for playing!\n")

guessing_game()
