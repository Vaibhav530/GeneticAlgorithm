import random
import ga2.gaDisc as gad

def diff(a , b):
    """
    Difference between 2 numbers
    """
    if(a > b):
        return(a - b)
    else:
        return(b - a)


def fitnessFun(agentObj):
    """
    Simple fitness function

    This fitness function checks for 
    how many of the dna's data are near to 0
    
    Here we are trying to get the dna of the agent
    as close as we can to the target vector
    """
    summ = 0
    target = [5, 7, 5, 10, 3]
    for i in range(len(target)):
        summ += diff(agentObj.dna[i], target[i])
    addToFitness = (200 - summ)
    return(agentObj.fitness + addToFitness)


if(__name__ == "__main__"):
    # running this file as main
    
    NUMBER_OF_EPOCH = 25
    NUMBER_OF_AGENTS = 25
    NUMBER_OF_PARAM = 5
    SPREAD = 1
    WILD_CARD_RATE = 0.01
    SURVIVAL_RATE = 0.05
    MUTATION_RATE = 0.05
    GENE_COPY = 0.9
    
    try:
        sess = gad.Session(agentCount=NUMBER_OF_AGENTS,
                           numParam=NUMBER_OF_PARAM,
                           spread = SPREAD,
                           genecopy = GENE_COPY,
                           survival=SURVIVAL_RATE,
                           mutation=MUTATION_RATE)
        sess.init()
    
        epoch = 0
        while(epoch < NUMBER_OF_EPOCH):
            
            # Code for printing the details of the epoch
            print("Epoch number {} ****************".format(epoch))
            print("Average fitness is {}".format(sess.getAverageFitness()))
            print("maximum fitness is {}".format(sess.getBestAgent().fitness))
            print("Best DNA is {}".format(sess.getBestAgent().dna))
            # Code for getting a single agent from current environment
            currGen = sess.getAllAgents()
            for agentID in currGen:
                # Update the agent's fitness value
                agent = sess.getAgent(agentID)
                agent.fitness = fitnessFun(agent)
                sess.updateAgent(agent)
            
            # Generates the next generation
            sess.createNextGen()
            epoch += 1
        
        print("FINAL ***************")
        print("Average fitness is {}".format(sess.getAverageFitness()))
        print("maximum fitness is {}".format(sess.getBestAgent().fitness))
        print("Best DNA is {}".format(sess.getBestAgent().dna))
    
    except Exception as e:
        print("Exception cought with message as {}".format(e))

    finally:
        sess.delete()
