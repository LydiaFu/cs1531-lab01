'''
task = produce list of fibonacci numbers of length n

DIFFICULTY = EASY
TOPICS = lists, variables, loops

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
'''

def produceFibsList(n):
    '''
    >>> produceFibsList(0)
    []
    >>> produceFibsList(1)
    [1]
    >>> produceFibsList(2)
    [1, 1]
    >>> produceFibsList(3)
    [1, 1, 2]
    >>> produceFibsList(5)
    [1, 1, 2, 3, 5]
    '''
    # TODO = fill in the code here, and return the correct result using the return keyword
    
    i = 1
    num = 1
    fiblist = []
    
    while i <= n and i < 1:
        i += 1 ;
    
    while i <= n and i < 2:
        fiblist.append(1)
        i +=1;
    
    i = 2
    while i <= n:
        fiblist.append(num)
        num = fiblist[-1] + fiblist[-2]
        i += 1
    
    print(fiblist)
    
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
