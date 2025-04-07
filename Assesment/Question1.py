def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(input_string)}")
