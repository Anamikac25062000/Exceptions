#1)Write a Python program that prompts the user to enter an integer and handles the ValueError exception if the user enters a non-integer value.


def integer_input():
    while True:
        try:
            input_value = input("Enter an integer: ")
            integer_value = int(input_value)
            return integer_value
        except ValueError:
            print("Please enter a valid integer.")

result = integer_input()
print(result)
