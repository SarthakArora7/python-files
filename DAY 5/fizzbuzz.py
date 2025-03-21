for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        num = "FizzBuzz"
    elif num % 3 == 0:
        num = "Fizz"
    elif num % 5 == 0:
        num = "Buzz"
    print(num)

    # or

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)