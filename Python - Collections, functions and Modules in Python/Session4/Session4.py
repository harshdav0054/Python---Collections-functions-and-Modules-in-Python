#Q:-1

# Create a tuple named my_profile that contains your name (string), age (integer), 
# favorite food (string), and a boolean indicating if you have a pet.

my_profile = ("Harsh", 20, "Pizza", True)

print(my_profile)


#Q:-2

# Given the tuple 
# playlist = ('Shape of You', 'Blinding Lights', 'Believer', 'Senorita', 'Levitating'), 
# use slicing to print only the 2nd, 3rd, and 4th songs.


playlist = ("Shape of You", "Blinding Lights", "Believer", "Senorita", "Levitating")

print(playlist[1:4])


#Q:-3

# Convert the tuple order = ('Burger', 'Fries', 'Coke') into a list, 
# add 'Ice Cream' to the end, then convert it back to a tuple and print the final tuple.

order = ("Burger", "Fries", "Coke")

order_list = list(order)
order_list.append("Ice Cream")

final_order = tuple(order_list)

print(final_order)


#Q:-4

# Create a mixed tuple called insta_post containing: 
# post_id (int), username (string), likes (int), hashtags (list of strings), 
# and is_public (boolean). Print the tuple and the type of each element.

insta_post = (101,"harsh",250,["python", "coding", "learning"],True)

print(insta_post)

for item in insta_post:
    print(item, type(item))


#Q:-5

# Take a tuple of your last 7 WhatsApp call durations in 
# minutes (e.g., (12, 5, 0, 20, 7, 3, 15)), convert it to a list,
# remove all calls shorter than 5 minutes, then convert it back to a tuple and 
# print the result.<br><br><em><strong>Hint:</strong> Use a for loop or list comprehension
#    to filter the list before converting back to tuple.</em>


calls = (12, 5, 0, 20, 7, 3, 15)

calls_list = [call for call in calls if call >= 5] #Lambda Fun

calls = tuple(calls_list)

print(calls)