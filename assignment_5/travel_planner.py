class KnowledgeBase:
    def __init__(self):
        self.places = {
            "Napa Valley": {"tags": ["wine", "scenic"], "cost_level": "luxury", "base_cost": 400, "food": "Fine Dining"},
            "Rome": {"tags": ["history", "culture", "wine", "food"], "cost_level": "moderate", "base_cost": 200, "food": "Italian"},
            "Tokyo": {"tags": ["tech", "modern", "food"], "cost_level": "luxury", "base_cost": 350, "food": "Japanese"},
            "Oaxaca": {"tags": ["culture", "food", "scenic"], "cost_level": "budget", "base_cost": 80, "food": "Mexican"},
            "Bordeaux": {"tags": ["wine", "history"], "cost_level": "luxury", "base_cost": 300, "food": "French"}
        }

        self.wine_ontology = {
            "Napa Valley": ["Cabernet Sauvignon", "Chardonnay"],
            "Rome": ["Frascati", "Chianti"],
            "Bordeaux": ["Merlot", "Cabernet Sauvignon"]
        }

        self.food_recommendations = {
            "Italian": ["Pasta Carbonara", "Pizza Margherita"],
            "Japanese": ["Sushi", "Ramen"],
            "Mexican": ["Mole Poblano", "Tacos al Pastor"],
            "Fine Dining": ["Degustation Menu"],
            "French": ["Duck Confit", "Foie Gras"]
        }

class AITravelPlanner:
    def __init__(self, kb):
        self.kb = kb
        self.cost_mapping = {"budget": 1, "moderate": 2, "luxury": 3}

    def generate_plan(self, preferences):
        matched_destinations = []
        max_pref_cost = self.cost_mapping.get(preferences.get("budget_level", "moderate"), 2)

        for name, info in self.kb.places.items():
            destination_cost = self.cost_mapping[info["cost_level"]]
            if destination_cost > max_pref_cost:
                continue

            score = sum(1 for tag in preferences.get("interests", []) if tag in info["tags"])
            if score > 0 or not preferences.get("interests"):
                matched_destinations.append((name, info, score))

        matched_destinations.sort(key=lambda x: x[2], reverse=True)

        if not matched_destinations:
            return "No destinations found matching your budget and interests."

        selected_name, selected_info, _ = matched_destinations[0]
        days = preferences.get("duration_days", 3)

        total_cost = (selected_info["base_cost"] * days) + (preferences.get("flight_cost", 0))

        food_type = selected_info["food"]
        recommended_dishes = self.kb.food_recommendations.get(food_type, [])
        wine_pairings = self.kb.wine_ontology.get(selected_name, []) if "wine" in preferences.get("interests", []) else []

        report = []
        report.append("--- PERSONALIZED AI TRAVEL ITINERARY ---")
        report.append(f"Destination: {selected_name}")
        report.append(f"Duration: {days} Days")
        report.append(f"Total Estimated Cost: ${total_cost}")
        report.append(f"  - Base Cost Per Day: ${selected_info['base_cost']}")
        report.append(f"  - Flight Cost: ${preferences.get('flight_cost', 0)}")

        report.append("\n--- LOCAL KNOWLEDGE & RECOMMENDATIONS ---")
        report.append(f"Food Category: {food_type}")
        if recommended_dishes:
            report.append(f"Must-Try Dishes: {', '.join(recommended_dishes)}")
        if wine_pairings:
            report.append(f"Regional Wine Pairings: {', '.join(wine_pairings)}")

        report.append("\n--- DAY-BY-DAY PLAN ---")
        for day in range(1, days + 1):
            report.append(f"Day {day}:")
            report.append(f"  Activity: Explore {selected_name} focusing on {', '.join(preferences.get('interests', ['general sightseeing']))}")
            meal = recommended_dishes[day % len(recommended_dishes)] if recommended_dishes else "Local Cuisine"
            report.append(f"  Meal Suggestion: {meal}")

        return "\n".join(report)

def test_travel_planner():
    kb = KnowledgeBase()
    planner = AITravelPlanner(kb)

    user_preferences = {
        "interests": ["wine", "history"],
        "budget_level": "luxury",
        "duration_days": 3,
        "flight_cost": 500
    }

    print(planner.generate_plan(user_preferences))

if __name__ == "__main__":
    test_travel_planner()
