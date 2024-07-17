import random
names = input("What are the names for the draw?\n").split(sep=", ")
length = (len(names)) - 1
random_name = names[random.randint(0, length)]

print(f"{random_name} is going to buy the meal today!")