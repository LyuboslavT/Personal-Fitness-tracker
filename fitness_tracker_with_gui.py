import tkinter as tk
from tkinter import messagebox

# Lists to store fitness data
workouts = []
calories = []

# Variables for daily goals
workout_goal = 0
calorie_goal = 0


def log_workout():
    """Logs a workout from user input fields."""
    workout_type = workout_entry.get()
    try:
        duration = int(duration_entry.get())
        workouts.append((workout_type, duration))
        messagebox.showinfo("Success", f"Workout Logged: {workout_type} - {duration} min")
        workout_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for duration!")


def log_calorie_intake():
    """Logs calorie intake from user input."""
    try:
        consumed = int(calories_entry.get())
        calories.append(consumed)
        messagebox.showinfo("Success", f"Calories Logged: {consumed}")
        calories_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for calories!")


def view_progress():
    """Calculates and displays progress."""
    total_time = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    progress_message = f"Total Workout Time: {total_time} min\nTotal Calories Taken: {total_calories}"

    # Encouragement message
    if total_time < workout_goal:
        progress_message += f"\n⚠️ You need {workout_goal - total_time} more minutes of activity!"
    elif total_time >= workout_goal:
        progress_message += "\n🎉 Amazing! You've reached your daily workout goal!"

    if total_calories > calorie_goal:
        progress_message += "\n⚠️ You are exceeding your calorie goal!"
    elif total_calories < calorie_goal:
        progress_message += f"\n🍽️ You need {calorie_goal - total_calories} more calories."

    messagebox.showinfo("Progress", progress_message)


def reset_progress():
    """Clears workout and calorie logs."""
    workouts.clear()
    calories.clear()
    messagebox.showinfo("Reset", "All progress has been reset!")


def set_daily_goals():
    """Sets workout and calorie goals from user input."""
    global workout_goal, calorie_goal
    try:
        workout_goal = int(goal_workout_entry.get())
        calorie_goal = int(goal_calories_entry.get())
        messagebox.showinfo("Success", f"Goals Set!\nWorkout Goal: {workout_goal} min\nCalorie Goal: {calorie_goal}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for goals!")


# Tkinter GUI Setup
root = tk.Tk()
root.title("Personal Fitness Tracker 🏋️‍♂️")

# Workout Section
tk.Label(root, text="Workout Type:").grid(row=0, column=0)
workout_entry = tk.Entry(root)
workout_entry.grid(row=0, column=1)

tk.Label(root, text="Duration (min):").grid(row=1, column=0)
duration_entry = tk.Entry(root)
duration_entry.grid(row=1, column=1)

tk.Button(root, text="Log Workout", command=log_workout).grid(row=2, column=0, columnspan=2)

# Calorie Section
tk.Label(root, text="Calories Consumed:").grid(row=3, column=0)
calories_entry = tk.Entry(root)
calories_entry.grid(row=3, column=1)

tk.Button(root, text="Log Calories", command=log_calorie_intake).grid(row=4, column=0, columnspan=2)

# Goal Setting Section
tk.Label(root, text="Set Workout Goal (min):").grid(row=5, column=0)
goal_workout_entry = tk.Entry(root)
goal_workout_entry.grid(row=5, column=1)

tk.Label(root, text="Set Calorie Goal:").grid(row=6, column=0)
goal_calories_entry = tk.Entry(root)
goal_calories_entry.grid(row=6, column=1)

tk.Button(root, text="Set Goals", command=set_daily_goals).grid(row=7, column=0, columnspan=2)

# Action Buttons
tk.Button(root, text="View Progress", command=view_progress).grid(row=8, column=0, columnspan=2)
tk.Button(root, text="Reset Progress", command=reset_progress).grid(row=9, column=0, columnspan=2)

# Run the GUI
root.mainloop()
