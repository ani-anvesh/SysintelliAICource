from typing import List

def extract_digits(s: str) -> List[int]:
    digits = []
    for char in s:
        if '0' <= char <= '9':
            digits.append(int(char))
    return digits


input_string = input("Enter a string: ")

print(f"Digits : {extract_digits(input_string)}")