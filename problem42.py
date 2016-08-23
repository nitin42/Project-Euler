from __future__ import division

def score(name):
    score = 0
    for char in name:
        score += ord(char) - ord('A') + 1 # The score for each character starting from index 1
    return abs(score)

def cal_score():
    '''
    >>> cal_score()
    847
    '''
    file_obj = open('words.txt', 'r')
    names = file_obj.read()
    names = names.replace('"', '')
    name = names.split(',')

    l = []

    for i in range(len(names)):
        res = score(names[i]) # Calculate the score for each word in the list
        l.append(res)

    l3 = map(int, l) # Map all the scores as integer

    #print l3

    l2 = []
    count = 0

    for i in l3:
        for j in range(1, 1000000):
            if i == ((j*j + j)/2): # Check for triangle for numbers
                count += 1 # If found 
            else:
                break

    print count

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
