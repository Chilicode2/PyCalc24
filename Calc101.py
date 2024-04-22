print(" _____________________")
print("|  _________________  |")
print("| |CALCULATOR 11000 | |")
print("| |_________________| |")
print("|  ___ ___ ___   ___  |")
print("| | 7 | 8 | 9 | | + | |")
print("| |___|___|___| |___| |")
print("| | 4 | 5 | 6 | | - | |")
print("| |___|___|___| |___| |")
print("| | 1 | 2 | 3 | | x | |")
print("| |___|___|___| |___| |")
print("| | . | 0 | = | | / | |")
print("| |___|___|___| |___| |")
print("|_____________________|")

def CalcMethod():
    print()
    ans = 0  # Initialize "answer" to view the stored value of the previous calculation
    
    while True:
        count = input("Choose either: \n+ \n- \n/ \n* \n^ \n(Type 'ans' to use the saved value or 'quit' to exit): ")
        if count.lower() == 'quit':
            break  # Exit the loop if the user types "quit"

        if count.lower() == 'ans':
            print(f"Current calculus: {ans}")
            continue

        # Include all calculations and related code within the try block
        try:
            # Split the input into operands and operator
            num1, operator, num2 = count.split()

            # Convert operands to float
            num1 = float(num1)
            num2 = float(num2)

            # Perform the corresponding operation based on the operator
            if operator == "+":
                ans = num1 + num2
            elif operator == "-":
                ans = num1 - num2
            elif operator == "/":
                if num2 == 0:
                    ans = "Cannot divide by zero"
                else:
                    ans = num1 / num2
            elif operator == "*":
                ans = num1 * num2
            elif operator == "^":
                ans = num1 ** num2
            else:
                raise ValueError("Invalid operator")

            # Print the result
            print(f"The answer is: {ans}")

        except ValueError:
            print("Invalid input. Please enter a valid calculation \n(e.g., '5 + 3') or type 'ans' to see the saved value.")
        except Exception as e:
            print("An error occurred:", e)
            
# Call the function to start the calculator
CalcMethod()

'''Förslag:
for-loop för kalkulationerna
repetera den där split-skiten x4 för varje metod? venne varför..
switch statement kanske!
eller så gör du bara dem till 1 metod/1 kalkyl och kallar på respektive senare i ett statement av något slags senare. idéer.'''
# Split kan bara ta emot ETT statement. ej flera. vad nördigt!


