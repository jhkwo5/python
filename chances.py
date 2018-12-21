import random

'''
Play until win but need to set maximum game played before its too big
stop when game won and calculate winAmount
'''

'''
initialBet = how much you want to start
gamePlayed = how many game you wnat to play
'''

globalWinAmount = []
globalLostAmount = []

def betAmount(initialBetAmount, gamePlayed):
    result = []
    totalSpent = 0
    for i in range(1, gamePlayed + 1):
        if (i == 1):
            result.append(initialBetAmount)
            totalSpent += initialBetAmount
            # print(initialBetAmount)
        else:
            initialBetAmount *= 2
            # print(initialBetAmount)
            totalSpent += initialBetAmount
            result.append(initialBetAmount)

    # print("Printing Total spent: ", totalSpent)
    # print(result)
    return result


def randomChances():
    chances = random.random()
    if chances < 0.4736842105263158:
        return "win"
    else:
        return "lost"


def gameStart():
    startAmount = 5  # set starting amount
    gamePlayed = 6  # set how many games during 1 game

    finalWin = sum(betAmount(startAmount, gamePlayed))  # played until aimed profit
    initialValue = sum(betAmount(startAmount, gamePlayed))
    gameBet = betAmount(startAmount, gamePlayed)  # Lists of bet amount
    findMax = []
    findMin = []

    everyGameCount = 0
    gameWonAt = 0  # many game have to play to win
    winRatio = 0
    lostRatio = 0

    print("Lists of betting amount {0}, total amount is {1}".format(gameBet, finalWin))

    while initialValue * 2 > finalWin > 0:
        for i in gameBet:
            random = randomChances()
            if random == "lost":
                gameWonAt += 1
                finalWin -= i
                everyGameCount += 1
                print("---------------during lost {0}, current value {1} ".format(i, finalWin))
                findMax.append(finalWin)
                # print("Game Lost during game")
            else:
                finalWin += i
                winRatio += 1  # winning percentage
                gameWonAt = 0  # reset game count during 1 game
                everyGameCount += 1
                findMax.append(finalWin)
                print("win => {0}".format(finalWin))
                break
            # print("Printing game win ", gameWonAt)
            # print("Printing Final win", finalWin)

            if gameWonAt == gamePlayed:
                lostRatio += 1  # Losing percentage
                print("Lost => {0}".format(finalWin))
                findMax.append(finalWin)

            if finalWin <= 0:
                print("Game ended due to low balance")
                #globalLostAmount.append(finalWin)
                break

    print("winning percentage => {0},"
          " losing percentage => {1} for Maximum betting {2}"
          .format(winRatio, lostRatio, initialValue))
    print("Maximum win was {0} and total game played {1} ".format(max(findMax), everyGameCount))

    if finalWin > 0:
        globalWinAmount.append(finalWin - initialValue)
        return True
    else:
        globalLostAmount.append(finalWin - initialValue)
        return False

    # print("Printing game count: ", gameCount)


# gameStart()


def main():
    gameCount = 0
    winCount = 0
    loseCount = 0

    while gameCount < 3:
        if gameStart() == True:
            winCount += 1
        else:
            loseCount += 1
        gameCount += 1

    print("Win: {0}, Lost: {1}".format(winCount, loseCount))
    print(globalWinAmount)
    print(globalLostAmount)
    print(sum(globalWinAmount))
    print(sum(globalLostAmount))



main()

"""
    TODO:   
        find During game calculate best possible chances to get maximum win
"""