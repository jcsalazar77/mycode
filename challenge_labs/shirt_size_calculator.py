#!/usr/bin/python3
  
##Shirt size calculator

print("Use this calculator to determine shirt size before ordering")

weight = float(input("How much do you weigh (in LBS)? Provide only a numerical value: "))

if weight <= 1:
    print(f"You entered {weight} lbs, please enter a valid weight.")
elif weight <= 100:
    print(f"You entered {weight} lbs, you should order a size X-small.")
elif weight <= 125:
    print(f"You entered {weight} lbs, you should order a size Small.")
elif weight <= 175:
    print(f"You entered {weight} lbs, you should order a size Medium.")
elif weight <= 200:
    print(f"You entered {weight} lbs, you should order a size Large.")
elif weight <= 250:
    print(f"You entered {weight} lbs, you should order a size X-Large.")
elif weight <= 300:
    print(f"You entered {weight} lbs, you should order a size XX-Large.")
elif weight > 376:
    print("Can only calculate shirt size up to 375 LBS. or XXL.")
else:
    print("You did not enter a valid weight. Please run calculator again with a valid weight.")
    
print("Exiting shirt size calculator")
