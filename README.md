# PyBroom
List of functions:
1. remove_variables(file_path): will remove unused variables from the specified file. Will also save a list of used variables to a separate python file. Will save a list of all variables to a different python file.
2. remove_local_variables(file_path): removes unused local variables
3. beautify(file_path): Improves code readability. Should only be used when you are absolutely desperate, since it affects strings and comments as well as the actual code (if you have a sensitive string that needs to be a certain way, then this function may cause it to cease to work).
4. suggestions(file_path): Offers "suggestions" for cleaner code. Like when it encounters a complex or hard-to-read line, or when it finds a variable, function, or class name that is not in the english dictionary (list of english words from https://pypi.org/project/english-words)
PyBroom also records the commands you entered into a list, which you can get with the history() command, and you can save the list into a file with save_history(file_path).

Notes:
1. It is HIGHLY recommended that you create a copy of your uncleaned file before using PyBroom.
2. The annoying comments at the top and the bottom are necessary for the code to work because the program needs the space it provides.
3. PyBroom is not a finished product and is still in development.
4. The code for removing variables replaces the lines with spaces. If you don't want that, call rstrip_all(file_path) to get rid of the spaces PyBroom left.
5. Very slow with large files, so be patient...

Credits:

Made in collaboration with @d10smaradona :)

https://www.geeksforgeeks.org/python-string-find/

https://stackoverflow.com/questions/15422144/how-to-read-a-long-multiline-string-line-by-line-in-python/15422155

https://stackoverflow.com/questions/13241399/check-string-indentation

https://www.programiz.com/python-programming/methods/list/remove

https://programiz.com/python-programming/methods/list/copy

https://www.programiz.com/python-programming/methods/string/count

https://stackoverflow.com/questions/12332975/installing-python-module-within-code

https://www.sanfoundry.com/python-program-check-common-letters-string/
