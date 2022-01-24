# PyBroom
This is for a science project. The idea is to make a computer program that cleans up your code. It is supposed to be able to:
1. Remove variables that are never used. The user can add a comment with the variable name somewhere if he doesn't want it to be removed. But anyway the changes will be saved to a different file so.... Also if there is an unused local variable with the same name I will try to make it be able to remove that.
3. Might be able to clean up indents
5. Can delete the file entirely.
6. Can offer advice to add comments to your code.
7. Can install system requirements.

List of functions:
1. remove_variables(file_path): will remove unused variables from the specified file. Will also save a list of used variables to a separate python file. Will save a list of all variables to a different python file.
2. remove_local_variables(file_path): removes unused local variables

Notes:
1. It is HIGHLY recommended that you create a copy of your uncleaned file before using PyBroom.
4. The annoying comments at the top and the bottom are necessary for the code to work because the program needs the space it provides.

Credits:

https://www.geeksforgeeks.org/python-string-find/

https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422155

https://stackoverflow.com/questions/13241399/check-string-indentation

https://www.programiz.com/python-programming/methods/list/remove

https://programiz.com/python-programming/methods/list/copy

https://www.programiz.com/python-programming/methods/string/count
