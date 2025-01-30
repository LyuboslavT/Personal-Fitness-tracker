# Personal Fitness Tracker System 🏋️‍♂️

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
    total_calories_taken = sum(calories)

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


    return total_time, total_calories_taken




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
    global workout_goal, calorie_goal

    workout_goal = workout_minutes
    calorie_goal = calorie_limit

    return workout_goal, calorie_goal


def encouragement_system():
    """
    Provide motivational feedback based on progress and goals.
    - Compare current totals to the daily goals.
    - Print encouragement messages.
    """

    global  workout_goal, calorie_goal

    total_time, total_calories_taken = view_progress()

    if total_time < workout_goal:
        return f"Keep going! You need to be more active\nYour GOAL is {workout_goal}, You need to push {workout_goal - total_time} minutes more!"

    elif total_time <= 30 and total_calories_taken > 1500:
        return f"Poor performance {total_time} minutes, Your Goal is {workout_goal}.\nYou eat a lot with {total_calories_taken}.\n Get you lazy ass up and go to the gym.\nYou need to stay active for at least {workout_goal} minutes."

    elif total_calories_taken < calorie_goal:
        return f'You need to eat more on a daily base. Your GOAL is {calorie_goal}.\nYou need {calorie_goal - total_calories_taken} calories more, to have energy for your workout'

    elif total_time >= workout_goal:
        return "Amazing You have reached your daily workout GOAL!"

    elif total_calories_taken == calorie_goal:
        return "Amazing You have reached your daily calories intake GOAL!"

    elif total_time >= workout_goal and total_calories_taken == calorie_goal:
        return "Amazing You have reached all of your GOALS!"

    elif total_calories_taken > calorie_goal:
        return "You are FAT. Keep your goals fulfilled!"

    elif total_time > workout_goal:
        return "Amazing You have overfilled your daily workout GOAL!"




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
            print(log_calorie_intake(calories_consumed=int(input("Enter Calories consumption: "))))
        elif choice == '3':
            # Call view_progress function
            print(view_progress())
            print(encouragement_system())
        elif choice == '4':
            # Call reset_progress function
            reset_progress()

        elif choice == '5':
            # Prompt for daily goals
            set_workout_minutes = int(input("Enter daily workout target in minutes: "))
            set_calories_limit = int(input('Enter daily calories intake limit: '))
            print(set_daily_goals(set_workout_minutes, set_calories_limit))
            print("Goals set successfully!")

        elif choice == '6':
            # Print a goodbye message and break the loop
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()


