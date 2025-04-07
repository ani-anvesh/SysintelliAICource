from typing import Dict

def word_count(sentence: str) -> Dict[str, int]:
    word_freq = {}
    
    sentence = sentence.lower()
    
    words = sentence.split()
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
            
    return word_freq

print(word_count("AI is the future and ai is powerful"))
print(word_count("Hello hello HELLO"))