# Pattern Problems
print("Pattern 1")
# 1
# 21
# 321
# 4321

n = 4
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

print("Pattern 2")
# *
# **
# ***
# **
# *
n = 5
for i in range(1, n//2 + 2):
    for j in range(i):
        print("*", end = " ")
    print()
for i in range(n//2, 0, -1):
    for j in range(i):
        print("*", end = " ")
    print()

print("Pattern 2 with better approach")
for i in range(1, n+1):
    if i <= n//2 + 1:
        stars = i
    else:
        stars = n-i + 1
    for j in range(stars):
        print("*", end = " ")
    print()

print("Pattern 3")
#    1
#   121
#  12321
# 1234321
n = 4
for i in range(1, n+1):
    k = 1
    for j in range(n-i):
        print(" ", end = " ")
    for j in range(2*i - 1):
        if j < i:
            print(j + 1, end = " ")
        else:
            print(j - k, end = " ")
            k += 2
    print()

print("Pettern 3 better version")
n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = " ")
    num = 1
    for j in range(1, i+1):
        print(num, end = " ")
        num += 1
    num -= 2
    for k in range(1, i):
        print(num, end = " ")
        num -= 1
    print()

print("Pattern 4")
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
n = 7
num = 1
for i in range(1, n+1):
    if i <= n//2 + 1:
        space = (n//2 + 1) - i
        stars = 2*i - 1
        for j in range(space):
            print(" ", end = " ")
        for j in range(stars):
            print("*", end = " ")
    else:
        space = num
        stars = n - 2*num
        for j in range(space):
            print(" ", end = " ")
        for j in range(stars):
            print("*", end = " ")
        num += 1
    print()

print("Pattern 4 better version")
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
n = 7
for i in range(1, n+1):
    if i <= n//2 + 1:
        space = (n//2 + 1) - i
        stars = 2*i - 1
    else:
        space = i - (n//2 + 1)
        stars = 2*(n - i) + 1
    print("  " * space + "* " * stars)

print("Reverse Triangle Numbers")
# 1
# 2 1
# 3 2 1
# 4 3 2 1

n = 4
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end = " ")
    print()

print("Diamond Star")
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = 7
for i in range(1, n+1):
    if i <= n//2 + 1:
        spaces = (n//2 + 1) - i
        stars = 2*i - 1
    else:
        spaces = i - (n//2 + 1)
        stars = 2*(n - i) + 1
    print("  " * spaces + "* " * stars)

print("First non-repeating chrecter")
word = input("enter a word: ")
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
for ch in word:
    if freq[ch] == 1:
        print(ch)
        break

print("Anagram Check")
freq = {}
is_anagram = True
word1 = input("enter word1: ").strip().lower()
word2 = input("enter word2: ").strip().lower()
if len(word1) != len(word2):
    print("Not Anagrams")
else:
    for ch in word1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in word2:
        freq[ch] = freq.get(ch, 0) - 1
    for value in freq.values():
        if value != 0:
            is_anagram = False
            break
    print("Anagrams" if is_anagram else "Not Anagrams")

print("Print Alphabets Triangle")
# A
# AB
# ABC
# ABCD

n = 4
for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end = " ")
    print()


