# Reverse, Sort
# Notes:
# Built in Functions are called by passing the list as an argument.
# Built in Functions are not tied to any objects and they do not modify original list but returns a new list
# Examples of built in functions are len, sum, min, max
# Methods belongs to object and they modify the original list itself and returns None.
# Examples of list methods are append, reverse, sort, pop
# Easy way to remember is Function is like a teacher, teacher is outside and can check any student but method is student who work on himself.

numbers = [10, 5, 8]

print("original:", numbers)
# Below sorted(numbers) is a function and it will return new list with sorted values and does not modify original list.
print("sorted():", sorted(numbers))
print("after sorted():", numbers)
# Below is list method and will change the original list and returns None.
numbers.sort()
print("after sort():", numbers)
# Iterator can be used only once, after that it will become empty.
print("Iterator:", reversed(numbers))
# Below list(reversed(numbers)) is a function and it will return new list with reversed values and does not modify original list.
print("reversed():", list(reversed(numbers)))
print("after reversed():", numbers)
# Below is list method and will change the original list and returns None.
numbers.reverse()
print("after reverse():", numbers)

# Pop
p_numbers = [20, 60, 40, 10, 80]
# pop() = remove + return value (removed value)
# Below removed the last value and returned the removed value.
removed = p_numbers.pop()
print(removed)
print(p_numbers)
# Idexing can be used to remove specific value.
p_numbers.pop(1)
print(p_numbers)

# Remove
r_numbers = [20, 60, 40, 10, 80]
# remove() uses value not index and returns None.
r_numbers.remove(40)
print(r_numbers)

# Insert
i_numbers = [20, 60, 40, 10, 80]
# adds element at specific position using index and returns None.
i_numbers.insert(2, 30)
print(i_numbers)

