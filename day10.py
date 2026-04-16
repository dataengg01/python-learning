# Tuples
numbers = (1,5,3,9,4,3,1)
print(numbers)

t = (10,20,30)
print(f"Sum of all numbers in the tuple are: {sum(t)}")

a = 5
b = 10
t = 5,10
a,b = 10,5
print(f"Values after swaping are: {a,b}")

def multi_val():
    return 10,20
x,y = multi_val()
print(f"Values from the function are: {x,y}")

print("Find intersection of two lists")
a = [1,2,3,4]
b = [3,4,5,6]
print(f"Intersection of two lists are: {list(set(a) & set(b))}")

print("Find first repeating number")
numbers = [5,3,4,3,5,6]
seen = set()
for num in numbers:
    if num in seen:
        print(f"First repeating number is: {num}")
        break
    else:
        seen.add(num)

print("Count frequency of words")
fruits = "apple banana apple mango banana apple"
fruits_list = fruits.split(" ")
freq = {}
for fruit in fruits_list:
    freq[fruit] = freq.get(fruit, 0) + 1
print(f"Frequency of fruits are: {freq}")

print("Find two numbers whose sum = target")
nums = [2,7,11,15]
target = 9
seen = {}
for num in nums:
    temp = target - num
    if temp in seen:
        print(temp, num)
    else:
        seen[num] = True

print("FInd two numbers whose sum = target")
nums = [2,7,11,15]
target = 9
seen1 = {}
for i, num in enumerate(nums):
    temp = target - num
    if temp in seen1:
        print(seen1[temp], i)
        break
    else:
        seen1[num] = i


print("Check if list contains duplicates")
num1 = [1,2,3,4,2]
num2 = list(set(num1))
if len(num1) != len(num2):
    print("yes")
else:
    print("No")

print("Group Anagrams")
words = ["eat","tea","tan","ate","nat","bat"]
anagrams_map = {}
for word in words:
    key = "".join(sorted(word))
    if key not in anagrams_map:
        anagrams_map[key] = []
    anagrams_map[key].append(word)
print(list(anagrams_map.values()))