# Define the list of game maps and their elapsed times
game_maps = [
    ["Map A", 0],  # Map A was playable 12 hours ago
    ["Map B", 1],  # Map B was playable 36 hours ago
    ["Map C", 2],  # Map C was playable 60 hours ago
    ["Map D", 3],
    ["Map E", 4],
    ["Map F", 5],
    ["Map G", 6],
    ["Map H", 7],
    # ... and so on for the other maps
]
# Define a function that takes a date and returns the playable map or maps
def get_playable_map(date):
  # Convert the date to a weekday number (0 for Monday, 6 for Sunday)
  weekday = date.weekday()
  # Initialize an empty list to store the playable map or maps
  playable_maps = []
  # Loop through the game maps list
  for map in game_maps:
    # Calculate the weekday number when the map was last playable
    map_weekday = (weekday - map[1]) % 7
    # Check if the map is on a recurring cycle through the week
    if map_weekday == 0:
      # Add the map name to the playable maps list
      playable_maps.append(map[0])
  # Return the playable maps list
  return playable_maps

# Import the datetime module
import datetime

# Ask the user for a date in the format YYYY-MM-DD
user_date = input("Enter a date in the format YYYY-MM-DD: ")

# Try to parse the user input as a date object
try:
  date = datetime.datetime.strptime(user_date, "%Y-%m-%d").date()
  # Call the get_playable_map function with the date object
  result = get_playable_map(date)
  # Check if the result is empty
  if not result:
    # Print a message that no map is playable on that date
    print("No map is playable on that date.")
  # Check if the result has only one element
  elif len(result) == 1:
    # Print a message that only one map is playable on that date
    print(f"Only {result[0]} is playable on that date.")
  # Otherwise
  else:
    # Print a message that multiple maps are playable on that date
    print(f"The following maps are playable on that date: {', '.join(result)}.")
# If the user input is not a valid date
except ValueError:
  # Print a message that the input is invalid
  print("Invalid input. Please enter a date in the format YYYY-MM-DD.")
