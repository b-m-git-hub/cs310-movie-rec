import requests
import time
import pandas as pd

# Constants - replace key with TMDB API key
API_KEY = "key"
REGION = "US"

# Creates hashmap of streaming services string names to IDs
def get_provider_map():

    # API call
    url = "https://api.themoviedb.org/3/watch/providers/movie"
    params = {"api_key": API_KEY, "watch_region": REGION}
    response = requests.get(url, params=params).json()
    
    # Hashmap linking provider name to ID
    provider_hashmap = {}

    # Checks each name and ID pair
    for item in response.get("results", []):
        # Store name as lowercase
        name = item["provider_name"].lower()
        provider_hashmap[name] = item["provider_id"]

    return provider_hashmap

# Converts user input provider names to IDs
def convert_name_to_id(provider_names, provider_hashmap):
    
    # Stores converted names
    user_ids = []

    # Check hashmap for name to ID conversion
    for name in provider_names:
        # Convert user input into lower
        lower_name = name.lower()
        # Check hashmap for name and add ID if found
        if lower_name in provider_hashmap:
            user_ids.append(provider_hashmap[lower_name])
    
    return user_ids

# Checks streaming availability for movies in dataframe
# Stops after 100 movies have been checked to keep run time down
# due to rate limiting
# Returns list of movies on streaming services user owns
def check_streaming_availability(df, provider_names):
    provider_hashmap = get_provider_map()
    user_provider_ids = convert_name_to_id(provider_names, provider_hashmap)

    # List to store available movies
    available_movies = []
    count = 0

    # Iterate through each movie in dataframe
    for index, row in df.iterrows():
        # Reset availability and select new movie
        available = False
        movie_id = row["id"]

        # API call to check streaming providers for movie
        url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
        params = {"api_key": API_KEY}
        response = requests.get(url.replace("{movie_id}", str(movie_id)), params=params).json()
        
        # Sets providers to be US and subscription based
        providers = response.get("results", {}).get(REGION, {})
        streaming_providers = providers.get("flatrate", [])
        
        # Goes through each provider to check if in user list
        for provider in streaming_providers:
            if provider["provider_id"] in user_provider_ids:
                available = True
                break
        # Adds movie to available list if matched
        if available:
            available_movies.append(row["title"])

        count += 1
        # To avoid hitting rate limits
        if count % 30 == 0:
            time.sleep(1)
        # Stop after checking 100 movies
        if count % 100 == 0:
            return available_movies

def main():
    provider_names = input("Enter owned streaming services: ").split(", ")
    df = 
    recommendations = check_streaming_availability(df, provider_names)
    print(recommendations)

if __name__ == "__main__":
    main()