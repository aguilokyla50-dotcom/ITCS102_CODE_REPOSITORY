Sender_Name = input("Name of Sender? --> ")

Type_of_Item = input("What type of Item did you order? ---> ")

Is_Fragile = bool(input("Is your order Fragile? (Enter \"yes\" if yes, eneter \"no\" if no) --->") == "yes")

weight = float(input("How heavy is the Weight of the object? (in kg) ---> "))

distance = float(input("How far is the destination(In km) ---- > "))

is_express = bool(input("Express? (Enter \"yes\" if yes, eneter \"no\" if no) --->")== "yes")

is_international = bool(input("International? (Enter \"yes\" if yes, eneter \"no\" if no) --->")== "yes")


# Calculating base cost

base_cost = (weight * 2.50) + (distance * 0.15)


#International Express



if weight <= 2  and distance <=100 and not is_international:
	print("free shipping!!!")
	total = 0

elif is_international and is_express:
	print("International express is applied")
	Total = (base_cost * 1.4) + 50

elif (is_express or is_international) and weight > 20: 
	print("Package is Express or Heavy International is applied")
	Total = (base_cost * 1.2) + 25

elif weight > 30 or distance > 1000: 
	print("Oversized is applied")
	Total = base_cost + 30
#Standard rate

else :
	Total = base_cost
	print("Standard rate is applied")

ShippingFee = total - base_cost


print("=================================")
print("KYLA'S DELIVERING COMPANY")
print("Name: ", Sender_Name)
print("ITEM: ", Type_of_Item)
print("WEIGHT: ", weight)
print("DISTANCE: ",distance)
print("FRAGILE???: ",Is_Fragile)
print("INTERNATIONAL?: ", is_international)
print("EXPRESS?: ", is_express)
print("TOTAL SHIPPING COST: PHP ", ShippingFee)
print("Total: PHP ", total)
print("================================")

print("Thank you so much for purchasing from us! We truly appreciate your support. We hope you love your purchase!")
("Thank you for choosing our small business!")



