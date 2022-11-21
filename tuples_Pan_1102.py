def skip_tuples(t):
    '''
    Input: tuple
    Output: tuple
    Returns a new tuple as output, such as every second element of the input 
    tuple is skipped, starting with the first one.
    '''
    # string slicing thingy
    return t[::2]

def main():
    tuple1 = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(tuple1))

if __name__ == '__main__':
    main()
