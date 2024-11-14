import Weather_API_FINAL
import Restaraunt_API_FINAL
import Attractions_API_FINAL

# Function to get API keys (not directly part of the city info processing, so it should be called once)
def load_api_keys():
    # Enter the full file path for where you store both of these values
    try:
        with open("C:/VSC_Coding_projects/dev_project2/dev_project2/GoogleAPI.txt", "r") as GAPI, \
             open("C:/VSC_Coding_projects/dev_project2/dev_project2/WeatherAPI.txt", "r") as WAPI:
            google_api_key = GAPI.read().strip()
            openweather_api_key = WAPI.read().strip()
        return google_api_key, openweather_api_key
    except Exception as e:
        print(f"Error loading API keys: {e}")
        return None, None

# Function to process city data, fetch weather, restaurants, and attractions
def process_city_info(city, state, area):
    google_api_key, openweather_api_key = load_api_keys()
    
    if not google_api_key or not openweather_api_key:
        return "Error loading API keys."

    try:
        # Get and print weather
        weather = Weather_API_FINAL.get_weather(openweather_api_key, city)
        Weather_API_FINAL.print_weather(weather)

        # Get and print restaurant suggestions
        restaurants = Restaraunt_API_FINAL.get_restaurants(google_api_key, city, state, area)
        Restaraunt_API_FINAL.print_restaurants(restaurants)

        # Get and print local attractions
        attractions = Attractions_API_FINAL.get_local_attractions(google_api_key, city, state, area)
        Attractions_API_FINAL.print_attractions(attractions)

        # Return success message
        return f"Successfully processed data for {city}, {state} within {area} km²."

    except ValueError as e:
        return "Error, please try entering your number as digits (i.e., '60' instead of 'sixty.')"
    except Exception as e:
        return f"An error occurred: {e}"

