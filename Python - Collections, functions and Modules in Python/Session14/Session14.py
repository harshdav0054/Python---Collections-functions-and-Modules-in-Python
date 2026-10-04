#Q:-1

# Create a dynamic nested dictionary in Python to represent a Flipkart shopping cart where 
# each user (by username) can have multiple items, and each item has a name, quantity, 
# and price. Add two users with at least two items each, then print the entire cart.

shopping_cart = {}

shopping_cart["harsh"] = {
    "item1": {
        "name": "Laptop",
        "quantity": 1,
        "price": 50000
    },
    "item2": {
        "name": "Mouse",
        "quantity": 2,
        "price": 800
    }
}

shopping_cart["raj"] = {
    "item1": {
        "name": "Keyboard",
        "quantity": 1,
        "price": 1200
    },
    "item2": {
        "name": "Headphones",
        "quantity": 2,
        "price": 1500
    }
}

print(shopping_cart)


#Q:-2

# Write a function add_song_to_playlist(playlists, user, playlist_name, song_title, artist) 
# that adds a song to a user's playlist in a nested dictionary structure like Spotify. '
# 'If the user or playlist doesn't exist, create them dynamically.

def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}

    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []

    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })


playlists = {}

add_song_to_playlist(playlists, "harsh", "Favourite", "Believer", "Imagine Dragons")
add_song_to_playlist(playlists, "harsh", "Favourite", "Perfect", "Ed Sheeran")
add_song_to_playlist(playlists, "raj", "Workout", "Blinding Lights", "The Weeknd")

print(playlists)



#Q:-3

# Build a dynamic nested dictionary to store IPL cricket match scores: for each team, 
# store a dictionary of player names and their runs. Add at least two teams with three 
# players each, then print the runs scored by a specific player of your choice.

teams = {}

teams["CSK"] = {
    "Dhoni": 45,
    "Ruturaj": 78,
    "Jadeja": 32
}

teams["MI"] = {
    "Rohit": 65,
    "Surya": 72,
    "Hardik": 40
}

player = "Ruturaj"

print("Runs scored by", player, ":", teams["CSK"][player])


#Q:-4

# Given a nested dictionary representing Zomato orders (order_id as key, value is another
# dictionary with 'restaurant', 'items' (list), and 'total'), write a function to add a new
# order and another function to update the total of an existing order.
# <br><br><em><strong>Hint:</strong> Use dict.setdefault() to handle missing keys dynamically.</em>

orders = {
    101: {
        "restaurant": "Pizza Point",
        "items": ["Pizza", "Coke"],
        "total": 500
    }
}


def add_order(orders, order_id, restaurant, items, total):
    orders[order_id] = {
        "restaurant": restaurant,
        "items": items,
        "total": total
    }


def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total


add_order(orders, 102, "Burger Hub", ["Burger", "Fries"], 350)

update_total(orders, 101, 550)

print(orders)


#Q:-5


# Refactor the following code to use dynamic nested dictionary creation so that it doesn't
# throw a KeyError when adding a new user or playlist:<br><br>
# playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}<br>playlists['user2']['Chill']
# .append('Song3')<br><br><em><strong>Hint:</strong> Use collections.defaultdict or check 
# if keys exist before accessing.</em>


playlists = {
    "user1": {
        "Favourites": ["Song1", "Song2"]
    }
}

playlists.setdefault("user2", {})
playlists["user2"].setdefault("Chill", [])

playlists["user2"]["Chill"].append("Song3")

print(playlists)