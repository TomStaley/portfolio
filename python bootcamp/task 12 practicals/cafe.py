'''

This code is used to help organise a cafe's stock and pricing
1. all items are stored in the list "menu"
2. the amount of stock is stored in the dictionary "stock"
3. all prices are stored in the dictionary "price"

The code then calculates the total stock worth of the cafe
1. all items in the two dictionaries should correspond to an item in the menu
2. for each item in the menu, use the given string as the key for the two dictionaries
3. multiply the two dictionary values for each item and then add all the items together
4. output result

'''
#stores all items sold by the cafe
menu = ["coffee", "tea", "sandwich", "milkshake"]

#dictionary storing the cafe's stock
#each item corresponds to an item in "menu"
stock = {
    "coffee": 10,
    "tea": 20,
    "sandwich": 15,
    "milkshake": 18
}

#dictionary storing the cafe's pricing information
#each item corresponds to an item in "menu"
price = {
    "coffee": 5,
    "tea": 7,
    "sandwich": 10,
    "milkshake": 9
}

#utility variable storing the total value
total_value = 0

#checks each item in the menu, finds that item in the dictionaries
#multiplies the given values to find the item price, adds that to the total price
for item in menu:
    item_value = stock[item] * price[item]
    print(item.upper())
    print(item_value)
    total_value += item_value

print(f"The total value of the cafe is: £{total_value}")
