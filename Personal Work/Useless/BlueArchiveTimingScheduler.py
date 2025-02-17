import matplotlib.pyplot as plt

# Initialize variable
durationArray = []
numberOfSkills = 0
begin = []
end = []

def generate_timing_map():
    for k in range(len(durationArray)):
        for i in range(int(240/durationArray[k][1])):
            begin.append(durationArray[k] + i*(CD+))
 # CD + k(CD+Dur)
 # (k+1)(CD + Dur)
    event = ["Event {}".format(i) for i in range(len(begin))]
    plt.barh(range(len(begin)),  end-begin, left=begin)
    plt.yticks(range(len(begin)), event)
    plt.show()
    pass


while True:
    print("Input 'g' to generate Map; input 'CD Duration' to add Timing")
    userInput = input()
    if userInput == "g":
        generate_timing_map()
        break
    else:
        try:
            processedTimingArray = list(map(int, userInput.split(" ", 1)))
            if (len(processedTimingArray) < 2) or (max(processedTimingArray) > 60) or (
                    min(processedTimingArray) < 1): raise ValueError
            durationArray.append(processedTimingArray)
            numberOfSkills = len(durationArray)
            print("Skill inputted, now we have", numberOfSkills, "skills, ", durationArray)
        except:
            print("Wrong input type, please input two 'Integer'(less than 60) separated using 'Space'")
            pass
