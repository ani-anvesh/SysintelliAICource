from typing import Dict

def sum_top_scorers(data: Dict[str, Dict[str, int]], subject: str, threshold: int) -> int:
    total_marks = 0
    for student, scores in data.items():
        if subject in scores and scores[subject] >= threshold:
            total_marks += scores[subject]
    return total_marks

data = {
    "John": {"Math": 85, "Science": 72},
    "Amy": {"Math": 45, "Science": 90},
    "Mark": {"Math": 92, "Science": 66}
}
subject = "Math"
threshold = 80
print(sum_top_scorers(data, subject, threshold))  

subject = "Science"
threshold = 75
print(sum_top_scorers(data, subject, threshold)) 