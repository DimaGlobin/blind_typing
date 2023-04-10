def split_to_substrs(str, substr_length = 2): 
    
    '''

    This function split you string to substrings of the length you need.

    input:
        str : string - string, that you want to split
        substr_length : int - length of substrings that you eant ot get
        
    output:
        substrs : list of  substrings of length = substr_length

    '''

    chunks, chunk_size = len(str), substr_length
    substrs = []

    for i in range(chunks):
        substr = str[i:i + chunk_size]
        if(len(substr) < chunk_size):
            break
        substrs.append(substr)

    return substrs

def file_to_dict(filename : str, substr_length = 2):
    
    '''
    
    This function read file and convert it to list of words and dictionary of substrings, where keys are substrings, 
    values is frequencies with which they occur in the file.

    input: 
        filename : string - name of the file that you want to read.

    output:
        list_of_words : list - list of words in the file separated by spaces.
        dict_of_substrs : dict - dictionary with subtrings in format [key : value], where key is subtring and value is requency with which it occurs in the file.

    '''

    with open(filename, 'r') as f:
        data = f.read()

    list_of_words = data.split(' ')
    set_of_substrs = set()

    for word in list_of_words:
        set_of_substrs.update(split_to_substrs(word, substr_length))

    dict_of_substrs = {}

    for substr in list(set_of_substrs):
        dict_of_substrs[substr] = data.count(substr)

    return list_of_words, dict_of_substrs

if __name__ == '__main__':

    length_of_substr = 3

    list_of_words, dict_of_substrs = file_to_dict('shakespeare.txt', length_of_substr) # read file and get list of words and dictionary of substrings

    dict_of_words = {}

    for word in list_of_words:                                                                                        # Here we create a dictionary of words, where - keys are words in file,
        amounts = [num for num in [dict_of_substrs[substr] for substr in split_to_substrs(word, length_of_substr)]]   # values are minimum of weights of their substrings.
        if (len(amounts) == 0):                                                                     
            continue
        dict_of_words[word] = min(amounts)

    result_list = list(dict(sorted(dict_of_words.items(), key = lambda x : x[1], reverse=True)).keys()) # Sort dictionary by values and get their keys

    with open('shakespeare_out.txt', 'w') as f:
        f.write(' '.join(word for word in result_list))
