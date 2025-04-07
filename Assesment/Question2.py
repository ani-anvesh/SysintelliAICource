def sum_even_numbers(n: int) -> int:
    if n < 2: return 0
    sum = 0
    for i in range(2, n + 1, 2):
        sum += i
    return sum

n = int(input("number: "))

print(f"Sum of even numbers: {sum_even_numbers(n)}")