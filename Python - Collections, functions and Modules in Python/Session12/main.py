#Q:-1

from musicplayer.player import play_song

play_song()


#Q:-2

from foodorder import get_menu, place_order

menu = get_menu()

print("Menu:", menu)

place_order("Pizza")


#Q:-3

from shoppingcart import add_to_cart

add_to_cart("Laptop")



#Q:-4

from instahelpers import format_likes

print(format_likes(1200))
print(format_likes(1500000))
print(format_likes(850))


#Q:-5

from ticketbooking import search_event, book_ticket

search_event("Music Concert")
book_ticket("Music Concert")