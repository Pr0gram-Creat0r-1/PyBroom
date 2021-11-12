# PyBroom
This is for a science project. The idea is to make a computer program that cleans up your code. It is supposed to be able to:
1. Remove variables that are never used. The user can add a comment with the variable name somewhere if he doesn't want it to be removed. But anyway the changes will be saved to a different file so.... Also if there is an unused local variable with the same name I will try to make it be able to remove that.
2. Remove functions and classes that are never called. Comment to stop the thing from being removed.
3. Might be able to clean up indents and fix the code so it doesn't raise error messages?????

Credits:

https://www.geeksforgeeks.org/python-string-find/

https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422155

https://stackoverflow.com/questions/13241399/check-string-indentation

Note: This program does not work ALL the time. The best ways to make it not work:

1. Make a variable like this: i=0 print('blah blah blah'). You may notice that "print" has the letter "i" in it, and the cleaner works by finding the variables and doing stuff with them, so...
