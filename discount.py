def calculate_discount(price,discount_percent):
#Calculate final price ater applying discount
    discounted_price=price-((discount_percent/100)*price)
    #Checks if discount offeredis higher than 20 or not
    if discount_percent>=20:
    
        return discounted_price
    else:
        return price
# prompts user to enter the price of an item
original_price=float(input("enter the price of the item  "))
#user prompted to enter discount
discounted_percentage=float(input("enter the discount being offered   "))
#calls the function to calculate new price after applying the discount
new_price= calculate_discount(original_price, discounted_percentage)
#prints the results if discount is applied or not
if new_price !=original_price:
    print("The new price after discount is,  ", new_price)
else:
    print("no discount applied. The price remains", original_price)