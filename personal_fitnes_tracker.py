# Personal Fitness Tracker System 🏋️‍♂️
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
    workouts.append((workout_type, duration))
    return "Log completed!"

def log_calorie_intake(calories_consumed):
    """
    Log calorie intake for a meal.
    - Append the calorie amount to the calories list.
    - Print a confirmation message.
    """
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
    Longer type of view progress solution below as comments
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


def set_daily_goals(workout_minutes, calorie_limit):
    """
    Set daily goals for workout time and calorie intake.
    - Update the global variables workout_goal and calorie_goal.
    - Print a confirmation message.
    """
    pass


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


if __name__ == "__main__":
    main()