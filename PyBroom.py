#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
import os
def find_strings(file_path):
    'Find strings in a text file. Internal use only. In development.'
    file_string=open(file_path).read()
    important_list=[]
    string_type_list=[]
    string_index_list=[]
    file_string=file_string.replace("\\\'", '  ').replace('\\\"', '  ')
    for finder in range(0, len(file_string)):
        index=file_string.find("'")
        if index!=-1:
            string_type_list.append("'")
            string_index_list.append(index)
        file_string=file_string.replace("'", ' ', 1)
    for finder in range(0, len(file_string)):
        index=file_string.find('"')
        if index!=-1:
            string_type_list.append('"')
            string_index_list.append(index)
        file_string=file_string.replace('"', ' ', 1)
    while len(string_index_list)>0:
        try:
            first_occurrence=min(string_index_list)
            first_occurrence_type=string_type_list[0]
            #Alright, so we now have all the information we need of the first occurrence.
            string_type_list.remove(first_occurrence_type)
            string_index_list.remove(first_occurrence)
            magic=string_type_list.index(first_occurrence_type)
            the_index=string_index_list[magic]
            important_list.append([first_occurrence, the_index])
        except ValueError:
            pass
        counter=0
        try:
            while min(string_index_list)<=the_index:
                string_index_list.remove(string_index_list[counter])
                string_type_list.remove(string_type_list[counter])
                counter+=1
        except ValueError:
            pass
        except IndexError:
            pass
        #Remove everything between the two elements in the lists. I will also put this in a loop later.
    counter=0
    the_string=open(file_path).read()
    for j in range(0, len(important_list)):
        replace_string=the_string[important_list[counter][0]:important_list[counter][1]+1]
        new_string=replace_string.replace('\n', '\\n')
        the_string=the_string.replace(replace_string, new_string)
        counter+=1
    new_the_string=open(file_path, 'w')
    new_the_string.write(the_string)
    return important_list
    #I think the index list will be in numerical order.
    #Okay, this is what I have so far.
    #By the way, I will also program this thing to remove comments :)
