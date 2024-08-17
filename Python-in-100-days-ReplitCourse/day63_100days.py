####################### test.py #####################
import random
num = random.randint(10,100)
def countdown():
  for i in range(num):
    print(i+1)
########################################################


######################### main.py #########################
import test
print("Countdown")
test.countdown()