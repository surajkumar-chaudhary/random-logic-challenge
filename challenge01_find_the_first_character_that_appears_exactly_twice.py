text = "programming"

unique_char = []
first_repeated_char = None
for ch in text:
    if ch not in unique_char:
        unique_char.append(ch)
    else:
        first_repeated_char = ch
        break

print(first_repeated_char)