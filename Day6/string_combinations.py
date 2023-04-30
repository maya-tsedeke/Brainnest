"""Write a generator function that takes a list of strings as input and generates all possible combinations of those
strings.For example, if the input list is ['a', 'b', 'c'], the generator should generate the combinations 'a', 'b',
'c', 'ab', 'ac', 'bc', and 'abc'. """


def string_combinations(strings):
    """Generator function to generate all possible combinations of a list of strings."""
    n = len(strings)
    # loop over all possible bitmasks
    for bitmask in range(1, 1 << n):
        combination = ''.join(strings[i] for i in range(n) if bitmask & (1 << i))
        # yield the combination if it's not empty
        if combination:
            yield combination


for combination in string_combinations(['a', 'b', 'c']):
    print(combination)



