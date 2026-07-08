def avg(num1)->float:
    if isinstance(num1, str):
        num1 = [int(value.strip()) for value in num1.split(",") if value.strip()]

    if not num1:
        raise ValueError("At least one number is required")

    total = 0
    for value in num1:
        total += value
    return total / len(num1)