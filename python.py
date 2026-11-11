
# Calculatir -> + - * / 


def sum (a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def devision(a, b):
    return a / b

while True:
    print(" Choose an uption: [1] sum, [2], subract, [3] multiply, [4] devision , [5] Exit")
    
    choice =  int(input("Choice : "))



    if choice == 5:
        print("Programe Exited")
        break
    elif choice > 5 or choice < 1 :
         print ("Please choise a range  1 - 5 ")
         continue


    print("Please Enter your Number : \n")
    num1 = int(input("Number 1:"))
    num2 = int(input("Number 2:"))
       
    

    if choice == 1:
     result = sum(num1, num2)
     print("Result is:", result)
       
    if choice == 2:
           result = subtract(num1, num2)
           print("Result is :", result)   
       
    if choice == 3:
           result = multiply(num1, num2)
           print("Result is:", result)   
       
    if choice == 4:
           result = devision(num1, num2)
           print("Result is :", result)


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

