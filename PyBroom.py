#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
import os
def remove_variables():
    'Remove unused variables.'
    file_path=input('Paste a file path here: ')
    file=open(file_path)
    text=file.read()
    new_text=text.replace(' =', '=')
    while new_text.count(' =')>=1:
        new_text.replace(' =', '=')
    the_list=new_text.splitlines()
    counter=0
    variable_list=[]
    word_list=[]
    real_word_list=[]
    variable=None
    for x in range(0, len(the_list)):
        line=the_list[counter]
        if line.count('=')>=1:
            new_line=line.replace('    ', '')
            variable=new_line.split('=')[0]
            variable_list.append(variable)
        counter+=1
    new_variable_list=variable_list.copy()
    string_of_variables='\n'.join(variable_list)
    open('%s_PyBroom_all_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
    counter=0
    new_list=the_list.copy()
    baby_word_string='\n'.join(new_list)
    word_string=baby_word_string.replace('    ', '').replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ')
    word_list=word_string.split('\n')
    for c in range(0, len(word_list)):
        string_list=word_list[counter].split(' ')
        subcounter=0
        for b in range(0, len(string_list)):
          real_word_list.append(string_list[subcounter])
          subcounter+=1
        counter+=1
    counter=0
    #As of now, we have a list of variables and a list of words. That is what the previous code is attempting to create.
    list_counter1=0
    list_counter2=0
    for y in range(0, len(variable_list)):
        list_counter2=0
        counted=0
        for a in range(0, len(real_word_list)):
            var=variable_list[list_counter1]
            word=real_word_list[list_counter2]
            if var==word:
                counted+=1
            list_counter2+=1
        if counted==1:
            string='\n'.join(the_list)
            remove_counter=0
            for z in range(0, len(the_list)):
                line=the_list[remove_counter].split('=')[0].replace('    ', '')
                if var==line:  
                    new=string.replace(the_list[remove_counter], '')
                    new_variable_list.remove(var)
                    the_list=new.splitlines()
                remove_counter+=1
        list_counter1+=1
    string='\n'.join(the_list)
    new_file_name=file_path.replace('.py', '_PyBroom_cleaned.py')
    new_file=open(new_file_name, 'w')
    new_file.write(string)
    string_of_variables='\n'.join(new_variable_list)
    open('%s_PyBroom_used_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
def remove_local_variables():
    'Remove local variables. Use this before cleaning global variables in the remove_variables() function.'
    pass
def remove_functions():
    'Remove unused functions.'
    pass #For now :)
def destroy():
    'Delete the file completely.'
    file_path=input('Paste a file path here: ')
    os.remove(file_path)
def test_for_errors():
    'Test the file for errors.'
    pass
def install_system_requirements():
    'Install the python modules needed; uses pip.'
    pass
def remove_classes():
    'Removes unused classes.'
    pass
def suggestions():
    'Give suggestions.'
    pass
def find_strings(file_path):
    'Find strings in a text file. Internal use only. In development.'
    file_string=open(file_path).read()
    important_list=[]
    string_type_list=[]
    string_index_list=[]
    file_string=file_string.replace("\\\'", '').replace('\\\"', '')
    for finder in range(0, len(file_string)):
        index=file_string.find("'")
        if index!=-1:
            string_type_list.append("'")
            string_index_list.append(index)
        file_string=file_string.replace("'", '', 1)
    for finder in range(0, len(file_string)):
        index=file_string.find('"')
        if index!=-1:
            string_type_list.append('"')
            string_index_list.append(index)
        file_string=file_string.replace('"', '', 1)
    first_occurrence=string_index_list[0]
    first_occurrence_type=string_type_list[0]
    #Alright, so we now have all the information we need of the first occurrence.
    string_type_list.remove(first_occurrence_type)
    string_index_list.remove(first_occurrence)
    magic=string_type_list.index(first_occurrence_type)+1
    the_index=string_index_list[magic]
    important_list.append([first_occurrence, the_index])
    print(string_index_list)
    print(string_type_list)
    print(file_string)
    return important_list
    #I think the index list will be in numerical order.
    #Okay, this is what I have so far.
    #By the way, I will also program this thing to remove comments :)
