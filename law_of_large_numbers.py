#program to prove the Law of Large Numbers
import matplotlib.pyplot as plt
import numpy as np

def coin_flip_experiment():
    coin = ['Heads','Tails']
    coin_side = np.random.choice(coin)
    if coin_side == "Heads":
        return 1
    return 0

if __name__ == '__main__':
    num_of_trials = int(input("Enter number of trials - "))
    prop_of_head = []
    total_flips = []
    count_of_head = 0
    for flip in range(num_of_trials):
        count_of_head+=coin_flip_experiment()
        prop_of_head.append(count_of_head/(flip+1))
        total_flips.append(flip+1)

    plt.plot(total_flips,prop_of_head,label = "Experimental Probability")
    plt.xlabel("Number of flips")
    plt.ylabel("Proportion of Head")
    plt.hlines(0.5,0, num_of_trials, colors='orange', label='True Probability')
    plt.legend()
    plt.show()
