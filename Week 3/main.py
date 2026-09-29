"""from magic_eight_ball import get_eight_ball_response

question = input("Ask the Magic Eight Ball a question: ")

try:
    if not question.strip():
        raise ValueError("Question can not be empty!")
    answer = get_eight_ball_response()
    print(f"\nMagic Eight Ball {answer}")
except ValueError as error:
    print(f"Input error: {error}")"""

""" balance = 500.00
print("Welcome to the class Bank")

while True:
    print("\n1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    option = input("Choose an option:")

    match option:
        case "1":
            print(f"Your balance is £{balance:.2f}")
        case "2":
            try:
                amount = float(input("Enter amount to deposit:"))
                if amount <= 0:
                    raise ValueError("Amount must be greater than 0")
                balance += amount
                print(f"Deposit successful")
                print(f"New balance {balance:.2f}")
            except ValueError as error:
                print("Error:", error)
        case "3":
            try:
                amount = float(input("Enter amount to withdraw:"))
                if amount <= 0:
                    raise ValueError("Amount must be greater than 0")
                balance -= amount
                print(f"Widrawn successful")
                print(f"New balance {balance:.2f}")
            except ValueError as error:
                print("Error:", error)
        case "4":
            print("See you around!")
            break
 """

print("Temperature converter")

while True:
    print("1. Celsius to Fahrenheits")
    print("2. Farenheits to Celsius")
    print("3. Celsius to kelvin")

    option = input("Enter the choosen option: ")

    match option:
        case "1":
            try:
                temp = float(input("Enter the temperature: "))
                fah = (temp * 9 / 5) + 32
                print(f"The conversion value is {fah:.2f}\n")
            except ValueError as error:
                print("Enter an integer or float value!\n")
        case "2":
            try:
                temp = float(input("Enter the temperature: "))
                cel = (temp - 32) * 9 / 5
                print(f"The conversion value is {cel:.2f}\n")
            except ValueError:
                print("Enter an integer or float value!\n")
        case "3":
            try:
                temp = float(input("Enter the temperature: "))
                kel = temp - 273.15
                print(f"The conversion value is {kel:.2f}\n")
            except ValueError as error:
                print("Enter an integer or float value!\n")
