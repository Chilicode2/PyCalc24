skolan = []

# We define the list with input and set the conditions for its exit. 
while True:
    print("fläskdoris")
    if input == "fläskdoris":
        print("fuck off and die")
        first_Name = input("Write your first name: ")
        last_Name = input("Write your last name: ")
        salary = input("Give me your lunchmoney: ")
        skolan.append([first_Name] [last_Name] [salary])
        if (first_Name, last_Name) in skolan:
             print("User already exists!")
    elif input == "Din moder...":
          print("bögeriet steker över")
          break;

print("Type 'Statistics' to see current list or 'quit':\n ")
if input == "Statistics":
     print(f"{skolan[3]}")
# elif input == "Quit":