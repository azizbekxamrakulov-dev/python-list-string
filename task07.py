text = input('input:') 

pairs = text.split(',')

for pair in pairs:
    seperatted_pair = pair.split(':')
    result = f"{seperatted_pair[0]}: {seperatted_pair[1]}"
print(result)