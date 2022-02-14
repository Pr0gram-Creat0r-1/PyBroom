#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
#PyBroom.install_system_requirements: [english-words]
import os
import sys
import subprocess
import datetime
from english_words import english_words_set
english_list=list(english_words_set)
english_list.append('')
history_list=[]
log_history=1
def find_strings(file_path):
    'Find strings in a text file. Internal use only. In development.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: find_strings(\"%s\")' % (str(datetime.datetime.now()), file_path))
    read_file=open(file_path).read()
    if read_file[0]!='#' or read_file.splitlines()[-1][0]!='#':
        with_comment='#PyBroom cleaned this file.\n'+read_file+'\n#https://github.com/Pr0gram-Creat0r-1/PyBroom\n#https://replit.com/@Pr0gram-Creat0r/PyBroom'
        open(file_path, 'w').write(with_comment)
    file_string=open(file_path).read()
    file_string_copy=open(file_path).read()
    important_list=[]
    important_list2=[]
    string_type_list=[]
    string_index_list=[]
    file_string=file_string.replace("\\\'", '  ').replace('\\\"', '  ')
    for finder in range(0, len(file_string)):
        index=file_string.find("'''")
        if index!=-1:
            string_type_list.append("'''")
            string_index_list.append(index)
        file_string=file_string.replace("'''", '   ', 1)
    for finder in range(0, len(file_string)):
        index=file_string.find('"""')
        if index!=-1:
            string_type_list.append('"""')
            string_index_list.append(index)
        file_string=file_string.replace('"""', '   ', 1)
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
    string_index_list.sort()
    counter=0
    for sort_types in range(0, len(string_index_list)):
        string_type=file_string_copy[string_index_list[counter]:string_index_list[counter]+3]
        if string_type=="'''":
            string_type_list[counter]="'''"
        if string_type=='"""':
            string_type_list[counter]='"""'
        if string_type[0]=="'" and string_type.count("'")!=3:
            string_type_list[counter]="'"
        if string_type[0]=='"' and string_type.count('"')!=3:
            string_type_list[counter]='"'
        counter+=1
    counter=0
    while len(string_index_list)>0:
        try:
            first_occurrence=string_index_list[0]
            first_occurrence_type=string_type_list[0]
            important_list2.append([first_occurrence_type, first_occurrence_type])
            string_type_list.remove(first_occurrence_type)
            string_index_list.remove(first_occurrence)
            magic=string_type_list.index(first_occurrence_type)
            the_index=string_index_list[magic]
            important_list.append([first_occurrence, the_index])
        except ValueError:
            pass
        try:
            while string_index_list[0]<=the_index:
                string_index_list.remove(string_index_list[0])
                string_type_list.remove(string_type_list[0])
        except ValueError:
            pass
        except IndexError:
            pass
    counter=0
    the_string=open(file_path).read()
    new_the_string=open(file_path, 'w')
    new_the_string.write(the_string)
    return important_list2
def find_comments(file_path):
    'Find comments.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: comments(\"%s\")' % (str(datetime.datetime.now()), file_path))
    strings_list=find_strings(file_path)
    baby_word_string=open(file_path).read()
    file_list=baby_word_string.splitlines()
    the_list=baby_word_string.splitlines()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
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
                baby_word_string=baby_word_string.replace(baby_word_string[comment[0]:comment[1]], ' '*len(baby_word_string[comment[0]:comment[1]]), 1)
                file_list[counter]=the_list[counter].split(the_list[counter][number])[0].replace('#'+line.split('#')[1], ' '*len('#'+line.split('#')[1]), 1)
                comment_list.append(comment)
        except IndexError:
            pass
        counter+=1
    counter=0
    return comment_list
def rstrip_all(file_path):
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: rstrip_all(\"%s\")' % (str(datetime.datetime.now()), file_path))
    strings_list=find_strings(file_path)
    comment_list=find_comments(file_path)
    baby_word_string=open(file_path).read()
    file=open(file_path).read()
    the_list=file.splitlines()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], 'p'*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], 'p'*len(strings_list[counter][1]), 1)
            counts=baby_word_string[par1:par2].count('\n')
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], 'p'*(len(baby_word_string[par1:par2])-counts)+'\n'*counts, 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    for m in range(0, len(comment_list)):
        try:
            par1=comment_list[counter][0]
            par2=comment_list[counter][1]
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], 'p'*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    the_new_list=baby_word_string.splitlines()
    for x in range(0, len(the_list)):
        line=the_list[counter]
        line2=the_new_list[counter]
        if line2.rstrip()!=line2:
            the_list[counter]=line.rstrip()
        counter+=1
    open(file_path, 'w').write('\n'.join(the_list))
