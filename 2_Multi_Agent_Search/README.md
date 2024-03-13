# Multi-Agent Search in Pacman

# Introduction
In this project, I designed agents for the classic version of Pacman, including ghosts. Along the way, I implemented both minimax and expectimax search and tried my hand at evaluation function design.

After downloading the code (multiagent.zip), unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:
```
python pacman.py
```
and using the arrow keys to move. Now, run the provided `ReflexAgent` in `multiAgents.py`
```
python pacman.py -p ReflexAgent
```
Note that it plays quite poorly even on simple layouts:
```
python pacman.py -p ReflexAgent -l testClassic
```
Inspect its code in `multiAgents.py`.


# Implementation
Followed all the steps from here: https://inst.eecs.berkeley.edu/~cs188/fa19/project2/

# Autograder (How to evaluate the program):
This project includes an autograder for you to grade your answers on your machine. This can be run with the command:
```
python autograder.py
```