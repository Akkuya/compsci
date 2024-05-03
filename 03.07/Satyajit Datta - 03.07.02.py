import random

number = random.randint(1,100)

if number <= 30:
    print("Reward: Flower")


elif number <=50:
    print("Reward: Sword")


elif number <= 60:
    print("Reward: Gold Coin")


elif number <= 30:
    print("Reward: Chicken")
    
else:
    print("Nothing")

print("Generated number:", number)