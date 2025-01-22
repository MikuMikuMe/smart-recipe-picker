Creating a "smart-recipe-picker" involves multiple parts, including handling user input/preferences, interacting with a recipe API for meal suggestions, and integrating a grocery delivery API to suggest real-time delivery options. Due to the limited format here, this script will demonstrate a simplified version of such a system. The program will include:

1. User input for dietary preferences and constraints.
2. A mock function to simulate API interaction for recipe suggestions.
3. A mock function to simulate API interaction for grocery delivery.

This example is intended to give you a structural starting point and demonstrate how to integrate error handling and comments.

```python
import json
import random

def get_user_preferences():
    """
    Collects dietary preferences and constraints from the user.
    Returns a dictionary containing these preferences.
    """
    print("Welcome to the Smart Recipe Picker!")
    preferences = {}
    
    # Get preferred cuisine type
    preferences['cuisine'] = input("Enter your preferred cuisine (e.g., Italian, Chinese, Mexican): ")
    
    # Get dietary restrictions
    preferences['dietary_restrictions'] = input("Enter any dietary restrictions (e.g., vegetarian, gluten-free): ")
    
    # Get number of meals
    try:
        preferences['num_meals'] = int(input("Enter the number of meals you want: "))
    except ValueError:
        print("Invalid input. Defaulting to 3 meals.")
        preferences['num_meals'] = 3

    return preferences

def get_recipes(preferences):
    """
    Simulates interacting with a recipe API to get meal suggestions based on preferences.
    For this example, returns a mock list of recipes.
    """
    try:
        # Simulated recipe database
        recipe_database = {
            "Italian": ["Pasta Carbonara", "Margherita Pizza", "Risotto"],
            "Chinese": ["Sweet and Sour Pork", "Kung Pao Chicken", "Spring Rolls"],
            "Mexican": ["Tacos", "Burritos", "Quesadillas"]
        }
        # Fetch the recipes from the 'database' based on cuisine type
        return random.sample(recipe_database.get(preferences['cuisine'], []), preferences['num_meals'])
    except Exception as e:
        print("Error fetching recipes:", e)
        return []

def integrate_grocery_delivery(recipes):
    """
    Simulates interacting with a grocery delivery API to provide delivery options for recipe ingredients.
    For this example, returns a mock delivery confirmation.
    """
    try:
        # Simulating interaction with a grocery API
        if not recipes:
            raise Exception("No recipes found to process for grocery delivery.")
        
        delivery_service = "GroceryNow"
        delivery_confirmation = {
            "service": delivery_service,
            "status": "Success",
            "recipes": recipes
        }
        
        # Normally here we would call an API
        print(f"Order for {', '.join(recipes)} confirmed with {delivery_service}")
        return delivery_confirmation
    except Exception as e:
        print("Error in grocery delivery integration:", e)
        return {}

def save_plan_to_file(plan):
    """
    Saves the meal plan to a JSON file.
    """
    try:
        with open('meal_plan.json', 'w') as file:
            json.dump(plan, file, indent=4)
        print("Meal plan saved to meal_plan.json")
    except IOError as e:
        print("File error:", e)

def main():
    """
    Main function to run the smart-recipe-picker.
    """
    try:
        user_preferences = get_user_preferences()
        recipes = get_recipes(user_preferences)
        grocery_info = integrate_grocery_delivery(recipes)
        
        plan = {
            "preferences": user_preferences,
            "recipes": recipes,
            "grocery_delivery": grocery_info
        }
        
        save_plan_to_file(plan)
    except Exception as e:
        print("An error occurred during the execution of the program:", e)

if __name__ == "__main__":
    main()
```

### Key Points:
- **Error Handling**: The script wraps potentially failing operations in try-except blocks to provide meaningful error messages.
- **User Input**: Data is collected from users using `input()`, and validation is performed to prevent invalid data entries.
- **Function Structure**: The program is modular with separate functions for each core feature—getting user preferences, fetching recipes, integrating grocery delivery, and saving data.
- **Mock Data**: Integration with real APIs is not included since this is a skeleton structure for educational purposes. In a real application, you would replace the mock functions with API calls using libraries like `requests`.

This script forms the basis of a smart-recipe-picker and can be expanded with actual API connections for recipes and grocery delivery services.