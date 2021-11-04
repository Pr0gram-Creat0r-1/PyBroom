#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
def clean():
  file_path=input('Paste a file path here: ')
  file=open(file_path)
  text=file.read()
  lines=text.count('\n')
  the_list=text.splitlines()
  for x in the_list:
    pass
