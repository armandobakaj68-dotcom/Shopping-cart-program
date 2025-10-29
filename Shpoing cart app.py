foods = []
prices = []
total = 0 
while True:
    food = input("Enrer a food to buy (press q to quit): ")
    if food.lower() == "q":
      break
    else:
       price = float(input(f"Enter the price of a {food}:$ "))
       foods.append(food)
       prices.append(price)
print("---YOUR CART---")
for food in foods:
   print(food.capitalize())

total = sum(prices)
print()

print(f"Your total is: ${total}")