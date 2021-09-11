import collections


def parse_user_data(line):
    """
    >>> parse_user_data('John Doe john.doe@example.com')
    ('John', 'Doe', 'john.doe', 'example.com')
    """
    parts = line.split(' ')
    email_parts = parts[2].split('@')
    return (parts[0], parts[1], email_parts[0], email_parts[1])


def compare_lists(dir_a, dir_b):
    """
    >>> dir_a = ['hello.py', 'readme.txt']
    >>> dir_b = ['readme.txt', 'install.txt', 'hello2.py']
    >>> compare_lists(dir_a, dir_b)
    {'removed': ['hello.py'], 'added': ['hello2.py', 'install.txt']}
    """

    removed = [filename for filename in dir_a if filename not in dir_b]
    added = [filename for filename in dir_b if filename not in dir_a]
    return {'removed': sorted(removed), 'added': sorted(added)}


from datetime import datetime


def print_log(message, process_id, timestamp, level=2):
    """
    >>> from datetime import datetime
    >>> print_log('System started!', 1532, datetime(2019, 1, 2, 10, 30, 55).isoformat(' '))
    2019-01-02 10:30:55 [1532] [INFO] System started!
    """

    loglevel = 'TRACE' if level == 0 else 'DEBUG' if level == 1 else 'INFO' if level == 2 else 'WARN' if level == 3 else 'ERROR' if level == 4 else 'None'
    print(timestamp + ' [' + str(process_id) + ']' + ' [' + loglevel + ']' + ' ' + message)


def biggest_rectangle(rectangles):
    """
    Find the biggest rectangle in a sequence.
    Rectangles are represented as tuples of (width, height).

    >>> biggest_rectangle([(2, 4), (3, 3), (4, 2)])
    (3, 3)
    """
    return [[r for r in rectangles if (r[0] * r[1]) == max([m[0] * m[1] for m in rectangles])]][0][0]


def find_in_file(pattern, filename):
    """
    Find a pattern in file. Print out all lines that match the pattern
    (case-insensitive) with line numbers.
    >>> find_in_file('nevermore', 'raven.txt')
     62 Quoth the Raven, "Nevermore."
     69 With such name as "Nevermore."
     77 Then the bird said, "Nevermore."
     84 Of 'Never- nevermore'."
     92 Meant in croaking "Nevermore."
     99 She shall press, ah, nevermore!
    107 Quoth the Raven, "Nevermore."
    115 Quoth the Raven, "Nevermore."
    123 Quoth the Raven, "Nevermore."
    132 Quoth the Raven, "Nevermore."
    140 Shall be lifted- nevermore!
    """

    with open(filename) as file:
        for line_num, line in enumerate(file) :
            if pattern.lower() in line.lower():
                print(('  ' if line_num < 10 else ' ' if line_num < 100 else '' )+ str(line_num), line.strip("\n").strip(" "))



def read_long_words(filename, min_length=0):
    """
    >>> words = read_long_words('raven.txt', 5)
    >>> words[:6]
    ['midnight', 'dreary', 'pondered', 'quaint', 'curious', 'volume']
    """
    with open(filename, 'r') as file:
        no_punct = [ch for ch in file.read() if ch not in r'[.,"!-]']
        return [word.lower() for word in (''.join(no_punct)).split() if len(word) > min_length]


def top_words(words, n=10):
    """
    Find top N words in a file. Return a list of tuples (word, count).

    >>> words = read_long_words('raven.txt', 5)
    >>> top_words(words, 5)
    [('chamber', 11), ('nevermore', 10), ('lenore', 8), ('nothing', 7), ('tapping', 5)]
    """

    result = [(count, word) for word, count in collections.Counter(words).items()]
    return [(count, word) for (word, count) in sorted(result, reverse=True)[:n]]


words = read_long_words('raven.txt', 5)
print(top_words(words, 5))
