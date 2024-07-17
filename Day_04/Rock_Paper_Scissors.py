import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose?\nType 0 for rock, 1 for paper and 2 for scissors\n"))

if user_choice >=3 or user_choice <0:
    print("You typed an invalid number. You lose.")
else:
    options = [rock, paper, scissors]
    user_image = options[user_choice]
    machine_choice = random.randint(0, 2)
    machine_image = options[machine_choice]
    win = "You win."
    lose = "You lose."

    print(f"You choose:\n{user_image}")
    print(f"The machine choose:\n{machine_image}")

    if user_choice == machine_choice:
        print("Draw.")
    elif user_choice == 0 and machine_choice == 2:
        print(win)
    elif machine_choice == 0 and user_choice == 2:
        print(lose)
    elif user_choice > machine_choice:
        print(win)
    elif machine_choice > user_choice:
        print(lose)
