"""Week 3 - Python Exception Handling Examples"""

def value_error_example():
    print("\n--- ValueError ---")
    try:
        number = int(input("Enter a whole number (try: hello): "))
        print(f"You entered: {number}")
    except ValueError:
        print("ValueError caught: Please enter a valid whole number.")

def zero_division_example():
    print("\n--- ZeroDivisionError ---")
    try:
        number = int(input("Enter a number to divide 100 by (try: 0): "))
        print(100 / number)
    except ValueError:
        print("ValueError caught: Please enter a valid number.")
    except ZeroDivisionError:
        print("ZeroDivisionError caught: You cannot divide by zero.")

def index_error_example():
    print("\n--- IndexError ---")
    numbers = [10, 20, 30]
    print("List:", numbers)
    try:
        index = int(input("Enter an index (try: 10): "))
        print(numbers[index])
    except ValueError:
        print("ValueError caught: The index must be a whole number.")
    except IndexError:
        print("IndexError caught: That index does not exist.")

def key_error_example():
    print("\n--- KeyError ---")
    student = {"name": "Alex", "course": "Programming"}
    print("Dictionary:", student)
    key = input("Enter a key (try: age): ").strip()
    try:
        print(student[key])
    except KeyError:
        print(f"KeyError caught: '{key}' does not exist.")

def file_error_example():
    print("\n--- FileNotFoundError ---")
    try:
        with open("this_file_does_not_exist.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("FileNotFoundError caught: The file could not be found.")

def type_error_example():
    print("\n--- TypeError ---")
    try:
        result = "Age: " + 20
        print(result)
    except TypeError:
        print("TypeError caught: A string and integer cannot be joined with +.")
        print('Correct example: "Age: " + str(20)')

def name_error_example():
    print("\n--- NameError ---")
    try:
        print(student_name)
    except NameError:
        print("NameError caught: student_name has not been defined.")

def attribute_error_example():
    print("\n--- AttributeError ---")
    message = "Hello"
    try:
        message.append("!")
    except AttributeError:
        print("AttributeError caught: strings do not have append().")

def else_finally_example():
    print("\n--- try / except / else / finally ---")
    try:
        number = int(input("Enter a number (try 5, 0, or hello): "))
        result = 100 / number
    except ValueError:
        print("except: Invalid integer.")
    except ZeroDivisionError:
        print("except: Cannot divide by zero.")
    else:
        print(f"else: No exception. Result = {result}")
    finally:
        print("finally: This always runs.")

def raise_example():
    print("\n--- raise and .strip() ---")
    question = input("Ask a question (or press Enter): ")
    try:
        if not question.strip():
            raise ValueError("Question cannot be empty.")
        print(f'Valid question: "{question.strip()}"')
    except ValueError as error:
        print(f"ValueError caught: {error}")

def multiple_exceptions_example():
    print("\n--- Multiple exceptions ---")
    numbers = [100, 50, 25]
    print("Numbers:", numbers)
    try:
        index = int(input("Choose index 0, 1 or 2: "))
        divisor = int(input("Enter a divisor: "))
        result = numbers[index] / divisor
    except ValueError:
        print("ValueError caught: Enter whole numbers.")
    except IndexError:
        print("IndexError caught: Index does not exist.")
    except ZeroDivisionError:
        print("ZeroDivisionError caught: Divisor cannot be zero.")
    else:
        print(f"Result: {result}")
    finally:
        print("Example finished.")

while True:
    print("""
==========================================================
WEEK 3 - PYTHON EXCEPTION HANDLING EXAMPLES
==========================================================
1.  ValueError
2.  ZeroDivisionError
3.  IndexError
4.  KeyError
5.  FileNotFoundError
6.  TypeError
7.  NameError
8.  AttributeError
9.  try / except / else / finally
10. raise + .strip()
11. Multiple exceptions together
0.  Exit
""")
    choice = input("Choose an example: ").strip()

    if choice == "1":
        value_error_example()
    elif choice == "2":
        zero_division_example()
    elif choice == "3":
        index_error_example()
    elif choice == "4":
        key_error_example()
    elif choice == "5":
        file_error_example()
    elif choice == "6":
        type_error_example()
    elif choice == "7":
        name_error_example()
    elif choice == "8":
        attribute_error_example()
    elif choice == "9":
        else_finally_example()
    elif choice == "10":
        raise_example()
    elif choice == "11":
        multiple_exceptions_example()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Choose 0 to 11.")

    input("\nPress Enter to return to the menu...")
