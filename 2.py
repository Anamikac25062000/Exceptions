# 2)Create a program that opens a file and reads its contents. Use a try-except block to handle the FileNotFoundError exception and display a custom error message if the file does not exist.


try:
    file_name = input("Enter file name: ")

    with open(file_name, 'r') as file:
        file_contents = file.read()
        print("File Contents:\n", file_contents)

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
