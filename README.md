# RLND-Navigation-Udacity
## This is the navigation project of RL nano degree in Udacity

## Requirements 
python 3.6 <br>pytorch 0.4.1<br>

## Environment
### For installation, use the command bellow
```
pip install unityagents
```
<br>
### and import the package
```
from unityagents import UnityEnvironment
```
### Then, download the environment
Next, we will start the environment! Before running the code cell below, change the file_name parameter to match the location of the Unity environment that you downloaded.

Mac: "path/to/Banana.app"
Windows (x86): "path/to/Banana_Windows_x86/Banana.exe"
Windows (x86_64): "path/to/Banana_Windows_x86_64/Banana.exe"
Linux (x86): "path/to/Banana_Linux/Banana.x86"
Linux (x86_64): "path/to/Banana_Linux/Banana.x86_64"
Linux (x86, headless): "path/to/Banana_Linux_NoVis/Banana.x86"
Linux (x86_64, headless): "path/to/Banana_Linux_NoVis/Banana.x86_64"
For instance, if you are using a Mac, then you downloaded Banana.app. If this file is in the same folder as the notebook, then the line below should appear as follows:
```
env = UnityEnvironment(file_name="Banana.app")
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


