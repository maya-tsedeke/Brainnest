"""import os

file_path = "mbox-short.txt"
if not os.path.isfile(file_path):
    print("File not found.")
else:
    with open(file_path) as f:
        lines = f.readlines()

    num_lines = len(lines)
    print('Total number of lines:', num_lines)

    email_counts = {}
    for line in lines:
        if line.startswith('From '):
            email = line.split()[1]
            domain = email.split('@')[1]
            if email not in email_counts:
                email_counts[email] = 1
            else:
                email_counts[email] += 1

            if domain not in email_counts:
                email_counts[domain] = 1
            else:
                email_counts[domain] += 1

    if email_counts:
        max_email = max(email_counts, key=email_counts.get)
        print("Email address with the most occurrences:", max_email)
        print("Number of occurrences:", email_counts[max_email])
        print("Frequency of other domains:", email_counts)
    else:
        print("No email addresses found in the file.")"""
#Answer from Brainnest developer team
d = dict()
fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    words = line.split()
    if len(words) < 3 or words[0] != 'From': continue
    else:
        if words[1] not in d:
            d[words[1]] = 1
        else:
            d[words[1]] += 1

print(d)

max_value = max(d.values())
key = max(d, key=d.get)
print(key + ': ' + str(max_value))