############## 1. Class Marks Report #############

marks = [78, 45, 92, 33, 67, 88, 51, 29]

print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print("Class average:", sum(marks) / len(marks))

passed = 0
for m in marks:
    if m >= 35:
        passed += 1
print("Students passed:", passed)


############## 2. Grocery Shopping List #############

shopping_list = []

while True:
    item = input("Enter item: ")
    if item == "done":
        break
    if item in shopping_list:
        print("Already added")
    else:
        shopping_list.append(item)

for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")
print("Total items:", len(shopping_list))


############## 3. Username Validator #############

username = input("Enter username: ")

if len(username) < 5 or len(username) > 12:
    print("Invalid: Username must be between 5 and 12 characters")
elif " " in username:
    print("Invalid: Username cannot contain spaces")
elif username[0].isdigit():
    print("Invalid: Username cannot start with a digit")
else:
    print("Valid username")


############## 4. Vowel Counter for a Tweet #############

sentence = input("Enter a sentence: ")

vowels = 0
consonants = 0
spaces = 0

for ch in sentence.lower():
    if ch in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)


############## 5. Palindrome Name Checker #############

name = input("Enter your name: ")

if name.lower() == name.lower()[::-1]:
    print("Bonus! Your name is a palindrome.")
else:
    print("Sorry, your name is not a palindrome.")


############## 6. Temperature Tracker #############

temps = [32, 35, 38, 41, 36, 29, 40]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("Heat alert days:")
for i in range(len(temps)):
    if temps[i] > 37:
        print(days[i], "-", temps[i])

hottest = max(temps)
print("Hottest day:", days[temps.index(hottest)], "-", hottest)

fahrenheit = []
for t in temps:
    fahrenheit.append(round(t * 9 / 5 + 32, 1))
print("Temperatures in Fahrenheit:", fahrenheit)


############## 7. Word Frequency in a Sentence #############

sentence = input("Enter a sentence: ")
words = sentence.split()

longest = words[0]
shortest = words[0]
capital_count = 0

for word in words:
    if len(word) > len(longest):
        longest = word
    if len(word) < len(shortest):
        shortest = word
    if word[0].isupper():
        capital_count += 1

print("Longest word:", longest)
print("Shortest word:", shortest)
print("Words starting with capital letter:", capital_count)


############## 8. Remove Negative Balances #############

balances = [1500, -200, 3000, -50, 0, 750, -1000]

positive_accounts = []
negative_accounts = []

for b in balances:
    if b > 0:
        positive_accounts.append(b)
    elif b < 0:
        negative_accounts.append(b)

print("Positive accounts:", positive_accounts)
print("Negative accounts:", negative_accounts)
print("Total amount owed:", abs(sum(negative_accounts)))


############## 9. Password Strength Checker #############

password = input("Enter password: ")

has_upper = False
has_lower = False
has_digit = False

for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True

conditions = 0
if has_upper:
    conditions += 1
if has_lower:
    conditions += 1
if has_digit:
    conditions += 1
if len(password) >= 8:
    conditions += 1

if conditions == 4:
    print("Strong")
elif conditions >= 2:
    print("Medium")
else:
    print("Weak")


############## 10. Simple Name Initials Generator #############

full_name = input("Enter full name: ")
parts = full_name.split()

initials = ""
for p in parts:
    initials += p[0].upper() + "."
print("Initials:", initials)

title_words = []
for p in parts:
    title_words.append(p[0].upper() + p[1:].lower())
print("Title case:", " ".join(title_words))

short_name = ""
for p in parts[:-1]:
    short_name += p[0].upper() + ". "
short_name += title_words[-1]
print("Short name:", short_name)
