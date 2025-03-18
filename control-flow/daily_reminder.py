############################################################################

task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ").lower().strip()
time_bound =input("Is it time_bound (yes/no): ").lower().strip()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"'{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"'{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"'{task}' is a medium priority task. Schedule it for today if possible.")
        else:
            print(f"'{task}' is a medium priority task. Complete it when you have some time.")
    case "low":
        if time_bound == "yes":
            print(f"'{task}' is a low priority task but needs to be done today.")
        else:
            print(f"'{task}' Consider completing it when you have free time.")
    case _:
        print("Please enter a valid priority (high, medium, low).")

############################################################################