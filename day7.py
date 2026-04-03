# Dictionaries continuation
print("print all numbers having maximum frequency")
numbers = [4,4,5,5,6]
freq = {}
max_count = 0
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
for key, value in freq.items():
    if value > max_count:
        max_count = value
for key, value in freq.items():
    if value == max_count:
        print(key)
        
print("print all numbers having maximum frequency with 2 loops")
numbers = [4,4,5,5,6]
freq = {}
max_count = 0
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
    if freq[num] > max_count:
        max_count = freq[num]
for key, value in freq.items():
    if value == max_count:
        print(key)

print("Print most frequent number and it's frequency")
numbers = [4, 4, 5, 6, 6]
freq = {}
max_count = 0
most_frequent = None
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
    if freq[num] >= max_count:
        max_count = freq[num]
        most_frequent = num
print(f"most frequent number is: {most_frequent}, {max_count}")

# string + Pattern Problems
print("Reverse a string without using slicing")
text = input("enter a string: ")
rev = text[::-1]
rev_string = ""
for ch in text:
    rev_string = ch + rev_string
print(f"reverse string using slicing technique is: {rev}, without using slicing is: {rev_string}")

print("Check if a string is palindrome (without slicing)")
word = input("enter a word: ")
# Below one for adding case sensitive and ignoring spaces
# word = input("enter a word: ").replace(" ", "").lower()
rev_word = ""
for ch in word:
    rev_word = ch + rev_word
if word == rev_word:
    print("entered word is Palindrome")
else:
    print("entered word is not a Palindrome")

print("Check if a string is palindrome using two pointers")
word = "racecar"

left = 0
right = len(word) - 1

is_palindrome = True

while left < right:
    if word[left] != word[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print("Palindrome" if is_palindrome else "Not Palindrome")

print("Count frequency of characters")
name = input("enter a name: ")
freq = {}
for ch in name:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

print("First Non-Repeating Character")
letters = input("enter letters: ")
freq = {}
for ch in letters:
    freq[ch] = freq.get(ch, 0) + 1
for ch in letters:
    if freq[ch] == 1:
        print(ch)
        break

print("Check if two strings are anagrams using sorted()")
text1 = input("enter text1: ")
text2 = input("enter text2: ")
sorted_text1 = sorted(text1)
sorted_text2 = sorted(text2)
if sorted_text1 == sorted_text2:
    print("two strings are anagrams")
else:
    print("two strings are not anagrams")


print("Check if two strings are anagrams without using sorted()")
text1 = input("enter text1: ")
text2 = input("enter text2: ")
text1_freq = {}
text2_freq = {}
is_anagrams = True
if len(text1) != len(text2):
    print("Not Anagrams")
else:
    for ch in text1:
        text1_freq[ch] = text1_freq.get(ch, 0) + 1
    for ch in text2:
        text2_freq[ch] = text2_freq.get(ch, 0) + 1
    for key,value in text1_freq.items():
        if key in text2_freq:
            if value == text2_freq[key]:
                continue
            else:
                is_anagrams = False
            continue
        else:
            is_anagrams = False
            break
    print("Anagrams" if is_anagrams else "Not Anagrams")   

print("Check if two strings are anagrams without using sorted() in optimized way")
text1 = input("enter text1: ")
text2 = input("enter text2: ")
freq = {}
is_anagrams = True
if len(text1) != len(text2):
    print("Not Anagrams")
else:
    for ch in text1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in text2:
        freq[ch] = freq.get(ch, 0) - 1
    for val in freq.values():
        if val != 0:
            is_anagrams = False
            break
    print("Anagrams" if is_anagrams else "Not Anagrams")
