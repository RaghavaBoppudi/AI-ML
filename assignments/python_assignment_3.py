############## 1. Phone Contact Book #############

contacts = {}

while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name in contacts:
            print("Contact already exists")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print("Contact added")
    elif choice == "2":
        name = input("Enter name to search: ")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found")
    elif choice == "3":
        if len(contacts) == 0:
            print("No contacts saved")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")


############## 2. Unique Visitors on a Website #############

visits = [101, 205, 101, 330, 205, 412, 101, 330, 509]

unique_visitors = set(visits)

print("Total visits:", len(visits))
print("Unique visitors:", len(unique_visitors))
print("Unique visitor IDs:", sorted(unique_visitors))


############## 3. Student Marks Dictionary #############

marks = {"Aman": 82, "Priya": 91, "Rahul": 45,
         "Sneha": 67, "Kiran": 30}

for name, mark in marks.items():
    if mark >= 40:
        print(name, "- Pass")
    else:
        print(name, "- Fail")

topper = ""
top_marks = 0
for name, mark in marks.items():
    if mark > top_marks:
        topper = name
        top_marks = mark
print("Topper:", topper, "with", top_marks, "marks")

passed_students = {}
for name, mark in marks.items():
    if mark >= 40:
        passed_students[name] = mark
print("Passed students:", passed_students)


############## 4. Common Friends #############

riya_friends = {"Aman", "Neha", "Karan", "Sita", "Vikram"}
arjun_friends = {"Neha", "Vikram", "Pooja", "Aman", "Rohan"}

print("Mutual friends:", riya_friends & arjun_friends)
print("Only Riya's friends:", riya_friends - arjun_friends)
print("All people:", riya_friends | arjun_friends)
print("Friend suggestions for Riya:", arjun_friends - riya_friends)


############## 5. Character Counter #############

text = input("Enter text: ")

char_count = {}
for ch in text:
    if ch != " ":
        char_count[ch] = char_count.get(ch, 0) + 1

print(char_count)

most_char = ""
most_count = 0
for ch, count in char_count.items():
    if count > most_count:
        most_char = ch
        most_count = count

print(f"Most frequent character: {most_char} ({most_count} times)")


############## 6. Restaurant Menu Billing #############

menu = {"dosa": 60, "idli": 40, "vada": 30,
        "coffee": 25, "tea": 15}

total = 0

while True:
    item = input("Enter item: ").lower()
    if item == "bill":
        break
    if item in menu:
        total += menu[item]
        print(item, "added")
    else:
        print("Item not available")

print("Total bill: Rs.", total)
if total > 200:
    discount = total * 0.10
    print("Discount (10%): Rs.", discount)
    print("Amount to pay: Rs.", total - discount)


############## 7. City Coordinates (Tuples) #############

cities = [("Hyderabad", 17.38, 78.48),
          ("Mumbai", 19.07, 72.87),
          ("Chennai", 13.08, 80.27),
          ("Delhi", 28.61, 77.20)]

for city, lat, lon in cities:
    print(f"{city}: Latitude {lat}, Longitude {lon}")

north_city = ""
max_lat = -90
for city, lat, lon in cities:
    if lat > max_lat:
        north_city = city
        max_lat = lat
print("Farthest north:", north_city, "-", max_lat)

# cities[1][1] = 20.00
# TypeError: 'tuple' object does not support item assignment
# Tuples are immutable, so their values cannot be changed after they are created.


############## 8. Library Book Tracker #############

books = {"Python Basics": 3, "Data Science 101": 0,
         "Machine Learning": 2, "SQL Guide": 1}

book = input("Enter book name to borrow: ")

if book not in books:
    print("Book not found")
elif books[book] == 0:
    print("Currently unavailable")
else:
    books[book] -= 1
    print("Book issued successfully")

print(books)


############## 9. Group Employees by Department #############

employees = [("Ravi", "IT"), ("Anjali", "HR"),
             ("Suresh", "IT"), ("Meena", "Finance"),
             ("Arun", "HR"), ("Divya", "IT")]

departments = {}
for name, dept in employees:
    if dept not in departments:
        departments[dept] = []
    departments[dept].append(name)

print(departments)

for dept, names in departments.items():
    print(dept, ":", len(names), "employees")


############## 10. Quiz Answer Checker #############

answer_key = ("B", "C", "A", "D", "B")

wrong_questions = set()
score = 0

for i in range(len(answer_key)):
    answer = input(f"Enter answer for Question {i + 1}: ").upper()
    if answer == answer_key[i]:
        print(f"Question {i + 1}: Correct")
        score += 1
    else:
        print(f"Question {i + 1}: Wrong")
        wrong_questions.add(i + 1)

print("Wrong questions:", wrong_questions)
print("Score:", score, "/ 5")

if score == 5:
    print("Excellent")
elif score >= 3:
    print("Good")
else:
    print("Needs improvement")
