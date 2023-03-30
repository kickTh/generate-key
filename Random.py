import random

set_random = "1234567890" + "MNBVCXZLKJHGFDSAPOIUYTREWQ" + "mnbvcxzlkjhgfdsapoiuytrewq"
set_number = [4,8,16,36,64]

def number_function():
  number = ''.join((random.choice(set_random) for i in range(random.choice(set_number))))
  return number

for i in range(1):
   let = number_function() + "-" + number_function() + "-" + number_function() + "-" + number_function()
   open("let.txt", "a").write(let + "\n")
   print(let)