import sys
import string

def is_valid_word(word):
    # Revizar el encoding de cada palabra
    return all(ord(char) < 128 for char in word)

word_counts = {}

for line in sys.stdin:
    word, count = line.strip().split('\t', 1)
    count = int(count)

    # revisar la válidez de las palabras
    if is_valid_word(word):
        if word in word_counts:
            word_counts[word] += count
        else:
            word_counts[word] = count

for word, count in word_counts.items():
    print(f"{word}\t{count}")