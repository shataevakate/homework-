import pandas as pd
import string

def length_stats(text):
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    words = cleaned_text.split()
    word_lengths = [len(word) for word in words]
    length_series = pd.Series(word_lengths, index=words)
    
    return length_series

print(length_stats('Мама мыла раму'), end='\n\n')
print(length_stats('Лес, опушка, странный домик. Лес, опушка и зверушка.'))
