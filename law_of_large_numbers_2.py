
# Proving the Law of Large numbers-2
# Experiment - two dice rolled simultaneously
# To find the experimental probability of outcomes of both the dice being same
import numpy as np
import matplotlib.pyplot as plt

def die_roll_exp():
    die = [1,2,3,4,5,6]
    choice_1 = np.random.choice(die)
    choice_2 = np.random.choice(die)
    if choice_1 == choice_2:
        return 1
    return 0

no_of_rolls = int(input("Enter number of rolls - "))
prop_of_same_side = []
total_rolls = []
count_of_same_side = 0
for roll in range(1,no_of_rolls+1):
    count_of_same_side+=die_roll_exp()
    prop_of_same_side.append(count_of_same_side/roll)
    total_rolls.append(roll)

plt.plot(total_rolls,prop_of_same_side,label = "Experimental Probability")
plt.xlabel("Number of rolls")
plt.ylabel("Proportion of both dice having the same sides")
plt.hlines(0.167,0, no_of_rolls, colors='orange', label='True Probability')
plt.legend()
plt.show()