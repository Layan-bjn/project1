i=input(int("choose: 1-add/sub 2-mean/avg "))
if i == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Choose operation (add/sub): ")
    if operation == "add":
        result = sum(num1 + num2)
        print(f"The sum is: {result}")
    elif operation == "sub":
        result = sub(num1 - num2)
        print(f"The difference is: {result}")
    else:
        print("Invalid operation selected.")
elif i == 2:
    numbers = input("Enter numbers separated by spaces: ")
    num_list = [int(num) for num in numbers.split()]
    mean = sum(num_list) / len(num_list)
    print(f"The mean is: {mean}")
else:
    print("Invalid choice. Please select 1 or 2.")