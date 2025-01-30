# Personal Fitness Tracker System 🏋️‍♂️

# importing libraries for the GUI
import tkinter as tk
from tkinter import messagebox

# importing libs for the main function logic
from functools import total_ordering


# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals
progres = [] # To store the whole duration of all workouts

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout(workout_type, duration):
    """
    Log a workout.
    - Append the workout type and duration to the workouts list.
    - Print a confirmation message.
    """
    #for the GUI comments
    # workout_type = workout_entry.get()
    # duration = duration_entry.get()
    workouts.append((workout_type, duration))
    return "Log completed!"

def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
    # for the GUI comments
    # calories_consumed = calories_entry.get()
    calories.append(calories_consumed)
    return "Log Completed!"

def view_progress():
    """
    Display a summary of the user's progress for the day.
    - Calculate the total workout time and total calories.
    - Print motivational feedback.
    """
    total_time = sum(duration for _, duration in workouts)
    total_calories_burned = sum(calories)

    """
    Longer type of view progress solution below as a comment
    _______________________________________________________
    # total_time = 0
    # durations = []
    # for workout_type, duration in workouts:
    #     durations.append(duration)
    #     total_time = sum(durations)
    # total_calories_burned = sum(calories)
    ________________________________________________________
    """


    if total_time <= 30:
        return f"Keep going! You need to be more active {total_time} minutes, {total_calories_burned} calories burned"

    elif total_time <= 60:
        return f"Great Job, Yoe are keeping up the good progress {total_time} minutes, {total_calories_burned} calories burned"

    else:
        return f"Amazing effort! You are on fire today! {total_time} minutes, {total_calories_burned} calories burned"




def reset_progress():
    """
    Clear all data from the workouts and calories lists.
    - Print a confirmation message.
    """
    workouts.clear()
    calories.clear()

    return "Workout Log and Calories Log are empty!"

# TODO: create a daily gaol entry!
def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass

# TODO: compare progress with daily goals and create encouragement messages!
def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """
    pass


def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Prompt for workout type and duration
            print(log_workout(workout_type=input("Enter your workout type: "), duration=int(input("Enter duration time: "))))
        elif choice == '2':
            # Prompt for calories consumed
            print(log_calorie_intake(calories_consumed=float(input("Enter Calories consumption: "))))
        elif choice == '3':
            # Call view_progress function
            print(view_progress())
        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            pass
        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


#TODO: Create a GUI for the tracker!

# root = tk.Tk()
# root.title("Fitness Tracker")
#
# # Workout input fields
# tk.Label(root, text="Workout Type:").grid(row=0, column=0)
# workout_entry = tk.Entry(root)
# workout_entry.grid(row=0, column=1)
#
# tk.Label(root, text="Duration (min):").grid(row=1, column=0)
# duration_entry = tk.Entry(root)
# duration_entry.grid(row=1, column=1)
#
# tk.Button(root, text="Log Workout", command=log_workout(workout_type=input(), duration=int(input()))).grid(row=2, column=0, columnspan=2)
#
# # Calorie input field
# tk.Label(root, text="Calories Consumed:").grid(row=3, column=0)
# calories_entry = tk.Entry(root)
# calories_entry.grid(row=3, column=1)
#
# tk.Button(root, text="Log Calories", command=log_calorie_intake).grid(row=4, column=0, columnspan=2)
#
# # Listbox to display workouts
# tk.Label(root, text="Workout History:").grid(row=5, column=0)
# workout_listbox = tk.Listbox(root, height=5, width=30)
# workout_listbox.grid(row=6, column=0, columnspan=2)
#
# # View progress button
# tk.Button(root, text="View Progress", command=view_progress).grid(row=7, column=0, columnspan=2)
#
# # Run the Tkinter event loop
# root.mainloop()


if __name__ == "__main__":
    main()


