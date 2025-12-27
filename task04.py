text = input('input: ')
emails = text.split(',')

domains = []
for email in emails:
    ind = email.find('@')
    if ind != -1:
        domain = email[idx:]
        domains.append(domain)

print(domains)
