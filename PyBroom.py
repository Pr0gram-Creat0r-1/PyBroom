#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
def clean():
  file_path=input('Paste a file path here: ')
  file=open(file_path)
  text=file.read()
  the_list=text.splitlines()
  counter=0
  for x in the_list:
    if the_list[counter].find('=')!=-1:
      #Identify as a variable assignment
      id_as_variable=the_list[counter].split('=')
      variable=id_as_variable[0]
      subcounter=0
      prev_find=0
      for y in the_list:
        number=the_list[subcounter].find(variable)
        prev_finds+=number
        subcounter+=1
      if prev_finds==1:
        new_string='\n'.join(the_list)
        new_string.replace(variable, '')
        new_string.replace(id_as_variable[1], '')
    counter+=1
