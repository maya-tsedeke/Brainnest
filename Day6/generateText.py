def lines_with_word(file_path, word):
    """Generator function to yield lines that contain a specific word."""
    with open(file_path, 'r') as file:
        for line in file:
            if word in line:
                yield line.strip()


for line in lines_with_word('romeo.txt', 'envious'):
    print(line)
""" 
Example
Output: Arise fair sun and kill the envious moon

"""
