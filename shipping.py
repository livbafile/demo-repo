
weight = 41.5

# Premium Ground Shipping Flat Rate
premium_ground_shipping = 125.00
print(f"Premium Ground Shipping has Flat Rate of {premium_ground_shipping} ")

# Ground shipping

if weight <= 2:
  cost_ground = weight * 4.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print(f"Ground Shipping cost is {cost_ground}")


# Drone Shipping

if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9.00
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25
print(f"Drone Shipping Cost is {cost_drone}")
