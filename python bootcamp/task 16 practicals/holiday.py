'''

This program is used to calculate a user's total holiday cost, which includes:
- plane expenses
- hotel expenses
- car-rental costs

The program takes user inputs for the following data:
- the city they will be flying to, stored as city_flight.
- the number of night spent at a hotel, stored as num_nights.
- the number of days that the user will hire a car for, stored as rental_days.

The data is put through the following functions:
- hotel_cost: uses num_nights as an argument, and will return the total cost of the stay.
- plane_cost: uses city_flight as an argument, and returns the cost of the flight
  (using the list of cities, see NOTES).
- car_rental: uses rental_days as an argument, and returns the total car rental cost.
- holiday_cost: uses 3 arguments, hotel_cost, plane_cost, and car_rental. This function
  calls the previous functions to return the total holiday cost.

The program then prints out all the data above, in a readable way.

NOTES:
- The city that the user inputs needs to be selected from a given list, which includes flight
  costs. This also means that the program needs to secure itself from missinputs.
- The prices for hotel stays and car rentals are built in to their respective functions
- The requirements suggest using if/else for the cities pricing, but that isn't very flexible,
  instead, I've chosen to store the city and cost in the same dictionary. This means developers
  can add more cities easily

'''


#define functions according to above specifications

def hotel_cost(night_no: int):
    price = 50
    total = night_no * price
    return total

def plane_cost(destination: str):
    total = city_dict[destination]
    return total

def car_rental(days: int):
    price = 10
    total = price * days
    return total

def holiday_cost(hotel: int, plane: str, car: int):
    total = hotel_cost(hotel) + plane_cost(plane) + car_rental(car)
    return total


#take user inputs / city dictionary

#city list stored in dictionary (all lowercase)
city_dict = {
    "london": 400,
    "glasgow": 200,
    "birmingham": 100,
    "bristol": 500
    }

#this formats the dictionary into a readable format
city_list = f'''
{"City":<15} {"Cost":<8} \n
'''

for city, cost in city_dict.items():
    temp_column = f"{city.title():<15} £{cost:<8} \n"
    city_list = city_list + temp_column


#inputs for city_flight, also includes error handling and formatting
while True:
    city_flight = str(input(f'''
    {city_list}
Please select the city you'll fly to, from the above list: 
'''))
    city_flight = city_flight.lower()
    if city_flight in city_dict:
        break
    else:
        print("That city is not in the list!")


#inputs for num_nights and rental_days, including error handling
while True:
    try:
        num_nights = int(input("\nPlease input how many nights you'll spend in the hotel (£50/night): "))
    except ValueError:
        print("Needs to be an integer!")
    else:
        break
while True:
    try:
        rental_days = int(input("\nPlease input how long you'll rent a car, in days (£10/day): "))
    except ValueError:
        print("Needs to be an integer!")
    else:
        break


#output

#This block calls all the relevent functions and assigns the output to variables
total_hotel = hotel_cost(num_nights)
total_plane = plane_cost(city_flight)
total_car = car_rental(rental_days)
grand_total = holiday_cost(num_nights, city_flight, rental_days)

#This part formats the outputs into a nice table
print(f'''
{"Total Hotel Cost:":<20} £{total_hotel:<10}
{"Total Travel Cost:":<20} £{total_plane:<10}
{"Total Rental Cost:":<20} £{total_car:<10}
{"Final Total:":<20} £{grand_total:<10}
''')
