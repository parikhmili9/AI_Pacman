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

# How to run
Download the folders and install them locally. You can run these commands on the terminal while being in the folder /multiagents: <br /> <br />
1. Reflex Agent:
```
  $ python pacman.py --frameTime 0 -p ReflexAgent -k 1
  $ python pacman.py --frameTime 0 -p ReflexAgent -k 2
  $ python autograder.py -q q1
```
2. Minimax algorithm:
```
  $ python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
  $ python pacman.py -p MinimaxAgent -l trappedClassic -a depth=3
  $ python autograder.py -q q2
```
3. Alpha-Beta pruning algorithm:
```
  $ python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
  $ python pacman.py -p AlphaBetaAgent -l trappedClassic -a depth=3 -q -n 10
  $ python autograder.py -q q3
```
4. Expectimax algorithm:
```
  $ python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
  $ python pacman.py -p ExpectimaxAgent -l trappedClassic -a depth=3 -q -n 10
  $ python autograder.py -q q4
```
5. Evaluation Function:
```
  $ python autograder.py -q q5
```




