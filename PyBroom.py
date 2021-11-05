#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
def clean():
    file_path=input('Paste a file path here: ')
    print('Cleaning...')
    file=open(file_path)
    text=file.read()
    the_list=text.splitlines()
    counter=0
    for x in the_list:
        if the_list[counter].find('=')!=-1:
            #Identify as a variable assignment
            id_as_variable=the_list[counter].split('=')
            variable=id_as_variable[0]
            exterminator=0
            previous_finds=0
            for y in the_list:  
                if the_list[exterminator].find(variable)!=-1:
                    number=1
                else:
                    number=0
                previous_finds+=number
                exterminator+=1
            if previous_finds==1:
                new_string='\n'.join(the_list)
                new_string.replace(variable, '')
                new_string.replace(id_as_variable[1], '')
        counter+=1
  new_file_name=file_path.replace('.py', '_PyBroom_cleaned.py')
  new_file=open(new_file_name, 'w')
  new_file.write(new_string)
  print('Done!')
