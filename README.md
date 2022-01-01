# PyBroom
This is for a science project. The idea is to make a computer program that cleans up your code. It is supposed to be able to:
1. Remove variables that are never used. The user can add a comment with the variable name somewhere if he doesn't want it to be removed. But anyway the changes will be saved to a different file so.... Also if there is an unused local variable with the same name I will try to make it be able to remove that.
2. Remove functions and classes that are never called. Comment to stop the thing from being removed.
3. Might be able to clean up indents and fix the code so it doesn't raise error messages?????
4. Can test a file for errors.
5. Can delete the file entirely.
6. Can offer advice to add comments to your code.
7. Can install system requirements.

List of functions:
1. clean_variables(): will remove unused variables from the specified file. Will also save a list of used variables to a separate python file. Will save a list of all variables to a different python file.
2. clean_functions(): will remove unused functions from the specified file. Leave a comment with the function name in your code if you do not want it to be removed. Will save a list of used functions to a different file.
3. clean_classes():

Notes:
1. If the remove_variables function raises and IndexError: list index out of range, then try removing any whitespace lines in your code, definitely at the end of the text at least.
2. You should probably make a copy of your file before cleaning.
3. The annoying comments at the top and the bottom are necessary for the code to work because the program needs the space it provides. So I thought, why not use it as free advertising? But you can delete them if you want (actually, you should, because if you use the program on the same file again it might mess up the formatting of the text).

Credits:

https://www.geeksforgeeks.org/python-string-find/

https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422155

https://stackoverflow.com/questions/13241399/check-string-indentation

https://www.programiz.com/python-programming/methods/list/remove

https://programiz.com/python-programming/methods/list/copy

