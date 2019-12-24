def spy_game(nums):
    '''
    Returns a boolean if 007 exists in order
    within a given list of numbers.
    '''

    new_string = ""
    for char in str(nums):
        #Create a string composed on 0 and 7 only.
        if char in "07":
            new_string += char

        #Check if 007 exists in the newly created string.
        if "007" in new_string:
            return True
    
    return False


spy_game([1,0,2,4,0,5,7])