# 5)Write a program that opens a file, reads its contents, and writes the contents to a new file. Use a try-except-finally block to ensure that the file is closed even if an exception occurs during the file operations.


try:
    source_file_name = input("Enter the name of the source file: ")

    destination_file_name = input("Enter the name of the destination file: ")

    with open(source_file_name, 'r') as source_file:
        file_contents = source_file.read()

    with open(destination_file_name, 'w') as destination_file:
        destination_file.write(file_contents)

except FileNotFoundError:
    print(f"Error: The file '{source_file_name}' does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")

finally:

    try:
        source_file.close()
    except NameError:
        pass 

    try:
        destination_file.close()
    except NameError:
        pass
