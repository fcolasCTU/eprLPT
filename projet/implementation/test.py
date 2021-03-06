import matrix as cm
import algorithms as cmm
import ScheduleManagment as sm
import pwa

def main():
    # set of testing matricies
    matricies = []
    print("Job Set size ============================================================")
    nN                  = int(input("Jobs number     : "))
    nMmachineNumber     = int(input("Machines number : "))

    print("Job set generation ======================================================")    
    matUniformNumber    = int(input("How many uniform matricies to generate : "))
    matNonUniformNumber = int(input("How many non uniform matricies to generate : "))
    matGammaNumber      = int(input("How many Gamma matricies to generate : "))
    matBetaNumber       = int(input("How many Beta matricies to generate : "))
    matExponentialNumber= int(input("How many Exponential matricies to generate : "))
    print("_____ From Parallel WorkLoad Archive _____")
    matRealFiles        = pwa.pwaFileChoice()
    
           

    print("Properties of generation ================================================")
    nAb = 1.0
    nBb = 100.0
    nAlpah = 1.0
    nBeta = 1.0
    nLambda = 1.0
    filename=""

    if (matUniformNumber > 0 or matNonUniformNumber > 0):
        nAb = float(input("a parameter : "))
        nBb = float(input("b parameter : "))
    if (matGammaNumber > 0 or matBetaNumber > 0):
        nAlpah = float(input("alpha parameter (for gamma and beta) : "))
    if (matGammaNumber > 0):
        nBeta = float(input("beta parameter (for gamma) : "))
    if (matExponentialNumber>0):
        nLambda = float(input("lambda parameter (for ecxponential) : "))

    print("Algorithms ================================================")
    useLPT     = int(input("Use LPT rule ? : (1 yes, 0 no) : "))
    useSLACK   = int(input("Use Slack    ? : (1 yes, 0 no) : "))
    useLDM     = int(input("Use LDM      ? : (1 yes, 0 no) : "))
    useCOMBINE = int(input("Use COMBINE  ? : (1 yes, 0 no) : "))

    print("Generation (please wait =================================================")
    # UNIFORM P    
    for i in range(matUniformNumber):
        m = cm.PTimes("UNIFORM", nN, nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, filename)
        matricies.append(m)
        
    # NON UNIFORM P    
    for i in range(matNonUniformNumber):
        m = cm.PTimes("NON_UNIFORM", nN, nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, filename)
        matricies.append(m)
    # GAMMA P    
    for i in range(matNonUniformNumber):
        m = cm.PTimes("GAMMA", nN, nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, filename)
        matricies.append(m)    
    # BETA P    
    for i in range(matNonUniformNumber):
        m = cm.PTimes("BETA", nN,  nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, filename)
        matricies.append(m)    
    # EXPENENTIAL P    
    for i in range(matNonUniformNumber):
        m = cm.PTimes("EXPONENTIAL", nN,  nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, filename)
        matricies.append(m)    
    # REAL P    
    for i in range(len(matRealFiles)):
        m = cm.PTimes("REAL", nN,  nMmachineNumber, nAb, nBb, nAlpah, nBeta, nLambda, matRealFiles[i])
        matricies.append(m)    

    print("===========================================================")
    print("OLGORITHMS ")    
    print("===========================================================")
    for i in range(len(matricies)):
        if useLPT == 1:
            print("-------------------------------------------------------")
            # work Times list
            r = cmm.lpt(matricies[i].Times, matricies[i].m)
            matricies[i].addSched(r)
            print("Expected lp :",matricies[i].BestResult_Makespan,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
            
            # work m1Times list
            r = cmm.lpt(matricies[i].m1Times, matricies[i].m)
            matricies[i].addM1Sched(r)
            print("Expected op :",matricies[i].m1Optimal,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
        # END IF

        if useSLACK == 1:
            print("-------------------------------------------------------")
            # work Times list
            r = cmm.slack(matricies[i].Times, matricies[i].m)
            matricies[i].addSched(r)
            print("Expected lb :",matricies[i].BestResult_Makespan,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
            # !!!!! issue lowBound false value

            # work m1Times list
            r = cmm.slack(matricies[i].m1Times, matricies[i].m)
            matricies[i].addM1Sched(r)
            print("Expected op :",matricies[i].m1Optimal,", Obtained :",r.getMakespan(), ", Time:", r.getTime())
        # END IF
        
        if useLDM == 1:
            print("-------------------------------------------------------")
            print("Not yet implemented.")
        # END IF    

        if useCOMBINE == 1:
            print("-------------------------------------------------------")
            print("Not yet implemented.")
        # END IF    

if __name__ == "__main__":
    main()

    
    
