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

if shopslen == ratioslen and shopslen == pageslen:

  print ("Today in Littfeld, the following shop wagons are present:") 
  for x in range (shopslen):
    presence = random.randint(1,100)
    if presence < ratios[x]:
      print(shops[x], "is present on page", pages[x])
      