def find_functions(file_path):
    'Find functions.'
    global log_history
    if log_history==1:
        history_list.append('%s: find_functions(\"%s\")' % (str(datetime.datetime.now()), file_path))
    read_file=open(file_path).read()
    if read_file[0]!='#' or read_file.splitlines()[-1][0]!='#':
        with_comment='#PyBroom cleaned this file.\n'+read_file+'\n#https://github.com/Pr0gram-Creat0r-1/PyBroom\n#https://replit.com/@Pr0gram-Creat0r/PyBroom'
        open(file_path, 'w').write(with_comment)
    strings_list=find_strings(file_path)
    baby_word_string=open(file_path).read()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    text=baby_word_string
    the_list=baby_word_string.splitlines()
    functions_list=[]
    for x in range(0, len(the_list)):
        line=the_list[counter]
        if (line.split('def')[0].isspace()==True or line.split('def')[0]=='') and line.lstrip()[0:4]=='def ':
            indents=line.split('def')[0].count('    ')  
            position=text.find(line.lstrip())
            text=text.replace(line, ' '*len(line), 1)
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
def find_classes(file_path):
    'Find classes.'
    global log_history
    if log_history==1:
        history_list.append('%s: find_classes(\"%s\")' % (str(datetime.datetime.now()), file_path))
    read_file=open(file_path).read()
    if read_file[0]!='#' or read_file.splitlines()[-1][0]!='#':
        with_comment='#PyBroom cleaned this file.\n'+read_file+'\n#https://github.com/Pr0gram-Creat0r-1/PyBroom\n#https://replit.com/@Pr0gram-Creat0r/PyBroom'
        open(file_path, 'w').write(with_comment)
    strings_list=find_strings(file_path)
    baby_word_string=open(file_path).read()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    text=baby_word_string
    the_list=baby_word_string.splitlines()
    classes_list=[]
    for x in range(0, len(the_list)):
        line=the_list[counter]
        if (line.split('class')[0].isspace()==True or line.split('class')[0]=='') and line.lstrip()[0:6]=='class ':
            indents=line.split('class')[0].count('    ')
            position=text.find(line.lstrip())
            text=text.replace(line, ' '*len(line), 1)
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
                classes_list.append([position, position2])
        counter+=1
    return classes_list
def remove_local_variables(file_path):
    'Remove local variables. Use this before cleaning global variables in the remove_variables() function.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: remove_local_variables(\"%s\")' % (str(datetime.datetime.now()), file_path))
    log_history=0
    if find_functions(file_path)!=[]:
        comment_list=find_comments(file_path)
        strings_list=find_strings(file_path)
        functions_list=find_functions(file_path)
        text=open(file_path).read()
        baby_word_string=open(file_path).read()
        baby_word_string2=open(file_path).read()
        counter=0
        function_list=[]
        for extract in range(0, len(functions_list)):
            function=baby_word_string2[functions_list[counter][0]:functions_list[counter][1]]
            function_list.append(function)
            counter+=1
        counter=0
        for m in range(0, len(strings_list)):
            try:
                par1=baby_word_string.find(strings_list[counter][0])
                baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
                par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
                baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
                baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
            except IndexError:
                pass
            counter+=1
        counter=0
        for m in range(0, len(comment_list)):
            try:
                par1=comment_list[counter][0]
                par2=comment_list[counter][1]
                baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
            except IndexError:
                pass
            counter+=1
        counter=0
        function_list2=[]
        for extract in range(0, len(functions_list)):
            function=baby_word_string[functions_list[counter][0]:functions_list[counter][1]]
            function_list2.append(function)
            counter+=1
        counter=0
        main_counter=0
        local_variables_list=[]
        used_local_variables=[]
        for remove in range(0, len(function_list)):
            counter=0
            function_text=function_list2[main_counter]
            the_new_list=function_text.splitlines()
            the_list=function_list[main_counter].splitlines()
            variable_list=[]
            real_word_list=[]
            for x in range(0, len(the_new_list)):
                line=the_new_list[counter]
                if line.count('=')==1 and line.split('=')[0].count('+')==0 and line.split('=')[0].count('-')==0 and line.split('=')[0].count('*')==0 and line.split('=')[0].count('/')==0 and line.split('=')[0].count('%')==0 and line.split('=')[0].count('<')==0 and line.split('=')[0].count('>')==0 and line.split('=')[0].count('!')==0:
                    new_line=line.strip()
                    variable=new_line.split('=')[0].strip()
                    if variable not in variable_list:
                        variable_list.append(variable)
                counter+=1
            new_variable_list=variable_list.copy()
            string_of_variables=' '.join(variable_list)
            local_variables_list.append(string_of_variables)
            local_variables_list=' '.join(local_variables_list)
            local_variables_list=local_variables_list.split(' ')
            counter=0
            baby_word_string=function_text.replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ').replace('<', ' ').replace('>', ' ').replace('%', ' ').replace('!', ' ')
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
                    remove_counter=0
                    for z in range(0, len(the_list)):
                        line=the_list[remove_counter].split('=')[0].strip()
                        if var==line:  
                            string_check=the_list[remove_counter]
                            string_check_list=[]
                            if string_check.count("'''")==1 or string_check.count('"""')==1:
                                finding=string_check.find("'''")
                                finding2=string_check.find('"""')
                                if finding!=-1:
                                    string_check_list.append(finding)
                                if finding2!=-1:
                                    string_check_list.append(finding2)
                                minimum=min(string_check_list)
                                minimum_type=string_check[minimum:minimum+3]
                                if string_check.count(minimum_type)==1:
                                    the_list[remove_counter]=' '*len(the_list[remove_counter])
                                    subcounter=remove_counter+1
                                    for x in range(0, len(the_list)-remove_counter-1):
                                        line=the_list[subcounter]
                                        if line.count(minimum_type)==0 or line.count(minimum_type)==1:
                                            the_list[subcounter]=' '*len(the_list[subcounter])
                                            if line.count(minimum_type)==1:
                                                break
                                        subcounter+=1
                                else:
                                    the_list[remove_counter]=' '*len(the_list[remove_counter])
                            else:
                                the_list[remove_counter]=' '*len(the_list[remove_counter])
                            try:
                                function_list[main_counter]='\n'.join(the_list)
                            except IndexError:
                                pass
                            new_variable_list.remove(var)
                        remove_counter+=1
                list_counter1+=1
            used_local_variables.append(new_variable_list)
            main_counter+=1
        main_counter=0
        counter=0
        new_text=text.replace(text[functions_list[counter][0]:functions_list[counter][1]], function_list[counter], 1)
        counter=1
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
            counter+=1
        open(file_path.replace('.py', '_used_local_variables.txt'), 'w').write(used_string)
    log_history=1
