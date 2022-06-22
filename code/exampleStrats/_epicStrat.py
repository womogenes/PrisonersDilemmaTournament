import math

def strategy(history, memory):
    n = history.shape[1]

    # Memory is:
    # 0. probability of opponent being random
    # 1. zero occurences
    # 2. one occurences
    # 3. -1 if not determined, 1 if random, 0 if not
    if n == 0:
        memory = [1, 0, 0, -1]

    if memory[3] == 1:
        return 0, memory

    # If undecided
    if memory[3] < 0:
        if n >= 1:
            memory[1] += history[1, -1] == 0
            memory[2] += history[1, -1] == 1

        if n >= 4:
            if memory[1] == 0 or memory[2] == 0:
                # Not random
                memory[3] = 0
            
            else:
                x = memory[1] / (memory[1] + memory[2])
                #print(x)

                # Probability of being random
                if H(x) >= 0.8:
                    memory[3] = 1
                    #print("it's random!")
                    return 0, memory


    # Otherwise do tit for tat
    choice = 1
    if n >= 1 and history[1, -1] == 0:
        choice = 0

    return choice, memory

# Binary entropy function: https://en.wikipedia.org/wiki/Binary_entropy_function
def H(x):
    return -x * math.log(x, 2) - (1 - x) * math.log(1 - x, 2)