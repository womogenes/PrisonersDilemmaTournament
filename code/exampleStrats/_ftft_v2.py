# How many defects are needed to trigger defect forever
threshold = 2

def strategy(history, memory):
    n = history.shape[1]

    # Memory stores how many times opponent has defected
    
    if n == 0:
        return 1, 0

    memory += not (history[1, -1])

    if memory < threshold:
        return history[1, -1], memory

    return 0, memory