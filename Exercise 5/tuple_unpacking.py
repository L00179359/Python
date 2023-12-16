'''
Tuple Unpacking
Coding using Tuple Unpacking By: Rahul Kharade
22OCT2023
'''

#Calculate most expensive car from the list
def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive car
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    # Iterate, unpacking the tuple
    for description, price in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
        # If it is not the maximum price, do nothing
        else:
            pass
    # Return the maximum prices item and its price
    return max_price_item, max_price

# Provide the price in Euros
price_list = [("Audi Q7", 100000), ("BMW X5", 90000), ("Toyota LC", 75000), ("KIA Sportage", 45000)]
# Call the function and unpack its return values
product, price  = most_expensive(price_list)
print('Most expensive car is :',product, ',Price is',price ,'Euros')