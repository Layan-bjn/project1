import add.py as add
import sub.py as sub
import div.py as div
import avg.py as avg
i=input(int("choose: 1-add/sub 2-div/avg "))
if i == 1:
    operation = input("Choose operation (add/sub): ")
    if operation == "add":
         num1 = int(input("Enter first number: "))
         num2 = int(input("Enter second number: "))
         result = sum(num1,num2)
         print(f"The sum is: {result}")
    elif operation == "sub":
         num1 = int(input("Enter first number: "))
         num2 = int(input("Enter second number: "))
         result = sub(num1,num2)
         print(f"The difference is: {result}")
    else:
        print("Invalid operation selected.")
elif i == 2:
    operation = input("Choose operation (div/avg): ")
    if operation == "div":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = div(num1,num2)
        print(f"The quotient is: {result}")
    elif operation == "avg":
        list_of_numbers = input("Enter numbers separated by commas: ")
        result = avg(list_of_numbers)
        print(f"The difference is: {result}")
    else:
        print("Invalid operation selected.")
else:
    print("Invalid choice. Please select 1 or 2.")