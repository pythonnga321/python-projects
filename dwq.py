import random
import tkinter as tk
from tkinter import ttk

breakfasts = [
    "Egg White and Spinach Scramble with Avocado",
    "Grilled Chicken and Egg Breakfast Burrito",
    "Protein Pancakes with Greek Yogurt and Almond Butter",
    "Turkey and Veggie Omelette",
    "Cottage Cheese with Almonds and Berries",
    "Scrambled Eggs with Chicken Breast",
    "Steak and Eggs"
]

lunches = [
    "Grilled Chicken Breast with Quinoa and Steamed Broccoli",
    "Tuna Salad with Mixed Greens and Avocado",
    "Turkey Burger with Sweet Potato Fries",
    "Grilled Salmon with Asparagus and Brown Rice",
    "Chicken and Broccoli Stir Fry with Cauliflower Rice",
    "Grilled Steak with Spinach Salad",
    "Chicken and Veggie Skewers"
]

dinners = [
    "Grilled Salmon with Steamed Veggies and Quinoa",
    "Chicken Breast with Sweet Potato and Kale Salad",
    "Ground Turkey with Zucchini Noodles and Spinach",
    "Beef Stir Fry with Broccoli and Brown Rice",
    "Grilled Chicken with Avocado and Mixed Vegetables",
    "Shrimp and Veggie Stir Fry with Cauliflower Rice",
    "Chicken Thighs with Sautéed Spinach and Mushrooms"
]

def random_meal_plan():
    morning_meal = random.choice(breakfasts)
    afternoon_meal = random.choice(lunches)
    evening_meal = random.choice(dinners)
    return {
        "Breakfast": morning_meal,
        "Lunch": afternoon_meal,
        "Dinner": evening_meal
    }

def show_meal_plan():
    meal_plan = random_meal_plan()
    breakfast_var.set(f"Breakfast: {meal_plan['Breakfast']}")
    lunch_var.set(f"Lunch: {meal_plan['Lunch']}")
    dinner_var.set(f"Dinner: {meal_plan['Dinner']}")

root = tk.Tk()
root.title("Protein-Packed Meal Planner")
root.geometry("500x300")
root.resizable(False, False)

title = ttk.Label(root, text="Hello, welcome to the diet assistant", font=("Arial", 14, "bold"))
title.pack(pady=10)

breakfast_var = tk.StringVar()
lunch_var = tk.StringVar()
dinner_var = tk.StringVar()

breakfast_label = ttk.Label(root, textvariable=breakfast_var, wraplength=480)
breakfast_label.pack(pady=5)

lunch_label = ttk.Label(root, textvariable=lunch_var, wraplength=480)
lunch_label.pack(pady=5)

dinner_label = ttk.Label(root, textvariable=dinner_var, wraplength=480)
dinner_label.pack(pady=5)

generate_button = ttk.Button(root, text="Generate Meal Plan", command=show_meal_plan)
generate_button.pack(pady=20)

root.mainloop()
