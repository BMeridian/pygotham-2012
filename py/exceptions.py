"""
exceptions.py
=====
To handle errors, use a try/catch block:

-----
try:
	# do your stuff
except SomeError:
	# deal with some error
-----

optionally... you can continue catching more than one exception:

-----
.
.
except AnotherError:
	# deal with another error
-----

Substitute SomeError with the kind of error you want to handle - for example:

KeyError
ValueError
TypeError
IndexError
ZeroDivisionError

You can get a hold of the exception by using "as some_name"
-----
.
.
except AnotherError as e:
	print e
-----


You can also define clean up by using finally
-----
.
.
finally:
	# clean stuff up
-----


You can raise an exception:
-----
raise Exception('uh oh')
-----

You should try to use one of the built in exceptions:
http://docs.python.org/library/exceptions.html
...but you can make your own class as well
-----
class MyException(Exception):
	pass
-----
"""
#KeyError

#ValueError (conversion errors)

#TypeError 

#IndexError

#ZeroDivisionError

#catching multiple possible exceptions - try possible KeyError AND TypeError like dictionary value divided by another value
#ex... which player do you want to add a score to, and add that score
