from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

Calorie_goal_limit = 3000  # kcal
Protein_goal = 180  # grams
Fat_goal = 80  # grams
Carbs_goal = 300  # grams

today = []


@dataclass
class Food:
    name: str
    calories: int
    protein: int
    fat: int
    carbs: int


done = False

while not done:
    print("""
    (1) Add a new food
    (2) Visualize 
    (q) Quit
    """)

    choice = input("choose an option")

    if choice == "1":
        print("Adding a new food")
        name = input("Name:")
        calories = int(input("Calories:"))
        proteins = int(input("Proteins:"))
        fats = int(input("fats:"))
        carbs = int(input("Carbs"))
        food = Food(name, calories, proteins, fats, carbs)
        today.append(food)
        print("successfully added")

    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today)  # Corrected this line
        fats_sum = sum(food.fat for food in today)  # Corrected this line
        carbs_sum = sum(food.carbs for food in today)  # Corrected this line

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fats_sum, carbs_sum], labels=["proteins", "fats", "carbs"], autopct="%1.1f%%")
        axs[0, 0].set_title("Macronutrients Distribution")

        axs[0, 1].bar([0, 1, 2], [protein_sum, fats_sum, carbs_sum], width=0.4, label="Consumed")
        axs[0, 1].bar([0.5, 1.5, 2.5], [Protein_goal, Fat_goal, Carbs_goal], width=0.4, label="Goals")
        axs[0, 1].set_title("Macronutrients Distribution")
        axs[0, 1].legend()

        axs[1, 0].pie([calorie_sum, Calorie_goal_limit - calorie_sum], labels=["calories", "remaining"],
                     autopct="%1.1f%%")
        axs[1, 0].set_title("Calories Goal Progress")

        axs[1, 1].plot(list(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [Calorie_goal_limit] * len(today), label="Calorie Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Calorie Goal Over Time")

        fig.tight_layout()
        plt.show()

    elif choice == "q":
        done = True
    else:
        print("Invalid choice")