def find_comments(file_path):
    'Find comments.'
    find_strings(file_path)
    strings_list=find_strings(file_path)
    baby_word_string=open(file_path).read()
    file_list=baby_word_string.splitlines()
    the_list=baby_word_string.splitlines()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(baby_word_string[strings_list[counter][0]])
            baby_word_string=baby_word_string.replace(baby_word_string[par1], ' ', 1)
            par2=baby_word_string.find(baby_word_string[strings_list[counter][1]])
            baby_word_string=baby_word_string.replace(baby_word_string[par2], ' ', 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    text_list=baby_word_string.splitlines()
    comment_list=[]
    counter=0
    for x in range(0, len(text_list)):
        line=text_list[counter]
        try:
            if line.count('#')>=1:
                number=line.find('#')
                comment=[baby_word_string.find('#'+line.split('#')[1]), baby_word_string.find('#'+line.split('#')[1])+len('#'+line.split('#')[1])]
                file_list[counter]=the_list[counter].split(the_list[counter][number])[0].replace('#'+line.split('#')[1], ' '*len('#'+line.split('#')[1]), 1)
                comment_list.append(comment)
        except IndexError:
            pass
        counter+=1
    return comment_list
def find_functions(file_path):
    'Find functions.'
    text=open(file_path).read()
    the_list=text.splitlines()
    counter=0
    functions_list=[]
    for x in range(0, len(the_list)):
        line=the_list[counter]
        if (line.split('def')[0].isspace()==True or line.split('def')[0]=='') and line.lstrip()[0:4]=='def ':
            indents=line.split('def')[0].count('    ')
            position=text.find(line.lstrip())
            subcounter=counter
            for y in range(0, len(the_list)-the_list.index(line)):
                subline=the_list[subcounter]    
                indents2=subline.replace(subline.lstrip(), '').count('    ')
                if indents2==indents and text.find(subline)-1>text.find(line):
                    position2=text.find(subline)-1
                    break
                else:
                    position2=None
                subcounter+=1
            if position2!=None:    
                functions_list.append([position, position2])
        counter+=1
    return functions_list
def remove_local_variables(file_path):
    'Remove local variables. Use this before cleaning global variables in the remove_variables() function.'
    read_file=open(file_path).read()
    with_comment='#PyBroom cleaned this file.\n'+read_file+'\n#https://github.com/Pr0gram-Creat0r-1/PyBroom\n#https://replit.com/@Pr0gram-Creat0r/PyBroom'
    open(file_path, 'w').write(with_comment)
    if find_functions(file_path)!=[]:
        comment_list=find_comments(file_path)
        find_strings(file_path)
        strings_list=find_strings(file_path)
        functions_list=find_functions(file_path)
        text=open(file_path).read()
        baby_word_string=open(file_path).read()
        baby_word_string2=open(file_path).read()
        counter=0
        function_list=[]
        for extract in range(0, len(functions_list)):
            function=baby_word_string2[functions_list[counter][0]:functions_list[counter][1]+1]
            function_list.append(function)
            counter+=1
        counter=0
        for m in range(0, len(strings_list)):
            try:
                par1=baby_word_string.find(baby_word_string[strings_list[counter][0]])
                baby_word_string=baby_word_string.replace(baby_word_string[par1], ' ', 1)
                par2=baby_word_string.find(baby_word_string[strings_list[counter][1]])
                baby_word_string=baby_word_string.replace(baby_word_string[par2], ' ', 1)
                baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
            except IndexError:
                pass
            counter+=1
        counter=0
        for m in range(0, len(comment_list)):
            try:
                par1=baby_word_string.find(baby_word_string[comment_list[counter][0]])
                baby_word_string=baby_word_string.replace(baby_word_string[par1], ' ', 1)
                par2=baby_word_string.find(baby_word_string[comment_list[counter][1]])
                baby_word_string=baby_word_string.replace(baby_word_string[par2], ' ', 1)
                baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
            except IndexError:
                pass
            counter+=1
        counter=0
        function_list2=[]
        for extract in range(0, len(functions_list)):
            function=baby_word_string[functions_list[counter][0]:functions_list[counter][1]+1]
            function_list2.append(function)
            counter+=1
        counter=0
        main_counter=0
        local_variables_list=[]
        used_local_variables=[]
        for remove in range(0, len(function_list)):
            function_text=function_list2[main_counter]
            the_new_list=function_text.splitlines()
            the_list=function_list[main_counter].splitlines()
            variable_list=[]
            real_word_list=[]
            for x in range(0, len(the_new_list)):
                line=the_new_list[counter]
                if line.count('=')==1:
                    new_line=line.replace(' ', '')
                    variable=new_line.split('=')[0]
                    variable_list.append(variable)
                counter+=1
            new_variable_list=variable_list.copy()
            string_of_variables=' '.join(variable_list)
            local_variables_list.append(string_of_variables)
            local_variables_list=' '.join(local_variables_list)
            local_variables_list=local_variables_list.split(' ')
            counter=0
            baby_word_string=function_text.replace('    ', '').replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ')
            word_list=baby_word_string.splitlines()
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
                        line=the_list[remove_counter].split('=')[0].replace(' ', '')
                        if var==line:  
                            new=string.replace(the_list[remove_counter], ' '*len(the_list[remove_counter]))
                            new_variable_list.remove(var)
                            the_list=new.splitlines()
                            try:
                                function_list[main_counter]=new
                            except IndexError:
                                pass
                        remove_counter+=1
                list_counter1+=1
            used_local_variables.append(new_variable_list)
            main_counter+=1
        main_counter=0
        new_text=text.replace(text[functions_list[counter][0]:functions_list[counter][1]], function_list[counter], 1)
        for edit_original in range(0, len(functions_list)-1):
            new_text=new_text.replace(new_text[functions_list[counter][0]:functions_list[counter][1]], function_list[counter], 1)
            counter+=1
        open(file_path, 'w').write(new_text)
        local_variables_string='\n'.join(local_variables_list)
        open(file_path.replace('.py', '_all_local_variables.txt'), 'w').write(local_variables_string)
        counter=0
        used_string=''
        for used in range(0, len(used_local_variables)):
            used_string=used_string+'\n'.join(used_local_variables[counter])+'\n'
        open(file_path.replace('.py', '_used_local_variables.txt'), 'w').write(used_string)
def remove_variables(file_path):
    'Remove unused variables.'
    remove_local_variables(file_path)
    file=open(file_path)
    comment_list=find_comments(file_path)
    find_strings(file_path)
    strings_list=find_strings(file_path)
    text=file.read()
    the_list=text.splitlines()
    counter=0
    variable_list=[]
    word_list=[]
    real_word_list=[]
    variable=None
    new_list=the_list.copy()
    baby_word_string='\n'.join(new_list)
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(baby_word_string[strings_list[counter][0]])
            baby_word_string=baby_word_string.replace(baby_word_string[par1], ' ', 1)
            par2=baby_word_string.find(baby_word_string[strings_list[counter][1]])
            baby_word_string=baby_word_string.replace(baby_word_string[par2], ' ', 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    for m in range(0, len(comment_list)):
        try:
            par1=baby_word_string.find(baby_word_string[comment_list[counter][0]])
            baby_word_string=baby_word_string.replace(baby_word_string[par1], ' ', 1)
            par2=baby_word_string.find(baby_word_string[comment_list[counter][1]])
            baby_word_string=baby_word_string.replace(baby_word_string[par2], ' ', 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    the_new_list=baby_word_string.splitlines()
    for x in range(0, len(the_new_list)):
        line=the_new_list[counter]
        if line.count('=')==1:
            new_line=line.replace(' ', '')
            variable=new_line.split('=')[0]
            variable_list.append(variable)
        counter+=1
    new_variable_list=variable_list.copy()
    string_of_variables='\n'.join(variable_list)
    open('%s_PyBroom_all_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
    counter=0
    baby_word_string=baby_word_string.replace('    ', '').replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ')
    word_list=baby_word_string.splitlines()
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
                line=the_list[remove_counter].split('=')[0].replace(' ', '')
                if var==line:  
                    new=string.replace(the_list[remove_counter], ' '*len(the_list[remove_counter]))
                    new_variable_list.remove(var)
                    the_list=new.splitlines()
                remove_counter+=1
        list_counter1+=1
    string='\n'.join(the_list)
    new_file=open(file_path, 'w')
    new_file.write(string)
    string_of_variables='\n'.join(new_variable_list)
    open('%s_PyBroom_used_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
def remove_functions():
    'Remove unused functions.'
    pass
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
