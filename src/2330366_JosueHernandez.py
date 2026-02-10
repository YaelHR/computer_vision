
#Manejo de funciones en Python
# Problem 1: Rectangle area and perimeter

# Description:
# Calculates the area and perimeter of a rectangle using functions.

# Inputs:
# - width (float)
# - height (float)

# Outputs:
# - Area
# - Perimeter

# Validations:
# - width > 0
# - height > 0

# Test cases:
# 1) Normal: width=5, height=3
# 2) Edge case: width=0.1, height=0.1
# 3) Error: width=-2, height=4


def calculate_area(width, height):
    return width * height


def calculate_perimeter(width, height):
    return 2 * (width + height)


# Main code - Problem 1
width = 5
height = 3

if width > 0 and height > 0:
    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)
    print("Area:", area)
    print("Perimeter:", perimeter)
else:
    print("Error: invalid input")



# Problem 2: Grade classifier

# Description:
# Classifies a numeric score into a letter grade.

# Inputs:
# - score (int or float)

# Outputs:
# - Score
# - Category

# Validations:
# - 0 <= score <= 100

# Test cases:
# 1) Normal: score=85
# 2) Edge case: score=100
# 3) Error: score=120


def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Main code - Problem 2
score = 85

if 0 <= score <= 100:
    grade = classify_grade(score)
    print("Score:", score)
    print("Category:", grade)
else:
    print("Error: invalid input")



# Problem 3: List statistics

# Description:
# Calculates min, max and average of a list of numbers.

# Inputs:
# - numbers_text (string)

# Outputs:
# - Min
# - Max
# - Average

# Validations:
# - text not empty
# - list not empty
# - all elements must be numbers

# Test cases:
# 1) Normal: "10,20,30"
# 2) Edge case: "5"
# 3) Error: "10,a,30"


def summarize_numbers(numbers_list):
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


# Main code - Problem 3
numbers_text = "10,20,30"
numbers_text = numbers_text.strip()

if numbers_text != "":
    parts = numbers_text.split(",")
    numbers_list = []
    valid_input = True

    for item in parts:
        try:
            numbers_list.append(float(item.strip()))
        except ValueError:
            valid_input = False
            break

    if valid_input and len(numbers_list) > 0:
        summary = summarize_numbers(numbers_list)
        print("Min:", summary["min"])
        print("Max:", summary["max"])
        print("Average:", summary["average"])
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")



# Problem 4: Apply discount list

# Description:
# Applies a discount to a list without modifying the original list.

# Inputs:
# - prices_text (string)
# - discount_rate (float)

# Outputs:
# - Original prices
# - Discounted prices

# Validations:
# - prices > 0
# - 0 <= discount_rate <= 1

# Test cases:
# 1) Normal: "100,200,300", discount=0.10
# 2) Edge case: "50", discount=0
# 3) Error: "100,-20,300", discount=1.5


def apply_discount(prices_list, discount_rate):
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted


# Main code - Problem 4
prices_text = "100,200,300"
discount_rate = 0.10
prices_text = prices_text.strip()

if prices_text != "" and 0 <= discount_rate <= 1:
    parts = prices_text.split(",")
    prices_list = []
    valid_input = True

    for item in parts:
        try:
            price = float(item.strip())
            if price <= 0:
                valid_input = False
                break
            prices_list.append(price)
        except ValueError:
            valid_input = False
            break

    if valid_input and len(prices_list) > 0:
        discounted_prices = apply_discount(prices_list, discount_rate)
        print("Original prices:", prices_list)
        print("Discounted prices:", discounted_prices)
    else:
        print("Error: invalid input")
else:
    print("Error: invalid input")



# Problem 5: Greeting function with default parameters

# Description:
# Generates a greeting using optional title.
#
# Inputs:
# - name
# - title (optional)
#
# Outputs:
# - Greeting message
#
# Validations:
# - name not empty
#
# Test cases:
# 1) Normal: "Alice", "Dr."
# 2) Edge case: "Bob", ""
# 3) Error: ""


def greet(name, title=""):
    if title != "":
        full_name = f"{title} {name}"
    else:
        full_name = name
    return f"Hello, {full_name}!"


# Main code - Problem 5
name = "Alice"
title = "Dr."

name = name.strip()
title = title.strip()

if name != "":
    greeting = greet(name, title=title)
    print("Greeting:", greeting)
else:
    print("Error: invalid input")



# Problem 6: Factorial function

# Description:
# Calculates factorial using iterative method.
#
# Inputs:
# - n (int)
#
# Outputs:
# - n
# - Factorial
#
# Validations:
# - n >= 0
# - n <= 20
#
# Test cases:
# 1) Normal: n=5
# 2) Edge case: n=0
# 3) Error: n=-3


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Main code - Problem 6
n = 5

if isinstance(n, int) and 0 <= n <= 20:
    result = factorial(n)
    print("n:", n)
    print("Factorial:", result)
else:
    print("Error: invalid input")
