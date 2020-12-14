# String Concatenation
print("Let's concatenate a string!")

first_word = input("What is the first word? ")
second_word = input("What is the second word? ")
answer = first_word + " " + second_word

print("The answer is: " + answer)

# Tip Calulator
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage? "))
number_people = int(input("How many people? "))
answer = round((total_bill + (total_bill / 100 * percentage)) / number_people, 2)

print("Every person has to pay: $" + str(answer))