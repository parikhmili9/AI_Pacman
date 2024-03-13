# Reinforcement Learning in Pacman

# Introduction
In this project, I implemented value iteration and Q-learning. I will test the agents first on Gridworld (from class), then apply them to a simulated robot controller (Crawler) and Pacman.

After downloading the code (reinforcement.zip), unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:
```
python pacman.py
```
To get started, run Gridworld in manual control mode, which uses the arrow keys:
```
python gridworld.py -m
```
You will see the two-exit layout from class. The blue dot is the agent. Note that when you press up, the agent only actually moves north 80% of the time. Such is the life of a Gridworld agent!

You can control many aspects of the simulation. A full list of options is available by running:
```
python gridworld.py -h
```
The default agent moves randomly:
```
python gridworld.py -g MazeGrid
```


# Implementation
Followed all the steps from here: https://inst.eecs.berkeley.edu/~cs188/fa19/project3/

# Autograder (How to evaluate the program):
This project includes an autograder for you to grade your answers on your machine. This can be run with the command:
```
python autograder.py
```

# How to run
Download the folders and install them locally. You can run these commands on the terminal while being in the folder /reinforcement: <br /> <br />
1. Value Iteration:
```
  $ python gridworld.py -a value -i 100 -k 10
  $ python gridworld.py -a value -i 5
```
2. Bridge Crossing Analysis:
```
  $ python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
  $ python autograder.py -q q2
```
3. Policies:
```
  $ python autograder.py -q q3
```
4. Asynchronous Value Iteration:
```
  $ python gridworld.py -a asynchvalue -i 1000 -k 10
  $ python autograder.py -q q4
```
5. Prioritized Sweeping Value Iteration:
```
  $ python gridworld.py -a priosweepvalue -i 1000
  $ python autograder.py -q q5
```
6. Q-Learning:
```
  $ python gridworld.py -a q -k 5 -m
  $ python autograder.py -q q6
```
7. Epsilon Greedy:
```
  $ python gridworld.py -a q -k 100
  $ python gridworld.py -a q -k 100 --noise 0.0 -e 0.1
  $ python gridworld.py -a q -k 100 --noise 0.0 -e 0.9
  $ python autograder.py -q q7
  $ python crawler.py
```
8. Bridge Crossing Revisited:
```
  $ python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1
  $ python autograder.py -q q8
```
9. Q-Learning and Pacman:
```
  $ python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l smallGrid
  $ python autograder.py -q q9
  $ python pacman.py -p PacmanQAgent -n 10 -l smallGrid -a numTraining=10
```
10. Approximate Q-Learning:
```
  $ python pacman.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid
  $ python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
  $ python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic
  $ python autograder.py -q q10
```




