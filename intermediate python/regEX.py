import re

text = "Hello, my number is 9841234567 and my friend's number is 9811111111."

pattern = r'\d{10}'  # find any 10 digits

matches = re.findall(pattern, text)
print(matches)



#searching in text
text = "The rain in Spain"

match = re.search(r"rain", text)
if match:
    print("Found:", match.group())



#email validation
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email = "user@example.com"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


#replace text
text = "Hello 123, this is 456."
new_text = re.sub(r'\d+', '###', text)
print(new_text)
