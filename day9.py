# Sets
# Sets internally use hash table (same as dictionary)
# Remove duplicates
numbers = [1,2,2,2,3,1,5,8]
print(f"Unique numbers are: {set(numbers)}")

# check if two lists have common elements
number1 = {1,4,7,3}
numbers2 = {1,5,9,3}
print(f"common elemets are: {number1 & numbers2}")

# Find missing numbers in the range of 5
num = {1,2,4,5}
for i in range(1, 6):
    if i not in num:
        print(i)

# Find unique characters in a string
fruit = "banana"
print(set(fruit))

# Find duplicates in list
num1 = [1,2,3,2,4,1]
seen = set()
duplicates = set()
for num in num1:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)
print(f"duplicate values are: {duplicates}")

# Return First duplicate number
num2 = [1,2,3,2,4,1]
seen = set()
found = False
for num in num2:
    if num in seen:
        print(f"First duplicate number is: {num}")
        break
    else:
        seen.add(num)
if not found: print("no duplicates")
    

