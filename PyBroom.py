#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)

### There are some obvious issues with the code. I am pointing them out in comment lines starting with 3 #s.
def clean():
  file_path=input('Paste a file path here: ')
  print('Cleaning...')
  file=open(file_path)
  text=file.read()
  the_list=text.splitlines()
  ### Iterating through a list doesn't really need the "counter". You can simply do "for x in the_list:" and then "x.find('=')!=-1".
  counter=0 ### You can remove this line. 
  for x in the_list:
    if the_list[counter].find('=')!=-1:
      #Identify as a variable assignment
      id_as_variable=the_list[counter].split('=')
      variable=id_as_variable[0]
      subcounter=0 ### Same thing with the "subcounter". You don't need it to iterate through a list.
      prev_find=0 ### Typo? You used "prev_finds" later.
      ### The following "for" loop - I don't understand exactly what you are trying to do with it.
      ### "prev_finds" is only set to 1 if the string value of "variable" happens to be at index 1 of the line "the_list[blah]".
      ### If "variable" appears in multiple places, "prev_finds" will keep adding up.
      ### Anyway, I assume you are trying to implement your goal #1 - remove unused variables. What is an unused variable in the first place?
      ### A variable that's only initialized but never appears again in the file? I think you may need to re-design the check for that.
      for y in the_list:
        number=the_list[subcounter].find(variable)
        prev_finds+=number
        subcounter+=1
      if prev_finds==1:
        new_string='\n'.join(the_list)
        new_string.replace(variable, '')
        new_string.replace(id_as_variable[1], '')
    counter+=1 ### You can remove this line.
  new_file_name=file_path.replace('.py', '_PB_cleaned.py')
  new_file=open(new_file_name, 'w')
  ### "new_string" is only initialized if prev_finds==1. If that "if" block is not entered, the next line will generate an error.
  ### You need to initialize this variable in an unconditional place.
  new_file.write(new_string)
  print('Done!')
  
  ### Even if you fix the simple typos (prev_finds/prev_find, properly initialize "new_string"), the program will still only generate an empty file. Try for yourself.