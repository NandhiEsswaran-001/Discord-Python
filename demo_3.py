list_1 = [1, 2.4, "Words", ["tennis ball", "stumper ball"], True]

new_list = list_1[:]
new_list += [["biryani", "maggi"]]
print(new_list)

print(list_1[-1])
print(list_1[3][0])
# print(list_1[3][1])

# if else
# food order

customer_choice = input("Choose your food: (dosa/idly/parota): ")

if customer_choice == "dosa":
  print(customer_choice + " is ordered")
elif customer_choice == "idly":
  print(customer_choice + " is ordered")
elif customer_choice == "parota":
  print(customer_choice + " is ordered")
else:
  print("We don't have " + customer_choice)

# for loop
members = ["Keerthi", "Mahesh", "Mon - Sabari", "Kayal - Son", "Head - Susee"] # iterable members
print(members)

for member in members:
  print(member)

for number in range(10, 0, -1):
  print(number)

# while

user_name = input("Enter your name: ")

# input validation
while user_name == "": # executes when it is true
  print("Hey you idot you need to enter your name: ")
  user_name = input("Enter your name: ") # "John" or "Mark"

print("Hello " + user_name)


count = 1
while count <= 10:
  print(count)
  count += 1

# break

list_1 = ["chocolates", "pink gua", "pussy orea"]

while True:
  if "milk" in list_1:
    print("Yeah milk is already on the list")
    break
  else:
    print("milk is not added")
    list_1.append("milk")

numbers = range(1, 10)

for number in numbers:
  if number == 5:
    break
  print(number)

# continue

nandhi_jersey_numbers = [10, 7, 9, 11]

print("---Here are the all available jersey numbers---")
for jersey_number in range(1, 21):
  if jersey_number in nandhi_jersey_numbers:
    continue
  print(jersey_number)

# home work - 1
# create a list of members
# check who's name starts with K and M using if_elif_else
# store them in separate lists one for K and one for M
# and loop through and print it using for loop

# home work -2
# create a simple menu display
# ask a user for the followings

# Welcome to our program
# 1.About
# 2.Work
# 3.Exit

# first print the options above
# next get input from the user
# the user needs to type from the above options
# use while for input validation
# if user types exit then while should break
# if user types about then it shows some messages
# if user types work then it shows some messages
# if user types some unwanted text then show please enter a valid option