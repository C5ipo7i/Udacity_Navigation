import numpy as np
import math
import matplotlib.pyplot as plt

def plot(scores,interval = 25):
    rolling_mean = [np.mean(scores[(slice_*interval):(slice_+1)*interval]) for slice_ in range(math.ceil(len(scores)/interval))]
    x_axis = np.arange(len(rolling_mean)) * interval
    plt.plot(x_axis, rolling_mean)
    plt.ylabel('Score')
    plt.xlabel('Episode #')
    # plt.show()
    plt.savefig('DQN_performance.png',bbox_inches='tight')