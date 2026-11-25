
# Problem No. 3 - Unit 3 (File Handling / Regular Expressions)
#
# Develop a Python program using regex to identify and extract
# valid Indian mobile phone numbers from a text document.
#
# --------------------------------------------------

import re

# Read text from file
file = open("input.txt", "r")
text = file.read()
file.close()

# Regular expression to identify valid Indian mobile numbers
pattern = r'(?<!\d)(?:\+91[-\s]?)?[6-9]\d{9}(?!\d)'

# Extract mobile numbers
numbers = re.findall(pattern, text)

# Display extracted numbers
print("Valid Indian Mobile Phone Numbers:")

if numbers:
    for number in numbers:
        print(number)
else:
    print("No valid mobile numbers found.")
