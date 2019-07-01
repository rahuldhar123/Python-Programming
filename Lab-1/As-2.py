stringinput = input('Please enter a string:')
current = []
strings = []

for char in stringinput:

    if char in current:

        strings.append(''.join(current))

        nextstring = current.index(char)+1
        current = current[nextstring:]

    current.append(char)

strings.append(''.join(current))

long = max(strings, key = len)

print('The longest string of characters without repeating is', long,'with a length of', len(long))