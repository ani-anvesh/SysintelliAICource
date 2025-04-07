from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    items = list(freq_map.items())
    items.sort(key=lambda x: x[1], reverse=True)
    top_k = []
    for i in range(k):
        if i < len(items):
            top_k.append(items[i][0])

    return top_k

nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
k = int(input("Enter value of k: "))
print(f"Top k frequent elements: {top_k_frequent(nums, k)}")