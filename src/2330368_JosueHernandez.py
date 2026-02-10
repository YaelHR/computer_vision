#Manejo de Listas, Tuplas y Diccionarios en Python



# Problem 1: Shopping list basics (list operations)

# Description:
# Works with a shopping list using list operations such as
# append, search and length calculation.

# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)

# Outputs:
# - Items list
# - Total items
# - Found item

# Validations:
# - initial_items_text not empty
# - new_item and search_item not empty

# Test cases:
# 1) Normal: "apple:2,banana:5", new_item="orange", search_item="apple"
# 2) Edge case: "milk:1", new_item="bread", search_item="bread"
# 3) Error: "" (empty text)


initial_items_text = "apple:2,banana:5,orange:3"
new_item = "grapes"
search_item = "banana"

initial_items_text = initial_items_text.strip()

if initial_items_text != "" and new_item.strip() != "" and search_item.strip() != "":
    items_list = []

    parts = initial_items_text.split(",")
    for item in parts:
        product = item.split(":")[0].strip().lower()
        items_list.append(product)

    new_item = new_item.strip().lower()
    items_list.append(new_item)

    search_item = search_item.strip().lower()
    found_item = search_item in items_list

    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", found_item)
else:
    print("Error: invalid input")


# Problem 2: Points and distances with tuples

# Description:
# Uses tuples to represent points and calculates distance
# and midpoint between them.

# Inputs:
# - x1, y1, x2, y2 (float)

# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint

# Validations:
# - All values convertible to float

# Test cases:
# 1) Normal: (0,0) and (3,4)
# 2) Edge case: same points
# 3) Error: non-numeric input

try:
    x1, y1 = 0, 0
    x2, y2 = 3, 4

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: invalid input")



# Problem 3: Product catalog with dictionary

# Description:
# Manages a product catalog using a dictionary and calculates
# total price based on quantity.

# Inputs:
# - product_name (string)
# - quantity (int)

# Outputs:
# - Unit price
# - Quantity
# - Total

# Validations:
# - product exists
# - quantity > 0

# Test cases:
# 1) Normal: apple, quantity=3
# 2) Edge case: banana, quantity=1
# 3) Error: product not found


product_prices = {
    "apple": 10.0,
    "banana": 8.5,
    "orange": 12.0
}

product_name = "apple"
quantity = 3

product_name = product_name.strip().lower()

if product_name != "" and isinstance(quantity, int) and quantity > 0:
    if product_name in product_prices:
        unit_price = product_prices[product_name]
        total_price = unit_price * quantity

        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")
else:
    print("Error: invalid input")



# Problem 4: Student grades with dict and list

# Description:
# Calculates the average grade of a student and determines
# if the student passed.

# Inputs:
# - student_name (string)

# Outputs:
# - Grades
# - Average
# - Passed

# Validations:
# - student exists
# - grades list not empty

# Test cases:
# 1) Normal: Alice
# 2) Edge case: Bob
# 3) Error: student not found


student_grades = {
    "alice": [90, 85, 88],
    "bob": [70, 72],
    "carol": [60, 65, 58]
}

student_name = "Alice"
student_name = student_name.strip().lower()

if student_name != "":
    if student_name in student_grades:
        grades_list = student_grades[student_name]

        if len(grades_list) > 0:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= 70.0

            print("Grades:", grades_list)
            print("Average:", average)
            print("Passed:", is_passed)
        else:
            print("Error: invalid input")
    else:
        print("Error: student not found")
else:
    print("Error: invalid input")



# Problem 5: Word frequency counter

# Description:
# Counts word frequency in a sentence using list and dictionary.

# Inputs:
# - sentence (string)

# Outputs:
# - Words list
# - Frequencies
# - Most common word

# Validations:
# - sentence not empty

# Test cases:
# 1) Normal: "Hello world hello"
# 2) Edge case: single word
# 3) Error: empty string


sentence = "Hello, world! Hello Python world."
sentence = sentence.strip().lower()

for char in ".,!?;:":
    sentence = sentence.replace(char, "")

if sentence != "":
    words_list = sentence.split()
    freq_dict = {}

    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common_word = ""
    max_count = 0

    for word, count in freq_dict.items():
        if count > max_count:
            max_count = count
            most_common_word = word

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common_word)
else:
    print("Error: invalid input")



# Problem 6: Simple address book (dictionary CRUD)

# Description:
# Implements a simple address book with add, search and delete
# operations using a dictionary.

# Inputs:
# - action_text
# - name
# - phone (for ADD)

# Outputs:
# - Messages based on operation

# Validations:
# - valid action
# - name not empty


contacts = {
    "alice": "1234567890",
    "bob": "5551234567"
}

action_text = "ADD"
name = "Carol"
phone = "9998887777"

action_text = action_text.strip().upper()
name = name.strip().lower()

if action_text in ["ADD", "SEARCH", "DELETE"] and name != "":
    if action_text == "ADD":
        if phone.strip() != "":
            contacts[name] = phone
            print("Contact saved:", name, phone)
        else:
            print("Error: invalid input")

    elif action_text == "SEARCH":
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Error: contact not found")

    elif action_text == "DELETE":
        if name in contacts:
            contacts.pop(name)
            print("Contact deleted:", name)
        else:
            print("Error: contact not found")
else:
    print("Error: invalid input")
