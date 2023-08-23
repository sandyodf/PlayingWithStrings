"""
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""


def hello_name(name):
    return f"Hello {name}!"


print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))


def make_tags(tag, word):
    return f"<{tag}>{word}<{tag}>"


print(make_tags('i', 'yay'))

name = 'deep'
print(name[-3] * 2)


def extra_end(str):
    if len(str) >= 2:
        length = len(str)
        return str[length - 2:] * 3
    else:
        return "invalid string"


print(extra_end('sa'))

"""
link:https://codingbat.com/prob/p184816

Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
If the string is shorter than length 2, return whatever there is, so "X" yields "X", 
and the empty string "
" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""


def first_two(str):
    if len(str) > 2:
        return str[0:2]
    else:
        return str


print(first_two('Hello'))
print(first_two('a'))

"""
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'

"""


def first_half(str):
    if len(str) % 2 == 0:
        return str[0:int(len(str) / 2)]


print(first_half('WooHoo'))
print(first_half('HelloThere'))

"""

Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.


without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'



"""


def without_end(str2):
    if len(str2) >= 2:
        return str2[1:len(str2) - 1]
    else:
        return str2


print('Hello --->', without_end('Hello'))
print('JAVA --->', without_end('java'))
print('Coding --->', without_end('Coding'))

"""

Given 2 strings, a and b, return a string of the form short+long+short, 
with the shorter string on the outside and the longer string on the inside. 
The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'

"""


def combo_string(s1, s2):
    if len(s1) > len(s2):
        return s2 + s1 + s2
    else:
        return s1 + s2 + s1


print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))

"""


Given 2 strings, return their concatenation, except omit the first char of each. 
The strings will be at least length 1.


non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'



"""


def non_start(m1, m2):
    if len(m1) >= 1 and len(m2) >= 1:
        return m1[1:] + m2[1:]
    else:
        return m1 + m2


print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))

"""
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. 
The string length will be at least 2.


left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'



"""


def left2(strings):
    if len(strings) >= 2:
        return strings[2:] + strings[0:2]


print(left2('Hello'))
