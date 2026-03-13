"""Gardening advice program.
This program prints gardening advice based on a season and
plant type.
"""


def get_season_advice(season):
    """Return advice for the season."""
    #Dictionary storing advice for different seasons.
    season_advice = {
        "summer": "Water your plants regularly and provide shade.",
        "winter": "Protect plants from frost using covers.",
        "spring": "Add compost to support new plant growth.",
        "autumn": "Clear fallen leaves and prepare beds for winter.",
    }

    return season_advice.get(season, "No advice available for this season.")


def get_plant_advice(plant_type):
    """Return advice based on the plant type."""
    #Dictionary storing advice for different plants.
    plant_advice = {
        "flower": "Use fertiliser to encourage blooming.",
        "vegetable": "Monitor plants carefully for pests.",
        "herb": "Harvest herbs regularly to encourage growth.",
    }

    return plant_advice.get(plant_type, "No advice available for this plant type.",)


def recommend_plants(season):
    """Recommend plants that grow well in a season."""
    seasonal_plants = {
        "summer": ["tomatoes", "peppers"],
        "winter": ["kale", "spinach"],
        "spring": ["lettuce", "carrots"],
        "autumn": ["broccoli", "cabbage"],
    }

    plants = seasonal_plants.get(season)

    if plants:
        return f"Recommended plants for {season}: {', '.join(plants)}."

    return "No plant recommendations available."


def main():
    """Run the gardening advice program."""
    #Hardcoded values are kept for now.
    #These will be replaced with Issue 2.
    season = "summer"
    plant_type = "flower"

    #Get advice
    season_message = get_season_advice(season)
    plant_message = get_plant_advice(plant_type)

    #Get plant recommendations
    recommendation = recommend_plants(season)

    #Print results
    print(season_message)
    print(plant_message)
    print(recommendation)


if __name__ == "__main__":
    main()
