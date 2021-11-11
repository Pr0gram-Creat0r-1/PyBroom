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
            line=the_list[counter]
            id_as_variable=the_list[counter].split('=', 1)
            variable=id_as_variable[0]
            exterminator=0
            for y in range(0, len(the_list)):
                string='\n'.join(the_list)
                subsubcounter=0
                sublist=[]
                for z in range(0, len(the_list)):
                    stringg=the_list[subsubcounter].split('=', 1)[0]
                    sublist.append(stringg)
                    subsubcounter+=1
                sublist_string='\n'.join(sublist)
                if sublist_string.count(variable)==1:
                    number=1
                else:
                    number=0
                if number==1:
                    new=string.replace(line, '')
                    the_list=new.splitlines()
                exterminator+=1
        counter+=1
    new_file_name=file_path.replace('.py', '_PyBroom_cleaned.py')
    new_file=open(new_file_name, 'w')
    new_file.write(string)
    print('Done!')
