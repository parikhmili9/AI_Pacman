# Search algorithms in Pacman

# Introduction
In this project, your Pacman agent will find paths through his maze world, both to reach a particular location and to collect food efficiently. You will build general search algorithms and apply them to Pacman scenarios.

After downloading the code (search.zip), unzipping it, and changing to the directory, you should be able to play a game of Pacman by typing the following at the command line:
```
python pacman.py
```

Pacman lives in a shiny blue world of twisting corridors and tasty round treats. Navigating this world efficiently will be Pacman’s first step in mastering his domain.

The simplest agent in `searchAgents.py` is called the  `GoWestAgent`, which always goes West (a trivial reflex agent). This agent can occasionally win:
```
python pacman.py --layout testMaze --pacman GoWestAgent
```

If Pacman gets stuck, you can exit the game by typing CTRL-c into your terminal.

Soon, your agent will solve not only tinyMaze, but any maze you want.

Note that `pacman.py` supports a number of options that can each be expressed in a long way (e.g., --layout) or a short way (e.g., -l). You can see the list of all options and their default values via:
```
python pacman.py -h
```
Also, all of the commands that appear in this project also appear in `commands.txt`, for easy copying and pasting. In UNIX/Mac OS X, you can even run all these commands in order with `bash commands.txt`.


# Autograder (How to evaluate the program):
This project includes an autograder for you to grade your answers on your machine. This can be run with the command:
```
python autograder.py
```

# Implementation
Followed all the steps from here: https://inst.eecs.berkeley.edu/~cs188/fa19/project1/

# How to run
Download the folders and install them locally. You can run these commands on the terminal while being in the folder /search:
<br /><br />
1. DFS (Depth-first-search) Algorithm:
```
  $ python pacman.py -l tinyMaze -p SearchAgent
  $ python pacman.py -l mediumMaze -p SearchAgent
  $ python pacman.py -l bigMaze -z .5 -p SearchAgent
```
2. BFS (Breadth-first-search) Algorithm:
```
  $ python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
  $ python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
3. Solving the eightpuzzle which puts all numbers of a box in order, using BFS:
```
  $ python eightpuzzle.py
```
4. Implemented Uniform-Cost-Search function:
```
  $ python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
  $ python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
  $ python pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```
5. A* (A star) graph search Algorithm:
```
  $ python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
6. Data decoding of the corners problem and run with BFS:
```
  $ python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
  $ python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
7. Using A* to solve the corners problem but with a new heuristic implemented by me:
```
  $ python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
8. Using A* to solve the corners problem:
```
  $ python pacman.py -l testSearch -p AStarFoodSearchAgent
```
9. Upgrade A* to make the pacman eat all the dots:
```
  $ python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
10. Implementing a greedy algorithm that always eats the closest dot and it is the most efficient one for this problem.
```
  $ python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5 
 ```
 