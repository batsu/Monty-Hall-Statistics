import random

def game():
  doors = ["goat", "goat", "money"]
  nums = [0, 1, 2]
  
  random.shuffle(doors)
  random.shuffle(nums)
  
  choice = random.randint(0, 2)
  
  otherDoor = 0
  
  goatDoor = 0
  
  nums.remove(choice)
  
  # print(doors, nums)
  
  if doors[choice] == "goat" and doors[nums[0]] == "goat":
    otherDoor = nums[1]
    goatDoor = nums[0]
  else:
    otherDoor = nums[0]
    goatDoor = nums[1]
  
  # print(otherDoor, goatDoor)
  
  options = ["y","n"]
  
  switch = random.choice(options)
  
  if switch == "y":
    choice = otherDoor
  
  if doors[choice] == "money":
    return True, switch
  
  else:
    return False, switch

win_switch = 0
win_no_switch = 0
lose_switch = 0
lose_no_switch = 0

p = int(input("How many times do you want to play? "))

for x in range(0,p):
  check = game()
  if check[0] is True and check[1] == "y":
    win_switch += 1
  elif check[0] is True and check[1] == "n":
    win_no_switch += 1
  elif check[0] is False and check[1] == "y":
    lose_switch += 1
  elif check[0] is False and check[1] == "n":
    lose_no_switch += 1

print("wins with switch: " + str(win_switch))
print("wins without switch: " + str(win_no_switch))
print("losses with switch: " + str(lose_switch))
print("losses without switch: " + str(lose_no_switch))

print("win percentage with switch: " + str(win_switch/(p)*100))
