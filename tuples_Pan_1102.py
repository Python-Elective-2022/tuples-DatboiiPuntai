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
    tuple2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(skip_tuples(tuple1))
    print(skip_tuples(tuple2))


if __name__ == '__main__':
    main()
