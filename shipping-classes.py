#Sal's shipping
#By Belinda
#Enter package weight here
weight = 1

#ground shipping
if weight <= 2:
  ground_shipping = 1.50 * weight + 20
elif weight <= 6:
  ground_shipping = 3.00 * weight + 20
elif weight <=10:
  ground_shipping = 4.00 * weight + 20
else:
  ground_shipping = 4.75 * weight + 20

premium_ground = 125.00


#drone shipping
if weight <= 2:
  drone_shipping = 4.50 * weight
elif weight <= 6:
  drone_shipping = 9.00 * weight
elif weight <=10:
  drone_shipping = 12.00 * weight
else:
  drone_shipping = 14.25 * weight

#UI
print("Package weight: ", weight)
print("Shipping Options")
print("----------------")
print("Ground Shipping: $" , ground_shipping)
print("Premium Ground Shipping: $" , premium_ground)
print("Drone Shipping: $" , drone_shipping)
print("----------------")

#compare prices
if drone_shipping <= ground_shipping and drone_shipping <= premium_ground:
  print("Your best option is Drone Shipping")
elif premium_ground <=ground_shipping and premium_ground <= drone_shipping:
  print("Your best option is Premium Ground Shipping")
else:
  print("Your best option is Ground Shipping")
