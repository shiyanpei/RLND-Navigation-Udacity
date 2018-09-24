# RLND-Navigation-Udacity
## This is the navigation project of RL nano degree in Udacity

## Requirements 
python 3.6 <br>pytorch 0.4.1<br>

## Environment
### For installation, use the command bellow
```
pip install unityagents
```
### Information of the environment
The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction. A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.<br> The reward in an episode over 15.0 is considerd to be solved.

## Code
### To train the agent, use the command bellow
```
python train.py
```
### To do inference, see an trained agent, please use the command bellow
```
python inference.py
```
### The code of the agent is in agent.py, the pytorch model is in model.py
### The plot of trainig scores is in scores.png
### Report of algorithm is in Report of P1 Navigation.pdf


