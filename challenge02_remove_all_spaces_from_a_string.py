text = "I love Python"

result = ""

for ch in text:
    if ch != " ":
        result += ch

print("String without spaces:",result)