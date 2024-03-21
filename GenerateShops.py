# GenerateShops.py
# A shop randomizer for the Littfeld Caravan in Beastworld 

import random

# Create Shops array/list

shops = ["Morris's Miscibles", "Gallery of Curios", "Violet's Athaneum",
         "Game Parlor", "Alver's Bakery", "Chunky's Pet Pals",
         "Hugo's Lifesavers", "Brauniard's Auctions", "Bard's Magical Secret",
         "House of Fineries", "Lucas and Grier's", "Mutya's This n That",
         "Angeline's Forgewagon", "Ayvaire's Nest", "Bluebird Wagon",
         "Delver Delicacies"] 
shopslen = len(shops)

# How often are these shops present? (Does not factor in time of year or day of week)
ratios = [8, 12, 75, 25, 87, 100, 100, 50, 25, 15, 50, 75, 75, 100, 85, 100]
ratioslen = len(ratios)

# What page of the Delver's Guide is the shop in question outlined on? 
pages = [39, 40, 42, 43, 44, 45, 45, 46, 46, 47, 47, 49, 50, 50, 51, 57]
pageslen = len(pages)

# Determine current date
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"] 

print("Today's day is a", days[random.randint(0,6)], "in" , months[random.randint(0,11)])

# Determine which shops are present

if shopslen == ratioslen and shopslen == pageslen:

  print ("Today in Littfeld, the following shop wagons are present:") 
  for x in range (shopslen):
    presence = random.randint(1,100)
    if presence < ratios[x]:
      print(shops[x], "is present on page", pages[x])
      

# To Do:
# Remove the 100 places/always print them at the top
# Figure out how to notate the ones that are Only Sometimes
# Is there an easier matrix way to declare my arrays? this sucks and is likely to have slipping errors
