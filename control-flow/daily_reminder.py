# daily_reminder.py

# Prompt the user for task details with exact expected prompts
task = input("Enter your task:")
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound? (yes/no):").strip().lower()

# Use match-case to handle priority-specific messaging
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task - please address this as soon as possible that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task - please address this as soon as possible")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task - plan to complete this soon that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task - plan to complete this soon")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task - complete it when you have free time that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task - complete it when you have free time")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level")

