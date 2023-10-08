import sys
import string

traductor = str.maketrans('', '', string.punctuation)

output_lines = []

for filename in sys.stdin:
    with open(filename.strip(), encoding='utf-8', errors='ignore') as file:
        for line in file:
            line = line.strip()
            words = line.split()
            for word in words:
                cleaned_word = word.translate(traductor).lower()
                if cleaned_word:
                    output_lines.append(f"{cleaned_word}\t1".encode('utf-8', errors='ignore').decode('utf-8', errors='ignore'))

# Imprimir los resultados por línea
for line in output_lines:
    try:
        print(line)
    except UnicodeEncodeError:
        pass