def remove_variables(file_path):
    'Remove unused variables.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: remove_variables(\"%s\")' % (str(datetime.datetime.now()), file_path))
    log_history=0
    file=open(file_path)
    comment_list=find_comments(file_path)
    strings_list=find_strings(file_path)
    text=file.read()
    the_list=text.splitlines()
    variable_list=[]
    word_list=[]
    real_word_list=[]
    variable=None
    new_list=the_list.copy()
    baby_word_string='\n'.join(new_list)
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    for m in range(0, len(comment_list)):
        try:
            par1=comment_list[counter][0]
            par2=comment_list[counter][1]
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    the_new_list=baby_word_string.splitlines()
    for x in range(0, len(the_new_list)):
        line=the_new_list[counter]
        if line.count('=')==1 and line.split('=')[0].count('+')==0 and line.split('=')[0].count('-')==0 and line.split('=')[0].count('*')==0 and line.split('=')[0].count('/')==0 and line.split('=')[0].count('%')==0 and line.split('=')[0].count('<')==0 and line.split('=')[0].count('>')==0 and line.split('=')[0].count('!')==0:
            new_line=line.strip()
            variable=new_line.split('=')[0].strip()
            if variable not in variable_list:
                variable_list.append(variable)
        counter+=1
    new_variable_list=variable_list.copy()
    string_of_variables='\n'.join(variable_list)
    open('%s_all_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
    counter=0
    baby_word_string=baby_word_string.replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ').replace('<', ' ').replace('>', ' ').replace('%', ' ').replace('!', ' ')
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
            remove_counter=0
            for z in range(0, len(the_list)):
                line=the_list[remove_counter].split('=')[0].strip()
                if var==line:
                    string_check=the_list[remove_counter]
                    string_check_list=[]
                    if string_check.count("'''")==1 or string_check.count('"""')==1:
                        finding=string_check.find("'''")
                        finding2=string_check.find('"""')
                        if finding!=-1:
                            string_check_list.append(finding)
                        if finding2!=-1:
                            string_check_list.append(finding2)
                        if finding<finding2:
                            if string_check.count("'''")>1:
                                the_list[remove_counter]=' '*len(the_list[remove_counter])
                        minimum=min(string_check_list)
                        minimum_type=string_check[minimum:minimum+3]
                        if string_check.count(minimum_type)==1:
                            the_list[remove_counter]=' '*len(the_list[remove_counter])
                            subcounter=remove_counter+1
                            for x in range(0, len(the_list)-remove_counter-1):
                                line=the_list[subcounter]
                                if line.count(minimum_type)==0 or line.count(minimum_type)==1:
                                    the_list[subcounter]=' '*len(the_list[subcounter])
                                    if line.count(minimum_type)==1:
                                        break
                                subcounter+=1
                        else:
                            the_list[remove_counter]=' '*len(the_list[remove_counter])
                    else:
                        the_list[remove_counter]=' '*len(the_list[remove_counter])
                    new_variable_list.remove(var)
                remove_counter+=1
        list_counter1+=1
    string='\n'.join(the_list)
    new_file=open(file_path, 'w')
    new_file.write(string)
    string_of_variables='\n'.join(new_variable_list)
    open('%s_used_variables.txt' % file_path.replace('.py', ''), 'w').write(string_of_variables)
    log_history=1
"""def remove_functions(file_path):
    'Remove unused functions.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: remove_functions(\"%s\")' % (str(datetime.datetime.now()), file_path))
    log_history=0
    comment_list=find_comments(file_path)
    strings_list=find_strings(file_path)
    function_list=find_functions(file_path)
    text=open(file_path).read()
    the_list=open(file_path).read().splitlines()
    word_list=[]
    real_word_list=[]
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
            par2=baby_word_string.find(baby_word_string[comment_list[counter][1]])
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2+1], ' '*len(baby_word_string[par1:par2+1]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    function_names=[]
    print(baby_word_string)
    for name_functions in range(0, len(function_list)):
        try:
            function_text=text[function_list[counter][0]:function_list[counter][1]]
            function_text_list=function_text.splitlines()
            name=function_text_list[0].split('def ')[1].split('(')[0].strip()
            function_names.append(name)
        except IndexError:
            pass
        counter+=1
    counter=0
    print(function_names)
    function_names_copy=function_names.copy()
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
    list_counter1=0
    list_counter2=0
    print(real_word_list)
    for y in range(0, len(function_names)):
        list_counter2=0
        counted=0
        for a in range(0, len(real_word_list)):
            func=function_names[list_counter1]
            word=real_word_list[list_counter2]
            if func==word:
                counted+=1
            list_counter2+=1
        if counted==1:
            text=text.replace(text[function_list[list_counter1][0]:function_list[list_counter1][1]], ' '*len(text[function_list[list_counter1][0]:function_list[list_counter1][1]]), 1)
            function_names_copy.remove(func)
        list_counter1+=1
    string=text
    open(file_path, 'w').write(string)
    log_history=1
    print(function_names_copy)"""
def destroy(file_path):
    'Delete the file completely.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: destroy(\"%s\")' % (str(datetime.datetime.now()), file_path))
    os.remove(file_path)
