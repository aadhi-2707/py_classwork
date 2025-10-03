import random
import math

names_input = input("Enter the names of  guests (comma-separated): ")

names = [name.strip() for name in names_input.split(',') if name.strip()]
unique_names = list(set(names))

total_unique = len(unique_names)
print(f"Total unique names: {total_unique}")

sqrt_rounded = round(math.sqrt(total_unique))
print(f"Rounded square root of unique names: {sqrt_rounded}")

if unique_names:
    chosen_name = random.choice(unique_names)
    print(f"Selected name for the game: {chosen_name}")

    reversed_name = chosen_name[::-1]
    print(f"Reversed name: {reversed_name}")
else:
    print("No valid names entered.")