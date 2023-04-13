import os

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
            if email not in email_counts:
                email_counts[email] = 1
            else:
                email_counts[email] += 1

    if email_counts:
        max_email = max(email_counts, key=email_counts.get)
        max_count = email_counts[max_email]
        print("Email address with the most occurrences:", max_email)
        print("Number of occurrences:", max_count)

        print("Email addresses and their occurrences:")
        for email, count in email_counts.items():
            print(email, count)
    else:
        print("No email addresses found in the file.")
