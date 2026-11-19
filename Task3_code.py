#!/usr/bin/env python
import sys

current_word = None
current_count = 0
word = None

word_counts = []

for line in sys.stdin:
    line = line.strip()
    try:
        word, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_word == word:
        current_count += count
    else:
        if current_word:
            word_counts.append((current_word, current_count))
        current_count = count
        current_word = word

if current_word == word:
    word_counts.append((current_word, current_count))

word_counts.sort(key=lambda x: x[1], reverse=True)

for w, c in word_counts[:3]:
    print('%s\t%s' % (w, c))