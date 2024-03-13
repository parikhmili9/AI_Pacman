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