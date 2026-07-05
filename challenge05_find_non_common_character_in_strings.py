text1 = "apple"
text2 = "grape"

# Find all characters that are not common in both strings
# Expected: ['l', 'g', 'r']

result = []

for ch in text1:
    if ch not in text2 and ch not in result:
        result.append(ch)

for ch in text2:
    if ch not in text1 and ch not in result:
        result.append(ch)

print(result)