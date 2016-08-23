def score(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1 # The score for each character starting from index 1
    return score

def name():
    '''
    >>> name()
    871198282
    '''
    file_obj = open('names.txt', 'r')
    names = file_obj.read() # Read the lines
    names = names.replace('"', '') # Make the names stringify
    names = names.split(',') # Make a list of all the names in the text file
    names.sort()

    total_score = 0

    for i in range(len(names)):
        my_score = score(names[i])*(i+1) # Score multiplied by the position of the word
        total_score += my_score

    print total_score


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
