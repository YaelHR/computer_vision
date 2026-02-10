#Manejo de bucles en Python



# Problem 1: Sum of integers in a range

# Description:
# Calculates the sum of integers from 1 to n and the sum
# of even numbers in the same range using a for loop.

# Inputs:
# - n (int)

# Outputs:
# - Sum 1..n
# - Even sum 1..n

# Validations:
# - n must be integer
# - n >= 1

# Test cases:
# 1) Normal: n = 10
# 2) Edge case: n = 1
# 3) Error: n = -5


n = 10

try:
    n = int(n)
    if n >= 1:
        total_sum = 0
        even_sum = 0

        for i in range(1, n + 1):
            total_sum += i
            if i % 2 == 0:
                even_sum += i

        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")



# Problem 2: Multiplication table with for

# Description:
# Displays the multiplication table of a number
# from 1 to m using a for loop.

# Inputs:
# - base (int)
# - m (int)

# Outputs:
# - Multiplication table lines

# Validations:
# - base and m must be integers
# - m >= 1

# Test cases:
# 1) Normal: base=5, m=4
# 2) Edge case: base=3, m=1
# 3) Error: m=0


base = 5
m = 4

try:
    base = int(base)
    m = int(m)

    if m >= 1:
        for i in range(1, m + 1):
            print(f"{base} x {i} = {base * i}")
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")



# Problem 3: Average of numbers with while and sentinel

# Description:
# Reads numbers until a sentinel value is entered
# and calculates the average of valid numbers.

# Inputs:
# - number (float, repeated)

# Outputs:
# - Count
# - Average

# Validations:
# - Only numbers >= 0 are accepted
# - Sentinel is ignored

# Test cases:
# 1) Normal: 10, 20, 30, -1
# 2) Edge case: -1
# 3) Error: "abc"

SENTINEL_VALUE = -1
count = 0
total = 0.0

print("Enter numbers (-1 to finish):")

while True:
    user_input = input()

    try:
        number = float(user_input)

        if number == SENTINEL_VALUE:
            break
        elif number < 0:
            print("Error: invalid input")
        else:
            total += number
            count += 1
    except ValueError:
        print("Error: invalid input")

if count > 0:
    average = total / count
    print("Count:", count)
    print("Average:", average)
else:
    print("Error: no data")



# Problem 4: Password attempts with while

# Description:
# Simulates a password login system with limited attempts.

# Inputs:
# - user_password (string)

# Outputs:
# - Login success
# - Account locked

# Validations:
# - MAX_ATTEMPTS > 0

# Test cases:
# 1) Normal: correct password on first try
# 2) Edge case: correct on last attempt
# 3) Error: all attempts wrong


CORRECT_PASSWORD = "admin123"
MAX_ATTEMPTS = 3

attempts = 0
login_success = False

while attempts < MAX_ATTEMPTS:
    user_password = input("Enter password: ")

    if user_password == CORRECT_PASSWORD:
        print("Login success")
        login_success = True
        break
    else:
        attempts += 1

if not login_success:
    print("Account locked")



# Problem 5: Simple menu with while

# Description:
# Displays a menu that repeats until the user exits.

# Inputs:
# - option (int)

# Outputs:
# - Messages based on option

# Validations:
# - option must be 0,1,2,3

# Test cases:
# 1) Normal: 1, 3, 0
# 2) Edge case: 2
# 3) Error: 5, "abc"


counter = 0
option = -1

while option != 0:
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    user_input = input("Select option: ")

    try:
        option = int(user_input)

        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
        else:
            print("Error: invalid option")
    except ValueError:
        print("Error: invalid option")



# Problem 6: Pattern printing with nested loops

# Description:
# Prints a right triangle pattern using nested for loops.

# Inputs:
# - n (int)

# Outputs:
# - Star pattern

# Validations:
# - n >= 1

# Test cases:
# 1) Normal: n = 4
# 2) Edge case: n = 1
# 3) Error: n = 0


n = 4

try:
    n = int(n)

    if n >= 1:
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
    else:
        print("Error: invalid input")
except ValueError:
    print("Error: invalid input")
