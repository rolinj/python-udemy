import re

def text_cleaner(word):
    """Removes non-alphabet characters from a string. """

    return re.sub("[^A-Za-z']+", '', word)

def char_count(word):
    """Count number of characters in a word. """
    return len(word)

def list_processor(**kwargs):
    """Handles the insertion of every word to correct list. """
    
    #Process the entry word only if it's not a space/blank.
    if kwargs['cleaned_text'] != '':

        # First word on the file will enter this block.
        # It will be the first member of the first list from the main list.
        if len(kwargs['main_list']) == 0:
            kwargs['main_list'].append(list([kwargs['cleaned_text']]))
        
        else:
            #This variable is for tracking whether the current word 
            #on the loop has been already inserted to a list or not.
            inserted = False

            for single_list in kwargs['main_list']:
                #If a list with with correct length is present, insert the word in it.
                #Then indicate that the word has been inserted already.
                if len(single_list[0]) == kwargs['text_char_count']:
                    single_list.append(kwargs['cleaned_text'])
                    inserted = True 

            #Once looped with every list available and still nothing suits with the length,
            #create a new list for it and append to the main list.
            if inserted == False:
                kwargs['main_list'].append(list([kwargs['cleaned_text']]))

if __name__ == "__main__":
    main_list = []

    #Iterate thru every words within the opened file.
    with open("sample.txt") as apple:
        for line in apple:
            #Retrieve individual words by splitting with spaces and process them.
            for word in line.split():
                cleaned_text = text_cleaner(word)
                text_char_count = char_count(cleaned_text)
                list_processor(text_char_count=text_char_count, 
                               cleaned_text=cleaned_text, main_list=main_list)

    #Print each list.
    for list_collection in main_list:
        print(len(list_collection[0]) ,list_collection)   

            



