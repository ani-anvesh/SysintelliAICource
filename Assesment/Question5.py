from typing import List, Any

def flatten_once(nested: List[Any]) -> List[Any]:
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


print(flatten_once([1, 12, 31, 4, [5, 6]]))
print(flatten_once([1, [2, 31, 4, [5, 6]]]))
print(flatten_once([[1, 21, [3], [4, 5]]]))