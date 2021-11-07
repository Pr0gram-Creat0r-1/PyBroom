#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
def clean():
    file_path=input('Paste a file path here: ')
    print('Cleaning...')
    file=open(file_path)
    text=file.read()
    the_list=text.splitlines()
    counter=0
    for x in range(0, len(the_list)):
        if the_list[counter].count('=')==1:
            #Identify as a variable assignment
            id_as_variable=the_list[counter].split('=')
            variable=id_as_variable[0]
            exterminator=0
            for y in range(0, len(the_list)):
                string='\n'.join(the_list)
                if string.count(variable)==1:
                    number=1
                else:
                    number=0
                if number==1:
                    new=string.replace(variable, '')
                    add_equal_sign='='+id_as_variable[1]
                    new_string=new.replace(add_equal_sign, '')
                    the_list=new_string.splitlines()
                exterminator+=1
        counter+=1
    new_file_name=file_path.replace('.py', '_PyBroom_cleaned.py')
    new_file=open(new_file_name, 'w')
    new_file.write(string)
    print('Done!')
