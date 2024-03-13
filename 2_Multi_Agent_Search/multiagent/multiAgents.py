# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from os import access, stat
import re
from typing import List
from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        #action should increase score of the pacman
        newScore = successorGameState.getScore()
        currScore = currentGameState.getScore()
        score = newScore - currScore

        #action should decrease the path length to the nearest food
        currPos = currentGameState.getPacmanPosition()
        for food in currentGameState.getFood().asList() :
            distanceToNearestFood = min([manhattanDistance(currPos, food)])

        distancesToNewFoods = []
        for food in newFood.asList() :
            distanceToNewFood = manhattanDistance(newPos, food)
            distancesToNewFoods.append(distanceToNewFood)

        if(not distancesToNewFoods) :
            newDistanceToNearestFood = 0
        else :
            newDistanceToNearestFood = min(distancesToNewFoods)

        nearFood = distanceToNearestFood - newDistanceToNearestFood

        #action to keep a good distance with the ghosts
        for state in newGhostStates :
            leastDistanceToGhost = min([manhattanDistance(newPos, state.getPosition())])

        direction = currentGameState.getPacmanState().getDirection()

        if(leastDistanceToGhost <= 1 or action == Directions.STOP) :
            return 0
        if score > 0 :
            return 32
        elif nearFood > 0 :
            return 16
        elif action == direction :
            return 8
        else :
            return 4

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"

        # minimum value function
        def minimumVal(state, agentIndex, depth):
            listOfLegalActions = state.getLegalActions(agentIndex)
            if not listOfLegalActions:
                return self.evaluationFunction(state)

            # pacman's turn is after all ghosts have taken their turns
            numberOfAgents = state.getNumAgents()
            getMaximumVal = []
            getMinimumVal = []
            if agentIndex == numberOfAgents - 1:
                 for action in listOfLegalActions:
                     getSuccesor = state.generateSuccessor(agentIndex,action)
                     getMaximumVal.append(maximumVal(getSuccesor, depth))
                 return min(getMaximumVal)

            else:
                 for action in listOfLegalActions:
                     getSuccesor = state.generateSuccessor(agentIndex,action)
                     getMinimumVal.append(minimumVal(getSuccesor, agentIndex + 1, depth))
                 return min(getMinimumVal)

        # maximum value function
        # used only for pacman's turn and hence the agent index is set to 0
        def maximumVal(state, depth):
            agentIndex = 0
            listOfLegalActions = state.getLegalActions(agentIndex)
            if not listOfLegalActions or depth == self.depth:
                return self.evaluationFunction(state)
            getMinimumVal = []
            for action in listOfLegalActions:
                getSuccesor = state.generateSuccessor(0,action)
                getMinimumVal.append(minimumVal(getSuccesor, 0 + 1,depth + 1))
            return max(getMinimumVal)

        optimalAction = max(gameState.getLegalActions(0),
                         key=lambda action: minimumVal(gameState.generateSuccessor(0, action), 1, 1))
        return optimalAction

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"

        InfNum = float('inf')

        def minimumVal(state, agentIndex, depth, alpha, beta):
            listoflegalActions = state.getLegalActions(agentIndex)
            if not listoflegalActions:
                return self.evaluationFunction(state)

            val = InfNum
            for action in listoflegalActions:
                getSuccesor = state.generateSuccessor(agentIndex, action)

                # checking if it is the last ghost
                if agentIndex == state.getNumAgents() - 1:
                    newVal = maximumVal(getSuccesor, depth, alpha, beta)
                else:
                    newVal = minimumVal(getSuccesor, agentIndex + 1, depth, alpha, beta)

                val = min(val, newVal)
                if val < alpha:
                    return val
                beta = min(beta, val)
            return val

        def maximumVal(state, depth, alpha, beta):
            agentIndex = 0
            listoflegalActions = state.getLegalActions(agentIndex)
            if not listoflegalActions or depth == self.depth:
                return self.evaluationFunction(state)

            val = -InfNum
           
            if depth == 0:
                optimalAction = listoflegalActions[0]
            for action in listoflegalActions:
                getSuccesor = state.generateSuccessor(0, action)
                newVal = minimumVal(getSuccesor, 0 + 1, depth + 1, alpha, beta)
                if newVal > val:
                    val = newVal
                    if depth == 0:
                        optimalAction = action
                if val > beta:
                    return val
                alpha = max(alpha, val)

            if depth == 0:
                return optimalAction
            return val

        optimalAction = maximumVal(gameState, 0, -InfNum, InfNum)
        return optimalAction
        
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"

        def expectedVal(state, agentIndex, depth):
            numberOfAgents = gameState.getNumAgents()
            listOfLegalActions = state.getLegalActions(agentIndex)

            if not listOfLegalActions:
                return self.evaluationFunction(state)

            expVal = 0
            prob = 1 / len(listOfLegalActions)

            for action in listOfLegalActions:
                if agentIndex == numberOfAgents - 1:
                    getSuccessor = state.generateSuccessor(agentIndex, action)
                    currExpectedValue = maximumVal(getSuccessor, agentIndex, depth)
                else :
                    getSuccessor = state.generateSuccessor(agentIndex, action)
                    currExpectedValue = expectedVal(getSuccessor, agentIndex + 1, depth)
                expVal = expVal + (currExpectedValue * prob)
            return expVal

        def maximumVal(state, agentIndex, depth):
            agentIndex = 0
            listOfLegalActions = state.getLegalActions(agentIndex)

            # if the list of legal actions is empty or the depth is reached
            if not listOfLegalActions or depth == self.depth:
                return self.evaluationFunction(state)
            
            getMaximumVal = []
            for action in listOfLegalActions:
                getSuccessor = state.generateSuccessor(agentIndex, action)
                getMaximumVal.append(expectedVal(getSuccessor, agentIndex + 1, depth + 1))
                maxValue = max(getMaximumVal)
            return maxValue

        actions = gameState.getLegalActions(0)
        listOfAllActions = {}
        for action in actions:
            getSuccessor = gameState.generateSuccessor(0, action)
            listOfAllActions[action] = expectedVal(getSuccessor, 1, 1)
        
        return max(listOfAllActions, key=listOfAllActions.get)

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    currPos = currentGameState.getPacmanPosition()
    currFood = currentGameState.getFood().asList()
    currGhostStates = currentGameState.getGhostStates()
    currScaredTimes = [ghostState.scaredTimer for ghostState in currGhostStates]
    currCapsule = currentGameState.getCapsules()

    #highest score for a win
    if currentGameState.isWin():
        return 99999

    # when ghost and pacman are at same place
    for state in currGhostStates:
        if state.getPosition() == currPos and state.scaredTimer == 1:
            return -99999

    score = 0

    #distance of nearest food from pacman
    listOfdistanceOfFood = []
    for food in currFood:
        listOfdistanceOfFood.append(util.manhattanDistance(currPos, food))
    closestFood = min(listOfdistanceOfFood)
    score = score + float(1 / closestFood)
    score = score - len(currFood)

    #capsule scores
    if currCapsule:
        listOfdistanceOfCapsule = []
        for capsule in currCapsule:
            listOfdistanceOfCapsule.append(util.manhattanDistance(currPos, capsule))
        closestFood = min(listOfdistanceOfCapsule)
        closestCapsule = min(listOfdistanceOfCapsule)
        score = score + float(1 / closestCapsule)


    ghostDistance = []
    for ghost in currentGameState.getGhostStates():
        ghostDistance.append(util.manhattanDistance(currPos, ghost.getPosition()))
    closestCurrentGhost = min(ghostDistance)
    scaredTime = sum(currScaredTimes)
    if closestCurrentGhost >= 1:
        if scaredTime < 0:
            score = score - 1 / closestCurrentGhost
        else:
            score = score + 1 / closestCurrentGhost

    return currentGameState.getScore() + score
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
