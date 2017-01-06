# Guess that Movie!
#### A practice problem for learning functions in python

This is designed as a guide to help learn functions in python by writing a fun game (hopefully it's fun!!).  The readme starts out with the description of the movie guessing game.  After the details about the guessing game, there is more information on what python functions are if you need a refresher. Lastly, there are additional resources to help you learn.

## Movie Guessing Game

In this repository, there are 3 python files: [movies.py](movies.py), [guess_that_movie.py](guess_that_movie.py), and [guess_that_movie_solution.py](guess_that_movie_solution.py).  Your task is to implement a movie guessing game in the [guess_that_movie.py](guess_that_movie.py) file.

### Game Requirements

The goal of the game is to try to guess the title of a random movie.  The code for getting a random movie is already provided by the [movie.py](movie.py) file.  You should not have to modify this file.

The game should first print all the actors in the movie, then present the user with a few options. The user has a few options: make a guess, ask for a hint, or quit the game.  If the user guesses correctly, the user wins and the user should be given another movie to guess.  If the user asks for a hint, more movie information should be shown. After all the hints are given, the user can give up and see the answer.  The user should be able to quit the game at any time.

Here is a suggested order for hints:

1. Actors
1. Year
1. Director
1.  Plot

Here is a sample of game output:

```sh
Guess the movie!
Actors: Brad Pitt, Christian Slater, Virginia McCollam, John McConnell
Type your guess, or
h - get a hint
q - quit
h
Year: 1994
Type your guess, or
h - get a hint
q - quit
h
Director: Neil Jordan
Type your guess, or
h - get a hint
q - quit
h
Plot: A vampire tells his epic life story: love, betrayal, loneliness, and hunger.
Type your guess, or
g - give up, tell me the answer
q - quit
g

The moive was Interview with the Vampire: The Vampire Chronicles

Guess the movie!
Actors: Thomas Rongen, Jaiyah Saelua, Nicky Salapu, Gene Ne'emia
Type your guess, or
h - get a hint
q - quit
q

Thanks for playing!


```

### File Details

* [movies.py](movies.py) - Has the function `random_movie_data` for getting a random movie.  You should not need to modify this file.
* [guess_that_movie.py](guess_that_movie.py) - The file you will edit to make your game
* [guess_that_movie_solution.py](guess_that_movie_solution.py) - A sample solution of the game.

### Running The Game

To run the game:

```py
python guess_that_movie.py
```

If you want a reference, you can run the solution:

```py
python guess_that_movie_solution.py
```


## What are Functions?

Functions are a set of instructions that you can use or _invoke_ as many times as you like in your program.  A function can have a set of inputs (data that the function needs to do its procedures) and an output (a returned result).

An analogy for a function is any kind of procedure you encounter in daily life.  For example:

* Pressing the button to turn on your laptop (pressing the button is like invoking the on function)
* Coffee machine - The inputs are water and coffee grounds (I think, I don't drink coffee) and the output that is returned is a hot bitter liquid

## Function Examples

Here is a simple function that prints `Hello World` in python 3.  It does not have any input, and there is no output returned either:

```py
def say_hello():
	print("Hello World")
	
say_hello()  # Hello World
```

Let's change the function to print my name. Notice in this example there are variables being passed to the function.  The variables are input to my say_hello function:

```py
def say_hello(first_name, last_name):
	print("Hello, {} {}".format(first_name, last_name))
	
say_hello("Tim", "Garcia")  # Hello, Tim Garcia
```

Now, let's create a function with inputs and an output.  We can create a function called `pow`, that takes in a base and and exponent and returns the result of taking the base to the power:

```py
def pow(base, exp):
	result = 1
	for i in range(exp):
		result *= base
	
	return result
	
pow(2,2)  # 4
pow(3,0)  # 1
pow(5,3)  # 125
```

## Pick a Number

Now let's create a number guessing game using prompt.  Then we can refactor it to use functions:

```py
import random

num = random.randint(1,10)

while True:
	guess = int(input("Pick a number between 1 and 10\n"))
	if guess < num:
		print("Too low!")
	elif guess > num:
		print("Too high!")
	else:
		print("You win! The number is {}".format(num))
		break
```

We can break this into a few functions.  First, we could write a function to ask for the number, and another to print our result with a `True` or `False` return to decide if we won:

```py
import random

num = random.randint(1,10)

def ask_for_guess():
	return int(input("Pick a number between 1 and 10\n"))
	
def check_guess(guess, num):
	won = False
	if guess < num:
		print("Too low!")
	elif guess > num:
		print("Too high!")
	else:
		print("You win! The number is {}".format(num))
		won = True
	
	return won
	

guess = ask_for_guess()
while not check_guess(guess, num):
	guess = ask_for_guess()
```

Now our code is a little more clear because we have grouped functionality into separate functions.

## Practice Problems

* Write a function called `your_name_in_stars` that takes a name as an input and returns the name surrounded by stars.  The number of stars on the left and on the right should be equal to the number of characters in your name:

```
def your_name_in_stars(name):
	# Your code here
	return name

# returns ****Jane****
your_name_in_stars('Jane')
```

* Write a function that returns the average for a list of numbers:

```py
def avg(nums):
	# Your code goes here
	return 0
```

* Write a function that finds the maximum and minimum value in a list of numbers.  Return the max and min as a tuple were the first number is the maximum and the second number is the minimum:

```py
def max_min(nums):
	# Your code goes here.
	# You will have to change the return value
	return (None, None);
```
* Write a function called `find_the_last`.  Your goal is to return the index of the _last_ occurrence of a character in a string.  If the character does not exist in the string, return None.

```py
def find_the_last(string, ch):
	# Your code goes here.
	return -1
```

## Resources For Function Practice

* [Rithm School's Python Course](https://www.rithmschool.com/courses/python-fundamentals-part-1) - A free course with lots of examples and exercises
* [Code Wars - Python](https://www.codewars.com/) - A website with hundreds of practice problems where you can test your answer
* [Learn Python The Hard Way](https://learnpythonthehardway.org/python3/ex19.html) There is an alpha version of learn python the hard way for python 3



