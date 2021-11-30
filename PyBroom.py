#I am going to try keeping this file clean
#Imagine cleaning a code cleaner :)
def clean_variables():
    file_path=input('Paste a file path here: ')
    print('Cleaning...')
    file=open(file_path)
    text=file.read()
    the_list=text.splitlines()
    counter=0
    variable_list=[]
    word_list=[]
    real_word_list=[]
    variable=None
    for x in range(0, len(the_list)):
        line=the_list[counter]
        if line.count('=')>=1:
            variable=line.split('=')[0]
        variable_list.append(variable)
        counter+=1
    counter=0
    baby_word_string='\n'.join(the_list)
    word_string=((((((baby_word_string.replace('(', ' ')).replace(')', ' ')).replace('+', ' ')).replace('-', ' ')).replace('*', ' ')).replace('/', ' ')).replace('=', ' ')
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
                line=the_list[remove_counter].split('=')[0]
                if var==line:  
                    new=string.replace(the_list[remove_counter], '')
                    the_list=new.splitlines()
                remove_counter+=1
        list_counter1+=1
    string='\n'.join(the_list)
    new_file_name=file_path.replace('.py', '_PyBroom_cleaned.py')
    new_file=open(new_file_name, 'w')
    new_file.write(string)
    print('Done!')
