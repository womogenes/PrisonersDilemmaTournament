# Reminder: For the history array, "cooperate" = 1, "defect" = 0
import random
def strategy(history, memory):
    choice = 1
    turn = len(history[1]) #Turns are 0-indexed
    betrayed = False #has the opponent ever attacked you?
    lastbetrayed = -1 #When has the opponent last sent out a betrayal?
    firstbetrayed = -1 #When have they first betrayed you
    for i in range(len(history[1])):
        if history[1][i] == 0:
            if betrayed == False:
                betrayed = True
                firstbetrayed = i
            lastbetrayed = i
    if betrayed: #If you aren't betrayed, just be cooperative I guess 
        if turn - firstbetrayed <= 10: #run tft a bit I guess
            choice = history[1][-1]
        elif turn - firstbetrayed == 11: #wait once to see what the opponent does
            choice = 1
        else:
            #We analyze the results and see how many times a "strange" move happens
            testvalues0 = history[0][firstbetrayed+1:firstbetrayed+11]
            testvalues1 = history[1][firstbetrayed+2:firstbetrayed+12] #off by one, since we want to see the opponent reactions
            points = 0 #How many non-tft moves the opponent makes
            for i in range(10):
                if testvalues1[i] != testvalues0[i]: #i.e., our opponent is doing something other than tft
                    points+=1
            if points >= 3: #if the opponent makes 3 or more dumb moves
                choice = 0 #Always defecting is by definition the right choice
            else:
                #Run randomnice! (i.e. tit-for-tat but on random occasions it is nice)
                if len(history[1])%10 == 5 or len(history[1])%10 == 6:
                    choice = 1
                else:
                    choice = 1
                    if history[1][-1] == 0:
                        choice = 0
    return choice, None