
import pandas as pd
import streamlit as st

from datetime import datetime

# Function to get the date from user input
def get_date():
    while True:
        date_str = input("Enter the due date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format. Please try again.")

# Function to get the priority from user input
def get_priority():
    while True:
        priority = input("Enter the priority (important/not important): ")
        if priority.lower() in ["important", "not important"]:
            return priority.lower()
        else:
            print("Invalid priority. Please try again.")

# Create a class for tasks
class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority

    def __str__(self):
        return f"{self.description} (Due: {self.due_date.strftime('%Y-%m-%d')}, Priority: {self.priority.capitalize()})"

# Create an empty list to store tasks
tasks = []

# Get the number of tasks from the user
num_tasks = int(input("Enter the number of tasks: "))

# Prompt the user to input task details
for i in range(1, num_tasks + 1):
    print(f"\nTask {i}:")
    description = input("Enter the task description: ")
    due_date = get_date()
    priority = get_priority()
    tasks.append(Task(description, due_date, priority))

# Sort tasks by due date and priority
sorted_tasks = sorted(tasks, key=lambda x: (x.due_date, x.priority == "important"), reverse=False)

# Print the sorted tasks
print("\nSorted Tasks:")
for task in sorted_tasks:
    print(task)
