print("The Love Calculator is calculating your score...")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
name = name1.lower() + name2.lower()

t_occurs = name.count("t")
r_occurs = name.count("r")
u_occurs = name.count("u")
e_occurs = name.count("e")

total_name1 = str(t_occurs + r_occurs + u_occurs + e_occurs)

l_occurs = name.count("l")
o_occurs = name.count("o")
v_occurs = name.count("v")
e_occurs = name.count("e")

total_name2 = str(l_occurs + o_occurs + v_occurs + e_occurs)

total = total_name1 + total_name2
total = (int(total))

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos." )
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}.")