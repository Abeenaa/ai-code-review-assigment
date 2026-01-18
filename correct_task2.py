import re

def count_valid_emails(emails):
    if not emails:
        return 0
    count = 0
    pattern = re.compile(r"^[^@]+@[^@]+\.[^@]+$")

    for email in emails:
        if isinstance(email, str) and pattern.match(email):
            count += 1

    return count