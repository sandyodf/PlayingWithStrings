"""

Given a string, return a string where for every char in the original, there are two chars.
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree

"""


# name='sandeep'
#
# for chars in name:
#     print(chars*2)

def double_char(str):
    result = ''
    for char in str:
        result += (char * 2)
    return result


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))

"""

Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True


"""


def cat_dog(str):
    count_of_cat = 0
    count_of_dog = 0
    for char in range(len(str) - 1):
        if str[char:char + 3] == 'cat':
            count_of_cat += 1
        if str[char:char + 3] == 'dog':
            count_of_dog += 1
    return count_of_cat == count_of_dog


print(cat_dog('cat'))

"""

Return the number of times that the string "code" appears anywhere in the given string, 
except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2

"""


def count_code(str2):
    count_code = 0
    for iter in range(len(str2) - 1):
        if str2[iter:iter + 2] == 'co' and str2[iter + 3]== 'e':
            count_code += 1

    return count_code


print(count_code('aaacodebbb'))

print(count_code('codexxcode'))

print(count_code('cozexxcope'))
print(count_code('codecopecopecode'))
