def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")

print(f"Number of vowels: {count_vowels(input_string)}")

def sum_even_numbers(n: int) -> int:
    if n < 2: return 0
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    return sum

n = int(input("number: "))

print(f"Sum of even numbers: {sum_even_numbers(n)}")