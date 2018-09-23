#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 18:51:57 2018

@author: shiyanpei
"""

from unityagents import UnityEnvironment
import numpy as np
from model import QNetwork
from agent import Agent
from collections import deque
import matplotlib.pyplot as plt
import torch
# load the weights from file
env = UnityEnvironment(file_name="./Banana.app")
# get the default brain
brain_name = env.brain_names[0]
brain = env.brains[brain_name]
agent=Agent(state_size=37, action_size=4, seed=0)
agent.qnetwork_local.load_state_dict(torch.load('./ckpt/checkpoint.pth'))


env_info = env.reset(train_mode=False)[brain_name] # reset the environment
state = env_info.vector_observations[0] 
score=0
for j in range(2000):
    action = agent.act(state)
    env_info = env.step(action)[brain_name]        # send the action to the environment
    next_state = env_info.vector_observations[0]   # get the next state
    reward = env_info.rewards[0]                   # get the reward
    done = env_info.local_done[0]             
        
    state = next_state
    if done:
        break 
    score += reward
print('total score is '+str(score))
#env.close()