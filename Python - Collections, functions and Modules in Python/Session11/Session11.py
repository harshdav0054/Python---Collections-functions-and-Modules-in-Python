#Q:-1

# Use the math.sqrt() function to calculate and print the square roots of the 
# numbers 16, 49, and 81.

import math

print("Square root of 16:", math.sqrt(16))
print("Square root of 49:", math.sqrt(49))
print("Square root of 81:", math.sqrt(81))


#Q:-2


# Build a Flipkart-style price rounder: given a list of product prices with decimals, 
# use math.ceil() to round each price up to the nearest whole number and display the 
# results.<br><br><em><strong>Hint:</strong> Try with prices like 199.1,
#  349.8, and 599.3.</em>

import math

prices = [199.1, 349.8, 599.3]

for price in prices:
    print(price, "->", math.ceil(price))



#Q:-3

# Create a Zomato order bill calculator that uses math.floor() to show the final bill
# amount after applying a 10% discount, rounding down to the nearest rupee.

import math

bill = float(input("Enter the bill amount: "))

discount = bill * 10 / 100
final_bill = bill - discount

final_bill = math.floor(final_bill)

print("Final Bill Amount:", final_bill)



#Q:-4

# Simulate a dice roll for a board game app using random.randint(1, 6) and 
# print the result each time you run the program.

import random

dice = random.randint(1, 6)

print("Dice Result:", dice)


#Q:-5

# Build a Spotify-style daily playlist shuffle: given a list of 8 song names, 
# use the random module to select and print 3 random songs for today's playlist.
# <br><br><em><strong>Hint:</strong> Use random.sample() for this task.</em>

import random

songs = [
    "Believer",
    "Shape of You",
    "Perfect",
    "Faded",
    "Kesariya",
    "Blinding Lights",
    "Levitating",
    "Havana"
]

today_playlist = random.sample(songs, 3)

print("Today's Playlist:")
for song in today_playlist:
    print(song)