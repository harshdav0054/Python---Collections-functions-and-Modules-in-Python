#Q:-1

# Given two lists — one of product names and one of their prices — use the zip() function 
# to create a dictionary mapping each product to its price, then print the dictionary.

products = ["Laptop", "Mobile", "Headphones", "Keyboard"]
prices = [50000, 20000, 1500, 1200]

product_dict = dict(zip(products, prices))

print(product_dict)


#Q:-2

# Write a loop that takes two lists: usernames and their follower counts, and 
# manually creates a dictionary (without using zip()) that maps each username to its 
# follower count, similar to how Instagram tracks followers.

usernames = ["raj_07", "ananya_xo", "harsh_21"]
followers = [1200, 2500, 1800]

user_followers = {}

for i in range(len(usernames)):
    user_followers[usernames[i]] = followers[i]

print(user_followers)


#Q:-3

# Suppose you have two lists: one with IPL team names and another with their total points 
# this season. Use zip() to combine them into a dictionary, then print only the teams that 
# have more than 10 points.<br><br><em><strong>Hint:</strong> After creating the dictionary,
# use a for loop to filter and print.</em>

teams = ["CSK", "MI", "GT", "RCB"]
points = [12, 8, 15, 10]

team_points = dict(zip(teams, points))

print(team_points)

for team, point in team_points.items():
    if point > 10:
        print(team, point)



#Q:-4

# Given three lists — movie titles, genres, and ratings — use zip() to create a list of 
# dictionaries where each dictionary contains keys 'title', 'genre', and 'rating' for a 
# movie, then print the list.<br><br><em><strong>Constraint:</strong> Do not use any 
# external libraries.</em>

titles = ["Pathaan", "Jawan", "Leo"]
genres = ["Action", "Action", "Thriller"]
ratings = [4.2, 4.5, 4.3]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    movies.append(movie)

print(movies)