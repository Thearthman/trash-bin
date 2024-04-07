from matplotlib import pyplot as plt


def drawplot(iteration=None, adList=None
             , titleprompt='(A+B) vs C vs D vs E  Absolute Deviations against Iteration'):
    if iteration is None:
        iteration = [0]
    if adList is None:
        adList = [0]
    ymin = min(adList)
    plt.plot(iteration, adList)
    plt.axhline(ymin, color='r')
    plt.text(iteration[len(iteration) - 1] * 3 / 4, min(adList) + (max(adList)-min(adList))*0.05, "ADmin = " + str(round(ymin,2)))
    plt.xlabel('Iteration')
    plt.ylabel('Absolute Deviation')
    plt.title(titleprompt)
    plt.show()
