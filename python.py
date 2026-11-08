
print("HELLO!")

print("Calculator with Python.")

num_1 = float(input("Enter First Number: "))
num_2 = float(input("Enter Second Number: "))

action = input("Choose an operator (+ - * /): ")

if action == "+":
    print("Result:", num_1 + num_2)

elif action == "-":
    print("Result:", num_1 - num_2)

elif action == "*":
    print("Result:", num_1 * num_2)

elif action == "/":
    if num_2 != 0:
        print("Result:", num_1 / num_2)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid operator!")
