# Lists
# Python allows mixed types in a list
# Lists are mutable
names = ["Swathi", "Shloka", "Oracle"]
print(f"first item is: {names[0]}")
print(f"second item is: {names[1]}")
print(f"third item is: {names[2]}")
print(f"length of the names list is: {len(names)}")

numbers = [5, 7, 3, 9]
print(numbers)
# Negative Indexing
print(f"Last number in the list is: {numbers[-1]}")
# Slicing
print(f"first two numbers are: {numbers[0:2]}")
# in Operator
if 7 in numbers:
    print("7 exist in the list")
# Sum, Min, Max
print(f"Sum of numbers in the list is: {sum(numbers)}, minimum number is: {min(numbers)} and maximum number is: {max(numbers)} ")

cities = ["gdlr", "hyd", "gnt"]
print(f"First city is {cities[0]}, Third city is {cities[2]}")
print(f"last city is {cities[-1]}")

fruits = ["apple", "banana", "orange"]
fruits[2] = "mango"
print(f"Updated list is {fruits}")

new_names = []
new_names.append("swathi")
new_names.append("eswar")
new_names.append("shloka")
print(f"final list is {new_names}")

even_numbers = [2, 4, 6, 8]
for num in even_numbers:
    print(num)

for i in range(len(even_numbers)):
    print(even_numbers[i])

print(f"First two even numbers are: {even_numbers[0:2]}")


cars = []
for i in range(3):
    cars.append(input("enter a car name: "))
print(f"list of cars are: {cars}")

