task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case priority if time_bound =="yes":
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    case priority if time_bound == "no":
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Kindly input your respones from the options provided")