def install_system_requirements(file_path):
    'Install the python modules needed; uses pip. Put a comment like this: #PyBroom.install_system_requirements: [package1, package2, package3 etc]. No string quotes anywhere. I only added this because I thought it would be simple and fun to make, and besides, some IDEs do not automatically install packages like replit.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: install_system_requirements(\"%s\")' % (str(datetime.datetime.now()), file_path))
    text_list=open(file_path).read().splitlines()
    counter=0
    check_for_line=0
    for x in range(0, len(text_list)):
        line=text_list[counter]
        if '#PyBroom.install_system_requirements: [' in line:
            check_for_line=1
            break
        counter+=1
    if check_for_line==1:
        list_part=line.strip().split(' ', 1)[1].split(']')[0]+']'
        counter=0
        list_part=list_part.replace('[', '').replace(']', '').replace(' ', '').split(',')
        for y in range(0, len(list_part)):
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', list_part[counter]])
            counter+=1
"""def remove_classes(file_path):
    'Removes unused classes.'
    pass"""
"""def remove_modules(file_path):
    pass #might do this..."""
def suggestions(file_path):
    'Give suggestions.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: suggestions(\"%s\")' % (str(datetime.datetime.now()), file_path))
    log_history=0
    text=open(file_path).read()
    comment_list=find_comments(file_path)
    strings_list=find_strings(file_path)
    function_list=find_functions(file_path)
    class_list=find_classes(file_path)
    baby_word_string=open(file_path).read()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    for m in range(0, len(comment_list)):
        try:
            par1=comment_list[counter][0]
            par2=comment_list[counter][1]
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    the_new_list=baby_word_string.splitlines()
    complex_list=[]
    complex_list_text=open(file_path).read().splitlines()
    for x in range(0, len(complex_list_text)):
        line=complex_list_text[counter]
        if line.count('(((')>=1 or line.count('    ')>=5 or len(line)>=200:
            complex_list.append(counter+1)
        counter+=1
    counter=0
    variable_list=[]
    real_word_list=[]
    function_names=[]
    class_names=[]
    for x in range(0, len(the_new_list)):
        line=the_new_list[counter]
        if line.count('=')==1 and line.split('=')[0].count('+')==0 and line.split('=')[0].count('-')==0 and line.split('=')[0].count('*')==0 and line.split('=')[0].count('/')==0 and line.split('=')[0].count('%')==0 and line.split('=')[0].count('<')==0 and line.split('=')[0].count('>')==0 and line.split('=')[0].count('!')==0:
            new_line=line.strip()
            variable=new_line.split('=')[0].strip()
            if variable not in variable_list:
                variable_list.append(variable)
        counter+=1
    counter=0
    baby_word_string=baby_word_string.replace('(', ' ').replace(')', ' ').replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').replace('=', ' ').replace('.', ' ').replace(':', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('{', ' ').replace('}', ' ').replace('<', ' ').replace('>', ' ').replace('%', ' ').replace('!', ' ')
    word_list=baby_word_string.splitlines()
    for c in range(0, len(word_list)):
        string_list=word_list[counter].split(' ')
        subcounter=0
        for b in range(0, len(string_list)):
            real_word_list.append(string_list[subcounter])
            subcounter+=1
        counter+=1
    counter=0
    for name_functions in range(0, len(function_list)):
        try:
            function_text=text[function_list[counter][0]:function_list[counter][1]]
            function_text_list=function_text.splitlines()
            name=function_text_list[0].split('def ')[1].split('(')[0].strip()
            function_names.append(name)
        except IndexError:
            pass
        counter+=1
    counter=0
    for name_classes in range(0, len(class_list)):
        try:
            class_text=text[class_list[counter][0]:class_list[counter][1]]
            class_text_list=class_text.splitlines()
            name=class_text_list[0].split('class ')[1].split(':')[0].split('(')[0].strip()
            class_names.append(name)
        except IndexError:
            pass
        counter+=1
    counter=0
    vars_not_word=[]
    funcs_not_word=[]
    classes_not_word=[]
    for x in range(0, len(variable_list)):
        var_words=variable_list[counter].replace('_', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ').split(' ')
        subcounter=0
        for y in range(0, len(var_words)):
            var=var_words[subcounter]
            if var not in english_list:
                vars_not_word.append(variable_list[counter])
                break
            subcounter+=1
        counter+=1
    counter=0
    for x in range(0, len(function_names)):
        func_words=function_names[counter].replace('_', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ').split(' ')
        subcounter=0
        for y in range(0, len(func_words)):
            func=func_words[subcounter]
            if func not in english_list:
                funcs_not_word.append(function_names[counter])
                break
            subcounter+=1
        counter+=1
    counter=0
    for x in range(0, len(class_names)):
        class_words=class_names[counter].replace('_', ' ').replace(',', ' ').replace('[', ' ').replace(']', ' ').replace('(', ' ').replace(')', ' ').replace('1', ' ').replace('2', ' ').replace('3', ' ').replace('4', ' ').replace('5', ' ').replace('6', ' ').replace('7', ' ').replace('8', ' ').replace('9', ' ').replace('0', ' ').split(' ')
        subcounter=0
        for y in range(0, len(class_words)):
            _class=class_words[subcounter]
            if _class not in english_list:
                classes_not_word.append(class_names[counter])
                break
            subcounter+=1
        counter+=1
    counter=0
    similar_list_var=[]
    similar_list_func=[]
    similar_list_class=[]
    for similarities_var in range(0, len(variable_list)):
        var=variable_list[counter]
        #Start with variable you want to compare
        subcounter=0
        for z in range(0, len(variable_list)):
            var2=variable_list[subcounter]
            common_letters=list(set(var) & set(var2))
            if len(common_letters)>=max([len(set(var)), len(set(var2))])*0.9 and var!=var2 and [var, var2] not in similar_list_var and [var2, var] not in similar_list_var:   
                similar_list_var.append([var, var2])
            subcounter+=1
        counter+=1
    counter=0
    for similarities_var in range(0, len(function_names)):
        func=function_names[counter]
        #Start with variable you want to compare
        subcounter=0
        for z in range(0, len(function_names)):
            func2=function_names[subcounter]
            common_letters=list(set(func) & set(func2))
            if len(common_letters)>=max([len(set(func)), len(set(func2))])*0.9 and func!=func2 and [func, func2] not in similar_list_func and [func2, func] not in similar_list_func:   
                similar_list_func.append([func, func2])
            subcounter+=1
        counter+=1
    counter=0
    for similarities_var in range(0, len(class_names)):
        _class=class_names[counter]
        #Start with variable you want to compare
        subcounter=0
        for z in range(0, len(class_names)):
            class2=class_names[subcounter]
            common_letters=list(set(_class) & set(class2))
            if len(common_letters)>=max([len(set(_class)), len(set(class2))])*0.9 and _class!=class2 and [_class, class2] not in similar_list_class and [class2, _class] not in similar_list_class:   
                similar_list_class.append([_class, class2])
            subcounter+=1
        counter+=1
    counter=0
    suggestions_file=open(file_path.replace('.py', '_suggestions.txt'), 'w')
    write_string='This is a file of variables, functions, and classes that are not word according to https://pypi.org/project/english-words/. It also contains variable, function, and class names that have been identified as similar. Lastly, this file contains lines that have been identified as hard to understand, that may require a comment stating its purpose.\n\n'+'Names that are not in the english-words list:\n\n'+'Variables: %s\n\n' % str(vars_not_word)+'Functions: %s\n\n' % str(funcs_not_word)+'Classes: %s\n\n' % str(classes_not_word)+'Similar names:\n\n'+'Variables: %s\n\n' % str(similar_list_var)+'Functions: %s\n\n' % str(similar_list_func)+'Classes: %s\n\n' % str(similar_list_class)+'Complex lines:\n\n%s' % str(complex_list)
    suggestions_file.write(write_string)
    log_history=1
def beautify(file_path):
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: beautify(\"%s\")' % (str(datetime.datetime.now()), file_path))
    log_history=0
    strings_list=find_strings(file_path)
    comment_list=find_comments(file_path)
    baby_word_string=open(file_path).read()
    file=open(file_path).read()
    text_list=file.splitlines()
    counter=0
    for m in range(0, len(strings_list)):
        try:
            par1=baby_word_string.find(strings_list[counter][0])
            baby_word_string=baby_word_string.replace(strings_list[counter][0], ' '*len(strings_list[counter][0]), 1)
            par2=baby_word_string.find(strings_list[counter][1])+len(strings_list[counter][1])
            baby_word_string=baby_word_string.replace(strings_list[counter][1], ' '*len(strings_list[counter][1]), 1)
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    for m in range(0, len(comment_list)):
        try:
            par1=comment_list[counter][0]
            par2=comment_list[counter][1]
            baby_word_string=baby_word_string.replace(baby_word_string[par1:par2], ' '*len(baby_word_string[par1:par2]), 1)
        except IndexError:
            pass
        counter+=1
    counter=0
    the_new_list=baby_word_string.splitlines()
    for x in range(0, len(text_list)):
        try:    
            line=text_list[counter]
        except IndexError:
            pass
        try:    
            line2=text_list[counter]
        except IndexError:
            pass
        for x in range(0, line.count('>>=')):
            try:
                if (line2.split('>>=', 1)[0].rstrip()==line2.split('>>=', 1)[0] and line2.split('>>=', 1)[1].lstrip()==line2.split('>>=', 1)[1]) and line2.find('>>=')!=-1:
                    index=line2.find('>>=')
                    line_list=list(line)
                    line_list[index]=' >'
                    line_list[index+1]='>'
                    line_list[index+2]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('>>=', '     ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('<<=')):
            try:
                if (line2.split('<<=', 1)[0].rstrip()==line2.split('<<=', 1)[0] and line2.split('<<=', 1)[1].lstrip()==line2.split('<<=', 1)[1]) and line2.find('<<=')!=-1:
                    index=line2.find('<<=')
                    line_list=list(line)
                    line_list[index]=' <'
                    line_list[index+1]='<'
                    line_list[index+2]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('<<=', '     ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('**=')):
            try:
                if (line2.split('**=', 1)[0].rstrip()==line2.split('**=', 1)[0] and line2.split('**=', 1)[1].lstrip()==line2.split('**=', 1)[1]) and line2.find('**=')!=-1:
                    index=line2.find('**=')
                    line_list=list(line)
                    line_list[index]=' *'
                    line_list[index+1]='*'
                    line_list[index+2]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('**=', '     ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('//=')):
            try:
                if (line2.split('//=', 1)[0].rstrip()==line2.split('//=', 1)[0] and line2.split('//=', 1)[1].lstrip()==line2.split('//=', 1)[1]) and line2.find('//=')!=-1:
                    index=line2.find('//=')
                    line_list=list(line)
                    line_list[index]=' /'
                    line_list[index+1]='/'
                    line_list[index+2]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('//=', '     ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('>>')):
            try:
                if (line2.split('>>', 1)[0].rstrip()==line2.split('>>', 1)[0] and line2.split('>>', 1)[1].lstrip()==line2.split('>>', 1)[1]) and (line[line2.find('>>')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('>>')!=-1:
                    index=line2.find('>>')
                    line_list=list(line)
                    line_list[index]=' >'
                    line_list[index+1]='> '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('>>', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('<<')):
            try:
                if (line2.split('<<', 1)[0].rstrip()==line2.split('<<', 1)[0] and line2.split('<<', 1)[1].lstrip()==line2.split('<<', 1)[1]) and (line[line2.find('<<')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('<<')!=-1:
                    index=line2.find('<<')
                    line_list=list(line)
                    line_list[index]=' <'
                    line_list[index+1]='< '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('<<', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('==')):
            try:
                if (line2.split('==', 1)[0].rstrip()==line2.split('==', 1)[0] and line2.split('==', 1)[1].lstrip()==line2.split('==', 1)[1]) and line2.find('==')!=-1:
                    index=line2.find('==')
                    line_list=list(line)
                    line_list[index]=' ='
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('==', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('+=')):
            try:
                if (line2.split('+=', 1)[0].rstrip()==line2.split('+=', 1)[0] and line2.split('+=', 1)[1].lstrip()==line2.split('+=', 1)[1]) and line2.find('+=')!=-1:
                    index=line2.find('+=')
                    line_list=list(line)
                    line_list[index]=' +'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('+=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('-=')):
            try:
                if (line2.split('-=', 1)[0].rstrip()==line2.split('-=', 1)[0] and line2.split('-=', 1)[1].lstrip()==line2.split('-=', 1)[1]) and line2.find('-=')!=-1:
                    index=line2.find('-=')
                    line_list=list(line)
                    line_list[index]=' -'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('-=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('*=')):
            try:
                if (line2.split('*=', 1)[0].rstrip()==line2.split('*=', 1)[0] and line2.split('*=', 1)[1].lstrip()==line2.split('*=', 1)[1]) and line2.find('*=')!=-1:
                    index=line2.find('*=')
                    line_list=list(line)
                    line_list[index]=' *'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('*=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('/=')):
            try:
                if (line2.split('/=', 1)[0].rstrip()==line2.split('/=', 1)[0] and line2.split('/=', 1)[1].lstrip()==line2.split('/=', 1)[1]) and line2.find('/=')!=-1:
                    index=line2.find('/=')
                    line_list=list(line)
                    line_list[index]=' /'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('/=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('!=')):
            try:
                if (line2.split('!=', 1)[0].rstrip()==line2.split('!=', 1)[0] and line2.split('!=', 1)[1].lstrip()==line2.split('!=', 1)[1]) and line2.find('!=')!=-1:
                    index=line2.find('!=')
                    line_list=list(line)
                    line_list[index]=' !'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('!=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('>=')):
            try:
                if (line2.split('>=', 1)[0].rstrip()==line2.split('>=', 1)[0] and line2.split('>=', 1)[1].lstrip()==line2.split('>=', 1)[1]) and line2.find('>=')!=-1:
                    index=line2.find('>=')
                    line_list=list(line)
                    line_list[index]=' >'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('>=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('<=')):
            try:
                if (line2.split('<=', 1)[0].rstrip()==line2.split('<=', 1)[0] and line2.split('<=', 1)[1].lstrip()==line2.split('<=', 1)[1]) and line2.find('<=')!=-1:
                    index=line2.find('<=')
                    line_list=list(line)
                    line_list[index]=' <'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('<=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('%=')):
            try:
                if (line2.split('%=', 1)[0].rstrip()==line2.split('%=', 1)[0] and line2.split('%=', 1)[1].lstrip()==line2.split('%=', 1)[1]) and line2.find('%=')!=-1:
                    index=line2.find('%=')
                    line_list=list(line)
                    line_list[index]=' %'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('%=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('**')):
            try:
                if (line2.split('**', 1)[0].rstrip()==line2.split('**', 1)[0] and line2.split('**', 1)[1].lstrip()==line2.split('**', 1)[1]) and (line[line2.find('**')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('**')!=-1:
                    index=line2.find('**')
                    line_list=list(line)
                    line_list[index]=' *'
                    line_list[index+1]='* '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('**', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('//')):
            try:
                if (line2.split('//', 1)[0].rstrip()==line2.split('//', 1)[0] and line2.split('//', 1)[1].lstrip()==line2.split('//', 1)[1]) and (line[line2.find('//')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('//')!=-1:
                    index=line2.find('//')
                    line_list=list(line)
                    line_list[index]=' /'
                    line_list[index+1]='/ '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('//', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('&=')):
            try:
                if (line2.split('&=', 1)[0].rstrip()==line2.split('&=', 1)[0] and line2.split('&=', 1)[1].lstrip()==line2.split('&=', 1)[1]) and line2.find('&=')!=-1:
                    index=line2.find('&=')
                    line_list=list(line)
                    line_list[index]=' &'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('&=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('|=')):
            try:
                if (line2.split('|=', 1)[0].rstrip()==line2.split('|=', 1)[0] and line2.split('|=', 1)[1].lstrip()==line2.split('|=', 1)[1]) and line2.find('|=')!=-1:
                    index=line2.find('|=')
                    line_list=list(line)
                    line_list[index]=' |'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('|=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('^=')):
            try:
                if (line2.split('^=', 1)[0].rstrip()==line2.split('^=', 1)[0] and line2.split('^=', 1)[1].lstrip()==line2.split('^=', 1)[1]) and line2.find('^=')!=-1:
                    index=line2.find('^=')
                    line_list=list(line)
                    line_list[index]=' ^'
                    line_list[index+1]='= '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('^=', '    ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('=')):
            try:
                if (line2.split('=', 1)[0].rstrip()==line2.split('=', 1)[0] or line2.split('=', 1)[1].lstrip()==line2.split('=', 1)[1]) and (line[line2.find('=')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('=')!=-1:
                    index=line2.find('=')
                    line_list=list(line)
                    line_list[index]=' = '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('=', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('+')):
            try:
                if (line2.split('+', 1)[0].rstrip()==line2.split('+', 1)[0] and line2.split('+', 1)[1].lstrip()==line2.split('+', 1)[1]) and (line[line2.find('+')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('+')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('+')!=-1:
                    index=line2.find('+')
                    line_list=list(line)
                    line_list[index]=' + '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('+', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('-')):
            try:
                if (line2.split('-', 1)[0].rstrip()==line2.split('-', 1)[0] and line2.split('-', 1)[1].lstrip()==line2.split('-', 1)[1]) and (line[line2.find('-')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('-')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('-')!=-1:
                    index=line2.find('-')
                    line_list=list(line)
                    line_list[index]=' - '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('-', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('*')):
            try:
                if (line2.split('*', 1)[0].rstrip()==line2.split('*', 1)[0] and line2.split('*', 1)[1].lstrip()==line2.split('*', 1)[1]) and (line[line2.find('*')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('*')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('*')!=-1:
                    index=line2.find('*')
                    line_list=list(line)
                    line_list[index]=' * '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('*', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('/')):
            try:
                if (line2.split('/', 1)[0].rstrip()==line2.split('/', 1)[0] and line2.split('/', 1)[1].lstrip()==line2.split('/', 1)[1]) and (line[line2.find('/')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('/')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('/')!=-1:
                    index=line2.find('/')
                    line_list=list(line)
                    line_list[index]=' / '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('/', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('<')):
            try:
                if (line2.split('<', 1)[0].rstrip()==line2.split('<', 1)[0] and line2.split('<', 1)[1].lstrip()==line2.split('<', 1)[1]) and (line[line2.find('<')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('<')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('<')!=-1:
                    index=line2.find('<')
                    line_list=list(line)
                    line_list[index]=' < '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('<', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('>')):
            try:
                if (line2.split('>', 1)[0].rstrip()==line2.split('>', 1)[0] and line2.split('>', 1)[1].lstrip()==line2.split('>', 1)[1]) and (line[line2.find('>')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('>')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('>')!=-1:
                    index=line2.find('>')
                    line_list=list(line)
                    line_list[index]=' > '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('>', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('%')):
            try:
                if (line2.split('%', 1)[0].rstrip()==line2.split('%', 1)[0] and line2.split('%', 1)[1].lstrip()==line2.split('%', 1)[1]) and (line[line2.find('%')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('%')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('%')!=-1:
                    index=line2.find('%')
                    line_list=list(line)
                    line_list[index]=' % '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('%', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count(',')):
            try:
                if (line2.split(',', 1)[0].rstrip()==line2.split(',', 1)[0] and line2.split(',', 1)[1].lstrip()==line2.split(',', 1)[1]) and (line[line2.find(',')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find(',')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find(',')!=-1:
                    index=line2.find(',')
                    line_list=list(line)
                    line_list[index]=', '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace(',', '  ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('&')):
            try:
                if (line2.split('&', 1)[0].rstrip()==line2.split('&', 1)[0] and line2.split('&', 1)[1].lstrip()==line2.split('&', 1)[1]) and (line[line2.find('&')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('&')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('&')!=-1:
                    index=line2.find('&')
                    line_list=list(line)
                    line_list[index]=' & '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('&', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('|')):
            try:
                if (line2.split('|', 1)[0].rstrip()==line2.split('|', 1)[0] and line2.split('|', 1)[1].lstrip()==line2.split('|', 1)[1]) and (line[line2.find('|')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('|')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('|')!=-1:
                    index=line2.find('|')
                    line_list=list(line)
                    line_list[index]=' | '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('|', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('^')):
            try:
                if (line2.split('^', 1)[0].rstrip()==line2.split('^', 1)[0] and line2.split('^', 1)[1].lstrip()==line2.split('^', 1)[1]) and (line[line2.find('^')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('^')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('^')!=-1:
                    index=line2.find('^')
                    line_list=list(line)
                    line_list[index]=' ^ '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('^', '   ', 1)
            except IndexError:
                pass
        for x in range(0, line.count('~')):
            try:
                if (line2.split('~', 1)[0].rstrip()==line2.split('~', 1)[0] and line2.split('~', 1)[1].lstrip()==line2.split('~', 1)[1]) and (line[line2.find('~')+1] not in ['+', '-', '*', '/', '=', '%', '>', '<'] and line[line2.find('~')-1] not in ['+', '-', '*', '/', '=', '%', '>', '<', '&', '^', '~', '|']) and line2.find('~')!=-1:
                    index=line2.find('~')
                    line_list=list(line)
                    line_list[index]=' ~ '
                    line=''.join(line_list)
                    text_list[counter]=line
                    line2=line2.replace('~', '   ', 1)
            except IndexError:
                pass
        counter+=1
    string='\n'.join(text_list)
    open(file_path, 'w').write(string)
    log_history=1
def history():
    'Return a list of the commands you did.'
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: history()' % str(datetime.datetime.now()))
    return history_list
def save_history(file_path):
    global history_list
    global log_history
    if log_history==1:
        history_list.append('%s: save_history(\"%s\")' % (str(datetime.datetime.now()), file_path))
    if os.path.isfile(file_path)==False:    
        file=open(file_path, 'x')
    file=open(file_path)
    file_text=file.read()
    new_file_text=file_text+str(datetime.datetime.now())+':'+str(history_list)+'\n'
    open(file_path, 'w').write(new_file_text)
