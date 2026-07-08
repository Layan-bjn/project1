from sub_add.add import add
from sub_add.sub import sub
from div_avg.div import div
from div_avg.avg import avg

i = int(input("choose:\n1-add/sub\n2-div/avg\n"))
if i == 1:
    operation = input("Choose operation (add/sub): ")
    if operation == "add":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = add(num1, num2)
        print(f"The sum is: {result}")
    elif operation == "sub":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = sub(num1, num2)
        print(f"The difference is: {result}")
    else:
        print("Invalid operation selected.")
elif i == 2:
    operation = input("Choose operation (div/avg): ")
    if operation == "div":
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = div(num1, num2)
        print(f"The quotient is: {result}")
    elif operation == "avg":
        list_of_numbers = input("Enter numbers separated by commas: ")
        result = avg(list_of_numbers)
        print(f"The average is: {result}")
    else:
        print("Invalid operation selected.")
else:
    print("Invalid choice. Please select 1 or 2.")