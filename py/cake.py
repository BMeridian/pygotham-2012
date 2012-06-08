"""
cake.py
=====
Write a program that asks the user if they want cake.  If the user answers yes, ask the user if they want frosting.  If the user answers yes again, print out a statement giving the user a cake with frosting. 

If the user says no to cake, print out a message saying "no cake for you!".  If the user says no to frosting, print out a message saying  "no frosting for you!".

Example Output (the > denotes user input):

$ python cake.py 
Do want cake?
> yes
Do you want frosting on your cake?
> yes
Have a cake with frosting!

$ python cake.py 
Do want cake?
> yes
Do you want frosting on your cake?
> no
No frosting for you!

$ python cake.py 
Do want cake?
> no
No cake for you!

Extra Credit #1 - normalize the user input by using a string function that will transform any variation in casing  ("Yes", "yes", "YES") so that you only have to compare the input to "yes"

Extra Credit #2 - if you didn't add an explicit check for "no", do so.  If the user does not respond with either a yes or a no, add a code path that berates the user for not answering appropriately!
"""
