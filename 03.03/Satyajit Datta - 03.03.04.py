score = int(input("Enter a score: "))

team_name = input("Enter the team name: ")

greeting = ""
if team_name == 'Eagles':
    greeting = "Welcome Eagles,"
elif team_name == 'Pandas':
    greeting = "Hi Pandas,"
else:
    greeting = "Go Cobras,"


message = "you are stars!"

if score < 31:
    message = "great effort!"
elif score < 61:
    message = "solid effort!"
elif score < 96:
    message = "good work!"

print(greeting, "and", message)