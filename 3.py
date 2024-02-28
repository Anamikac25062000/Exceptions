# 3)Write a program that calculates the division of two numbers entered by the user. Use a try-except block to handle the ZeroDivisionError exception and display an appropriate error message if the user tries to divide by zero.


try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))

    result = numerator / denominator

    print(f"Result of {numerator} / {denominator} = {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero denominator.")
except ValueError:
    print("Error: Please enter valid numeric values.")
except Exception as e:
    print(f"An error occurred: {e}")
