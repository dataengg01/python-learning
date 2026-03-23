print("Hello Oracle")
print("I want job in Oracle")

# ===========================
#variables
# ===========================
my_name = "swathi"
print(my_name)

#Python automatically understands type unlike Java.
age = 25
future_age = age+5
print(future_age)

# ===========================
#print() Function
# ===========================
print("My age is", age)
# While using concat, we must convert int to str
print("My age is " + str(age))
print(f"My age is {age}")
print(f"My age is {age}, after 5 years my age is {age + 5}")

baby="Adhya"
city="Giddalur"
print(f"My baby {baby} lives in {city}")

# ===========================
#input() Function
# ===========================
company = input("Enter your dream company:")
print(f"You want job in {company}")
current_age = int(input("enter your current age "))
print(f"After 5 years your age is {current_age + 5}")
baby = input("baby name ")
city = input("city ")
print(f"{baby} lives in {city}")

# ===========================
#Data Types
# ===========================
name = "swathi"
my_age = 25
weight = 55.5

print(type(name))
print(type(my_age))
print(type(weight))

marks = int(input("enter marks "))
print(type(marks))
print(f"your marks after bonus is {marks + 10}")

learning_python = True
print(type(learning_python))

# ===========================
#If Else Functions
# ===========================
user_age = int(input("enter your age "))
if(user_age > 18):
    print(f"you are eligible for job")
else:
    print(f"you need more time")

user_age = int(input("enter your age "))
if user_age < 13:
    print("child")
elif user_age < 20:
    print("teen")
else:
    print("adult") 

salary = int(input("enter your salary "))
if salary > 50000:
    print("high income")
else:
    print("normal income")

company = input("enter your dream company ")
if company.lower() == "oracle":
    print("Great goal!!")
else:
    print("Keep trying")

# ===========================
#Loops
# ===========================
for i in range(5):
    print("I want oracle job")

for i in range(10, 16):
    print(i)

print("print 1 to 10 numbers:")
for i in range(1, 11):
    print(i)
print("print odd numbers:")
for i in range(1, 11):
    if i%2!=0:
        print(i)

num = int(input("enter number: "))
for i in range(num):
    print("Hello World") 