text = "I love Python"

result = ""

for ch in text:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch

print(result)