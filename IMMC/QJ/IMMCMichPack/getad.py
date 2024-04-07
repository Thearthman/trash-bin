def getad(replacementList):
    candidateNumber = len(replacementList.columns)
    dNew = 0
    for i in range(candidateNumber):
        dNew += abs(replacementList.sum().sum() / candidateNumber - replacementList.sum().iloc[i])
    return dNew/candidateNumber



