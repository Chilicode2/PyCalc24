print(" _____________________")
print("|  _________________  |")
print("| |CALCULATOR 10000 | |")
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
    ans = 0  # Initialize ans to store the result of the calculation

    while True:
        count = input("What's the calculus? (Type 'ans' \nto use the saved value or 'quit' to exit): ")

        if count.lower() == 'quit':
            break  # Exit the loop if the user types 'quit'

        if count.lower() == 'ans':
            print("Current value of 'ans':", ans)
            continue

        try:
            split_index = count.index("+", "-", "/", "*")
            operand1 = int(count[:split_index])
            operand2 = int(count[split_index + 1:])
            ans = operand1 + operand2  # Calculate the result and store it in ans
            print("Result:", ans)
            
        except ValueError:
            print("Invalid input. Please enter a valid calculation \n(e.g., '5+3') or type 'ans' to see the saved value.")
        except Exception as e:
            print("An error occurred:", e)

        '''Förslag:
for-loop för kalkulationerna
repetera den där split-skiten x4 för varje metod? venne varför..
switch statement kanske!
eller så gör du bara dem till 1 metod/1 kalkyl och kallar på respektive senare i ett statement av något slags senare. idéer.'''
# Split kan bara ta emot ETT statement. ej flera. vad nördigt!

# Call the function to start the calculator
CalcMethod()

