gap = input().split()

palindromlar = []

for soz in gap:
    if soz == soz[::-1]:
        palindromlar.append(soz)

print(palindromlar)