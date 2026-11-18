# Activity 1: Student Information Formatter (Version 2)

# 1. Get inputs and remove extra leading/trailing spaces using .strip()
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
section = input("Enter section: ").strip()
favorite_subject = input("Enter favorite subject: ").strip()

# 2. Combine first and last name, and remove extra internal spaces if any
clean_first = " ".join(first_name.split())
clean_last = " ".join(last_name.split())
full_name = f"{clean_first} {clean_last}"

# 3. Apply string manipulation methods
proper_name = full_name.title()
upper_name = full_name.upper()
upper_section = section.upper()
proper_subject = " ".join(favorite_subject.split()).title()
char_count = len(proper_name)

# 4. Display formatted output
print("\nFormatted Output:")
print(f"Name: {proper_name}")
print(f"Name Code: {upper_name}")
print(f"Section: {upper_section}")
print(f"Favorite Subject: {proper_subject}")
print(f"Character Count: {char_count}")