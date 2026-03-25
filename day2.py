# #While Loop
# print("print 5 -> 1 using while")
# i = 5
# while i > 0:
#     print(i)
#     i = i - 1

# print("print multiplication table using user provided number")
# num = int(input("enter a number "))
# i = 1
# while i <= 10:
#     print(f"{num} * {i} = {num*i}")
#     i = i+1

# print("Sum of all numbers from 1 to user given number")
# last_num = int(input("enetr a number "))
# i = 1
# total_sum = 0
# while i <= last_num:
#     total_sum = total_sum + i
#     i = i + 1
# print(f"Sum = {total_sum}")

# print("repeat the loop until user guess the lucky number")
# lucky_number = 7
# while True:
#     entered_number = int(input("enter a number "))
#     if entered_number != lucky_number:
#         print("Try again")
#     else:
#         print("You gussed it")
#         break

# print("repeat the loop until user guess the random number")
# module → random
# function → randint
# parameters → start, end
# import random
# lucky_number = random.randint(1, 10)
# i = 0
# while True:
#     entered_number = int(input("enter a number "))
#     i = i + 1
#     if entered_number != lucky_number:
#         print("try again")
#     else:
#         print(f"you guessed in {i} attempts")
#         break
