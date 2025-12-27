text = input()

result = text.lower().replace(", ", "_").replace(" ", "_")

print(result)