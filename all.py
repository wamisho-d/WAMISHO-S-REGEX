# Question 1 Task 1:Email Extraction Enhancement.
import re
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print(emails)

pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com\b)[A-Za-z0-9.-]+\.[A_Z|a-z]{2,}\b"
emails = re.findall(pattern, text)
print(emails)