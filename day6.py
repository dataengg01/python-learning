# ======================
# DICTIONARY BASICS
# ======================

customer = {
    "name": "swathi",
    "age":  25,
    "city": "gdlr"
}

print("print each key and value using loop")
for key, value in customer.items():
    print(f"{key} -> {value}")


numbers = [3, 5, 8, 2]
target = 10
print("Find 2 numbers whose sum = 10")
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])


print("Find 2 numbers whose sum = 10 using single loop")
seen = {}
for num in numbers:
    needed = target - num
    if needed in seen:
        print(needed, num)
        break
    seen[num] = True


print("Frequency counting using dictionaries")
numbers = [4, 4, 5, 6, 6, 6]
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)

print("Professional shortcut")
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1
print(frequency)

print("Print duplicate numbers only")
numbers = [4, 4, 5, 6, 6]
freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
for key, value in freq.items():
    if value > 1:
        print(key)


print("Print most frequent number")
numbers = [4, 4, 5, 6, 6, 6]
freq = {}
max_count = 0
most_frequent = None
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
for key, value in freq.items():
    if value > max_count:
        max_count = value
        most_frequent = key
print(f"most frequent number is: {most_frequent}")

print("Print most frequent number using one loop")
numbers = [4, 4, 5, 6, 6, 6]
freq = {}
max_count = 0
most_frequent = None
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
    if freq[num] > max_count:
        max_count = freq[num]
        most_frequent = num
print(f"most frequent number is: {most_frequent}")


