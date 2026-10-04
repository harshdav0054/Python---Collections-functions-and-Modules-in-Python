#Q:-1

# Create a Python dictionary called playlist with three songs as keys and 
# their durations (in seconds) as values. Update the duration of one song and 
# print the updated dictionary.

playlist = {
    "Believer": 204,
    "Shape of You": 234,
    "Faded": 212
}

playlist["Believer"] = 220

print(playlist)


#Q:-2

# Build a nested dictionary called user_profiles where each key is a 
# username (like 'raj_07', 'ananya_xo') and the value is another dictionary 
# with keys: 'followers', 'following', and 'posts'. Add data for at least two users and
# print the number of followers for 'ananya_xo'.

user_profiles = {
    "raj_07": {
        "followers": 1200,
        "following": 350,
        "posts": 45
    },
    "ananya_xo": {
        "followers": 2500,
        "following": 500,
        "posts": 80
    }
}

print("Posts by ananya_xo:", user_profiles["ananya_xo"]["posts"])


#Q:-3

# Simulate a Zomato-style restaurant menu using a nested dictionary: 
# each restaurant name as a key, and its value as another dictionary with 
# keys 'cuisine' and 'rating'. Add two restaurants, then update the rating of one 
# restaurant to a new value.<br><br><em><strong>Hint:</strong> Use dictionary indexing to 
# access and update the nested 'rating' value.</em>

restaurants = {
    "Burger Hub": {
        "cuisine": "Fast Food",
        "rating": 4.2
    },
    "Pizza Point": {
        "cuisine": "Italian",
        "rating": 4.0
    }
}

restaurants["Burger Hub"]["rating"] = 4.5

print(restaurants)


#Q:-4

# Given the following nested dictionary representing an IPL cricket team squad:
# <br><br>team = {'CSK': {'captain': 'Dhoni', 'players': 18}, 
#                 'MI': {'captain': 'Rohit', 'players': 17}}
# <br><br>Write code to add a new team 'GT' with captain 'Hardik' and 16 players, 
# then print all team names and their captains.

team = {
    "CSK": {
        "captain": "Dhoni",
        "players": 18
    },
    "MI": {
        "captain": "Rohit",
        "players": 17
    }
}

team["GT"] = {
    "captain": "Gill",
    "players": 16
}

for team_name, details in team.items():
    print("Team:", team_name, "| Captain:", details["captain"])