text = "i love python programming"

words = text.split()

result = []

for word in words:
    if 'a' <= word[0] <= 'z':
        capitalize_chr = chr(ord(word[0]) - 32) + word[1:]
        result.append(capitalize_chr)
    else:
        result.append(word)

print(' '.join(result))

    