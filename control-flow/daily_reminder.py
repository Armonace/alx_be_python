# Prompt the user for task details
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes or no): ").strip().lower()

# Base reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Use match-case to handle priority-specific messaging
match priority:
    case "high":
        reminder += " - please address this as soon as possible"
    case "medium":
        reminder += " - plan to complete this soon"
    case "low":
        reminder += " - complete it when you have free time"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Check if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Display the customized reminder
print(reminder)