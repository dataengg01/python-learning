numbers = [40, 20, 60, 90, 10]

# Pop
removed = numbers.pop()
print(f"Removed element is {removed}")

numbers.remove(60)
print(f"Updated list is: {numbers}")

numbers.insert(2, 70)
print(f"new list is {numbers}")

print("Print largest number manually")
largest_number = numbers[0]
for num in numbers:
    if num > largest_number:
        largest_number = num
print(f"largest number is {largest_number}")

print("Count Even Numbers")
new_numbers = [4, 7, 14, 73, 91, 22, 46]
count = 0
for num in new_numbers:
    if num % 2 == 0:
        count += 1
print(f"total even numbers are {count}")

print("Remove duplicates from list")
d_list = [4, 6, 4, 2, 8, 2]
unique_list = []
for num in d_list:
    if num not in unique_list:
        unique_list.append(num)
print(f"unique list is {unique_list}")

print("Print second largest number")
u_numbers = []
for num in new_numbers:
    if num not in u_numbers:
        u_numbers.append(num)
temp = sorted(u_numbers)
print(f"Second largest number is: {temp[-2]}")

print("Print Reversed List")
r_list = []
for num in new_numbers:
    r_list.insert(0, num)
print(f"reversed list is: {r_list}")

print("Count frequency")
f_list = [1,1,1,2,3,3,4,4,4,5]
unique = []
for num in f_list:
    if num not in unique:
        unique.append(num)
for num in unique:
    count = 0
    for n in f_list:
        if n == num:
            count += 1
    print(f"{num} --> {count}")
    

print("Find missing number")
m_list = [1,2,3,5,6]
for num in range(1, len(m_list) + 2):
    if num not in m_list:
        print(f"missing number is: {num}")
        break

print("Print Sum of even numbers only")
e_list = [4, 5, 7, 2, 8]
total = 0
for num in e_list:
    if num % 2 == 0:
        total += num
print(f"sum of even numbers is: {total}")