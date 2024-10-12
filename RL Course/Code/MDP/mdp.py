import gym
import numpy as np
from IPython import display
from matplotlib import pyplot as plt
from utility import *

# %matplotlib inline

if __name__ == '__main__':
   
    env = Maze()

    initial_state = env.reset()
    print(f"The new episode will start in state: {initial_state}")


    frame = env.render(mode='rgb_array')
    plt.axis('off')
    plt.title(f"State: {initial_state}")
    plt.imshow(frame)
    plt.show()
    

    action = 2
    next_state, reward, done, info = env.step(action)
    print(f"After moving down 1 row, the agent is in state: {next_state}")
    print(f"After moving down 1 row, we got a reward of: {reward}")
    print("After moving down 1 row, the task is", "" if done else "not", "finished")

    frame = env.render(mode='rgb_array')
    plt.axis('off')
    plt.title(f"State: {next_state}")
    plt.imshow(frame)
    plt.show()