"""
guess_number.py
=====
1.  Write a program that stores a number in a variable named secret_number.  When the program is run, it asks the user to:

Guess what number I'm thinking of...

For a hint on how to get user input, see exercise 11 of LPTHW (http://learnpythonthehardway.org/book/ex11.html).  Use the function "int()" to convert the user's input into an integer.  Store the user's guess in a variable called guess (of course!).  If the number entered is the same as the secret number, print out "You got it!".  If the number entered is not equal to the secret number, print out whether or not it was too low or to high.  Use conditionals to implement this - see exercises 29 through 31 in LPTHW for hints.

Example:

(number stored in variable is 5)

walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...  25
Too high!
walsh:~ joe$ python /tmp/guess_number.py 
Guess what number I'm thinking of...  2
Too low!
walsh:~ joe$ python /tmp/guess_number.py 
Guess what number I'm thinking of...  5
You got it!

	a.  Test your program with 3 test cases - one too high, one too low, and one that's equal.  

	b.  Why do you have to use int() to convert user input?  Use help(raw_input) and help(int) in the interactive shell for some hints.  

2.  Modify your program to output the guess, as well the message.  If the guess is wrong, also print out the correct answer (in the same line).  Don't hardcode the numbers; use the variables that you created and use string interpolation.  

Example:

(number stored in variable is 5)

walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...  25
You guessed 25.  Too high!  The right answer is 5.
walsh:~ joe$ python /tmp/guess_number.py 
Guess what number I'm thinking of...  2
You guessed 2.  Too low!  The right answer is 5.
walsh:~ joe$ python /tmp/guess_number.py 
Guess what number I'm thinking of...  5
You guessed 5.  You got it!

3.  Continue modifying your program.  It should still do the same thing as #2.  However, if the guess is either one below or one above, instead of printing "Too high!" or "Too low!", print out "You were just off by 1!"
	
Example:

walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...1
You guessed 1.  Too low!  The right answer is 5.
walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...7
You guessed 7.  Too high!  The right answer is 5.
walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...4
You guessed 4.  You were just off by 1.  The right answer is 5
walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...6
You guessed 6.  You were just off by 1.  The right answer is 5
walsh:~ joe$ python /tmp/guess_number.py
Guess what number I'm thinking of...5
You guessed 5.  You got it
"""
