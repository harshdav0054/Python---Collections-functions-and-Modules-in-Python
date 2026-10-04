#Q :- 1

# Create a Python list named fav_items that contains your favorite song name (string), 
# your age (integer), your monthly mobile data usage in GB (float), and a boolean indicating 
# if you have a premium subscription on any app.

fav_items = ["Believer", 21, 20.5, True]

print(fav_items)


# Q :- 2

# Update the fav_items list by changing the song name to another song you like
# and increasing your age by 1.

fav_items[0] = "Shape of You"
fav_items[1] = fav_items[1] + 1

print(fav_items)


# Q :- 3

# Remove the mobile data usage value from fav_items using the del statement,
# then print the updated list.
# <br><br><em><strong>Hint:</strong> Use the index of the value you want to remove.</em>

del fav_items[2]

print(fav_items)


# Q :- 4

# Create a new list called weekend_plan with at least 5 items 
# representing things you want to do this weekend (mix of strings and numbers).
# Remove the last item using the pop()
#  method and display the removed item and the updated list.

weekend_plan = ["Watch Movie", "Play Cricket", "Study Python", 2, "Go Shopping"]

removed_item = weekend_plan.pop()

print("Removed Item:", removed_item)
print("Updated List:", weekend_plan)